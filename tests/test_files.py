"""Tests for the custom file helpers (tar extraction safety)."""

import io
import tarfile

import pytest

from islo.custom.files import _safe_tar_extract


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
