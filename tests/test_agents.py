import pytest
from pytest_httpx import HTTPXMock

from islo import AsyncIslo, Islo


def test_saved_agent_run_contract(httpx_mock: HTTPXMock, monkeypatch):
    monkeypatch.delenv("ISLO_API_KEY", raising=False)
    httpx_mock.add_response(
        method="POST",
        url="https://api.islo.dev/factories/team/agents/verifier/sessions",
        json={
            "job_run_id": "run-1",
            "sandbox_name": "sandbox",
            "session_name": "session",
            "region": "region",
        },
        status_code=201,
    )
    httpx_mock.add_response(
        method="GET",
        url="https://api.islo.dev/factories/team/agents/verifier/sessions/run-1",
        json={"run_id": "run-1", "status": "succeeded", "output": "Passed", "error": None},
    )
    client = Islo()
    session = client.agents.start_factory_agent_session("team", "verifier", message="Verify PR")
    result = client.agents.get_factory_agent_run("team", "verifier", session.job_run_id)
    assert result.output == "Passed"


@pytest.mark.asyncio
async def test_agent_run_error_is_preserved(httpx_mock: HTTPXMock, monkeypatch):
    monkeypatch.delenv("ISLO_API_KEY", raising=False)
    httpx_mock.add_response(
        method="GET",
        url="https://api.islo.dev/factories/team/agents/verifier/sessions/run-1",
        json={"run_id": "run-1", "status": "failed", "output": None, "error": "Machine unavailable"},
    )
    client = AsyncIslo()
    result = await client.agents.get_factory_agent_run("team", "verifier", "run-1")
    assert result.error == "Machine unavailable"
