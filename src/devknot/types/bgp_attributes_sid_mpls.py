# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpAttributesSidMpls"]


class BgpAttributesSidMpls(BaseModel):
    flag_bos: Optional[bool] = None
    """Bottom of Stack"""

    label: Optional[int] = None
    """20 bit MPLS Label value."""

    traffic_class: Optional[int] = None
    """3 bits of Traffic Class."""

    ttl: Optional[int] = None
    """8 bits Time to Live"""
