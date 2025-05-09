# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BgpCommunityParam"]


class BgpCommunityParam(TypedDict, total=False):
    as_custom: int
    """Last two octets of the community value."""

    as_number: int
    """First two octets of 32 bit community AS number."""

    type: Literal["manual_as_number", "no_export", "no_advertised", "no_export_subconfed", "llgr_stale", "no_llgr"]
    """The type of community AS number."""
