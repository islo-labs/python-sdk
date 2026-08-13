"""Exec helpers: start a command and poll for completion."""

from __future__ import annotations

import asyncio
import math
import time
import typing

from pydantic import BaseModel

from ..core.api_error import ApiError

if typing.TYPE_CHECKING:
    from ..base_client import AsyncBaseIslo, BaseIslo

_TERMINAL_STATUSES = frozenset({"completed", "failed", "timeout"})
_MAX_CONSECUTIVE_POLL_ERRORS = 5


class ExecResult(BaseModel):
    """Result of an exec command."""

    stdout: str
    stderr: str
    exit_code: int
    timed_out: bool = False
    status: str = "completed"
    truncated: bool = False
    exec_id: str | None = None
    remote_may_be_running: bool = False


async def exec_and_wait(
    client: AsyncBaseIslo,
    sandbox_name: str,
    command: list[str],
    *,
    workdir: str | None = None,
    env: dict[str, str | None] | None = None,
    user: str | None = None,
    timeout: float | None = None,
    poll_interval: float = 2.0,
) -> ExecResult:
    """Start a command and poll until completion.

    Uses only generated SDK calls (with built-in retry + auth refresh):
    1. ``exec_in_sandbox()`` -- fire command, get ``exec_id``
    2. ``get_exec_result()`` -- poll until completed/failed/timeout

    When *timeout* is ``None`` the poll loop runs indefinitely, relying on
    the caller (e.g. ``asyncio.wait_for``) to enforce an outer deadline.
    """
    if timeout is not None and (type(timeout) not in {int, float} or not math.isfinite(timeout) or timeout <= 0):
        raise ValueError(f"timeout must be a positive finite number or None, got {timeout!r}")
    if type(poll_interval) not in {int, float} or not math.isfinite(poll_interval) or poll_interval <= 0:
        raise ValueError(f"poll_interval must be a positive finite number, got {poll_interval!r}")

    kwargs: dict[str, typing.Any] = {"command": command}
    if workdir is not None:
        kwargs["workdir"] = workdir
    if env is not None:
        kwargs["env"] = env
    if user is not None:
        kwargs["user"] = user
    if timeout is not None:
        # The API currently treats this as a compatibility hint. Sending it keeps
        # the helper forward-compatible with server-enforced exec deadlines while
        # the monotonic client deadline below still bounds the local wait today.
        kwargs["timeout_secs"] = max(1, math.ceil(timeout))

    resp = await client.sandboxes.exec_in_sandbox(sandbox_name, **kwargs)
    exec_id = resp.exec_id

    deadline = time.monotonic() + timeout if timeout is not None else None
    consecutive_errors = 0
    last_result: typing.Any = None
    while deadline is None or time.monotonic() < deadline:
        try:
            result = await client.sandboxes.get_exec_result(sandbox_name, exec_id)
            last_result = result
            consecutive_errors = 0
        except ApiError as e:
            if e.status_code is not None and e.status_code >= 500 and consecutive_errors < _MAX_CONSECUTIVE_POLL_ERRORS:
                consecutive_errors += 1
                await asyncio.sleep(poll_interval)
                continue
            raise
        if result.status in _TERMINAL_STATUSES:
            return ExecResult(
                stdout=result.stdout or "",
                stderr=result.stderr or "",
                exit_code=result.exit_code if result.exit_code is not None else -1,
                timed_out=result.status == "timeout",
                status=result.status,
                truncated=getattr(result, "truncated", False),
                exec_id=exec_id,
            )
        await asyncio.sleep(poll_interval)

    return ExecResult(
        stdout=(last_result.stdout or "") if last_result is not None else "",
        stderr=(last_result.stderr or "") if last_result is not None else "",
        exit_code=-1,
        timed_out=True,
        status="client_timeout",
        truncated=getattr(last_result, "truncated", False) if last_result is not None else False,
        exec_id=exec_id,
        # The public API does not currently expose exec cancellation. A local
        # polling timeout therefore cannot claim that the remote process stopped.
        remote_may_be_running=True,
    )


def exec_and_wait_sync(
    client: BaseIslo,
    sandbox_name: str,
    command: list[str],
    *,
    workdir: str | None = None,
    env: dict[str, str | None] | None = None,
    user: str | None = None,
    timeout: float | None = None,
    poll_interval: float = 2.0,
) -> ExecResult:
    """Synchronous version of :func:`exec_and_wait`."""
    if timeout is not None and (type(timeout) not in {int, float} or not math.isfinite(timeout) or timeout <= 0):
        raise ValueError(f"timeout must be a positive finite number or None, got {timeout!r}")
    if type(poll_interval) not in {int, float} or not math.isfinite(poll_interval) or poll_interval <= 0:
        raise ValueError(f"poll_interval must be a positive finite number, got {poll_interval!r}")

    kwargs: dict[str, typing.Any] = {"command": command}
    if workdir is not None:
        kwargs["workdir"] = workdir
    if env is not None:
        kwargs["env"] = env
    if user is not None:
        kwargs["user"] = user
    if timeout is not None:
        kwargs["timeout_secs"] = max(1, math.ceil(timeout))

    resp = client.sandboxes.exec_in_sandbox(sandbox_name, **kwargs)
    exec_id = resp.exec_id

    deadline = time.monotonic() + timeout if timeout is not None else None
    consecutive_errors = 0
    last_result: typing.Any = None
    while deadline is None or time.monotonic() < deadline:
        try:
            result = client.sandboxes.get_exec_result(sandbox_name, exec_id)
            last_result = result
            consecutive_errors = 0
        except ApiError as e:
            if e.status_code is not None and e.status_code >= 500 and consecutive_errors < _MAX_CONSECUTIVE_POLL_ERRORS:
                consecutive_errors += 1
                time.sleep(poll_interval)
                continue
            raise
        if result.status in _TERMINAL_STATUSES:
            return ExecResult(
                stdout=result.stdout or "",
                stderr=result.stderr or "",
                exit_code=result.exit_code if result.exit_code is not None else -1,
                timed_out=result.status == "timeout",
                status=result.status,
                truncated=getattr(result, "truncated", False),
                exec_id=exec_id,
            )
        time.sleep(poll_interval)

    return ExecResult(
        stdout=(last_result.stdout or "") if last_result is not None else "",
        stderr=(last_result.stderr or "") if last_result is not None else "",
        exit_code=-1,
        timed_out=True,
        status="client_timeout",
        truncated=getattr(last_result, "truncated", False) if last_result is not None else False,
        exec_id=exec_id,
        remote_may_be_running=True,
    )
