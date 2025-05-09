# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BgpAttributesNextHop", "Ipv6TwoAddresses"]


class Ipv6TwoAddresses(BaseModel):
    first: Optional[str] = None
    """The first IPv6 next hop in the 32 byte IPv6 Next Hop."""

    second: Optional[str] = None
    """The second IPv6 next hop in the 32 byte IPv6 Next Hop."""


class BgpAttributesNextHop(BaseModel):
    choice: Literal["ipv4", "ipv6", "ipv6_two_addresses"]
    """The type of the next HOP."""

    ipv4: Optional[str] = None
    """The 4 byte IPv4 address of the next-hop from which the route was received."""

    ipv6: Optional[str] = None
    """The 16 byte IPv6 address of the next-hop from which the route was received."""

    ipv6_two_addresses: Optional[Ipv6TwoAddresses] = None
    """
    There is a specific scenario in which it is possible to receive a Global and
    Link Local address in the Next Hop field in a MP_REACH attribute or in the
    NEXT_HOP attribute(RFC2545: Section 3).
    """
