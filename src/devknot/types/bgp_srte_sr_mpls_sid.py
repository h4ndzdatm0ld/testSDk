# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpSrteSrMplsSid"]


class BgpSrteSrMplsSid(BaseModel):
    label: Optional[int] = None
    """Label value in [0, 2^20 -1]."""

    s_bit: Optional[bool] = None
    """Bottom-of-Stack bit."""

    tc: Optional[int] = None
    """Traffic class in bits."""

    ttl: Optional[int] = None
    """Time To Live."""
