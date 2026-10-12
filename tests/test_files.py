"""Tests for the custom file helpers (tar extraction safety)."""

import asyncio
import io
import tarfile
from types import SimpleNamespace

import httpx
import pytest

from islo.custom import files
from islo.custom.files import _safe_tar_extract


@pytest.mark.asyncio
async def test_async_upload_file_retries_429_using_retry_after(tmp_path, monkeypatch):
    source = tmp_path / "artifact.json"
    source.write_text('{"ok": true}')
    responses = iter([429, 429, 429, 200])
    attempts = []
    delays = []

    def handler(request):
        attempts.append(request.content)
        return httpx.Response(next(responses), headers={"Retry-After": "17"})

    async_client = httpx.AsyncClient
    monkeypatch.setattr(files.httpx, "AsyncClient", lambda: async_client(transport=httpx.MockTransport(handler)))

    async def record_sleep(seconds):
        delays.append(seconds)

    monkeypatch.setattr(asyncio, "sleep", record_sleep)
    client = SimpleNamespace(
        _client_wrapper=SimpleNamespace(
            async_get_headers=lambda: _headers(),
            get_environment=lambda: SimpleNamespace(compute="https://compute.example"),
        )
    )
    await files.async_upload_file(client, "sandbox", source, "/app/artifact.json")

    assert len(attempts) == 4
    assert all(source.read_bytes() in body for body in attempts)
    assert delays == [17, 17, 17]


async def _headers():
    return {"Authorization": "Bearer test"}


@pytest.mark.asyncio
async def test_async_upload_file_retries_read_error(tmp_path, monkeypatch):
    source = tmp_path / "artifact.json"
    source.write_text("payload")
    attempts = 0

    def handler(request):
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise httpx.ReadError("connection closed", request=request)
        return httpx.Response(200)

    async_client = httpx.AsyncClient
    monkeypatch.setattr(files.httpx, "AsyncClient", lambda: async_client(transport=httpx.MockTransport(handler)))

    async def no_sleep(_seconds):
        pass

    monkeypatch.setattr(asyncio, "sleep", no_sleep)
    client = SimpleNamespace(
        _client_wrapper=SimpleNamespace(
            async_get_headers=lambda: _headers(),
            get_environment=lambda: SimpleNamespace(compute="https://compute.example"),
        )
    )
    await files.async_upload_file(client, "sandbox", source, "/app/artifact.json")
    assert attempts == 3


@pytest.mark.asyncio
async def test_async_upload_file_does_not_retry_other_client_errors(tmp_path, monkeypatch):
    source = tmp_path / "artifact.json"
    source.write_text("payload")
    attempts = 0

    def handler(request):
        nonlocal attempts
        attempts += 1
        return httpx.Response(400)

    async_client = httpx.AsyncClient
    monkeypatch.setattr(files.httpx, "AsyncClient", lambda: async_client(transport=httpx.MockTransport(handler)))
    client = SimpleNamespace(
        _client_wrapper=SimpleNamespace(
            async_get_headers=lambda: _headers(),
            get_environment=lambda: SimpleNamespace(compute="https://compute.example"),
        )
    )
    with pytest.raises(httpx.HTTPStatusError) as exc_info:
        await files.async_upload_file(client, "sandbox", source, "/app/artifact.json")
    assert exc_info.value.response.status_code == 400
    assert attempts == 1


class TestSafeTarExtract:
    def test_normal_extraction(self, tmp_path):
        buf = io.BytesIO()
        with tarfile.open(fileobj=buf, mode="w:gz") as tar:
            info = tarfile.TarInfo(name="hello.txt")
            data = b"hello world"
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
        buf.seek(0)

        dest = tmp_path / "output"
        dest.mkdir()
        with tarfile.open(fileobj=buf, mode="r:gz") as tar:
            _safe_tar_extract(tar, dest)

        assert (dest / "hello.txt").read_text() == "hello world"

    def test_nested_extraction(self, tmp_path):
        buf = io.BytesIO()
        with tarfile.open(fileobj=buf, mode="w:gz") as tar:
            info = tarfile.TarInfo(name="sub/dir/file.txt")
            data = b"nested"
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
        buf.seek(0)

        dest = tmp_path / "output"
        dest.mkdir()
        with tarfile.open(fileobj=buf, mode="r:gz") as tar:
            _safe_tar_extract(tar, dest)

        assert (dest / "sub" / "dir" / "file.txt").read_text() == "nested"

    def test_path_traversal_blocked(self, tmp_path):
        buf = io.BytesIO()
        with tarfile.open(fileobj=buf, mode="w:gz") as tar:
            info = tarfile.TarInfo(name="../escape.txt")
            data = b"evil"
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))
        buf.seek(0)

        dest = tmp_path / "output"
        dest.mkdir()
        with tarfile.open(fileobj=buf, mode="r:gz") as tar:
            with pytest.raises(ValueError, match="escape target directory"):
                _safe_tar_extract(tar, dest)
