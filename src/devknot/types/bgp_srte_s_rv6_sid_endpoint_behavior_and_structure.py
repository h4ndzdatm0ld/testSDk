# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpSrteSRv6SidEndpointBehaviorAndStructure"]


class BgpSrteSRv6SidEndpointBehaviorAndStructure(BaseModel):
    arg_length: Optional[int] = None
    """SRv6 SID Arguments length in bits."""

    func_length: Optional[int] = None
    """SRv6 SID Function length in bits."""

    lb_length: Optional[int] = None
    """SRv6 SID Locator Block length in bits."""

    ln_length: Optional[int] = None
    """SRv6 SID Locator Node length in bits."""
