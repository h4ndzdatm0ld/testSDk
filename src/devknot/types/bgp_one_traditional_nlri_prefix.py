# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .bgp_nlri_prefix_path_id import BgpNlriPrefixPathID

__all__ = ["BgpOneTraditionalNlriPrefix"]


class BgpOneTraditionalNlriPrefix(BaseModel):
    address: Optional[str] = None
    """The IPv4 address of the network."""

    path_id: Optional[BgpNlriPrefixPathID] = None
    """Optional field in the NLRI carrying Path Id of the prefix."""

    prefix: Optional[int] = None
    """The IPv4 network prefix length to be applied to the address."""
