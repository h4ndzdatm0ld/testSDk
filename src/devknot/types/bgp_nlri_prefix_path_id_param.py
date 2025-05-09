# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpNlriPrefixPathIDParam"]


class BgpNlriPrefixPathIDParam(TypedDict, total=False):
    value: int
    """The value of the optional Path ID of the prefix."""
