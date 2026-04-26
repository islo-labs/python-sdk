"""Tests for the custom auth helpers."""

import httpx
import pytest
from pytest_httpx import HTTPXMock

from islo.custom.auth import SyncTokenProvider, exchange_access_key


@pytest.fixture(autouse=True)
def _clear_borg_state():
    """Clear shared Borg state between tests."""
    SyncTokenProvider._shared.clear()
    yield
    SyncTokenProvider._shared.clear()


class TestExchangeAccessKey:
    def test_success(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(
            url="https://api.islo.dev/auth/token",
            json={"session_token": "jwt-abc"},
        )

        result = exchange_access_key("https://api.islo.dev", "ak_test_key")
        assert result["session_token"] == "jwt-abc"

    def test_unauthorized(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(
            url="https://api.islo.dev/auth/token",
            status_code=401,
        )

        with pytest.raises(httpx.HTTPStatusError):
            exchange_access_key("https://api.islo.dev", "bad-key")


class TestSyncTokenProvider:
    def test_calls_exchange_and_caches(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(
            url="https://api.islo.dev/auth/token",
            json={"session_token": "jwt-cached", "cookie_max_age": 600},
        )

        provider = SyncTokenProvider("https://api.islo.dev", "ak_test")
        token1 = provider()
        token2 = provider()

        assert token1 == "jwt-cached"
        assert token2 == "jwt-cached"
        assert len(httpx_mock.get_requests()) == 1

    def test_refreshes_when_expired(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(
            url="https://api.islo.dev/auth/token",
            json={"session_token": "jwt-first", "cookie_max_age": 0},
        )

        provider = SyncTokenProvider("https://api.islo.dev", "ak_test", refresh_margin_sec=0)
        token1 = provider()
        assert token1 == "jwt-first"

        httpx_mock.add_response(
            url="https://api.islo.dev/auth/token",
            json={"session_token": "jwt-second", "cookie_max_age": 600},
        )

        token2 = provider()
        assert token2 == "jwt-second"
        assert len(httpx_mock.get_requests()) == 2

    def test_borg_shares_state_across_instances(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(
            url="https://api.islo.dev/auth/token",
            json={"session_token": "jwt-shared", "cookie_max_age": 600},
        )

        provider_a = SyncTokenProvider("https://api.islo.dev", "ak_same_key")
        provider_b = SyncTokenProvider("https://api.islo.dev", "ak_same_key")

        token_a = provider_a()
        token_b = provider_b()

        assert token_a == "jwt-shared"
        assert token_b == "jwt-shared"
        assert len(httpx_mock.get_requests()) == 1

    def test_borg_different_keys_are_independent(self, httpx_mock: HTTPXMock):
        httpx_mock.add_response(
            url="https://api.islo.dev/auth/token",
            json={"session_token": "jwt-key-1", "cookie_max_age": 600},
        )

        provider_a = SyncTokenProvider("https://api.islo.dev", "ak_key_1")
        provider_a()

        httpx_mock.add_response(
            url="https://api.islo.dev/auth/token",
            json={"session_token": "jwt-key-2", "cookie_max_age": 600},
        )

        provider_b = SyncTokenProvider("https://api.islo.dev", "ak_key_2")
        token_b = provider_b()

        assert token_b == "jwt-key-2"
        assert len(httpx_mock.get_requests()) == 2
