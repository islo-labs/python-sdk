"""Agent run result generated from the public API contract."""

import typing

import pydantic

from ..core.pydantic_utilities import UniversalBaseModel


class AgentRunResponse(UniversalBaseModel):
    run_id: str
    status: str
    output: str | None = None
    error: str | None = None

    model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
