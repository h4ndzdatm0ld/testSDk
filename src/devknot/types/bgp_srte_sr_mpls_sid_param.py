# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpSrteSrMplsSidParam"]


class BgpSrteSrMplsSidParam(TypedDict, total=False):
    label: int
    """Label value in [0, 2^20 -1]."""

    s_bit: bool
    """Bottom-of-Stack bit."""

    tc: int
    """Traffic class in bits."""

    ttl: int
    """Time To Live."""
