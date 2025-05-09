# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BgpCommunity"]


class BgpCommunity(BaseModel):
    as_custom: Optional[int] = None
    """Last two octets of the community value."""

    as_number: Optional[int] = None
    """First two octets of 32 bit community AS number."""

    type: Optional[
        Literal["manual_as_number", "no_export", "no_advertised", "no_export_subconfed", "llgr_stale", "no_llgr"]
    ] = None
    """The type of community AS number."""
