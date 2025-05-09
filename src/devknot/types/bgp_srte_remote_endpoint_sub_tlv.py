# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BgpSrteRemoteEndpointSubTlv"]


class BgpSrteRemoteEndpointSubTlv(BaseModel):
    address_family: Optional[Literal["ipv4", "ipv6"]] = None
    """Determines the address type"""

    as_number: Optional[int] = None
    """Autonomous system (AS) number"""

    ipv4_address: Optional[str] = None
    """The IPv4 address of the Remote Endpoint."""

    ipv6_address: Optional[str] = None
    """The IPv6 address of the Remote Endpoint."""
