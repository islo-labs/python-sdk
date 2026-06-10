"""Tests for generated Pydantic types."""

from islo.types import (
    ErrorResponse,
    SandboxResponse,
    SandboxSpec,
)


class TestErrorResponse:
    def test_basic_fields(self):
        err = ErrorResponse(
            code="SANDBOX_NOT_FOUND",
            message="sandbox not found",
        )
        assert err.code == "SANDBOX_NOT_FOUND"
        assert err.message == "sandbox not found"

    def test_with_capacity_fields(self):
        err = ErrorResponse(
            code="INSUFFICIENT_RESOURCES",
            message="not enough capacity",
            available=2,
            limit=8,
            requested=4,
            resource="vcpus",
        )
        assert err.available == 2
        assert err.limit == 8
        assert err.requested == 4
        assert err.resource == "vcpus"

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
            created_at="2026-05-28T00:00:00Z",
            spec=SandboxSpec(vcpus=2, memory_mb=4096, disk_gb=10),
        )
        assert sandbox.name == "test-sandbox"
        assert sandbox.status == "running"
        assert sandbox.spec.vcpus == 2
        assert sandbox.created_at == "2026-05-28T00:00:00Z"
