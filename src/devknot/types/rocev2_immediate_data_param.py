# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Rocev2ImmediateDataParam"]


class Rocev2ImmediateDataParam(TypedDict, total=False):
    immediate_data: str
    """Four bytes of immediate Data for SEND/WRITE with immediate."""
