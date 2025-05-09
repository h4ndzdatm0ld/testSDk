# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .flow_param import FlowParam

__all__ = ["ConfigUpdateParams", "Flows"]


class ConfigUpdateParams(TypedDict, total=False):
    choice: Literal["flows"]

    flows: Flows
    """
    A container of flows with associated properties to be updated without affecting
    the flows current transmit state.
    """


class Flows(TypedDict, total=False):
    flows: Required[Iterable[FlowParam]]
    """The list of configured flows for which given property will be updated."""

    property_names: Required[List[Literal["rate", "size"]]]
    """Flow properties to be updated without affecting the transmit state."""
