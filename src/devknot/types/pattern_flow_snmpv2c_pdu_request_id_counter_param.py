# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PatternFlowSnmpv2cPduRequestIDCounterParam"]


class PatternFlowSnmpv2cPduRequestIDCounterParam(TypedDict, total=False):
    count: int

    start: int

    step: int
