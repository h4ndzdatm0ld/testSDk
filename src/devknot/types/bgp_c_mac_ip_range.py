# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .bgp_as_path import BgpAsPath
from .bgp_community import BgpCommunity
from .v4_route_address import V4RouteAddress
from .v6_route_address import V6RouteAddress
from .bgp_ext_community import BgpExtCommunity
from .bgp_route_advanced import BgpRouteAdvanced

__all__ = ["BgpCMacIPRange", "MacAddresses"]


class MacAddresses(BaseModel):
    address: str
    """The starting address of the MAC Range."""

    count: Optional[int] = None
    """The total number of mac addresses in the range."""

    prefix: Optional[int] = None
    """The MAC prefix length to be applied to the address."""

    step: Optional[int] = None
    """
    Increments the mac address prefixes within a mac range where multiple routes are
    present. The value is incremented according to the mac prefix Length and Step.
    """


class BgpCMacIPRange(BaseModel):
    name: str
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    advanced: Optional[BgpRouteAdvanced] = None
    """Configuration for advanced BGP route range settings."""

    as_path: Optional[BgpAsPath] = None
    """Optional AS PATH settings."""

    communities: Optional[List[BgpCommunity]] = None
    """Optional community settings."""

    ext_communities: Optional[List[BgpExtCommunity]] = None
    """Optional Extended Community settings.

    The Extended Communities Attribute is a transitive optional BGP attribute, with
    the Type Code 16. Community and Extended Communities attributes are utilized to
    trigger routing decisions, such as acceptance, rejection, preference, or
    redistribution. An extended community is an 8-Bytes value. It is divided into
    two main parts. The first 2 Bytes of the community encode a type and sub-type
    fields and the last 6 Bytes carry a unique set of data in a format defined by
    the type and sub-type field. Extended communities provide a larger range for
    grouping or categorizing communities. When type is administrator_as_2octet or
    administrator_as_4octet, the valid sub types are route target and origin. The
    valid value for administrator_as_2octet and administrator_as_4octet type is
    either two byte AS followed by four byte local administrator id or four byte AS
    followed by two byte local administrator id. When type is
    administrator_ipv4_address the valid sub types are route target and origin. The
    valid value for administrator_ipv4_address is a four byte IPv4 address followed
    by a two byte local administrator id. When type is opaque, valid sub types are
    color and encapsulation. When sub type is color, first two bytes of the value
    field contain flags and last four bytes contains the value of the color. When
    sub type is encapsulation the first four bytes of value field are reserved and
    last two bytes carries the tunnel type from IANA's "ETHER TYPES" registry e.g
    IPv4 (protocol type = 0x0800), IPv6 (protocol type = 0x86dd), and MPLS (protocol
    type = 0x8847). When type is administrator_as_2octet_link_bandwidth the valid
    sub type is extended_bandwidth. The first two bytes of the value field contains
    the AS number and the last four bytes contains the bandwidth in IEEE floating
    point format. When type is evpn the valid subtype is mac_address. In the value
    field the low-order bit of the first byte(Flags) is defined as the
    "Sticky/static" flag and may be set to 1, indicating the MAC address is static
    and cannot move. The second byte is reserved and the last four bytes contain the
    sequence number which is used to ensure that PEs retain the correct MAC/IP
    Advertisement route when multiple updates occur for the same MAC address.
    """

    include_default_gateway: Optional[bool] = None
    """
    Include default Gateway Extended Community in MAC/IP Advertisement Route (Type
    2).
    """

    ipv4_addresses: Optional[V4RouteAddress] = None
    """Host IPv4 address range per Broadcast Domain."""

    ipv6_addresses: Optional[V6RouteAddress] = None
    """Host IPv6 address range per Broadcast Domain."""

    l2vni: Optional[int] = None
    """
    Layer 2 Virtual Network Identifier (L2VNI) to be advertised with MAC/IP
    Advertisement Route (Type 2)
    """

    l3vni: Optional[int] = None
    """
    Layer 3 Virtual Network Identifier (L3VNI) to be advertised with MAC/IP
    Advertisement Route (Type 2).
    """

    mac_addresses: Optional[MacAddresses] = None
    """Host MAC address range per Broadcast Domain."""
