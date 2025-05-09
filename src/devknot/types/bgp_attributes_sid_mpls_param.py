# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpAttributesSidMplsParam"]


class BgpAttributesSidMplsParam(TypedDict, total=False):
    flag_bos: bool
    """Bottom of Stack"""

    label: int
    """20 bit MPLS Label value."""

    traffic_class: int
    """3 bits of Traffic Class."""

    ttl: int
    """8 bits Time to Live"""
