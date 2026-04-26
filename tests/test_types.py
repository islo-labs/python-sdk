"""Tests for generated Pydantic types."""

from islo.types import (
    ErrorResponse,
    SandboxResponse,
    SandboxSpec,
    TokenResponse,
)


class TestErrorResponse:
    def test_basic_fields(self):
        err = ErrorResponse(
            code="SANDBOX_NOT_FOUND",
            message="sandbox not found",
        )
        assert err.code == "SANDBOX_NOT_FOUND"
        assert err.message == "sandbox not found"
        assert err.hint is None

    def test_with_hint(self):
        err = ErrorResponse(
            code="VALIDATION_ERROR",
            message="bad input",
            hint="check the name field",
        )
        assert err.hint == "check the name field"

    def test_extra_fields_allowed(self):
        err = ErrorResponse(
            code="INTERNAL_ERROR",
            message="error",
            extra_field="should not raise",
        )
        assert err.message == "error"


class TestSandboxResponse:
    def test_required_fields(self):
        sandbox = SandboxResponse(
            id="uuid-1234",
            name="test-sandbox",
            status="running",
            image="ubuntu:22.04",
            spec=SandboxSpec(vcpus=2, memory_mb=4096, disk_gb=10),
        )
        assert sandbox.name == "test-sandbox"
        assert sandbox.status == "running"
        assert sandbox.spec.vcpus == 2


class TestTokenResponse:
    def test_fields(self):
        token = TokenResponse(session_token="jwt-abc")
        assert token.session_token == "jwt-abc"
