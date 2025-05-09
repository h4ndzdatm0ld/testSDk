# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BgpRouteDistinguisherParam"]


class BgpRouteDistinguisherParam(TypedDict, total=False):
    auto_config_rd_ip_addr: bool
    """Allow to automatically configure RD IP address from local ip."""

    rd_type: Literal["as_2octet", "ipv4_address", "as_4octet"]
    """Route Distinguisher Type field of 2 Byte.

    - as_2octet: Two-Octet AS Specific Extended Community (RFC 4360).
    - ipv4_address: IPv4 Address Specific Extended Community (RFC 4360).
    - as_4octet: 4-Octet AS Specific Extended Community (RFC 5668).
    """

    rd_value: str
    """Colon separated Extended Community value of 6 Bytes - "AS number: Value".

    Example - for the as_2octet or as_4octet "60005:100", for ipv4_address
    "1.1.1.1:100"
    """
