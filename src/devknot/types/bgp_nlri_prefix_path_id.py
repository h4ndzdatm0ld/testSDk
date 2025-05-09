# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpNlriPrefixPathID"]


class BgpNlriPrefixPathID(BaseModel):
    value: Optional[int] = None
    """The value of the optional Path ID of the prefix."""
