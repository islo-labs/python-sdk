"""Tests for the custom Islo client (api_key auth, env var detection, defaults)."""

from pytest_httpx import HTTPXMock

from islo import AsyncIslo, Islo
from islo.custom.auth import SyncTokenProvider


class TestIsloClient:
    def test_default_base_url(self, monkeypatch):
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        client = Islo()
        assert "api.islo.dev" in client._client_wrapper._base_url

    def test_env_base_url(self, monkeypatch):
        monkeypatch.setenv("ISLO_BASE_URL", "https://custom.example.com")
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        client = Islo()
        assert "custom.example.com" in client._client_wrapper._base_url

    def test_explicit_base_url_overrides_env(self, monkeypatch):
        monkeypatch.setenv("ISLO_BASE_URL", "https://env.example.com")
        client = Islo(base_url="https://explicit.example.com")
        assert "explicit.example.com" in client._client_wrapper._base_url

    def test_api_key_creates_token_provider(self, monkeypatch):
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        client = Islo(api_key="ak_test_key")
        assert isinstance(client._client_wrapper._token, SyncTokenProvider)

    def test_env_api_key_creates_token_provider(self, monkeypatch):
        monkeypatch.setenv("ISLO_API_KEY", "ak_env_key")
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        client = Islo()
        assert isinstance(client._client_wrapper._token, SyncTokenProvider)

    def test_explicit_token_bypasses_exchange(self, monkeypatch):
        monkeypatch.setenv("ISLO_API_KEY", "ak_should_be_ignored")
        client = Islo(token="pre-existing-jwt")
        assert client._client_wrapper._token == "pre-existing-jwt"

    def test_token_takes_precedence_over_api_key(self):
        client = Islo(api_key="ak_ignored", token="jwt-wins")
        assert client._client_wrapper._token == "jwt-wins"

    def test_resource_clients_available(self, monkeypatch):
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        client = Islo()
        assert hasattr(client, "sandboxes")
        assert hasattr(client, "integrations")

    def test_excluded_resource_clients_not_available(self, monkeypatch):
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        client = Islo()
        # /auth/token is x-fern-ignored on the API side; users go through
        # the hand-written custom/auth.py token providers instead.
        assert not hasattr(client, "auth")
        assert not hasattr(client, "api_keys")
        assert not hasattr(client, "shares")
        assert not hasattr(client, "usage")
        assert not hasattr(client, "certificate_authority")
        assert not hasattr(client, "tenants")
        assert not hasattr(client, "users")
        assert not hasattr(client, "models")


class TestAsyncIsloClient:
    def test_default_base_url(self, monkeypatch):
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        client = AsyncIslo()
        assert "api.islo.dev" in client._client_wrapper._base_url

    def test_api_key_creates_async_token_provider(self, monkeypatch):
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        from islo.custom.auth import AsyncTokenProvider

        client = AsyncIslo(api_key="ak_test_key")
        assert isinstance(client._client_wrapper._async_token, AsyncTokenProvider)

    def test_explicit_async_token_bypasses_exchange(self, monkeypatch):
        monkeypatch.delenv("ISLO_API_KEY", raising=False)

        async def my_token():
            return "custom-jwt"

        client = AsyncIslo(async_token=my_token)
        assert client._client_wrapper._async_token is my_token


class TestTokenProviderIntegration:
    def test_api_key_exchange_on_first_call(self, httpx_mock: HTTPXMock, monkeypatch):
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)

        httpx_mock.add_response(
            url="https://api.islo.dev/auth/token",
            json={"session_token": "jwt-from-exchange", "cookie_max_age": 600},
        )

        client = Islo(api_key="ak_test")
        token = client._client_wrapper._token()
        assert token == "jwt-from-exchange"
