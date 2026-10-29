"""Agent session creation generated from the public API contract."""

import typing

import pydantic

from ..core.pydantic_utilities import UniversalBaseModel


class AgentSessionResponse(UniversalBaseModel):
    job_run_id: str
    sandbox_name: str
    session_name: str
    region: str

    model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
