"""Saved prompt Agent runs."""

from __future__ import annotations

from urllib.parse import quote

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pydantic_utilities import parse_obj_as
from ..types.agent_run_response import AgentRunResponse
from ..types.agent_session_response import AgentSessionResponse


def _path(factory: str, name: str, run_id: str | None = None) -> str:
    path = f"factories/{quote(factory, safe='')}/agents/{quote(name, safe='')}/sessions"
    return f"{path}/{quote(run_id, safe='')}" if run_id is not None else path


class AgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def start_factory_agent_session(
        self, factory: str, name: str, *, message: str
    ) -> AgentSessionResponse:
        response = self._client_wrapper.httpx_client.request(
            _path(factory, name),
            base_url=self._client_wrapper.get_environment().control,
            method="POST",
            json={"message": message},
            headers={"content-type": "application/json"},
        )
        response.raise_for_status()
        return parse_obj_as(type_=AgentSessionResponse, object_=response.json())

    def get_factory_agent_run(
        self, factory: str, name: str, job_run_id: str
    ) -> AgentRunResponse:
        response = self._client_wrapper.httpx_client.request(
            _path(factory, name, job_run_id),
            base_url=self._client_wrapper.get_environment().control,
            method="GET",
        )
        response.raise_for_status()
        return parse_obj_as(type_=AgentRunResponse, object_=response.json())


class AsyncAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def start_factory_agent_session(
        self, factory: str, name: str, *, message: str
    ) -> AgentSessionResponse:
        response = await self._client_wrapper.httpx_client.request(
            _path(factory, name),
            base_url=self._client_wrapper.get_environment().control,
            method="POST",
            json={"message": message},
            headers={"content-type": "application/json"},
        )
        response.raise_for_status()
        return parse_obj_as(type_=AgentSessionResponse, object_=response.json())

    async def get_factory_agent_run(
        self, factory: str, name: str, job_run_id: str
    ) -> AgentRunResponse:
        response = await self._client_wrapper.httpx_client.request(
            _path(factory, name, job_run_id),
            base_url=self._client_wrapper.get_environment().control,
            method="GET",
        )
        response.raise_for_status()
        return parse_obj_as(type_=AgentRunResponse, object_=response.json())
