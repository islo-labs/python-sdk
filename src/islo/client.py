"""Islo SDK client with automatic API key exchange and token refresh."""

from __future__ import annotations

import os
import typing

import httpx

from .base_client import AsyncBaseIslo, BaseIslo
from .core.logging import LogConfig, Logger
from .custom.auth import AsyncTokenProvider, SyncTokenProvider

_DEFAULT_BASE_URL = "https://api.islo.dev"
_ENV_API_KEY = "ISLO_API_KEY"
_ENV_BASE_URL = "ISLO_BASE_URL"


def _resolve_auth(
    base_url: str,
    api_key: str | None,
    token: str | typing.Callable[[], str] | None,
) -> str | typing.Callable[[], str] | None:
    """Resolve authentication: api_key → auto-refreshing provider, token → passthrough."""
    if token is not None:
        return token
    resolved_key = api_key or os.environ.get(_ENV_API_KEY)
    if resolved_key is not None:
        return SyncTokenProvider(base_url, resolved_key)
    return None


def _resolve_async_auth(
    base_url: str,
    api_key: str | None,
    token: str | typing.Callable[[], str] | None,
    async_token: typing.Callable[[], typing.Awaitable[str]] | None,
) -> tuple[str | typing.Callable[[], str] | None, typing.Callable[[], typing.Awaitable[str]] | None]:
    """Resolve async authentication: api_key → async provider, token/async_token → passthrough."""
    if async_token is not None or token is not None:
        return token, async_token
    resolved_key = api_key or os.environ.get(_ENV_API_KEY)
    if resolved_key is not None:
        return None, AsyncTokenProvider(base_url, resolved_key)
    return None, None


class Islo(BaseIslo):
    """Islo sandbox platform client (synchronous).

    Provide an ``api_key`` and the client automatically exchanges it for
    a session JWT and refreshes it before expiry.

    .. code-block:: python

        client = Islo(api_key="ak_...")
        # or set ISLO_API_KEY env var
        client = Islo()

    Parameters
    ----------
    api_key : str, optional
        Islo API key (Descope access key). Exchanged for a short-lived JWT
        automatically. Falls back to the ``ISLO_API_KEY`` environment variable.
    token : str or callable, optional
        Pre-existing JWT or callable returning a JWT. When provided,
        ``api_key`` is ignored and no exchange occurs.
    base_url : str, optional
        API base URL. Defaults to ``ISLO_BASE_URL`` env var or
        ``https://api.islo.dev``.
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        token: str | typing.Callable[[], str] | None = None,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
        follow_redirects: bool | None = True,
        httpx_client: httpx.Client | None = None,
        logging: LogConfig | Logger | None = None,
    ):
        resolved_base_url = base_url or os.environ.get(_ENV_BASE_URL, _DEFAULT_BASE_URL)
        resolved_token = _resolve_auth(resolved_base_url, api_key, token)

        super().__init__(
            base_url=resolved_base_url,
            api_key=resolved_token,
            headers=headers,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
        )


class AsyncIslo(AsyncBaseIslo):
    """Islo sandbox platform client (asynchronous).

    Provide an ``api_key`` and the client automatically exchanges it for
    a session JWT and refreshes it before expiry.

    .. code-block:: python

        client = AsyncIslo(api_key="ak_...")
        # or set ISLO_API_KEY env var
        client = AsyncIslo()

    Parameters
    ----------
    api_key : str, optional
        Islo API key (Descope access key). Exchanged for a short-lived JWT
        automatically. Falls back to the ``ISLO_API_KEY`` environment variable.
    token : str or callable, optional
        Pre-existing JWT. When provided, ``api_key`` is ignored.
    async_token : callable, optional
        Async callable returning a JWT. When provided, ``api_key`` is ignored.
    base_url : str, optional
        API base URL. Defaults to ``ISLO_BASE_URL`` env var or
        ``https://api.islo.dev``.
    """

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        token: str | typing.Callable[[], str] | None = None,
        async_token: typing.Callable[[], typing.Awaitable[str]] | None = None,
        headers: dict[str, str] | None = None,
        timeout: float | None = None,
        follow_redirects: bool | None = True,
        httpx_client: httpx.AsyncClient | None = None,
        logging: LogConfig | Logger | None = None,
    ):
        resolved_base_url = base_url or os.environ.get(_ENV_BASE_URL, _DEFAULT_BASE_URL)
        resolved_token, resolved_async_token = _resolve_async_auth(resolved_base_url, api_key, token, async_token)

        super().__init__(
            base_url=resolved_base_url,
            api_key=resolved_token,
            headers=headers,
            async_token=resolved_async_token,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            logging=logging,
        )
