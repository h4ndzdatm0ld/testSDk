# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FlowDelay"]


class FlowDelay(BaseModel):
    bytes: Optional[float] = None
    """
    The delay before starting transmission of packets. A value of 0 indicates no
    delay.
    """

    choice: Optional[Literal["bytes", "nanoseconds", "microseconds"]] = None

    microseconds: Optional[float] = None
    """
    The delay before starting transmission of packets. A value of 0 indicates no
    delay.
    """

    nanoseconds: Optional[float] = None
    """
    The delay before starting transmission of packets. A value of 0 indicates no
    delay.
    """
