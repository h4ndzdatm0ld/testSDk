# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FlowDelayParam"]


class FlowDelayParam(TypedDict, total=False):
    bytes: float
    """
    The delay before starting transmission of packets. A value of 0 indicates no
    delay.
    """

    choice: Literal["bytes", "nanoseconds", "microseconds"]

    microseconds: float
    """
    The delay before starting transmission of packets. A value of 0 indicates no
    delay.
    """

    nanoseconds: float
    """
    The delay before starting transmission of packets. A value of 0 indicates no
    delay.
    """
