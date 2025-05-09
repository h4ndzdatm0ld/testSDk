# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PatternFlowIcmpv6EchoIdentifierCounterParam"]


class PatternFlowIcmpv6EchoIdentifierCounterParam(TypedDict, total=False):
    count: int

    start: int

    step: int
