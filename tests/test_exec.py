"""Tests for the custom exec helpers."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from islo.core.api_error import ApiError
from islo.custom.exec import (
    _MAX_CONSECUTIVE_POLL_ERRORS,
    ExecResult,
    exec_and_wait,
    exec_and_wait_sync,
)


class TestExecResult:
    def test_model_fields(self):
        result = ExecResult(stdout="hello", stderr="", exit_code=0)
        assert result.stdout == "hello"
        assert result.stderr == ""
        assert result.exit_code == 0

    def test_nonzero_exit(self):
        result = ExecResult(stdout="", stderr="fail", exit_code=1)
        assert result.exit_code == 1
        assert result.stderr == "fail"

    def test_timed_out_default(self):
        result = ExecResult(stdout="", stderr="", exit_code=0)
        assert result.timed_out is False

    def test_timed_out_true(self):
        result = ExecResult(stdout="", stderr="", exit_code=-1, timed_out=True)
        assert result.timed_out is True


class TestExecAndWait:
    @pytest.mark.asyncio
    async def test_immediate_completion(self):
        exec_resp = MagicMock(exec_id="test-exec-123")
        result_resp = MagicMock(status="completed", exit_code=0, stdout="hello\n", stderr="", truncated=False)

        client = MagicMock()
        client.sandboxes.exec_in_sandbox = AsyncMock(return_value=exec_resp)
        client.sandboxes.get_exec_result = AsyncMock(return_value=result_resp)

        result = await exec_and_wait(client, "my-sandbox", ["echo", "hello"])

        assert result.stdout == "hello\n"
        assert result.stderr == ""
        assert result.exit_code == 0
        assert result.timed_out is False

        client.sandboxes.exec_in_sandbox.assert_awaited_once()
        client.sandboxes.get_exec_result.assert_awaited_once_with("my-sandbox", "test-exec-123")

    @pytest.mark.asyncio
    async def test_polls_until_complete(self):
        exec_resp = MagicMock(exec_id="poll-exec")
        running_resp = MagicMock(status="running", exit_code=None, stdout="", stderr="")
        done_resp = MagicMock(status="completed", exit_code=42, stdout="output", stderr="err")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox = AsyncMock(return_value=exec_resp)
        client.sandboxes.get_exec_result = AsyncMock(side_effect=[running_resp, running_resp, done_resp])

        with patch("islo.custom.exec.asyncio.sleep", new_callable=AsyncMock):
            result = await exec_and_wait(client, "sb", ["cmd"], poll_interval=0.01)

        assert result.exit_code == 42
        assert result.stdout == "output"
        assert result.stderr == "err"
        assert client.sandboxes.get_exec_result.await_count == 3

    @pytest.mark.asyncio
    async def test_client_timeout(self):
        exec_resp = MagicMock(exec_id="timeout-exec")
        running_resp = MagicMock(status="running", exit_code=None, stdout="", stderr="")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox = AsyncMock(return_value=exec_resp)
        client.sandboxes.get_exec_result = AsyncMock(return_value=running_resp)

        with patch("islo.custom.exec.asyncio.sleep", new_callable=AsyncMock):
            result = await exec_and_wait(client, "sb", ["sleep", "999"], timeout=0.01, poll_interval=0.001)

        assert result.timed_out is True
        assert result.exit_code == -1

    @pytest.mark.asyncio
    async def test_failed_status(self):
        exec_resp = MagicMock(exec_id="fail-exec")
        fail_resp = MagicMock(status="failed", exit_code=None, stdout="partial", stderr="crash")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox = AsyncMock(return_value=exec_resp)
        client.sandboxes.get_exec_result = AsyncMock(return_value=fail_resp)

        result = await exec_and_wait(client, "sb", ["cmd"])

        assert result.exit_code == -1
        assert result.stdout == "partial"
        assert result.stderr == "crash"

    @pytest.mark.asyncio
    async def test_passes_optional_params(self):
        exec_resp = MagicMock(exec_id="params-exec")
        done_resp = MagicMock(status="completed", exit_code=0, stdout="", stderr="")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox = AsyncMock(return_value=exec_resp)
        client.sandboxes.get_exec_result = AsyncMock(return_value=done_resp)

        await exec_and_wait(
            client,
            "sb",
            ["make"],
            workdir="/app",
            env={"FOO": "bar"},
            user="islo",
        )

        call_kwargs = client.sandboxes.exec_in_sandbox.call_args
        assert call_kwargs.kwargs["workdir"] == "/app"
        assert call_kwargs.kwargs["env"] == {"FOO": "bar"}
        assert call_kwargs.kwargs["user"] == "islo"

    @pytest.mark.asyncio
    async def test_retries_on_transient_5xx(self):
        """Transient 5xx errors during polling should be retried, not raised."""
        exec_resp = MagicMock(exec_id="retry-exec")
        done_resp = MagicMock(status="completed", exit_code=0, stdout="ok", stderr="")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox = AsyncMock(return_value=exec_resp)
        client.sandboxes.get_exec_result = AsyncMock(
            side_effect=[
                ApiError(status_code=502, body="Bad Gateway"),
                ApiError(status_code=503, body="Service Unavailable"),
                done_resp,
            ]
        )

        with patch("islo.custom.exec.asyncio.sleep", new_callable=AsyncMock):
            result = await exec_and_wait(client, "sb", ["cmd"], poll_interval=0.01)

        assert result.exit_code == 0
        assert result.stdout == "ok"
        assert client.sandboxes.get_exec_result.await_count == 3

    @pytest.mark.asyncio
    async def test_raises_after_max_consecutive_5xx(self):
        """After MAX_CONSECUTIVE_POLL_ERRORS 5xx errors, the exception propagates."""
        exec_resp = MagicMock(exec_id="max-err-exec")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox = AsyncMock(return_value=exec_resp)
        errors = [ApiError(status_code=500, body="error") for _ in range(_MAX_CONSECUTIVE_POLL_ERRORS + 1)]
        client.sandboxes.get_exec_result = AsyncMock(side_effect=errors)

        with patch("islo.custom.exec.asyncio.sleep", new_callable=AsyncMock):
            with pytest.raises(ApiError) as exc_info:
                await exec_and_wait(client, "sb", ["cmd"], timeout=60, poll_interval=0.01)

        assert exc_info.value.status_code == 500

    @pytest.mark.asyncio
    async def test_does_not_retry_4xx(self):
        """Non-5xx errors (e.g. 404) should propagate immediately."""
        exec_resp = MagicMock(exec_id="4xx-exec")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox = AsyncMock(return_value=exec_resp)
        client.sandboxes.get_exec_result = AsyncMock(side_effect=ApiError(status_code=404, body="Not Found"))

        with pytest.raises(ApiError) as exc_info:
            await exec_and_wait(client, "sb", ["cmd"])

        assert exc_info.value.status_code == 404
        assert client.sandboxes.get_exec_result.await_count == 1

    @pytest.mark.asyncio
    async def test_consecutive_error_counter_resets_on_success(self):
        """A successful poll resets the consecutive error counter."""
        exec_resp = MagicMock(exec_id="reset-exec")
        running_resp = MagicMock(status="running", exit_code=None, stdout="", stderr="")
        done_resp = MagicMock(status="completed", exit_code=0, stdout="ok", stderr="")

        max_errs = _MAX_CONSECUTIVE_POLL_ERRORS
        side_effects: list = []
        side_effects.extend([ApiError(status_code=503, body="blip")] * (max_errs - 1))
        side_effects.append(running_resp)
        side_effects.extend([ApiError(status_code=502, body="blip")] * (max_errs - 1))
        side_effects.append(done_resp)

        client = MagicMock()
        client.sandboxes.exec_in_sandbox = AsyncMock(return_value=exec_resp)
        client.sandboxes.get_exec_result = AsyncMock(side_effect=side_effects)

        with patch("islo.custom.exec.asyncio.sleep", new_callable=AsyncMock):
            result = await exec_and_wait(client, "sb", ["cmd"], timeout=60, poll_interval=0.01)

        assert result.exit_code == 0
        assert client.sandboxes.get_exec_result.await_count == len(side_effects)


class TestExecAndWaitSync:
    def test_immediate_completion(self):
        exec_resp = MagicMock(exec_id="sync-exec")
        result_resp = MagicMock(status="completed", exit_code=0, stdout="ok\n", stderr="")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox.return_value = exec_resp
        client.sandboxes.get_exec_result.return_value = result_resp

        result = exec_and_wait_sync(client, "sb", ["echo", "ok"])

        assert result.stdout == "ok\n"
        assert result.exit_code == 0
        assert result.timed_out is False

    def test_polls_until_complete(self):
        exec_resp = MagicMock(exec_id="sync-poll")
        running_resp = MagicMock(status="running", exit_code=None, stdout="", stderr="")
        done_resp = MagicMock(status="completed", exit_code=0, stdout="done", stderr="")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox.return_value = exec_resp
        client.sandboxes.get_exec_result.side_effect = [running_resp, done_resp]

        with patch("islo.custom.exec.time.sleep"):
            result = exec_and_wait_sync(client, "sb", ["cmd"], poll_interval=0.001)

        assert result.stdout == "done"
        assert client.sandboxes.get_exec_result.call_count == 2

    def test_retries_on_transient_5xx(self):
        """Transient 5xx errors during polling should be retried, not raised."""
        exec_resp = MagicMock(exec_id="sync-retry")
        done_resp = MagicMock(status="completed", exit_code=0, stdout="ok", stderr="")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox.return_value = exec_resp
        client.sandboxes.get_exec_result.side_effect = [
            ApiError(status_code=502, body="Bad Gateway"),
            ApiError(status_code=503, body="Service Unavailable"),
            done_resp,
        ]

        with patch("islo.custom.exec.time.sleep"):
            result = exec_and_wait_sync(client, "sb", ["cmd"], poll_interval=0.001)

        assert result.exit_code == 0
        assert result.stdout == "ok"
        assert client.sandboxes.get_exec_result.call_count == 3

    def test_raises_after_max_consecutive_5xx(self):
        """After MAX_CONSECUTIVE_POLL_ERRORS 5xx errors, the exception propagates."""
        exec_resp = MagicMock(exec_id="sync-max-err")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox.return_value = exec_resp
        client.sandboxes.get_exec_result.side_effect = [
            ApiError(status_code=500, body="error") for _ in range(_MAX_CONSECUTIVE_POLL_ERRORS + 1)
        ]

        with patch("islo.custom.exec.time.sleep"):
            with pytest.raises(ApiError) as exc_info:
                exec_and_wait_sync(client, "sb", ["cmd"], timeout=60, poll_interval=0.001)

        assert exc_info.value.status_code == 500

    def test_does_not_retry_4xx(self):
        """Non-5xx errors (e.g. 404) should propagate immediately."""
        exec_resp = MagicMock(exec_id="sync-4xx")

        client = MagicMock()
        client.sandboxes.exec_in_sandbox.return_value = exec_resp
        client.sandboxes.get_exec_result.side_effect = ApiError(status_code=404, body="Not Found")

        with pytest.raises(ApiError) as exc_info:
            exec_and_wait_sync(client, "sb", ["cmd"])

        assert exc_info.value.status_code == 404
        assert client.sandboxes.get_exec_result.call_count == 1
