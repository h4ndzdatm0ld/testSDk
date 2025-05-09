# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MetricTimestamp"]


class MetricTimestamp(BaseModel):
    first_timestamp_ns: Optional[float] = None
    """First timestamp in nanoseconds"""

    last_timestamp_ns: Optional[float] = None
    """Last timestamp in nanoseconds"""
