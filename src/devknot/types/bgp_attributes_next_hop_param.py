# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BgpAttributesNextHopParam", "Ipv6TwoAddresses"]


class Ipv6TwoAddresses(TypedDict, total=False):
    first: str
    """The first IPv6 next hop in the 32 byte IPv6 Next Hop."""

    second: str
    """The second IPv6 next hop in the 32 byte IPv6 Next Hop."""


class BgpAttributesNextHopParam(TypedDict, total=False):
    choice: Required[Literal["ipv4", "ipv6", "ipv6_two_addresses"]]
    """The type of the next HOP."""

    ipv4: str
    """The 4 byte IPv4 address of the next-hop from which the route was received."""

    ipv6: str
    """The 16 byte IPv6 address of the next-hop from which the route was received."""

    ipv6_two_addresses: Ipv6TwoAddresses
    """
    There is a specific scenario in which it is possible to receive a Global and
    Link Local address in the Next Hop field in a MP_REACH attribute or in the
    NEXT_HOP attribute(RFC2545: Section 3).
    """
