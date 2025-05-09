# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .bgp_as_path_param import BgpAsPathParam
from .bgp_add_path_param import BgpAddPathParam
from .bgp_community_param import BgpCommunityParam
from .v4_route_address_param import V4RouteAddressParam
from .bgp_ext_community_param import BgpExtCommunityParam
from .bgp_route_advanced_param import BgpRouteAdvancedParam
from .bgp_extended_community_param import BgpExtendedCommunityParam

__all__ = ["BgpV4RouteRangeParam"]


class BgpV4RouteRangeParam(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    add_path: BgpAddPathParam
    """
    The BGP Additional Paths feature is a BGP extension that allows the
    advertisement of multiple paths for the same prefix without the new paths
    implicitly replacing any previous paths.
    """

    addresses: Iterable[V4RouteAddressParam]
    """A list of group of IPv4 route addresses."""

    advanced: BgpRouteAdvancedParam
    """Configuration for advanced BGP route range settings."""

    as_path: BgpAsPathParam
    """
    This attribute identifies the autonomous systems through which routing
    information carried in this UPDATE message has passed. This contains the
    configuration of how to include the Local AS in the AS path attribute of the MP
    REACH NLRI. It also contains optional configuration of additional AS Path
    Segments that can be included in the AS Path attribute. The AS Path consists of
    a Set or Sequence of Autonomous Systems (AS) numbers that a routing information
    passes through to reach the destination.
    """

    communities: Iterable[BgpCommunityParam]
    """Optional community settings."""

    ext_communities: Iterable[BgpExtCommunityParam]
    """
    Deprecated: This property is deprecated in favor of property
    extended_communities

    Optional Extended Community settings. The Extended Communities Attribute is a
    transitive optional BGP attribute, with the Type Code 16. Community and Extended
    Communities attributes are utilized to trigger routing decisions, such as
    acceptance, rejection, preference, or redistribution. An extended community is
    an 8-Bytes value. It is divided into two main parts. The first 2 Bytes of the
    community encode a type and sub-type fields and the last 6 Bytes carry a unique
    set of data in a format defined by the type and sub-type field. Extended
    communities provide a larger range for grouping or categorizing communities.
    When type is administrator_as_2octet or administrator_as_4octet, the valid sub
    types are route target and origin. The valid value for administrator_as_2octet
    and administrator_as_4octet type is either two byte AS followed by four byte
    local administrator id or four byte AS followed by two byte local administrator
    id. When type is administrator_ipv4_address the valid sub types are route target
    and origin. The valid value for administrator_ipv4_address is a four byte IPv4
    address followed by a two byte local administrator id. When type is opaque,
    valid sub types are color and encapsulation. When sub type is color, first two
    bytes of the value field contain flags and last four bytes contains the value of
    the color. When sub type is encapsulation the first four bytes of value field
    are reserved and last two bytes carries the tunnel type from IANA's "ETHER
    TYPES" registry e.g IPv4 (protocol type = 0x0800), IPv6 (protocol type =
    0x86dd), and MPLS (protocol type = 0x8847). When type is
    administrator_as_2octet_link_bandwidth the valid sub type is extended_bandwidth.
    The first two bytes of the value field contains the AS number and the last four
    bytes contains the bandwidth in IEEE floating point format. When type is evpn
    the valid subtype is mac_address. In the value field the low-order bit of the
    first byte(Flags) is defined as the "Sticky/static" flag and may be set to 1,
    indicating the MAC address is static and cannot move. The second byte is
    reserved and the last four bytes contain the sequence number which is used to
    ensure that PEs retain the correct MAC/IP Advertisement route when multiple
    updates occur for the same MAC address. Note evpn type is defined mainly for use
    with evpn route updates and not for IPv4 and IPv6 route updates.
    """

    extended_communities: Iterable[BgpExtendedCommunityParam]
    """Optional Extended Community settings.

    The Extended Communities Attribute is a transitive optional BGP attribute, with
    the Type Code 16. Community and Extended Communities attributes are utilized to
    trigger routing decisions, such as acceptance, rejection, preference, or
    redistribution. An extended community is an eight byte value. It is divided into
    two main parts. The first two bytes of the community encode a type and sub-type
    fields and the last six bytes carry a unique set of data in a format defined by
    the type and sub-type field. Extended communities provide a larger range for
    grouping or categorizing communities.
    """

    next_hop_address_type: Literal["ipv4", "ipv6"]
    """If the Nexthop Mode is Manual, it sets the type of the NextHop IP address."""

    next_hop_ipv4_address: str
    """
    The IPv4 address of the next hop if the Nexthop Mode is manual and the Nexthop
    type is IPv4. If BGP peer is of type IPv6, Nexthop Encoding capability should be
    enabled.
    """

    next_hop_ipv6_address: str
    """
    The IPv6 address of the next hop if the Nexthop Mode is manual and the Nexthop
    type is IPv6.
    """

    next_hop_mode: Literal["local_ip", "manual"]
    """Specify the NextHop in MP REACH NLRI.

    The mode for setting the IP address of the NextHop in the MP REACH NLRI can be
    one of the following: Local IP: Automatically fills the Nexthop with the Local
    IP of the BGP peer. If BGP peer is of type IPv6, Nexthop Encoding capability
    should be enabled. Manual: Override the Nexthop with any arbitrary IPv4/IPv6
    address.
    """
