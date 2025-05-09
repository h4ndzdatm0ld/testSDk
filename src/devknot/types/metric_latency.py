# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MetricLatency"]


class MetricLatency(BaseModel):
    average_ns: Optional[float] = None
    """Average latency in nanoseconds"""

    maximum_ns: Optional[float] = None
    """Maximum latency in nanoseconds"""

    minimum_ns: Optional[float] = None
    """Minimum latency in nanoseconds"""
