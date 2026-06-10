"""Tests for the custom Islo client (api_key auth, env var detection, defaults)."""

from pytest_httpx import HTTPXMock

from islo import AsyncIslo, Islo
from islo.custom.auth import SyncTokenProvider
from islo.environment import IsloEnvironment


class TestIsloClient:
    def test_default_base_url(self, monkeypatch):
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        monkeypatch.delenv("ISLO_COMPUTE_URL", raising=False)
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        client = Islo()
        environment = client._client_wrapper.get_environment()
        assert environment.control == "https://api.islo.dev"
        assert environment.compute == "https://ca.compute.islo.dev"

    def test_env_base_url(self, monkeypatch):
        monkeypatch.setenv("ISLO_BASE_URL", "https://custom.example.com")
        monkeypatch.setenv("ISLO_COMPUTE_URL", "https://compute.example.com")
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        client = Islo()
        environment = client._client_wrapper.get_environment()
        assert environment.control == "https://custom.example.com"
        assert environment.compute == "https://compute.example.com"

    def test_explicit_base_url_overrides_env(self, monkeypatch):
        monkeypatch.setenv("ISLO_BASE_URL", "https://env.example.com")
        monkeypatch.setenv("ISLO_COMPUTE_URL", "https://compute.env.example.com")
        client = Islo(
            base_url="https://explicit.example.com",
            compute_url="https://compute.explicit.example.com",
        )
        environment = client._client_wrapper.get_environment()
        assert environment.control == "https://explicit.example.com"
        assert environment.compute == "https://compute.explicit.example.com"

    def test_environment_override(self, monkeypatch):
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        monkeypatch.delenv("ISLO_COMPUTE_URL", raising=False)
        client = Islo(
            environment=IsloEnvironment(
                control="https://control.environment.example.com",
                compute="https://compute.environment.example.com",
            )
        )
        environment = client._client_wrapper.get_environment()
        assert environment.control == "https://control.environment.example.com"
        assert environment.compute == "https://compute.environment.example.com"

    def test_explicit_urls_override_environment(self, monkeypatch):
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        monkeypatch.delenv("ISLO_COMPUTE_URL", raising=False)
        client = Islo(
            base_url="https://control.explicit.example.com",
            compute_url="https://compute.explicit.example.com",
            environment=IsloEnvironment(
                control="https://control.environment.example.com",
                compute="https://compute.environment.example.com",
            ),
        )
        environment = client._client_wrapper.get_environment()
        assert environment.control == "https://control.explicit.example.com"
        assert environment.compute == "https://compute.explicit.example.com"

    def test_api_key_creates_token_provider(self, monkeypatch):
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        client = Islo(api_key="ak_test_key")
        assert isinstance(client._client_wrapper._api_key, SyncTokenProvider)

    def test_env_api_key_creates_token_provider(self, monkeypatch):
        monkeypatch.setenv("ISLO_API_KEY", "ak_env_key")
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        client = Islo()
        assert isinstance(client._client_wrapper._api_key, SyncTokenProvider)

    def test_resource_clients_available(self, monkeypatch):
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        client = Islo()
        public_resource_clients = {
            name
            for cls in type(client).mro()
            for name, value in vars(cls).items()
            if isinstance(value, property) and not name.startswith("_")
        }

        assert public_resource_clients == {
            "cloud_roles",
            "credits",
            "gateway_profiles",
            "integrations",
            "sandboxes",
            "shares",
            "snapshots",
            "tenants",
        }

    def test_excluded_resource_clients_not_available(self, monkeypatch):
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        client = Islo()
        # /auth/token is x-fern-ignored on the API side; users go through
        # the hand-written custom/auth.py token providers instead.
        assert not hasattr(client, "auth")
        assert not hasattr(client, "api_keys")
        assert not hasattr(client, "usage")
        assert not hasattr(client, "certificate_authority")
        assert not hasattr(client, "users")
        assert not hasattr(client, "models")
        assert not hasattr(client, "compute")
        assert not hasattr(client, "sessions")


class TestAsyncIsloClient:
    def test_default_base_url(self, monkeypatch):
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        monkeypatch.delenv("ISLO_COMPUTE_URL", raising=False)
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        client = AsyncIslo()
        environment = client._client_wrapper.get_environment()
        assert environment.control == "https://api.islo.dev"
        assert environment.compute == "https://ca.compute.islo.dev"

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
        monkeypatch.delenv("ISLO_COMPUTE_URL", raising=False)

        httpx_mock.add_response(
            url="https://api.islo.dev/auth/token",
            json={"session_token": "jwt-from-exchange", "cookie_max_age": 600},
        )

        client = Islo(api_key="ak_test")
        token = client._client_wrapper._api_key()
        assert token == "jwt-from-exchange"

    def test_api_key_exchange_uses_custom_control_url(self, httpx_mock: HTTPXMock, monkeypatch):
        monkeypatch.delenv("ISLO_API_KEY", raising=False)
        monkeypatch.delenv("ISLO_BASE_URL", raising=False)
        monkeypatch.delenv("ISLO_COMPUTE_URL", raising=False)

        httpx_mock.add_response(
            url="https://control.customer.example.com/auth/token",
            json={"session_token": "jwt-from-custom-control", "cookie_max_age": 600},
        )

        client = Islo(
            api_key="ak_test",
            base_url="https://control.customer.example.com",
            compute_url="https://compute.customer.example.com",
        )
        token = client._client_wrapper._api_key()
        assert token == "jwt-from-custom-control"
