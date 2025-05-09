# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpSrteSRv6SidEndpointBehaviorAndStructureParam"]


class BgpSrteSRv6SidEndpointBehaviorAndStructureParam(TypedDict, total=False):
    arg_length: int
    """SRv6 SID Arguments length in bits."""

    func_length: int
    """SRv6 SID Function length in bits."""

    lb_length: int
    """SRv6 SID Locator Block length in bits."""

    ln_length: int
    """SRv6 SID Locator Node length in bits."""
