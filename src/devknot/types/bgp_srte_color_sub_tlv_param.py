# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpSrteColorSubTlvParam"]


class BgpSrteColorSubTlvParam(TypedDict, total=False):
    color: str
    """Six octet values. Example: 000000000064 for color value 100."""
