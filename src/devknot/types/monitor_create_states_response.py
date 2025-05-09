# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .ospfv2_lsa_header import Ospfv2LsaHeader
from .ospfv3_lsa_header import Ospfv3LsaHeader
from .isis_lsp_v4_prefix import IsisLspV4Prefix
from .result_bgp_as_path import ResultBgpAsPath
from .isis_lsp_prefix_sid import IsisLspPrefixSid
from .result_bgp_community import ResultBgpCommunity
from .result_extended_community import ResultExtendedCommunity
from .isis_lsp_prefix_attributes import IsisLspPrefixAttributes

__all__ = [
    "MonitorCreateStatesResponse",
    "BgpPrefix",
    "BgpPrefixIpv4UnicastPrefix",
    "BgpPrefixIpv6UnicastPrefix",
    "Dhcpv4Interface",
    "Dhcpv4Lease",
    "Dhcpv4LeaseLease",
    "Dhcpv6Interface",
    "Dhcpv6InterfaceIaAddress",
    "Dhcpv6InterfaceIapdAddress",
    "Dhcpv6Lease",
    "Dhcpv6LeaseLease",
    "Ipv4Neighbor",
    "Ipv6Neighbor",
    "IsisLsp",
    "IsisLspLsp",
    "IsisLspLspFlags",
    "IsisLspLspTlvs",
    "IsisLspLspTlvsExtendedIpv4ReachabilityTlv",
    "IsisLspLspTlvsExtendedIpv4ReachabilityTlvPrefix",
    "IsisLspLspTlvsExtendedIsReachabilityTlv",
    "IsisLspLspTlvsExtendedIsReachabilityTlvNeighbor",
    "IsisLspLspTlvsExtendedIsReachabilityTlvNeighborAdjacencySid",
    "IsisLspLspTlvsExtendedIsReachabilityTlvNeighborAdjacencySidFlags",
    "IsisLspLspTlvsHostnameTlv",
    "IsisLspLspTlvsIpv4ExternalReachabilityTlv",
    "IsisLspLspTlvsIpv4InternalReachabilityTlv",
    "IsisLspLspTlvsIpv6ReachabilityTlv",
    "IsisLspLspTlvsIpv6ReachabilityTlvPrefix",
    "IsisLspLspTlvsIsReachabilityTlv",
    "IsisLspLspTlvsIsReachabilityTlvNeighbor",
    "IsisLspLspTlvsRouterCapability",
    "IsisLspLspTlvsRouterCapabilitySrCapability",
    "IsisLspLspTlvsRouterCapabilitySrCapabilityFlags",
    "IsisLspLspTlvsRouterCapabilitySrCapabilitySrgbRange",
    "IsisLspLspTlvsRouterCapabilitySrlbRange",
    "LldpNeighbor",
    "LldpNeighborCapability",
    "LldpNeighborCustomTlv",
    "Ospfv2Lsa",
    "Ospfv2LsaExternalAsLsa",
    "Ospfv2LsaNetworkLsa",
    "Ospfv2LsaNetworkSummaryLsa",
    "Ospfv2LsaNssaLsa",
    "Ospfv2LsaOpaqueLsa",
    "Ospfv2LsaRouterLsa",
    "Ospfv2LsaRouterLsaLink",
    "Ospfv2LsaSummaryAsLsa",
    "Ospfv3Lsa",
    "Ospfv3LsaExternalAsLsa",
    "Ospfv3LsaInterAreaPrefixLsa",
    "Ospfv3LsaInterAreaRouterLsa",
    "Ospfv3LsaIntraAreaPrefixLsa",
    "Ospfv3LsaLinkLsa",
    "Ospfv3LsaNetworkLsa",
    "Ospfv3LsaNssaLsa",
    "Ospfv3LsaRouterLsa",
    "Ospfv3LsaRouterLsaLink",
    "RsvpLsp",
    "RsvpLspIpv4Lsp",
    "RsvpLspIpv4LspEro",
    "RsvpLspIpv4LspLsp",
    "RsvpLspIpv4LspRro",
]


class BgpPrefixIpv4UnicastPrefix(BaseModel):
    as_path: Optional[ResultBgpAsPath] = None
    """
    This attribute identifies the autonomous systems through which routing
    information carried in this UPDATE message has passed.
    """

    communities: Optional[List[ResultBgpCommunity]] = None
    """Optional community attributes."""

    extended_communities: Optional[List[ResultExtendedCommunity]] = None
    """Optional received Extended Community attributes.

    Each received Extended Community attribute is available for retrieval in two
    forms. Support of the 'raw' format in which all 8 bytes (16 hex characters) is
    always present and available for use. In addition, if supported by the
    implementation, the Extended Community attribute may also be retrieved in the
    'structured' format which is an optional field.
    """

    ipv4_address: Optional[str] = None
    """An IPv4 unicast address"""

    ipv4_next_hop: Optional[str] = None
    """The IPv4 address of the egress interface."""

    ipv6_next_hop: Optional[str] = None
    """The IPv6 address of the egress interface."""

    local_preference: Optional[int] = None
    """
    The local preference is a well-known attribute and the value is used for route
    selection. The route with the highest local preference value is preferred.
    """

    multi_exit_discriminator: Optional[int] = None
    """
    The multi exit discriminator (MED) is an optional non-transitive attribute and
    the value is used for route selection. The route with the lowest MED value is
    preferred.
    """

    origin: Optional[Literal["igp", "egp", "incomplete"]] = None
    """The origin of the prefix."""

    path_id: Optional[int] = None
    """The path id."""

    prefix_length: Optional[int] = None
    """The length of the prefix."""


class BgpPrefixIpv6UnicastPrefix(BaseModel):
    as_path: Optional[ResultBgpAsPath] = None
    """
    This attribute identifies the autonomous systems through which routing
    information carried in this UPDATE message has passed.
    """

    communities: Optional[List[ResultBgpCommunity]] = None
    """Optional community attributes."""

    extended_communities: Optional[List[ResultExtendedCommunity]] = None
    """Optional received Extended Community attributes.

    Each received Extended Community attribute is available for retrieval in two
    forms. Support of the 'raw' format in which all 8 bytes (16 hex characters) is
    always present and available for use. In addition, if supported by the
    implementation, the Extended Community attribute may also be retrieved in the
    'structured' format which is an optional field.
    """

    ipv4_next_hop: Optional[str] = None
    """The IPv4 address of the egress interface."""

    ipv6_address: Optional[str] = None
    """An IPv6 unicast address"""

    ipv6_next_hop: Optional[str] = None
    """The IPv6 address of the egress interface."""

    local_preference: Optional[int] = None
    """
    The local preference is a well-known attribute and the value is used for route
    selection. The route with the highest local preference value is preferred.
    """

    multi_exit_discriminator: Optional[int] = None
    """
    The multi exit discriminator (MED) is an optional non-transitive attribute and
    the value is used for route selection. The route with the lowest MED value is
    preferred.
    """

    origin: Optional[Literal["igp", "egp", "incomplete"]] = None
    """The origin of the prefix."""

    path_id: Optional[int] = None
    """The path id."""

    prefix_length: Optional[int] = None
    """The length of the prefix."""


class BgpPrefix(BaseModel):
    bgp_peer_name: Optional[str] = None
    """The name of a BGP peer."""

    ipv4_unicast_prefixes: Optional[List[BgpPrefixIpv4UnicastPrefix]] = None

    ipv6_unicast_prefixes: Optional[List[BgpPrefixIpv6UnicastPrefix]] = None


class Dhcpv4Interface(BaseModel):
    dhcp_client_name: Optional[str] = None
    """The name of a DHCPv4 Client."""

    gateway_address: Optional[str] = None
    """The Gateway Ipv4 address associated with this DHCP Client session."""

    ipv4_address: Optional[str] = None
    """The IPv4 address associated with this DHCP Client session."""

    lease_time: Optional[int] = None
    """The duration of the IPv4 address lease, in seconds."""

    prefix_length: Optional[int] = None
    """The length of the prefix."""

    rebind_time: Optional[int] = None
    """Time in seconds until the DHCPv4 client starts rebinding."""

    renew_time: Optional[int] = None
    """Time in seconds until the DHCPv4 client starts renewing the lease."""


class Dhcpv4LeaseLease(BaseModel):
    address: Optional[str] = None
    """The IPv4 address associated with this lease."""

    circuit_id: Optional[str] = None
    """The Circuit ID option found in the last request message."""

    client_id: Optional[str] = None
    """The ID of the DHCPv4 client holding this lease."""

    preferred_time: Optional[int] = None
    """The elapsed time in seconds since the address has been renewed."""

    rebind_time: Optional[int] = None
    """Time in seconds until the DHCPv4 client starts rebinding."""

    remote_id: Optional[str] = None
    """The Remote ID option found in the last request message."""

    renew_time: Optional[int] = None
    """Time in seconds until the DHCPv4 client starts renewing the lease."""

    valid_time: Optional[int] = None
    """The time in seconds after which the IPv4 address lease will expire."""


class Dhcpv4Lease(BaseModel):
    dhcp_server_name: Optional[str] = None
    """The name of a DHCP Server."""

    leases: Optional[List[Dhcpv4LeaseLease]] = None


class Dhcpv6InterfaceIaAddress(BaseModel):
    address: Optional[str] = None
    """The address associated with this DHCPv6 Client session."""

    gateway: Optional[str] = None
    """The Gateway address associated with this DHCPv6 Client session."""

    lease_time: Optional[int] = None
    """The duration of the IPv6 address lease, in seconds."""


class Dhcpv6InterfaceIapdAddress(BaseModel):
    address: Optional[str] = None
    """The IAPD address associated with this DHCPv6 Client session."""

    lease_time: Optional[int] = None
    """The duration of the IPv6 address lease, in seconds."""

    prefix_length: Optional[int] = None
    """
    The prefix length of the IAPD address associated with this DHCPv6 Client
    session.
    """


class Dhcpv6Interface(BaseModel):
    dhcp_client_name: Optional[str] = None
    """The name of a DHCPv6 Client."""

    ia_addresses: Optional[List[Dhcpv6InterfaceIaAddress]] = None
    """
    The IPv6 IATA/IANA addresses and gateways associated with this DHCP Client
    session.
    """

    iapd_addresses: Optional[List[Dhcpv6InterfaceIapdAddress]] = None
    """The IPv6 IAPD addresses and prefixes associated with this DHCP Client session."""


class Dhcpv6LeaseLease(BaseModel):
    address: Optional[str] = None
    """The IPv6 address associated with this lease."""

    client_id: Optional[str] = None
    """The ID of the DHCPv6 client holding this lease."""

    interface_id: Optional[str] = None
    """The Interface ID option found in the last request message."""

    preferred_time: Optional[int] = None
    """The time in seconds, elapsed time since address has been renewed."""

    rebind_time: Optional[int] = None
    """Time in seconds until the DHCPv6 client starts rebinding."""

    remote_id: Optional[str] = None
    """The Remote ID option found in the last request message."""

    renew_time: Optional[int] = None
    """Time in seconds until the DHCPv6 client starts renewing the lease."""

    valid_time: Optional[int] = None
    """The time in seconds, IP address lease will expire."""


class Dhcpv6Lease(BaseModel):
    dhcp_server_name: Optional[str] = None
    """The name of a DHCP Server."""

    leases: Optional[List[Dhcpv6LeaseLease]] = None


class Ipv4Neighbor(BaseModel):
    ethernet_name: str
    """
    The name of the Ethernet interface associated with the Neighbor state (ARP cache
    entry).
    """

    ipv4_address: str
    """The IPv4 address of the neighbor."""

    link_layer_address: Optional[str] = None
    """The link-layer address (MAC) of the neighbor."""


class Ipv6Neighbor(BaseModel):
    ethernet_name: str
    """
    The name of the Ethernet interface associated with the Neighbor state (NDISC
    cache entry).
    """

    ipv6_address: str
    """The IPv6 address of the neighbor."""

    link_layer_address: Optional[str] = None
    """The link-layer address (MAC) of the neighbor."""


class IsisLspLspFlags(BaseModel):
    attached_default: Optional[bool] = None
    """
    Default Metric - when set, the originator is attached to another area using the
    referred metric.
    """

    attached_delay: Optional[bool] = None
    """
    Delay Metric - when set, the originator is attached to another area using the
    referred metric.
    """

    attached_error: Optional[bool] = None
    """When set, the originator is attached to another area using the referred metric."""

    attached_expense: Optional[bool] = None
    """When set, the originator is attached to another area using the referred metric."""

    overload: Optional[bool] = None
    """
    Overload bit - when set, the originator is overloaded, and must be avoided in
    path calculation.
    """

    partition_repair: Optional[bool] = None
    """When set, the originator supports partition repair."""


class IsisLspLspTlvsExtendedIpv4ReachabilityTlvPrefix(BaseModel):
    ipv4_address: Optional[str] = None
    """An IPv4 unicast prefix reachable via the originator of this LSP."""

    metric: Optional[int] = None
    """ISIS wide metric."""

    prefix_attributes: Optional[IsisLspPrefixAttributes] = None
    """Extended Prefix Attribute flags container sub-TLV is type 4."""

    prefix_length: Optional[int] = None
    """The length of the IPv4 prefix."""

    prefix_sids: Optional[List[IsisLspPrefixSid]] = None
    """Prefix Segment-ID list.

    IGP-Prefix Segment is an IGP segment attached to an IGP prefix. An IGP-Prefix
    Segment is global (unless explicitly advertised otherwise) within the SR/IGP
    domain.
    """

    redistribution_type: Optional[Literal["up", "down"]] = None
    """
    Up (0)-used when a prefix is initially advertised within the ISIS L3 hierarchy,
    and for all other prefixes in L1 and L2 LSPs. (default) Down (1)-used when an
    L1/L2 router advertises L2 prefixes in L1 LSPs. The prefixes are being
    advertised from a higher level (L2) down to a lower level (L1).
    """


class IsisLspLspTlvsExtendedIpv4ReachabilityTlv(BaseModel):
    prefixes: Optional[List[IsisLspLspTlvsExtendedIpv4ReachabilityTlvPrefix]] = None
    """IPv4 prefix contained within extended reachability TLVs."""


class IsisLspLspTlvsExtendedIsReachabilityTlvNeighborAdjacencySidFlags(BaseModel):
    b_flag: Optional[bool] = None
    """The backup flag. If set, the Adj-SID is eligible for protection."""

    f_flag: Optional[bool] = None
    """The address family flag.

    If unset, then the Adj-SID refers to an adjacency with outgoing IPv4
    encapsulation. If set then the Adj-SID refers to an adjacency with outgoing IPv6
    encapsulation.
    """

    l_flag: Optional[bool] = None
    """The local flag.

    If set, then the value/index carried by the Adj-SID has local significance.
    """

    p_flag: Optional[bool] = None
    """The persistent flag.

    When set, the P-Flag indicates that the Adj-SID is persistently allocated, i.e.,
    the Adj-SID value remains consistent across router restart and/or interface
    flap.
    """

    s_flag: Optional[bool] = None
    """The set flag.

    When set, the S-Flag indicates that the Adj-SID refers to a set of adjacencies
    (and therefore MAY be assigned to other adjacencies as well).
    """

    v_flag: Optional[bool] = None
    """The value flag. If set, then the Adj-SID carries a value."""


class IsisLspLspTlvsExtendedIsReachabilityTlvNeighborAdjacencySid(BaseModel):
    flags: Optional[IsisLspLspTlvsExtendedIsReachabilityTlvNeighborAdjacencySidFlags] = None
    """Flags associated with Adjacency Segment-ID."""

    sids: Optional[List[int]] = None
    """
    One or more SID/Indices are the SID/Label values associated with the IGP
    adjacency SID.
    """

    type: Optional[Literal["adj_sid", "lan_adj_sid"]] = None
    """Adjacency-SID type: Adjacency SIDs(31) or LAN adjacency SID (32)."""

    weight: Optional[int] = None
    """
    The value represents the weight of the Adj-SID for the purpose of load
    balancing.
    """


class IsisLspLspTlvsExtendedIsReachabilityTlvNeighbor(BaseModel):
    adjacency_sids: Optional[List[IsisLspLspTlvsExtendedIsReachabilityTlvNeighborAdjacencySid]] = None
    """List of segment routing adjacency SIDs."""

    system_id: Optional[str] = None
    """The System ID for this emulated ISIS router, e.g. "640100010000"."""


class IsisLspLspTlvsExtendedIsReachabilityTlv(BaseModel):
    neighbors: Optional[List[IsisLspLspTlvsExtendedIsReachabilityTlvNeighbor]] = None
    """This container describes IS neighbors."""


class IsisLspLspTlvsHostnameTlv(BaseModel):
    hostname: Optional[str] = None
    """Hostname for an ISIS router."""


class IsisLspLspTlvsIpv4ExternalReachabilityTlv(BaseModel):
    prefixes: Optional[List[IsisLspV4Prefix]] = None
    """Describes list of IPv4 prefixes in this TLV.."""


class IsisLspLspTlvsIpv4InternalReachabilityTlv(BaseModel):
    prefixes: Optional[List[IsisLspV4Prefix]] = None
    """Describes list of IPv4 prefixes in this TLV."""


class IsisLspLspTlvsIpv6ReachabilityTlvPrefix(BaseModel):
    ipv6_address: Optional[str] = None
    """An IPv6 unicast prefix reachable via the originator of this LSP."""

    metric: Optional[int] = None
    """ISIS wide metric."""

    origin_type: Optional[Literal["internal", "external"]] = None
    """The origin of the advertised route-internal or external to the ISIS area.

    Options include the following: Internal-for intra-area routes, through Level 1
    LSPs. External-for inter-area routes redistributed within L1, through Level 1
    LSPs.
    """

    prefix_attributes: Optional[IsisLspPrefixAttributes] = None
    """Extended Prefix Attribute flags container sub-TLV is type 4."""

    prefix_length: Optional[int] = None
    """The length of the IPv6 prefix."""

    prefix_sids: Optional[List[IsisLspPrefixSid]] = None
    """Prefix Segment-ID list.

    IGP-Prefix Segment is an IGP segment attached to an IGP prefix. An IGP-Prefix
    Segment is global (unless explicitly advertised otherwise) within the SR/IGP
    domain.
    """

    redistribution_type: Optional[Literal["up", "down"]] = None
    """
    Up (0)-used when a prefix is initially advertised within the ISIS L3 hierarchy,
    and for all other prefixes in L1 and L2 LSPs. (default) Down (1)-used when an
    L1/L2 router advertises L2 prefixes in L1 LSPs. The prefixes are being
    advertised from a higher level (L2) down to a lower level (L1).
    """


class IsisLspLspTlvsIpv6ReachabilityTlv(BaseModel):
    prefixes: Optional[List[IsisLspLspTlvsIpv6ReachabilityTlvPrefix]] = None
    """IPv6 prefix contained within reachability TLVs."""


class IsisLspLspTlvsIsReachabilityTlvNeighbor(BaseModel):
    system_id: Optional[str] = None
    """The System ID for this emulated ISIS router, e.g. "640100010000"."""


class IsisLspLspTlvsIsReachabilityTlv(BaseModel):
    neighbors: Optional[List[IsisLspLspTlvsIsReachabilityTlvNeighbor]] = None
    """This container describes Intermediate System (IS) neighbors."""


class IsisLspLspTlvsRouterCapabilitySrCapabilityFlags(BaseModel):
    ipv4_mpls: Optional[bool] = None
    """I-Flag for the MPLS IPv4 Flag.

    If set, then the router is capable of processing SR-MPLS-encapsulated IPv4
    packets on all interfaces.
    """

    ipv6_mpls: Optional[bool] = None
    """V-Flag for the MPLS IPv6 Flag.

    If set, then the router is capable of processing SR-MPLS-encapsulated IPv6
    packets on all interfaces.
    """


class IsisLspLspTlvsRouterCapabilitySrCapabilitySrgbRange(BaseModel):
    range: Optional[int] = None
    """This represents the number of SID in a SRGB range."""

    starting_sid: Optional[int] = None
    """
    The SID/Label sub-TLV contains the first value of the SRGB while the range
    contains the number of SRGB elements.
    """


class IsisLspLspTlvsRouterCapabilitySrCapability(BaseModel):
    flags: Optional[IsisLspLspTlvsRouterCapabilitySrCapabilityFlags] = None
    """1 octet of flags."""

    srgb_ranges: Optional[List[IsisLspLspTlvsRouterCapabilitySrCapabilitySrgbRange]] = None
    """This contains the list of SRGB."""


class IsisLspLspTlvsRouterCapabilitySrlbRange(BaseModel):
    range: Optional[int] = None
    """This represents the number of SID in a SRGB range."""

    starting_sid: Optional[int] = None
    """
    The SID/Label sub-TLV contains the first value of the SRGB while the range
    contains the number of SRGB elements.
    """


class IsisLspLspTlvsRouterCapability(BaseModel):
    algorithms: Optional[List[int]] = None
    """This contains one or more SR-Algorithm."""

    d_bit: Optional[Literal["down", "not_down"]] = None
    """
    D bit (0x02): When the IS-IS Router CAPABILITY TLV is leaked from Level 2 (L2)
    to Level 1 (L1), the D bit MUST be set. Otherwise, this bit MUST be clear. IS-IS
    Router CAPABILITY TLVs with the D bit set MUST NOT be leaked from Level 1 to
    Level 2. This is to prevent TLV looping.
    """

    router_cap_id: Optional[str] = None
    """Router CapabilityID in IPv4 address format."""

    s_bit: Optional[Literal["flood", "not_flood"]] = None
    """
    S bit (0x01): If the S bit is set(1), the IS-IS Router CAPABILITY TLV MUST be
    flooded across the entire routing domain. If the S bit is not set(0), the TLV
    MUST NOT be leaked between levels. This bit MUST NOT be altered during the TLV
    leaking.
    """

    sr_capability: Optional[IsisLspLspTlvsRouterCapabilitySrCapability] = None
    """SR-Capabilities."""

    srlb_ranges: Optional[List[IsisLspLspTlvsRouterCapabilitySrlbRange]] = None
    """This contains the list of SR Local Block (SRLB)"""


class IsisLspLspTlvs(BaseModel):
    extended_ipv4_reachability_tlvs: Optional[List[IsisLspLspTlvsExtendedIpv4ReachabilityTlv]] = None
    """Array of IPv4 Extended Reachability TLVs (type 135) present in this LSP."""

    extended_is_reachability_tlvs: Optional[List[IsisLspLspTlvsExtendedIsReachabilityTlv]] = None
    """Array of Extended IS-Reachability TLVs (type 22) present in this LSP."""

    hostname_tlvs: Optional[List[IsisLspLspTlvsHostnameTlv]] = None
    """Array of Hostname TLVs ( type 137) present in this LSP."""

    ipv4_external_reachability_tlvs: Optional[List[IsisLspLspTlvsIpv4ExternalReachabilityTlv]] = None
    """Array of IPv4 External Reachability TLVs (type 130) present in this LSP."""

    ipv4_internal_reachability_tlvs: Optional[List[IsisLspLspTlvsIpv4InternalReachabilityTlv]] = None
    """Array of IPv4 Internal Reachability TLVs (type 128) present in this LSP."""

    ipv6_reachability_tlvs: Optional[List[IsisLspLspTlvsIpv6ReachabilityTlv]] = None
    """Array of IPv6 Reachability TLVs (type 236) present in this LSP."""

    is_reachability_tlvs: Optional[List[IsisLspLspTlvsIsReachabilityTlv]] = None
    """Array of IS-Reachability TLVs (type 2) present in this LSP."""

    router_capabilities: Optional[List[IsisLspLspTlvsRouterCapability]] = None
    """IS-IS Router Capabilities: TLV 242. This container defines Router Capabilities."""


class IsisLspLsp(BaseModel):
    lsp_id: str
    """LSP ID in the format, e.g.

    '640000000001-00-00'. LSP ID consists of the System ID of a neighbor, the
    Pseudonode ID, and the LSP number. The last two bytes represent Pseudonode ID
    and LSP number respectively. A pseudonode is a logical representation of the LAN
    which is generated by a Designated Intermediate System (DIS) on a LAN segment.
    If one LSP exceeds the maximum LSP size then it is sent in another LSP with the
    LSP number incremented by one. A router's learned LSP gets refreshed by
    'remaining_lifetime'. Then the sequence number is incremented by 1.
    """

    flags: Optional[IsisLspLspFlags] = None
    """LSP Type-Block flags."""

    is_type: Optional[int] = None
    """IS Type - bits 1 and 2 indicate the type of Intermediate System. 1 - ( i.e.

    bit 1 set) Level 1 Intermediate system. 2 - Unused value. 3 - (i.e. bits 1 and 2
    set) Level 2 Intermediate system.
    """

    pdu_length: Optional[int] = None
    """Total length of the LSP."""

    pdu_type: Optional[Literal["level_1", "level_2"]] = None
    """Link State PDU type."""

    remaining_lifetime: Optional[int] = None
    """Remaining lifetime in seconds before LSP expires."""

    sequence_number: Optional[int] = None
    """Sequence number of the LSP."""

    tlvs: Optional[IsisLspLspTlvs] = None
    """It refers to Link State PDU State TLVs container."""


class IsisLsp(BaseModel):
    isis_router_name: Optional[str] = None
    """The name of the ISIS Router."""

    lsps: Optional[List[IsisLspLsp]] = None
    """One or more LSPs that are learned by this ISIS router."""


class LldpNeighborCapability(BaseModel):
    capability_enabled: Optional[bool] = None
    """
    Indicates whether the corresponding system capability is enabled on the
    neighbor.
    """

    capability_name: Optional[
        Literal[
            "mac_bridge",
            "two_port_mac_relay",
            "repeater",
            "docsis_cable_device",
            "s_vlan",
            "telephone",
            "other",
            "router",
            "c_vlan",
            "station_only",
            "wlan_access_point",
        ]
    ] = None
    """Name of the system capability advertised by the neighbor.

    Capabilities are represented in a bitmap that defines the primary functions of
    the system. The capabilities are defined in IEEE 802.1AB.
    """


class LldpNeighborCustomTlv(BaseModel):
    custom_type: Optional[int] = None
    """
    The integer value identifying the type of information contained in the value
    field.
    """

    information: Optional[str] = None
    """
    Contains information on the remaining bytes of the received
    Organization-Specific TLV after the sub-type field. The value must be returned
    in lowercase hexadecimal format.
    """

    oui: Optional[str] = None
    """
    The organizationally unique identifier field shall contain the organization's
    OUI as defined in Clause 9 of IEEE Std 802. The high-order octet is 0 and the
    low-order 3 octets are the SMI Network Management Private Enterprise Code of the
    Vendor in network byte order, as defined in the 'Assigned Numbers' RFC
    [RFC3232].
    """

    oui_subtype: Optional[int] = None
    """
    The organizationally defined subtype field shall contain a unique subtype value
    assigned by the defining organization.
    """


class LldpNeighbor(BaseModel):
    age: Optional[int] = None
    """Age since discovery in seconds."""

    capabilities: Optional[List[LldpNeighborCapability]] = None

    chassis_id: Optional[str] = None
    """
    The Chassis ID is a mandatory TLV which identifies the chassis component of the
    endpoint identifier associated with the transmitting LLDP agent.
    """

    chassis_id_type: Optional[
        Literal[
            "port_component",
            "network_address",
            "chassis_component",
            "mac_address",
            "interface_name",
            "local",
            "interface_alias",
        ]
    ] = None
    """This field identifies the format and source of the chassis identifier string.

    It is an enumerator defined by the LldpChassisIdSubtype object from IEEE 802.1AB
    MIB.
    """

    custom_tlvs: Optional[List[LldpNeighborCustomTlv]] = None

    last_update: Optional[int] = None
    """Seconds since last update received."""

    lldp_name: Optional[str] = None
    """The name of the LLDP instance."""

    management_address: Optional[str] = None
    """
    The Management Address is a mandatory TLV which identifies a network address
    associated with the local LLDP agent, which can be used to reach the agent on
    the port identified in the Port ID TLV.
    """

    management_address_type: Optional[str] = None
    """The enumerated value for the network address type identified in this TLV.

    This enumeration is defined in the 'Assigned Numbers' RFC [RFC3232] and the
    ianaAddressFamilyNumbers object.
    """

    neighbor_id: Optional[str] = None
    """System generated identifier for the neighbor on the LLDP instance."""

    port_description: Optional[str] = None
    """
    The binary string containing the actual port identifier for the port which this
    LLDP PDU was transmitted. The source and format of this field is defined by
    PtopoPortId from RFC2922.
    """

    port_id: Optional[str] = None
    """
    The Port ID is a mandatory TLV which identifies the port component of the
    endpoint identifier associated with the transmitting LLDP agent. If the
    specified port is an IEEE 802.3 Repeater port, then this TLV is optional.
    """

    port_id_type: Optional[
        Literal[
            "port_component",
            "network_address",
            "agent_circuit_id",
            "mac_address",
            "interface_name",
            "local",
            "interface_alias",
        ]
    ] = None
    """This field identifies the format and source of the port identifier string.

    It is an enumerator defined by the PtopoPortIdType object from RFC2922.
    """

    system_description: Optional[str] = None
    """
    The system description field shall contain an alpha-numeric string that is the
    textual description of the network entity. The system description should include
    the full name and version identification of the system's hardware type, software
    operating system, and networking software. If implementations support IETF RFC
    3418, the sysDescr object should be used for this field.
    """

    system_name: Optional[str] = None
    """
    The system name field shall contain an alpha-numeric string that indicates the
    system's administratively assigned name. The system name should be the system's
    fully qualified domain name. If implementations support IETF RFC 3418, the
    sysName object should be used for this field.
    """

    ttl: Optional[int] = None
    """
    The time-to-live (TTL) in seconds is a mandatory TLV which indicates how long
    information from the neighbor should be considered valid.
    """


class Ospfv2LsaExternalAsLsa(BaseModel):
    header: Optional[Ospfv2LsaHeader] = None
    """Contents of the LSA header."""

    metric: Optional[int] = None
    """The cost of the summary route TOS level 0 and all unspecified levels."""

    metric_type: Optional[int] = None
    """The type of metric associated with the route range."""

    network_mask: Optional[str] = None
    """The IPv4 address mask for the network."""


class Ospfv2LsaNetworkLsa(BaseModel):
    header: Optional[Ospfv2LsaHeader] = None
    """Contents of the LSA header."""

    neighbor_router_ids: Optional[List[str]] = None
    """Neighbor router ids that are described within the LSA."""

    network_mask: Optional[str] = None
    """The IPv4 address mask for the network."""


class Ospfv2LsaNetworkSummaryLsa(BaseModel):
    header: Optional[Ospfv2LsaHeader] = None
    """Contents of the LSA header."""

    metric: Optional[int] = None
    """The cost of the summary route TOS level 0 and all unspecified levels."""

    network_mask: Optional[str] = None
    """The IPv4 address mask for the network."""


class Ospfv2LsaNssaLsa(BaseModel):
    forwarding_address: Optional[str] = None
    """IPv4 Forwarding address."""

    header: Optional[Ospfv2LsaHeader] = None
    """Contents of the LSA header."""

    metric: Optional[int] = None
    """The cost of the summary route TOS level 0 and all unspecified levels."""

    metric_type: Optional[int] = None
    """The type of metric associated with the route range."""

    network_mask: Optional[str] = None
    """The IPv4 address mask for the network."""


class Ospfv2LsaOpaqueLsa(BaseModel):
    header: Optional[Ospfv2LsaHeader] = None
    """Contents of the LSA header."""

    type: Optional[Literal["local", "area", "domain"]] = None
    """The type of Opaque TE LSAs. The LSA type."""


class Ospfv2LsaRouterLsaLink(BaseModel):
    id: Optional[str] = None
    """The identifier for the link specified.

    The value of the link identifier is dependent upon the type of the LSA.
    """

    data: Optional[str] = None
    """The data associated with the link type.

    The value is dependent upon the subtype of the LSA. When the connection is to a
    stub network it represents the mask; for p2p connections that are unnumbered it
    represents the ifIndex value of the router's interface; for all other
    connections it represents the local system's IP address.
    """

    metric: Optional[int] = None
    """The data associated with the link type.

    The value is dependent upon the subtype of the LSA. When the connection is to a
    stub network it represents the mask; for p2p connections that are unnumbered it
    represents the ifIndex value of the router's interface; for all other
    connections it represents the local system's IP address.
    """

    type: Optional[Literal["point_to_point", "transit", "stub", "virtual"]] = None
    """The data associated with the link type.

    The value is dependent upon the subtype of the LSA. - point_to_point: The LSA
    represents a point-to-point connection to another router. - transit: The LSA
    represents a connection to a transit network. - stub: The LSA represents a
    connection to a stub network. - virtual: The LSA represents a virtual link
    connection.
    """


class Ospfv2LsaRouterLsa(BaseModel):
    header: Optional[Ospfv2LsaHeader] = None
    """Contents of the LSA header."""

    links: Optional[List[Ospfv2LsaRouterLsaLink]] = None
    """Links that are described within the LSA."""


class Ospfv2LsaSummaryAsLsa(BaseModel):
    header: Optional[Ospfv2LsaHeader] = None
    """Contents of the LSA header."""

    metric: Optional[int] = None
    """The cost of the summary route TOS level 0 and all unspecified levels."""

    network_mask: Optional[str] = None
    """The IPv4 address mask for the network."""


class Ospfv2Lsa(BaseModel):
    external_as_lsas: Optional[List[Ospfv2LsaExternalAsLsa]] = None
    """OSPFv2 AS-External-LSA - Type 5."""

    network_lsas: Optional[List[Ospfv2LsaNetworkLsa]] = None
    """One or more OSPFv2 Network-LSA - Type 2."""

    network_summary_lsas: Optional[List[Ospfv2LsaNetworkSummaryLsa]] = None
    """One or more OSPFv2 Network summary LSA - Type 3."""

    nssa_lsas: Optional[List[Ospfv2LsaNssaLsa]] = None
    """One or more OSPFv2 NSSA-LSA - Type 7."""

    opaque_lsas: Optional[List[Ospfv2LsaOpaqueLsa]] = None
    """One or more OSPFv2 Link-Scope Opaque-LSA - Type 9."""

    router_lsas: Optional[List[Ospfv2LsaRouterLsa]] = None
    """One or more OSPFv2 Router-LSA - Type 1."""

    router_name: Optional[str] = None
    """The name of the OSPFv2 Router that learned the LSA information."""

    summary_as_lsas: Optional[List[Ospfv2LsaSummaryAsLsa]] = None
    """
    One or more OSPFv2 Autonomous System Boundary Router (ASBR) summary LSA -
    Type 4.
    """


class Ospfv3LsaExternalAsLsa(BaseModel):
    address_prefix: Optional[str] = None
    """The first IPv6 address prefix to be advertised in the LSA."""

    forwarding_address: Optional[str] = None
    """The IPV6 address where traffic for the advertised destination is forwarded."""

    header: Optional[Ospfv3LsaHeader] = None
    """Contents of the LSA header."""

    metric: Optional[int] = None
    """The cost metric value for the route to this destination router."""

    prefix_length: Optional[int] = None
    """The length of the IPv6 address prefix, in bits."""

    referenced_ls_type: Optional[int] = None
    """If non-zero, an LSA with this LS type is to be associated with this LSA."""

    route_tag: Optional[str] = None
    """
    The optional field may be used to communicate additional information between AS
    boundary routers.
    """


class Ospfv3LsaInterAreaPrefixLsa(BaseModel):
    address_prefix: Optional[str] = None
    """The prefix for Inter Area Prefix LSA Address."""

    header: Optional[Ospfv3LsaHeader] = None
    """Contents of the LSA header."""

    metric: Optional[int] = None
    """The cost of the summary route TOS level 0 and all unspecified levels."""

    prefix_length: Optional[int] = None
    """The prefix length for the IP address."""


class Ospfv3LsaInterAreaRouterLsa(BaseModel):
    destination_router_id: Optional[str] = None
    """The id of the destination router of LSA."""

    header: Optional[Ospfv3LsaHeader] = None
    """Contents of the LSA header."""

    metric: Optional[int] = None
    """The cost of the summary route TOS level 0 and all unspecified levels."""


class Ospfv3LsaIntraAreaPrefixLsa(BaseModel):
    address_prefix: Optional[str] = None
    """The first IPv6 address prefix to be advertised in the LSA."""

    header: Optional[Ospfv3LsaHeader] = None
    """Contents of the LSA header."""

    metric: Optional[int] = None
    """The cost metric value for the route to this destination router."""

    prefix_length: Optional[int] = None
    """The length of the IPv6 address prefix, in bits."""


class Ospfv3LsaLinkLsa(BaseModel):
    address_prefix: Optional[str] = None
    """The first IPv6 address prefix to be advertised in the LSA."""

    header: Optional[Ospfv3LsaHeader] = None
    """Contents of the LSA header."""

    link_local_address: Optional[str] = None
    """
    The IPV6 Link Local address for the originating router's interface attached to
    this link.
    """

    prefix_length: Optional[int] = None
    """The length of the IPv6 address prefix, in bits."""


class Ospfv3LsaNetworkLsa(BaseModel):
    attached_router_ids: Optional[List[str]] = None
    """Attached router ids that are described within the LSA."""

    header: Optional[Ospfv3LsaHeader] = None
    """Contents of the LSA header."""


class Ospfv3LsaNssaLsa(BaseModel):
    address_prefix: Optional[str] = None
    """The first IPv6 address prefix to be advertised in the LSA."""

    forwarding_address: Optional[str] = None
    """The IPV6 address where traffic for the advertised destination is forwarded."""

    header: Optional[Ospfv3LsaHeader] = None
    """Contents of the LSA header."""

    metric: Optional[int] = None
    """The cost metric value for the route to this destination router."""

    prefix_length: Optional[int] = None
    """The length of the IPv6 address prefix, in bits."""

    route_tag: Optional[str] = None
    """
    The optional field may be used to communicate additional information between AS
    boundary routers.
    """


class Ospfv3LsaRouterLsaLink(BaseModel):
    metric: Optional[int] = None
    """The data associated with the link type.

    The value is dependent upon the subtype of the LSA. When the connection is to a
    stub network it represents the mask; for p2p connections that are unnumbered it
    represents the ifIndex value of the router's interface; for all other
    connections it represents the local system's IP address.
    """

    type: Optional[Literal["point_to_point", "transit", "stub", "virtual"]] = None
    """The data associated with the link type.

    The value is dependent upon the subtype of the LSA. - point_to_point: The LSA
    represents a point-to-point connection to another router. - transit: The LSA
    represents a connection to a transit network. - stub: The LSA represents a
    connection to a stub network. - virtual: The LSA represents a virtual link
    connection.
    """


class Ospfv3LsaRouterLsa(BaseModel):
    header: Optional[Ospfv3LsaHeader] = None
    """Contents of the LSA header."""

    links: Optional[List[Ospfv3LsaRouterLsaLink]] = None
    """Links that are described within the LSA."""

    neighbor_router_id: Optional[str] = None
    """Neighbor router id that is described within the LSA."""


class Ospfv3Lsa(BaseModel):
    external_as_lsas: Optional[List[Ospfv3LsaExternalAsLsa]] = None
    """OSPFv3 AS-External LSA - Type 5."""

    inter_area_prefix_lsas: Optional[List[Ospfv3LsaInterAreaPrefixLsa]] = None
    """One or more OSPFv3 Inter-Area-Prefix LSA - Type 3."""

    inter_area_router_lsas: Optional[List[Ospfv3LsaInterAreaRouterLsa]] = None
    """One or more OSPFv3 Inter-Area-Router LSA - Type 4."""

    intra_area_prefix_lsas: Optional[List[Ospfv3LsaIntraAreaPrefixLsa]] = None
    """One or more OSPFv3 Intra-Area-Prefix LSA - Type 9."""

    link_lsas: Optional[List[Ospfv3LsaLinkLsa]] = None
    """One or more OSPFv3 Link LSA - Type 8."""

    network_lsas: Optional[List[Ospfv3LsaNetworkLsa]] = None
    """One or more OSPFv3 Network LSA - Type 2."""

    nssa_lsas: Optional[List[Ospfv3LsaNssaLsa]] = None
    """One or more OSPFv3 NSSA LSA - Type 7."""

    router_lsas: Optional[List[Ospfv3LsaRouterLsa]] = None
    """One or more OSPFv3 Router LSA - Type 1."""

    router_name: Optional[str] = None
    """The name of the OSPFv3 Router that learned the LSA information."""


class RsvpLspIpv4LspEro(BaseModel):
    asn: Optional[int] = None
    """The autonomous system number indicated by the ERO.

    Specified only when the ERO hop is an 2 or 4-byte AS number.
    """

    prefix: Optional[str] = None
    """The IPv4 prefix indicated by the ERO.

    Specified only when the ERO hop is an IPv4 prefix.
    """

    type: Optional[Literal["ipv4", "ipv6", "asn", "asn4", "label", "unnumbered_interface"]] = None
    """The type indicated by the ERO."""


class RsvpLspIpv4LspLsp(BaseModel):
    label_in: Optional[int] = None
    """The label received by RSVP-TE ingress."""

    label_out: Optional[int] = None
    """The label assigned by RSVP-TE egress."""

    last_flap_reason: Optional[Literal["resv_tear", "path_tear", "path_timeout"]] = None
    """The reason for the last flap of this RSVP session."""

    lsp_id: Optional[int] = None
    """
    The lsp-id of RSVP session which acts as a differentiator for two lsps
    originating from the same headend, commonly used to distinguish RSVP sessions
    during make before break operations.
    """

    session_name: Optional[str] = None
    """The value of RSVP-TE Session Name field of the Session Attribute object."""

    session_status: Optional[Literal["up", "down"]] = None
    """Operational state of the RSVP LSP."""

    tunnel_id: Optional[int] = None
    """
    The tunnel id of RSVP session which acts as an identifier that remains constant
    over the life of the tunnel.
    """

    up_time: Optional[int] = None
    """The tunnel UP time in milli seconds.

    If the tunnel is DOWN the UP time will be zero.
    """


class RsvpLspIpv4LspRro(BaseModel):
    address: Optional[str] = None
    """
    The IPv4 addresses of the routers that the traffic engineering tunnel traversed.
    """

    reported_label: Optional[int] = None
    """Label reported for RRO hop.

    When the Label_Recording flag is set in the Session Attribute object, nodes
    doing route recording should include the Label Record subobject containing the
    reported label.
    """


class RsvpLspIpv4Lsp(BaseModel):
    destination_address: Optional[str] = None
    """The IPv4 destination address of RSVP session."""

    eros: Optional[List[RsvpLspIpv4LspEro]] = None
    """It refers to RSVP ERO objects container."""

    lsp: Optional[RsvpLspIpv4LspLsp] = None
    """It refers to the RSVP LSP properties."""

    rros: Optional[List[RsvpLspIpv4LspRro]] = None
    """It refers to RSVP RRO objects container."""

    source_address: Optional[str] = None
    """The origin IPv4 address of RSVP session."""


class RsvpLsp(BaseModel):
    ipv4_lsps: Optional[List[RsvpLspIpv4Lsp]] = None
    """IPv4 Point-to-Point RSVP-TE Discovered LSPs."""

    rsvp_router_name: Optional[str] = None
    """The name of the RSVP-TE Router."""


class MonitorCreateStatesResponse(BaseModel):
    bgp_prefixes: Optional[List[BgpPrefix]] = None

    choice: Optional[
        Literal[
            "ipv4_neighbors",
            "ipv6_neighbors",
            "bgp_prefixes",
            "isis_lsps",
            "lldp_neighbors",
            "rsvp_lsps",
            "dhcpv4_interfaces",
            "dhcpv4_leases",
            "dhcpv6_interfaces",
            "dhcpv6_leases",
            "ospfv2_lsas",
            "ospfv3_lsas",
        ]
    ] = None

    dhcpv4_interfaces: Optional[List[Dhcpv4Interface]] = None

    dhcpv4_leases: Optional[List[Dhcpv4Lease]] = None

    dhcpv6_interfaces: Optional[List[Dhcpv6Interface]] = None

    dhcpv6_leases: Optional[List[Dhcpv6Lease]] = None

    ipv4_neighbors: Optional[List[Ipv4Neighbor]] = None

    ipv6_neighbors: Optional[List[Ipv6Neighbor]] = None

    isis_lsps: Optional[List[IsisLsp]] = None

    lldp_neighbors: Optional[List[LldpNeighbor]] = None

    ospfv2_lsas: Optional[List[Ospfv2Lsa]] = None

    ospfv3_lsas: Optional[List[Ospfv3Lsa]] = None

    rsvp_lsps: Optional[List[RsvpLsp]] = None
