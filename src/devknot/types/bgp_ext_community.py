# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BgpExtCommunity"]


class BgpExtCommunity(BaseModel):
    subtype: Optional[
        Literal["route_target", "origin", "extended_bandwidth", "color", "encapsulation", "mac_address"]
    ] = None
    """Extended Community Sub Type field of 1 Byte.

    - route_target: Route Target.
    - origin: Origin.
    - extended_bandwidth: Specifies the link bandwidth.
    - color: Specifies the color value.
    - encapsulation: Specifies the Encapsulation Extended Community.
    - mac_address: Specifies the Extended community MAC address.
    """

    type: Optional[
        Literal[
            "administrator_as_2octet",
            "administrator_ipv4_address",
            "administrator_as_4octet",
            "opaque",
            "evpn",
            "administrator_as_2octet_link_bandwidth",
        ]
    ] = None
    """Extended Community Type field of 1 Byte.

    - administrator_as_2octet: Two-Octet AS Specific Extended Community (RFC 4360).
    - administrator_ipv4_address: IPv4 Address Specific Extended Community (RFC
      4360).
    - administrator_as_4octet: 4-Octet AS Specific Extended Community (RFC 5668).
    - opaque: Opaque Extended Community (RFC 7432).
    - evpn: EVPN Extended Community (RFC 7153).
    - administrator_as_2octet_link_bandwidth : Link Bandwidth Extended Community
      (RFC 7153).
    """

    value: Optional[str] = None
    """Extended Community value of 6 Bytes.

    Example - for the Opaque type and Color subtype value can be '0000000000c8' for
    the color value 200.
    """
