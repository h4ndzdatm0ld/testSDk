# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .bgp_as_path_param import BgpAsPathParam
from .bgp_add_path_param import BgpAddPathParam
from .bgp_community_param import BgpCommunityParam
from .bgp_ext_community_param import BgpExtCommunityParam
from .bgp_route_advanced_param import BgpRouteAdvancedParam
from .bgp_srte_segment_list_param import BgpSrteSegmentListParam
from .bgp_srte_color_sub_tlv_param import BgpSrteColorSubTlvParam
from .bgp_srte_binding_sub_tlv_param import BgpSrteBindingSubTlvParam
from .bgp_srte_preference_sub_tlv_param import BgpSrtePreferenceSubTlvParam
from .bgp_srte_policy_name_sub_tlv_param import BgpSrtePolicyNameSubTlvParam
from .bgp_srte_policy_priority_sub_tlv_param import BgpSrtePolicyPrioritySubTlvParam
from .bgp_srte_remote_endpoint_sub_tlv_param import BgpSrteRemoteEndpointSubTlvParam
from .bgp_srte_explicit_null_label_policy_sub_tlv_param import BgpSrteExplicitNullLabelPolicySubTlvParam

__all__ = ["BgpSrteV6PolicyParam", "TunnelTlv"]


class TunnelTlv(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    active: bool
    """
    If enabled means that this part of the configuration including any active
    'children' nodes will be advertised to peer. If disabled, this means that though
    config is present, it is not taking any part of the test but can be activated at
    run-time to advertise just this part of the configuration to the peer.
    """

    binding_sub_tlv: BgpSrteBindingSubTlvParam
    """Configuration for the binding SID sub-TLV.

    This is used to signal the binding SID related information of the SR Policy
    candidate path.
    """

    color_sub_tlv: BgpSrteColorSubTlvParam
    """Configuration for the Policy Color attribute sub-TLV.

    The Color sub-TLV MAY be used as a way to "color" the corresponding Tunnel TLV.
    The Value field of the sub-TLV is eight octets long and consists of a Color
    Extended Community. First two octets of its Value field are 0x030b as type and
    subtype of extended community. Remaining six octets are are exposed to
    configure.
    """

    explicit_null_label_policy_sub_tlv: BgpSrteExplicitNullLabelPolicySubTlvParam
    """Configuration for BGP explicit null label policy sub TLV settings."""

    policy_name_sub_tlv: BgpSrtePolicyNameSubTlvParam
    """Configuration for the Policy Name sub-TLV.

    The Policy Name sub-TLV is used to attach a symbolic name to the SR Policy
    candidate path.
    """

    policy_priority_sub_tlv: BgpSrtePolicyPrioritySubTlvParam
    """Configuration for the Policy Priority sub-TLV.

    The Policy Priority to indicate the order in which the SR policies are
    re-computed upon topological change.
    """

    preference_sub_tlv: BgpSrtePreferenceSubTlvParam
    """Configuration for BGP preference sub TLV of the SR Policy candidate path."""

    remote_endpoint_sub_tlv: BgpSrteRemoteEndpointSubTlvParam
    """Configuration for the BGP remote endpoint sub TLV."""

    segment_lists: Iterable[BgpSrteSegmentListParam]


class BgpSrteV6PolicyParam(TypedDict, total=False):
    ipv6_endpoint: Required[str]
    """Specifies a single node or a set of nodes (e.g., an anycast address).

    It is selected on the basis of the SR Policy type (AFI).
    """

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    active: bool
    """
    If enabled means that this part of the configuration including any active
    'children' nodes will be advertised to peer. If disabled, this means that though
    config is present, it is not taking any part of the test but can be activated at
    run-time to advertise just this part of the configuration to the peer.
    """

    add_path: BgpAddPathParam
    """
    The BGP Additional Paths feature is a BGP extension that allows the
    advertisement of multiple paths for the same prefix without the new paths
    implicitly replacing any previous paths.
    """

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

    color: int
    """Identifies the policy.

    It is used to match the color of the destination prefixes to steer traffic into
    the SR Policy.
    """

    communities: Iterable[BgpCommunityParam]
    """Optional community settings."""

    distinguisher: int
    """Identifies the policy in the context of (color and endpoint) tuple.

    It is used by the SR Policy originator to make unique multiple occurrences of
    the same SR Policy.
    """

    extcommunities: Iterable[BgpExtCommunityParam]
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

    next_hop_address_type: Literal["ipv4", "ipv6"]
    """Type of next hop IP address to be used when 'next_hop_mode' is set to 'manual'."""

    next_hop_ipv4_address: str
    """
    The IPv4 address of the Nexthop if the 'next_hop_mode' is 'manual' and the
    Nexthop type 'next_hop_address_type' is IPv4. If BGP peer is of type IPv6,
    Nexthop Encoding capability extended_next_hop_encoding should be enabled.
    """

    next_hop_ipv6_address: str
    """
    The IPv6 address of the next hop if the Nexthop Mode 'next_hop_address_type' is
    'manual' and the Nexthop type 'next_hop_address_type' is IPv6.
    """

    next_hop_mode: Literal["local_ip", "manual"]
    """Mode for choosing the NextHop in MP REACH NLRI.

    Available modes are : Local IP: Automatically fills the Nexthop with the Local
    IP of the BGP peer. For IPv6 BGP peer the Nexthop Encoding capability should be
    enabled. Manual: Override the Nexthop with any arbitrary IPv4/IPv6 address.
    """

    tunnel_tlvs: Iterable[TunnelTlv]
    """List of optional tunnel TLV settings."""
