# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BgpSrteRemoteEndpointSubTlvParam"]


class BgpSrteRemoteEndpointSubTlvParam(TypedDict, total=False):
    address_family: Literal["ipv4", "ipv6"]
    """Determines the address type"""

    as_number: int
    """Autonomous system (AS) number"""

    ipv4_address: str
    """The IPv4 address of the Remote Endpoint."""

    ipv6_address: str
    """The IPv6 address of the Remote Endpoint."""
