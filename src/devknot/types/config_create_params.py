# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .flow_param import FlowParam
from .bgp_as_path_param import BgpAsPathParam
from .device_vlan_param import DeviceVlanParam
from .rocev2_q_ps_param import Rocev2QPsParam
from .bgp_advanced_param import BgpAdvancedParam
from .bgp_community_param import BgpCommunityParam
from .capture_field_param import CaptureFieldParam
from .link_state_te_param import LinkStateTeParam
from .bgp_capability_param import BgpCapabilityParam
from .bgp_route_target_param import BgpRouteTargetParam
from .v4_route_address_param import V4RouteAddressParam
from .v6_route_address_param import V6RouteAddressParam
from .bgp_ext_community_param import BgpExtCommunityParam
from .bgp_update_replay_param import BgpUpdateReplayParam
from .bgp_c_mac_ip_range_param import BgpCMacIPRangeParam
from .bgp_route_advanced_param import BgpRouteAdvancedParam
from .bgp_srte_v4_policy_param import BgpSrteV4PolicyParam
from .bgp_srte_v6_policy_param import BgpSrteV6PolicyParam
from .bgp_v4_route_range_param import BgpV4RouteRangeParam
from .bgp_v6_route_range_param import BgpV6RouteRangeParam
from .isis_sr_prefix_sid_param import IsisSrPrefixSidParam
from .bgp_graceful_restart_param import BgpGracefulRestartParam
from .isis_interface_level_param import IsisInterfaceLevelParam
from .rocev2_immediate_data_param import Rocev2ImmediateDataParam
from .rocev2_priority_value_param import Rocev2PriorityValueParam
from .bgp_route_distinguisher_param import BgpRouteDistinguisherParam
from .dhcpv6_server_pool_info_param import Dhcpv6ServerPoolInfoParam
from .isis_authentication_base_param import IsisAuthenticationBaseParam
from .dhcpv6_server_iapd_pool_info_param import Dhcpv6ServerIapdPoolInfoParam
from .secure_entity_static_key_sak_param import SecureEntityStaticKeySakParam
from .bgp_learned_information_filter_param import BgpLearnedInformationFilterParam
from .ospfv2_v4_rr_extd_prefix_flags_param import Ospfv2V4RrExtdPrefixFlagsParam
from .bgp_ethernet_segment_df_election_param import BgpEthernetSegmentDfElectionParam
from .device_dhcpv6client_ia_time_value_param import DeviceDhcpv6clientIaTimeValueParam
from .dhcpv6_options_vendor_specific_options_param import Dhcpv6OptionsVendorSpecificOptionsParam
from .dhcpv6_client_options_included_messages_param import Dhcpv6ClientOptionsIncludedMessagesParam
from .dhcpv6_server_options_included_messages_param import Dhcpv6ServerOptionsIncludedMessagesParam
from .dhcpv6_client_options_link_layer_address_param import Dhcpv6ClientOptionsLinkLayerAddressParam
from .vxlan_tunnel_destination_ip_mode_unicast_arp_suppression_cache_param import (
    VxlanTunnelDestinationIPModeUnicastArpSuppressionCacheParam,
)

__all__ = [
    "ConfigCreateParams",
    "Capture",
    "CaptureFilter",
    "CaptureFilterCustom",
    "CaptureFilterEthernet",
    "CaptureFilterIpv4",
    "CaptureFilterIpv6",
    "CaptureFilterVlan",
    "Device",
    "DeviceBgp",
    "DeviceBgpIpv4Interface",
    "DeviceBgpIpv4InterfacePeer",
    "DeviceBgpIpv4InterfacePeerEvpnEthernetSegment",
    "DeviceBgpIpv4InterfacePeerEvpnEthernetSegmentEvi",
    "DeviceBgpIpv4InterfacePeerEvpnEthernetSegmentEviEviVxlan",
    "DeviceBgpIpv4InterfacePeerEvpnEthernetSegmentEviEviVxlanBroadcastDomain",
    "DeviceBgpIpv6Interface",
    "DeviceBgpIpv6InterfacePeer",
    "DeviceBgpIpv6InterfacePeerEvpnEthernetSegment",
    "DeviceBgpIpv6InterfacePeerEvpnEthernetSegmentEvi",
    "DeviceBgpIpv6InterfacePeerEvpnEthernetSegmentEviEviVxlan",
    "DeviceBgpIpv6InterfacePeerEvpnEthernetSegmentEviEviVxlanBroadcastDomain",
    "DeviceBgpIpv6InterfacePeerSegmentRouting",
    "DeviceDhcpServer",
    "DeviceDhcpServerIpv4Interface",
    "DeviceDhcpServerIpv4InterfaceAddressPool",
    "DeviceDhcpServerIpv4InterfaceAddressPoolOptions",
    "DeviceDhcpServerIpv6Interface",
    "DeviceDhcpServerIpv6InterfaceLease",
    "DeviceDhcpServerIpv6InterfaceLeaseIaType",
    "DeviceDhcpServerIpv6InterfaceLeaseIaTypeIanapd",
    "DeviceDhcpServerIpv6InterfaceOptions",
    "DeviceDhcpServerIpv6InterfaceOptionsBootfileURL",
    "DeviceDhcpServerIpv6InterfaceOptionsBootfileURLBootfileParam",
    "DeviceDhcpServerIpv6InterfaceOptionsDNS",
    "DeviceDhcpServerIpv6InterfaceOptionsDNSSecondaryDNS",
    "DeviceDhcpServerIpv6InterfaceOptionsVendorInfo",
    "DeviceEthernet",
    "DeviceEthernetConnection",
    "DeviceEthernetConnectionSimulatedLink",
    "DeviceEthernetDhcpv4Interface",
    "DeviceEthernetDhcpv4InterfaceParametersRequestList",
    "DeviceEthernetDhcpv6Interface",
    "DeviceEthernetDhcpv6InterfaceDuidType",
    "DeviceEthernetDhcpv6InterfaceDuidTypeEn",
    "DeviceEthernetDhcpv6InterfaceIaType",
    "DeviceEthernetDhcpv6InterfaceOptions",
    "DeviceEthernetDhcpv6InterfaceOptionsFqdn",
    "DeviceEthernetDhcpv6InterfaceOptionsServerIdentifier",
    "DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidEn",
    "DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidLl",
    "DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidLlt",
    "DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidUuid",
    "DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidUuidVariant",
    "DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidUuidVersion",
    "DeviceEthernetDhcpv6InterfaceOptionsVendorClass",
    "DeviceEthernetDhcpv6InterfaceOptionsVendorInfo",
    "DeviceEthernetDhcpv6InterfaceOptionsRequest",
    "DeviceEthernetDhcpv6InterfaceOptionsRequestRequest",
    "DeviceEthernetDhcpv6InterfaceOptionsRequestRequestCustom",
    "DeviceEthernetIpv4Address",
    "DeviceEthernetIpv4AddressGatewayMac",
    "DeviceEthernetIpv6Address",
    "DeviceEthernetIpv6AddressGatewayMac",
    "DeviceIpv4Loopback",
    "DeviceIpv6Loopback",
    "DeviceIsis",
    "DeviceIsisInterface",
    "DeviceIsisInterfaceAdjacencySid",
    "DeviceIsisInterfaceAdvanced",
    "DeviceIsisInterfaceAuthentication",
    "DeviceIsisInterfaceLinkProtection",
    "DeviceIsisInterfaceMultiTopologyID",
    "DeviceIsisAdvanced",
    "DeviceIsisBasic",
    "DeviceIsisInstance",
    "DeviceIsisRouterAuth",
    "DeviceIsisSegmentRouting",
    "DeviceIsisSegmentRoutingRouterCapability",
    "DeviceIsisSegmentRoutingRouterCapabilitySrCapability",
    "DeviceIsisSegmentRoutingRouterCapabilitySrCapabilityFlags",
    "DeviceIsisSegmentRoutingRouterCapabilitySrCapabilitySrgbRange",
    "DeviceIsisSegmentRoutingRouterCapabilitySrlbRange",
    "DeviceIsisV4Route",
    "DeviceIsisV6Route",
    "DeviceMacsec",
    "DeviceMacsecEthernetInterface",
    "DeviceMacsecEthernetInterfaceSecureEntity",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocol",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMka",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasic",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySource",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySourcePsk",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySourcePskEndOffsetTime",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySourcePskStartOffsetTime",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicPskChainStartTime",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicPskChainStartTimeUtc",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicRekeyMode",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicRekeyModeTimerBased",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicSupportedCipherSuites",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaTx",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaTxSecureChannel",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaKeyServer",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKey",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyRx",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyRxSecureChannel",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTx",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTxRekeyMode",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTxRekeyModeTimerBased",
    "DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTxSecureChannel",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlane",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulation",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngine",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnly",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannel",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannelTxPn",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannelTxPnFixed",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannelTxPnIncrementing",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlyTrafficOptions",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationRx",
    "DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationTx",
    "DeviceOspfv2",
    "DeviceOspfv2Interface",
    "DeviceOspfv2InterfaceAdvanced",
    "DeviceOspfv2InterfaceArea",
    "DeviceOspfv2InterfaceAuthentication",
    "DeviceOspfv2InterfaceAuthenticationMd5",
    "DeviceOspfv2InterfaceLinkProtection",
    "DeviceOspfv2InterfaceNetworkType",
    "DeviceOspfv2InterfaceNetworkTypePointToMultipoint",
    "DeviceOspfv2Capabilities",
    "DeviceOspfv2GracefulRestart",
    "DeviceOspfv2RouterID",
    "DeviceOspfv2V4Route",
    "DeviceOspfv2V4RouteRouteOrigin",
    "DeviceOspfv2V4RouteRouteOriginExternalType1",
    "DeviceOspfv2V4RouteRouteOriginExternalType2",
    "DeviceOspfv2V4RouteRouteOriginInterArea",
    "DeviceOspfv2V4RouteRouteOriginIntraArea",
    "DeviceOspfv2V4RouteRouteOriginNssaExternal",
    "DeviceOspfv3",
    "DeviceOspfv3Instance",
    "DeviceOspfv3InstanceInterface",
    "DeviceOspfv3InstanceInterfaceAdvanced",
    "DeviceOspfv3InstanceInterfaceArea",
    "DeviceOspfv3InstanceInterfaceNetworkType",
    "DeviceOspfv3InstanceInterfaceNetworkTypeBroadcast",
    "DeviceOspfv3InstanceInterfaceOptions",
    "DeviceOspfv3InstanceCapabilities",
    "DeviceOspfv3InstanceGracefulRestart",
    "DeviceOspfv3InstanceV6Route",
    "DeviceOspfv3InstanceV6RouteRouteOrigin",
    "DeviceOspfv3InstanceV6RouteRouteOriginNssaExternal",
    "DeviceOspfv3InstanceV6RouteRouteOriginNssaExternalCapabilities",
    "DeviceOspfv3InstanceV6RouteRouteOriginNssaExternalCapabilitiesForwardingAddress",
    "DeviceOspfv3RouterID",
    "DeviceRocev2",
    "DeviceRocev2Ipv4Interface",
    "DeviceRocev2Ipv4InterfacePeer",
    "DeviceRocev2Ipv6Interface",
    "DeviceRocev2Ipv6InterfacePeer",
    "DeviceRsvp",
    "DeviceRsvpIpv4Interface",
    "DeviceRsvpLspIpv4Interface",
    "DeviceRsvpLspIpv4InterfaceP2pEgressIpv4Lsps",
    "DeviceRsvpLspIpv4InterfaceP2pIngressIpv4Lsp",
    "DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspEro",
    "DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspEroSubobject",
    "DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspFastReroute",
    "DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspSessionAttribute",
    "DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspSessionAttributeResourceAffinities",
    "DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspTspec",
    "DeviceVxlan",
    "DeviceVxlanV4Tunnel",
    "DeviceVxlanV4TunnelDestinationIPMode",
    "DeviceVxlanV4TunnelDestinationIPModeMulticast",
    "DeviceVxlanV4TunnelDestinationIPModeUnicast",
    "DeviceVxlanV4TunnelDestinationIPModeUnicastVtep",
    "DeviceVxlanV6Tunnel",
    "DeviceVxlanV6TunnelDestinationIPMode",
    "DeviceVxlanV6TunnelDestinationIPModeMulticast",
    "DeviceVxlanV6TunnelDestinationIPModeUnicast",
    "DeviceVxlanV6TunnelDestinationIPModeUnicastVtep",
    "EgressOnlyTracking",
    "EgressOnlyTrackingFilter",
    "EgressOnlyTrackingMetricTag",
    "Events",
    "EventsCpEvents",
    "EventsDpEvents",
    "Lag",
    "LagPort",
    "LagPortEthernet",
    "LagPortLacp",
    "LagProtocol",
    "LagProtocolLacp",
    "LagProtocolStatic",
    "Layer1",
    "Layer1AutoNegotiation",
    "Layer1FlowControl",
    "Layer1FlowControlIeee802_1qbb",
    "Lldp",
    "LldpConnection",
    "LldpChassisID",
    "LldpChassisIDMacAddressSubtype",
    "LldpOrgInfo",
    "LldpOrgInfoInformation",
    "LldpPortID",
    "LldpPortIDInterfaceNameSubtype",
    "LldpSystemName",
    "Options",
    "OptionsPerPortOption",
    "OptionsPerPortOptionProtocol",
    "OptionsPerPortOptionProtocolRocev2",
    "OptionsPerPortOptionProtocolRocev2Cnp",
    "OptionsPerPortOptionProtocolRocev2ConnectionType",
    "OptionsPerPortOptionProtocolRocev2ConnectionTypeReliableConnection",
    "OptionsPerPortOptionProtocolRocev2ConnectionTypeReliableConnectionAck",
    "OptionsPerPortOptionProtocolRocev2ConnectionTypeReliableConnectionNak",
    "OptionsPerPortOptionProtocolRocev2DcqcnSettings",
    "OptionsPortOptions",
    "OptionsProtocolOptions",
    "Port",
    "StatefulFlows",
    "StatefulFlowsRocev2",
    "StatefulFlowsRocev2TxPort",
    "StatefulFlowsRocev2TxPortTransmitType",
    "StatefulFlowsRocev2TxPortTransmitTypeTargetLineRate",
    "StatefulFlowsRocev2TxPortTransmitTypeTargetLineRateFlow",
    "StatefulFlowsRocev2TxPortTransmitTypeTargetLineRateFlowRocev2Verb",
]


class ConfigCreateParams(TypedDict, total=False):
    captures: Iterable[Capture]
    """The capture settings that will be configured on the traffic generator."""

    devices: Iterable[Device]
    """
    The emulated devices that will be configured on the traffic generator. Each
    device contains configurations for network interfaces and protocols running on
    top of those interfaces.
    """

    egress_only_tracking: Iterable[EgressOnlyTracking]
    """
    Container for specification of desired tracking, based on certain offset and
    length of bits for received packets on specified receive ports. It enables the
    user to retrieve information based on number of unique packets received for each
    unique value in the bits being tracked from the beginning of the test.
    """

    events: Events
    """
    Under Review: Event configuration is currently under review for pending
    exploration on use cases.

    The optional container for event configuration. Both cp_events.enable and
    dp_events.enable must be explicitly set to true to get
    control_plane_data_plane_convergence_us metric values for convergence metrics.
    """

    flows: Iterable[FlowParam]
    """The flows that will be configured on the traffic generator."""

    lags: Iterable[Lag]
    """The LAGs that will be configured on the traffic generator."""

    layer1: Iterable[Layer1]
    """
    The layer1 settings that will be configured on the traffic generator. Since
    layer1 settings usually vary across variety of test ports, these most likely
    won't be portable.
    """

    lldp: Iterable[Lldp]
    """LLDP protocol that will be configured on traffic generator."""

    options: Options
    """Global configuration options."""

    ports: Iterable[Port]
    """The ports that will be configured on the traffic generator."""

    stateful_flows: StatefulFlows
    """
    Conversational traffic where the responding side can be responded back with
    control messages, eg incase of rocev2 responding side can send ack, nak.
    """


class CaptureFilterCustom(TypedDict, total=False):
    bit_length: int
    """The bit length of field to filter on"""

    mask: str

    negate: bool

    offset: int
    """The bit offset of field to filter on"""

    value: str


class CaptureFilterEthernet(TypedDict, total=False):
    dst: CaptureFieldParam

    ether_type: CaptureFieldParam

    pfc_queue: CaptureFieldParam

    src: CaptureFieldParam


class CaptureFilterIpv4(TypedDict, total=False):
    dont_fragment: CaptureFieldParam

    dst: CaptureFieldParam

    fragment_offset: CaptureFieldParam

    header_checksum: CaptureFieldParam

    header_length: CaptureFieldParam

    identification: CaptureFieldParam

    more_fragments: CaptureFieldParam

    priority: CaptureFieldParam

    protocol: CaptureFieldParam

    reserved: CaptureFieldParam

    src: CaptureFieldParam

    time_to_live: CaptureFieldParam

    total_length: CaptureFieldParam

    version: CaptureFieldParam


class CaptureFilterIpv6(TypedDict, total=False):
    dst: CaptureFieldParam

    flow_label: CaptureFieldParam

    hop_limit: CaptureFieldParam

    next_header: CaptureFieldParam

    payload_length: CaptureFieldParam

    src: CaptureFieldParam

    traffic_class: CaptureFieldParam

    version: CaptureFieldParam


class CaptureFilterVlan(TypedDict, total=False):
    id: CaptureFieldParam

    cfi: CaptureFieldParam

    priority: CaptureFieldParam

    protocol: CaptureFieldParam


class CaptureFilter(TypedDict, total=False):
    choice: Literal["custom", "ethernet", "vlan", "ipv4", "ipv6"]
    """The type of capture filter."""

    custom: CaptureFilterCustom
    """Offset from last filter in the list.

    If no filters are present it is offset from position 0. Multiple custom filters
    can be present, the length of each custom filter is the length of the value
    being filtered.
    """

    ethernet: CaptureFilterEthernet

    ipv4: CaptureFilterIpv4

    ipv6: CaptureFilterIpv6

    vlan: CaptureFilterVlan


class Capture(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    port_names: Required[List[str]]
    """The unique names of ports that the capture settings will apply to.

    Port_names cannot be duplicated between capture objects.

    x-constraint:

    - /components/schemas/Port/properties/name
    """

    filters: Iterable[CaptureFilter]
    """A list of filters to apply to the capturing ports.

    If no filters are specified then all packets will be captured. A capture can
    have multiple filters. The number of filters supported is determined by the
    implementation which can be retrieved using the capabilities API. When multiple
    filters are specified the capture implementation must && (and) all the filters.
    """

    format: Literal["pcap", "pcapng"]
    """The format of the capture file."""

    overwrite: bool
    """Overwrite the capture buffer."""

    packet_size: int
    """The maximum size of each captured packet.

    If no value is specified or it is null then the entire packet will be captured.
    """


class DeviceBgpIpv4InterfacePeerEvpnEthernetSegmentEviEviVxlanBroadcastDomain(TypedDict, total=False):
    cmac_ip_range: Iterable[BgpCMacIPRangeParam]
    """
    This contains the list of Customer MAC/IP Ranges to be configured per Broadcast
    Domain.

    Advertises following route - Type 2 - MAC/IP Advertisement Route.
    """

    ethernet_tag_id: int
    """The Ethernet Tag ID of the Broadcast Domain."""

    vlan_aware_service: bool
    """VLAN-Aware service to be enabled or disabled."""


class DeviceBgpIpv4InterfacePeerEvpnEthernetSegmentEviEviVxlan(TypedDict, total=False):
    ad_label: int
    """
    The Auto-discovery Route label (AD label) value, which gets advertised in the
    Ethernet Auto-discovery Route per <EVI, ESI>
    """

    advanced: BgpRouteAdvancedParam
    """Configuration for advanced BGP route range settings."""

    as_path: BgpAsPathParam
    """Optional AS PATH settings."""

    broadcast_domains: Iterable[DeviceBgpIpv4InterfacePeerEvpnEthernetSegmentEviEviVxlanBroadcastDomain]
    """This contains the list of Broadcast Domains to be configured per EVI."""

    communities: Iterable[BgpCommunityParam]
    """Optional community settings."""

    ext_communities: Iterable[BgpExtCommunityParam]
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

    l3_route_target_export: Iterable[BgpRouteTargetParam]
    """List of Layer 3 Virtual Network Identifier (L3VNI) Export Route Targets."""

    l3_route_target_import: Iterable[BgpRouteTargetParam]
    """List of L3VNI Import Route Targets."""

    pmsi_label: int
    """
    Downstream assigned VNI to be carried as Part of P-Multicast Service Interface
    Tunnel attribute (PMSI Tunnel Attribute) in Type 3 Inclusive Multicast Ethernet
    Tag Route.
    """

    replication_type: Literal["ingress_replication"]
    """This model only supports Ingress Replication"""

    route_distinguisher: BgpRouteDistinguisherParam
    """
    Colon separated Extended Community value of 6 Bytes - "AS number: Value"
    identifying an EVI. Example - for the as_2octet "60005:100".
    """

    route_target_export: Iterable[BgpRouteTargetParam]
    """
    List of Layer 2 Virtual Network Identifier (L2VNI) export targets associated
    with this EVI.
    """

    route_target_import: Iterable[BgpRouteTargetParam]
    """List of L2VNI import targets associated with this EVI."""


class DeviceBgpIpv4InterfacePeerEvpnEthernetSegmentEvi(TypedDict, total=False):
    choice: Literal["evi_vxlan"]

    evi_vxlan: DeviceBgpIpv4InterfacePeerEvpnEthernetSegmentEviEviVxlan
    """EVPN VXLAN instance to be configured per Ethernet Segment."""


class DeviceBgpIpv4InterfacePeerEvpnEthernetSegment(TypedDict, total=False):
    active_mode: Literal["single_active", "all_active"]
    """Single Active or All Active mode Redundancy mode selection for Multi-home."""

    advanced: BgpRouteAdvancedParam
    """Configuration for advanced BGP route range settings."""

    as_path: BgpAsPathParam
    """Optional AS PATH settings."""

    communities: Iterable[BgpCommunityParam]
    """Optional community settings."""

    df_election: BgpEthernetSegmentDfElectionParam
    """Designated Forwarder (DF) election configuration."""

    esi: str
    """
    10-octet Ethernet Segment Identifier (ESI) Example - For multi-home scenario
    nonZero ESI is '10000000000000000000' .
    """

    esi_label: int
    """The label value to be advertised as ESI Label in ESI Label Extended Community.

    This is included in Ethernet Auto-discovery per ES Routes advertised by a
    router.
    """

    evis: Iterable[DeviceBgpIpv4InterfacePeerEvpnEthernetSegmentEvi]
    """This contains the list of EVIs."""

    ext_communities: Iterable[BgpExtCommunityParam]
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


class DeviceBgpIpv4InterfacePeer(TypedDict, total=False):
    as_number: Required[int]
    """Autonomous System Number (AS number or ASN)"""

    as_type: Required[Literal["ibgp", "ebgp"]]
    """The type of BGP autonomous system.

    External BGP is used for BGP links between two or more autonomous systems
    (ebgp). Internal BGP is used within a single autonomous system (ibgp). BGP
    property defaults are aligned with this object defined as an internal BGP peer.
    If the as_type is specified as 'ebgp' then other properties will need to be
    specified as per an external BGP peer. Specifically, for 'ebgp', 'as_set_mode'
    attribute in 'as_path' field in any Route Range should be changed from default
    value 'do_not_include_local_as' to any other value.
    """

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects. Globally unique name of
    an object. It also serves as the primary key for arrays of objects.
    """

    peer_address: Required[str]
    """IPv4 address of the BGP peer for the session."""

    advanced: BgpAdvancedParam
    """Configuration for BGP advanced settings."""

    as_number_width: Literal["two", "four"]
    """The width in bytes of the as_number values.

    Any as_number values that exceeds the width MUST result in an error.
    """

    capability: BgpCapabilityParam
    """Configuration for BGP capability settings."""

    evpn_ethernet_segments: Iterable[DeviceBgpIpv4InterfacePeerEvpnEthernetSegment]
    """
    This contains the list of Ethernet Virtual Private Network (EVPN) Ethernet
    Segments (ES) Per BGP Peer for IPv4 Address Family Identifier (AFI).

    Each Ethernet Segment contains a list of EVPN Instances (EVIs) . Each EVI
    contains a list of Broadcast Domains. Each Broadcast Domain contains a list of
    MAC/IP Ranges.

    <Ethernet Segment, EVI, Broadcast Domain> is responsible for advertising
    Ethernet Auto-discovery Route Per EVI (Type 1).

    <Ethernet Segment, EVI> is responsible for advertising Ethernet Auto-discovery
    Route Per Ethernet Segment (Type 1).

    <Ethernet Segment, EVI, Broadcast Domain, MAC/IP> is responsible for advertising
    MAC/IP Advertisement Route (Type 2).

    <Ethernet Segment, EVI, Broadcast Domain> is responsible for advertising
    Inclusive Multicast Ethernet Tag Route (Type 3).

    Ethernet Segment is responsible for advertising Ethernet Segment Route (Type 4).
    """

    graceful_restart: BgpGracefulRestartParam
    """
    The Graceful Restart Capability (RFC 4724) is a BGP capability that can be used
    by a BGP speaker to indicate its ability to preserve its forwarding state during
    BGP restart. The Graceful Restart (GR) capability is advertised in OPEN messages
    sent between BGP peers. After a BGP session has been established, and the
    initial routing update has been completed, an End-of-RIB (Routing Information
    Base) marker is sent in an UPDATE message to convey information about routing
    convergence.
    """

    learned_information_filter: BgpLearnedInformationFilterParam
    """
    Configuration for controlling storage of BGP learned information recieved from
    the peer.
    """

    replay_updates: BgpUpdateReplayParam
    """
    BGP Updates to be sent to the peer as specified after the session is
    established.
    """

    v4_routes: Iterable[BgpV4RouteRangeParam]
    """Emulated BGPv4 route ranges."""

    v4_srte_policies: Iterable[BgpSrteV4PolicyParam]
    """
    Segment Routing Traffic Engineering (SR TE) Policies for IPv4 Address Family
    Identifier (AFI).
    """

    v6_routes: Iterable[BgpV6RouteRangeParam]
    """Emulated BGPv6 route ranges."""

    v6_srte_policies: Iterable[BgpSrteV6PolicyParam]
    """
    Segment Routing Traffic Engineering (SR TE) Policies for IPv6 Address Family
    Identifier (AFI).
    """


class DeviceBgpIpv4Interface(TypedDict, total=False):
    ipv4_name: Required[str]
    """
    The unique name of the IPv4, Loopback IPv4 interface or DHCPv4 client used as
    the source IP for this list of BGP peers.

    x-constraint:

    - /components/schemas/Device.Ipv4/properties/name
    - /components/schemas/Device.Ipv4Loopback/properties/name
    - /components/schemas/Device.Dhcpv4client/properties/name
    """

    peers: Iterable[DeviceBgpIpv4InterfacePeer]
    """This contains the list of BGPv4 peers configured on this interface."""


class DeviceBgpIpv6InterfacePeerEvpnEthernetSegmentEviEviVxlanBroadcastDomain(TypedDict, total=False):
    cmac_ip_range: Iterable[BgpCMacIPRangeParam]
    """
    This contains the list of Customer MAC/IP Ranges to be configured per Broadcast
    Domain.

    Advertises following route - Type 2 - MAC/IP Advertisement Route.
    """

    ethernet_tag_id: int
    """The Ethernet Tag ID of the Broadcast Domain."""

    vlan_aware_service: bool
    """VLAN-Aware service to be enabled or disabled."""


class DeviceBgpIpv6InterfacePeerEvpnEthernetSegmentEviEviVxlan(TypedDict, total=False):
    ad_label: int
    """
    The Auto-discovery Route label (AD label) value, which gets advertised in the
    Ethernet Auto-discovery Route per <EVI, ESI>
    """

    advanced: BgpRouteAdvancedParam
    """Configuration for advanced BGP route range settings."""

    as_path: BgpAsPathParam
    """Optional AS PATH settings."""

    broadcast_domains: Iterable[DeviceBgpIpv6InterfacePeerEvpnEthernetSegmentEviEviVxlanBroadcastDomain]
    """This contains the list of Broadcast Domains to be configured per EVI."""

    communities: Iterable[BgpCommunityParam]
    """Optional community settings."""

    ext_communities: Iterable[BgpExtCommunityParam]
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

    l3_route_target_export: Iterable[BgpRouteTargetParam]
    """List of Layer 3 Virtual Network Identifier (L3VNI) Export Route Targets."""

    l3_route_target_import: Iterable[BgpRouteTargetParam]
    """List of L3VNI Import Route Targets."""

    pmsi_label: int
    """
    Downstream assigned VNI to be carried as Part of P-Multicast Service Interface
    Tunnel attribute (PMSI Tunnel Attribute) in Type 3 Inclusive Multicast Ethernet
    Tag Route.
    """

    replication_type: Literal["ingress_replication"]
    """This model only supports Ingress Replication"""

    route_distinguisher: BgpRouteDistinguisherParam
    """
    Colon separated Extended Community value of 6 Bytes - "AS number: Value"
    identifying an EVI. Example - for the as_2octet "60005:100".
    """

    route_target_export: Iterable[BgpRouteTargetParam]
    """
    List of Layer 2 Virtual Network Identifier (L2VNI) export targets associated
    with this EVI.
    """

    route_target_import: Iterable[BgpRouteTargetParam]
    """List of L2VNI import targets associated with this EVI."""


class DeviceBgpIpv6InterfacePeerEvpnEthernetSegmentEvi(TypedDict, total=False):
    choice: Literal["evi_vxlan"]

    evi_vxlan: DeviceBgpIpv6InterfacePeerEvpnEthernetSegmentEviEviVxlan
    """EVPN VXLAN instance to be configured per Ethernet Segment."""


class DeviceBgpIpv6InterfacePeerEvpnEthernetSegment(TypedDict, total=False):
    active_mode: Literal["single_active", "all_active"]
    """Single Active or All Active mode Redundancy mode selection for Multi-home."""

    advanced: BgpRouteAdvancedParam
    """Configuration for advanced BGP route range settings."""

    as_path: BgpAsPathParam
    """Optional AS PATH settings."""

    communities: Iterable[BgpCommunityParam]
    """Optional community settings."""

    df_election: BgpEthernetSegmentDfElectionParam
    """Designated Forwarder (DF) election configuration."""

    esi: str
    """
    10-octet Ethernet Segment Identifier (ESI) Example - For multi-home scenario
    nonZero ESI is '10000000000000000000' .
    """

    esi_label: int
    """The label value to be advertised as ESI Label in ESI Label Extended Community.

    This is included in Ethernet Auto-discovery per ES Routes advertised by a
    router.
    """

    evis: Iterable[DeviceBgpIpv6InterfacePeerEvpnEthernetSegmentEvi]
    """This contains the list of EVIs."""

    ext_communities: Iterable[BgpExtCommunityParam]
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


class DeviceBgpIpv6InterfacePeerSegmentRouting(TypedDict, total=False):
    advertise_sr_te_policy: bool
    """TBD"""

    auto_generate_segment_left_value: bool
    """TBD"""

    copy_time_to_live: bool
    """TBD"""

    ingress_supports_vpn: bool
    """TBD"""

    max_sids_per_srh: int
    """TBD"""

    reduced_encapsulation: bool
    """TBD"""

    segment_left_value: int
    """TBD"""

    time_to_live: int
    """TBD"""


class DeviceBgpIpv6InterfacePeer(TypedDict, total=False):
    as_number: Required[int]
    """Autonomous System Number (AS number or ASN)"""

    as_type: Required[Literal["ibgp", "ebgp"]]
    """The type of BGP autonomous system.

    External BGP is used for BGP links between two or more autonomous systems
    (ebgp). Internal BGP is used within a single autonomous system (ibgp). BGP
    property defaults are aligned with this object defined as an internal BGP peer.
    If the as_type is specified as 'ebgp' then other properties will need to be
    specified as per an external BGP peer. Specifically, for 'ebgp', 'as_set_mode'
    attribute in 'as_path' field in any Route Range should be changed from default
    value 'do_not_include_local_as' to any other value.
    """

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects. Globally unique name of
    an object. It also serves as the primary key for arrays of objects.
    """

    peer_address: Required[str]
    """IPv6 address of the BGP peer for the session"""

    advanced: BgpAdvancedParam
    """Configuration for BGP advanced settings."""

    as_number_width: Literal["two", "four"]
    """The width in bytes of the as_number values.

    Any as_number values that exceeds the width MUST result in an error.
    """

    capability: BgpCapabilityParam
    """Configuration for BGP capability settings."""

    evpn_ethernet_segments: Iterable[DeviceBgpIpv6InterfacePeerEvpnEthernetSegment]
    """
    This contains the list of Ethernet Virtual Private Network (EVPN) Ethernet
    Segments (ES) Per BGP Peer for IPv6 Address Family Identifier (AFI).

    Each Ethernet Segment contains a list of EVPN Instances (EVIs) . Each EVI
    contains a list of Broadcast Domains. Each Broadcast Domain contains a list of
    MAC/IP Ranges.

    <Ethernet Segment, EVI, Broadcast Domain> is responsible for advertising
    Ethernet Auto-discovery Route Per EVI (Type 1).

    <Ethernet Segment, EVI> is responsible for advertising Ethernet Auto-discovery
    Route Per Ethernet Segment (Type 1).

    <Ethernet Segment, EVI, Broadcast Domain, MAC/IP> is responsible for advertising
    MAC/IP Advertisement Route (Type 2).

    <Ethernet Segment, EVI, Broadcast Domain> is responsible for advertising
    Inclusive Multicast Ethernet Tag Route (Type 3).

    Ethernet Segment is responsible for advertising Ethernet Segment Route (Type 4).
    """

    graceful_restart: BgpGracefulRestartParam
    """
    The Graceful Restart Capability (RFC 4724) is a BGP capability that can be used
    by a BGP speaker to indicate its ability to preserve its forwarding state during
    BGP restart. The Graceful Restart (GR) capability is advertised in OPEN messages
    sent between BGP peers. After a BGP session has been established, and the
    initial routing update has been completed, an End-of-RIB (Routing Information
    Base) marker is sent in an UPDATE message to convey information about routing
    convergence.
    """

    learned_information_filter: BgpLearnedInformationFilterParam
    """
    Configuration for controlling storage of BGP learned information recieved from
    the peer.
    """

    replay_updates: BgpUpdateReplayParam
    """
    BGP Updates to be sent to the peer as specified after the session is
    established.
    """

    segment_routing: DeviceBgpIpv6InterfacePeerSegmentRouting
    """Configuration for BGPv6 segment routing settings."""

    v4_routes: Iterable[BgpV4RouteRangeParam]
    """Emulated BGPv4 route ranges."""

    v4_srte_policies: Iterable[BgpSrteV4PolicyParam]
    """
    Segment Routing Traffic Engineering (SR TE) Policies for IPv4 Address Family
    Identifier (AFI).
    """

    v6_routes: Iterable[BgpV6RouteRangeParam]
    """Emulated BGPv6 route ranges."""

    v6_srte_policies: Iterable[BgpSrteV6PolicyParam]
    """
    Segment Routing Traffic Engineering (SR TE) Policies for IPv6 Address Family
    Identifier (AFI).
    """


class DeviceBgpIpv6Interface(TypedDict, total=False):
    ipv6_name: Required[str]
    """
    The unique name of IPv6 Loopback IPv6 interface or DHCPv4 client used as the
    source IP for this list of BGP peers.

    x-constraint:

    - /components/schemas/Device.Ipv6/properties/name
    - /components/schemas/Device.Ipv6Loopback/properties/name
    - /components/schemas/Device.Dhcpv6client/properties/name
    """

    peers: Iterable[DeviceBgpIpv6InterfacePeer]
    """This contains the list of BGPv6 peers configured on this interface."""


class DeviceBgp(TypedDict, total=False):
    router_id: Required[str]
    """The BGP router ID is a unique identifier used by BGP.

    It is a 32-bit value that is often represented by an IPv4 address.
    """

    ipv4_interfaces: Iterable[DeviceBgpIpv4Interface]
    """
    This contains an array of references to IPv4 interfaces, each of which will have
    list of peers to different destinations.
    """

    ipv6_interfaces: Iterable[DeviceBgpIpv6Interface]
    """
    This contains an array of references to IPv6 interfaces, each of which will have
    list of peers to different destinations.
    """


class DeviceDhcpServerIpv4InterfaceAddressPoolOptions(TypedDict, total=False):
    echo_relay_with_tlv_82: bool
    """
    If selected, the DHCP server includes in its replies the TLV information for the
    DHCPv4 Relay Agent Option 82 and the corresponding sub-TLVs that it receives
    from a DHCP relay agent, otherwise it replies without including this TLV.
    """

    primary_dns_server: str
    """
    The primary DNS server address that is offered to DHCP clients that request this
    information through a TLV option.
    """

    router_address: str
    """The Router address advertised by the DHCPv4 server in Offer and Ack messages."""

    secondary_dns_server: str
    """
    The primary DNS server address that is offered to DHCP clients that request this
    information through a TLV option.
    """


class DeviceDhcpServerIpv4InterfaceAddressPool(TypedDict, total=False):
    start_address: Required[str]
    """The IPv4 address of the first lease pool."""

    count: int
    """The total number of addresses in the pool."""

    lease_time: int
    """The duration of time in seconds that is assigned to a lease."""

    name: str
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    options: DeviceDhcpServerIpv4InterfaceAddressPoolOptions
    """Optional configuration for DHCPv4 address pool for the lease."""

    prefix_length: int
    """The IPv4 network prefix length to be applied to the address."""

    step: int
    """The increment value for the lease address within the lease pool.

    The value is incremented according to the prefix_length and step.
    """


class DeviceDhcpServerIpv4Interface(TypedDict, total=False):
    address_pools: Required[Iterable[DeviceDhcpServerIpv4InterfaceAddressPool]]
    """List of DHCPv4 Server Lease parameters"""

    ipv4_name: Required[str]
    """The unique name of the IPv4 on which DHCPv4 server will run.

    x-constraint:

    - /components/schemas/Device.Ipv4/properties/name
    """

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """


class DeviceDhcpServerIpv6InterfaceLeaseIaTypeIanapd(TypedDict, total=False):
    iana: Dhcpv6ServerPoolInfoParam
    """The pool configurations for IA types iana in ianapd."""

    iapd: Dhcpv6ServerIapdPoolInfoParam
    """The pool configurations for IA types iapd in ianapd."""


class DeviceDhcpServerIpv6InterfaceLeaseIaType(TypedDict, total=False):
    choice: Literal["iana", "iata", "iapd", "ianapd"]
    """Identity Association: a collection of leases assigned to a client.

    Each IA has an associated IAID. Each IA holds one type of lease, like an
    identity association for temporary addresses (IA_TA) holds temporary addresses,
    and an identity association for prefix delegation (IA_PD).
    """

    iana: Dhcpv6ServerPoolInfoParam
    """The container for pool configurations for IA types iana and iata."""

    ianapd: DeviceDhcpServerIpv6InterfaceLeaseIaTypeIanapd
    """The container for pool configurations for IA type ianapd."""

    iapd: Dhcpv6ServerIapdPoolInfoParam
    """The container for prefix pool configurations for IA type iapd."""

    iata: Dhcpv6ServerPoolInfoParam
    """The container for pool configurations for IA types iana and iata."""


class DeviceDhcpServerIpv6InterfaceLease(TypedDict, total=False):
    ia_type: Required[DeviceDhcpServerIpv6InterfaceLeaseIaType]

    lease_time: int
    """
    The Life Time length in seconds that is assigned to a lease if the requesting
    DHCP client does not specify a specific expiration time.
    """


class DeviceDhcpServerIpv6InterfaceOptionsBootfileURLBootfileParam(TypedDict, total=False):
    parameter: Required[str]
    """UTF-8 strings are parameters needed for booting, e.g., kernel parameters."""


class DeviceDhcpServerIpv6InterfaceOptionsBootfileURL(TypedDict, total=False):
    url: Required[str]
    """The URL for the boot file. It must comply with STD 66 format."""

    associated_dhcp_messages: Dhcpv6ServerOptionsIncludedMessagesParam
    """The list of dhcpv6 client messages where this option is included."""

    bootfile_params: Iterable[DeviceDhcpServerIpv6InterfaceOptionsBootfileURLBootfileParam]
    """
    They are used to specify parameters for the boot file (similar to the command
    line arguments in most modern operating systems). For example, these parameters
    could be used to specify the root file system of the OS kernel, or the location
    from which a second-stage boot-loader program can download its configuration
    file.
    """


class DeviceDhcpServerIpv6InterfaceOptionsDNSSecondaryDNS(TypedDict, total=False):
    ip: str
    """
    The secondary DNS server address that is offered to DHCP clients that request
    this information through a TLV option.
    """


class DeviceDhcpServerIpv6InterfaceOptionsDNS(TypedDict, total=False):
    primary: Required[str]
    """
    The primary DNS server address that is offered to DHCP clients that request this
    information through a TLV option.
    """

    secondary_dns: Iterable[DeviceDhcpServerIpv6InterfaceOptionsDNSSecondaryDNS]
    """DHCP server secondary dns configuration options.

    If included secondary DNS server address will be offered to DHCP clients that
    request this information through a TLV option.
    """


class DeviceDhcpServerIpv6InterfaceOptionsVendorInfo(TypedDict, total=False):
    associated_dhcp_messages: Required[Dhcpv6ServerOptionsIncludedMessagesParam]
    """The list of dhcpv6 client messages where this option is included."""

    enterprise_number: Required[int]
    """The vendor's registered Enterprise Number as registered with IANA."""

    option_data: Required[Iterable[Dhcpv6OptionsVendorSpecificOptionsParam]]
    """
    An opaque object of octets,interpreted by vendor-specific code on the clients
    and servers.
    """


class DeviceDhcpServerIpv6InterfaceOptions(TypedDict, total=False):
    bootfile_url: DeviceDhcpServerIpv6InterfaceOptionsBootfileURL
    """
    The server sends this option to inform the client about a URL to a boot file
    which client will use for network boots.
    """

    dns: DeviceDhcpServerIpv6InterfaceOptionsDNS
    """Additional DHCP server primary dns and other configuration options."""

    vendor_info: DeviceDhcpServerIpv6InterfaceOptionsVendorInfo
    """
    This option is used by servers to exchange vendor-specific information with
    clients.
    """


class DeviceDhcpServerIpv6Interface(TypedDict, total=False):
    ipv6_name: Required[str]
    """The unique name of the IPv6 on which DHCPv6 server will run.

    x-constraint:

    - /components/schemas/Device.Ipv6/properties/name
    """

    leases: Required[Iterable[DeviceDhcpServerIpv6InterfaceLease]]
    """Array of DHCP pools configured on a server."""

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    options: DeviceDhcpServerIpv6InterfaceOptions
    """Optional DHCPv4 Server options that are sent in Dhcp server messages."""

    rapid_commit: bool
    """
    If Rapid Commit is set, server responds to client initiated Rapid Commit
    two-message exchanges.
    """

    reconfigure_via_relay_agent: bool
    """
    If the server does not have an address to which it can send the Reconfigure
    message directly to the client, the server uses a Relay-reply message to send
    the Reconfigure message to a relay agent that will relay the message to the
    client.
    """


class DeviceDhcpServer(TypedDict, total=False):
    ipv4_interfaces: Iterable[DeviceDhcpServerIpv4Interface]
    """
    This contains an array of references to IPv4 interfaces, each of which will
    contain one DHCPv4 server.
    """

    ipv6_interfaces: Iterable[DeviceDhcpServerIpv6Interface]
    """
    This contains an array of references to IPv6 interfaces, each of which will
    contain one DHCPv6 server.
    """


class DeviceEthernetConnectionSimulatedLink(TypedDict, total=False):
    link_type: Literal["primary", "secondary"]
    """
    By default, simulated links are treated as Primary links , which means that the
    intention is for connected device to advertise this and full topology of devices
    connected to it. e.g. when advertised as ISIS Simulated Topology.

    All simulated links inside one topology subset would normally can point to only
    other unconnected devices in the same topology or to the 'root' emulated device.
    If a link is designated as secondary , only that link information will be
    advertised by the IGP e.g. ISIS , and not the entire topology behind it. The
    optional secondary option allows emulation of external link scenarios where a
    simulated device (e.g. part of a ISIS simulated topology ) is advertised as
    reachable part of the topology by the emulated router behind which this is
    configured , as well as the other end of the secondary link which could be

    - 1. either a simulated device behind a different emulated router.
    - 2. or an emulated router on same or different port. This allows emulation of
         scenarios where one device/router is emulated to be reachable from
         different Emulated Routers connected to the Device Under Test. (e.g. for
         FRR scenarios)

    If an implementation does not support multiple primary links from same simulated
    topology i.e. full topology advertised via multiple emulated routers, it should
    return an error during set_config operation with such a topology.
    """

    remote_simulated_link: str
    """
    Name of the remote end of the simulated interface which also must be a
    simulated_link on a device which might be acting either as an unconnected device
    in a simulated topology ( all ethernet links of type simulated_link ) or an
    emulated device connected to the Device Under Test (has at atleast one ethernet
    interface with connection to the port or lag connected to the DUT)

    x-constraint:

    - #/components/schemas/Device.Ethernet/properties/name
    """


class DeviceEthernetConnection(TypedDict, total=False):
    choice: Literal["port_name", "lag_name", "vxlan_name", "simulated_link"]
    """port_name, lag_name, vxlan_name or simulated_link"""

    lag_name: str
    """Name of the LAG that the Ethernet interface is configured on.

    x-constraint:

    - /components/schemas/Lag/properties/name
    """

    port_name: str
    """Name of the port that the Ethernet interface is configured on.

    x-constraint:

    - /components/schemas/Port/properties/name
    """

    simulated_link: DeviceEthernetConnectionSimulatedLink
    """
    Details of the internal link which can be used to create simulated device
    topologies behind an emulated router. MAC, VLAN and MTU information for the
    internal links are not used for purposes of emulating Simulated Topologies (
    e.g. by ISIS Emulated Router behind which this is configured )
    """

    vxlan_name: str
    """
    Name of the VXLAN instance (or VXLAN tunnel) that this Ethernet interface is
    connected to.

    x-constraint:

    - #/components/schemas/Vxlan.V4Tunnel/properties/name
    - #/components/schemas/Vxlan.V6Tunnel/properties/name
    """


class DeviceEthernetDhcpv4InterfaceParametersRequestList(TypedDict, total=False):
    rebinding_timer: bool
    """Request for the rebinding timer (T2).

    When expires, the client transitions to the REBINDING state.
    """

    renewal_timer: bool
    """Request for the renewal timer, T1.

    When the timer expires, the client transitions from the BOUND state to the
    RENEWING state.
    """

    router: bool
    """
    Request for the router option that specifies a list of IP addresses for routers
    on the client's subnet.
    """

    subnet_mask: bool
    """
    Request for the subnet mask option specifies the client's subnet mask as per
    RFC950.
    """


class DeviceEthernetDhcpv4Interface(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    broadcast: bool
    """
    If the broadcast bit is set, then the server and relay agent broadcast DHCPOFFER
    and DHCPACK messages.
    """

    choice: Literal["first_server", "server_address"]
    """
    The client receives one or more DHCPOFFER messages from one or more servers and
    client may choose to wait for multiple responses. The client chooses one server
    from which to request configuration parameters, based on the configuration
    parameters offered in the DHCPOFFER messages.

    - first_server: if selected, the subnet accepts the IP addresses offered by the
      first server to respond with an offer of IP addresses.
    - server_address: The address of the DHCP server from which the subnet will
      accept IP addresses.
    """

    parameters_request_list: DeviceEthernetDhcpv4InterfaceParametersRequestList
    """Optional parameters field request list of DHCPv4 Client."""

    server_address: str
    """The address of the DHCP server."""


class DeviceEthernetDhcpv6InterfaceDuidTypeEn(TypedDict, total=False):
    enterprise_id: int
    """
    4-octet vendor's registered Private Enterprise Number as maintained by IANA
    [IANA-PEN].
    """

    vendor_id: int
    """Unique identifier assigned by the vendor."""


class DeviceEthernetDhcpv6InterfaceDuidType(TypedDict, total=False):
    choice: Literal["llt", "en", "ll"]
    """Each DHCP client and server has a DUID.

    DHCP clients use DUIDs to identify a server in messages where a server needs to
    be identified.
    """

    en: DeviceEthernetDhcpv6InterfaceDuidTypeEn
    """The container for the DUID-EN.

    This consists of the 4-octet vendor's registered Private Enterprise Number as
    maintained by IANA [IANA-PEN] followed by a unique identifier assigned by the
    vendor.
    """

    ll: object
    """The container for DUID-LL and DUID-LLT."""

    llt: object
    """The container for DUID-LL and DUID-LLT."""


class DeviceEthernetDhcpv6InterfaceIaType(TypedDict, total=False):
    choice: Literal["iana", "iata", "iapd", "ianapd"]
    """Identity Association: Each IA has an associated IAID.

    IA_NA and IA_TA options represent different types of IPv6 addresses and
    parameters accepted by DHCPv6 clients each used in different context by an IPv6
    node. IA_NA is the Identity Association for Non-temporary Addresses option.
    IA_TA is the Identity Association for Temporary Addresses option. IA_PD and
    IA_NAPD options represent one or more IPv6 prefix and parameters. IA_PD is the
    Identity Association for Prefix Delegation and IA_NAPD s the Identity
    Association for Temporary Prefix Delegation.
    """

    iana: DeviceDhcpv6clientIaTimeValueParam
    """
    The container for the suggested times at which the client contacts the server or
    any available server.
    """

    ianapd: DeviceDhcpv6clientIaTimeValueParam
    """
    The container for the suggested times at which the client contacts the server or
    any available server.
    """

    iapd: DeviceDhcpv6clientIaTimeValueParam
    """
    The container for the suggested times at which the client contacts the server or
    any available server.
    """


class DeviceEthernetDhcpv6InterfaceOptionsFqdn(TypedDict, total=False):
    domain_name: Required[str]
    """
    The Domain Name part of the option carries all or part of the FQDN of a DHCPv6
    client. A client MAY also leave the Domain Name field empty if it desires the
    server to provide a name. A fully qualified domain name (FQDN) is the complete
    address of an internet host or computer. It provides its exact location within
    the domain name system (DNS) by specifying the hostname, domain name and
    top-level domain (TLD). An FQDN isn't the same as a URL but rather is a part of
    it that fully identifies the server to which the request is addressed. An FQDN
    doesn't carry the TCP/IP protocol information, such as Hypertext Transfer
    Protocol (HTTP) or Hypertext Transfer Protocol Secure (HTTPS), which is always
    used at the beginning of a URL. Therefore, adding the prefix http:// or https://
    to the FQDN turns it into a full URL. One example can be microsoft.com.
    """

    associated_dhcp_messages: Dhcpv6ClientOptionsIncludedMessagesParam
    """The list of dhcpv6 client messages where this option is included."""

    flag_n: bool
    """The "N" bit indicates whether the server should not perform any DNS updates.

    A client sets this bit to 0 to request that the server should perform updates
    (the PTR RR and possibly the AAAA RR based on the "S" bit) or to 1 to request
    that the server should not perform any DNS updates. A server sets the "N" bit to
    indicate whether the server shall (0) or shall not (1) perform DNS updates. If
    the "N" bit is 1, the "S" bit MUST be 0.
    """

    flag_o: bool
    """
    The "O" bit indicates whether the server has overridden the client's preference
    for the "S" bit. A client must set this bit to 0. A server must set this bit to
    1 if the "S" bit in its reply to the client does not match the "S" bit received
    from the client.
    """

    flag_s: bool
    """
    The "S" bit indicates whether the server should or should not perform the AAAA
    RR (FQDN-to-address) DNS updates. A client sets the bit to 0 to indicate that
    the server should not perform the updates and 1 to indicate that the server
    should perform the updates. The state of the bit in the reply from the server
    indicates the action to be taken by the server. If it is 1, the server has taken
    responsibility for AAAA RR updates for the FQDN.
    """


class DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidEn(TypedDict, total=False):
    enterprise_number: Required[int]
    """Vendor's registered private enterprise number as maintained by IANA."""

    identifier: Required[str]
    """The unique identifier assigned by the vendor."""


class DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidLl(TypedDict, total=False):
    link_layer_address: Required[Dhcpv6ClientOptionsLinkLayerAddressParam]
    """The link-layer address is stored in canonical form, as described in RFC 2464."""


class DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidLlt(TypedDict, total=False):
    link_layer_address: Required[Dhcpv6ClientOptionsLinkLayerAddressParam]
    """The link-layer address is stored in canonical form, as described in RFC 2464."""

    time: Required[int]
    """
    The time value is the time that the DUID is generated represented in seconds
    since midnight (UTC), January 1, 2000, modulo 2^32. The DUID generatation time
    will the current time when dhcpv6 client contacts the server.
    """


class DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidUuidVariant(TypedDict, total=False):
    choice: Literal["ncs", "dce", "guid", "var_reserved"]
    """The current variants are ncs, dce,microsoft guid and reserved."""


class DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidUuidVersion(TypedDict, total=False):
    choice: Literal["v_1", "v_2", "v_3", "v_4", "v_5"]
    """
    The version values are from 1 to 5 in the most significant 4 bits of the
    timestamp (bits 4 through 7 of the time_hi_and_version field).
    """


class DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidUuid(TypedDict, total=False):
    clock_seq_hi_and_reserved: int
    """The high field of the clock sequence multiplexed with the variant."""

    clock_seq_low: int
    """The low field of the clock sequence."""

    node: str
    """The spatially unique node identifier."""

    time_hi_and_version: int
    """The high field of the timestamp multiplexed with the version number."""

    time_low: int
    """The low field of the timestamp."""

    time_mid: int
    """The middle field of the timestamp."""

    variant: DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidUuidVariant
    """The variant field determines the layout of the UUID.

    It is multiplexed with clock_seq_hi_and_reserved.
    """

    version: DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidUuidVersion
    """
    The version number is in the most significant 4 bits of the timestamp (bits 4
    through 7 of the time_hi_and_version field).
    """


class DeviceEthernetDhcpv6InterfaceOptionsServerIdentifier(TypedDict, total=False):
    choice: Literal["duid_llt", "duid_en", "duid_ll", "duid_uuid"]
    """The Identifier option is used to carry a DUID.

    The option code is 2. The server identifier identifies a server. This option is
    used when client wants to contact a particular server.
    """

    duid_en: DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidEn
    """DUID assigned by vendor based on enterprise number."""

    duid_ll: DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidLl
    """DUID based on Link Layer address.

    Hardware Type will be auto assigned to ethernet type.
    """

    duid_llt: DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidLlt
    """DUID based on Link Layer address plus time.

    Hardware Type will be auto assigned to ethernet type.
    """

    duid_uuid: DeviceEthernetDhcpv6InterfaceOptionsServerIdentifierDuidUuid
    """DUID embedded a Universally Unique IDentifier (UUID).

    A UUID is an identifier that is unique across both space and time, with respect
    to the space of all UUIDs.
    """


class DeviceEthernetDhcpv6InterfaceOptionsVendorClass(TypedDict, total=False):
    associated_dhcp_messages: Required[Dhcpv6ClientOptionsIncludedMessagesParam]
    """The dhcpv6 client messages where this option is included."""

    class_data: Required[List[str]]
    """
    The opaque data representing the hardware configuration of the host on which the
    client is running. Examples of class data instances might include the version of
    the operating system the client is running or the amount of memory installed on
    the client.
    """

    enterprise_number: Required[int]
    """The vendor's registered Enterprise Number as registered with IANA."""


class DeviceEthernetDhcpv6InterfaceOptionsVendorInfo(TypedDict, total=False):
    associated_dhcp_messages: Required[Dhcpv6ClientOptionsIncludedMessagesParam]
    """The list of dhcpv6 client messages where this option is included."""

    enterprise_number: Required[int]
    """The vendor's registered Enterprise Number as registered with IANA."""

    option_data: Required[Iterable[Dhcpv6OptionsVendorSpecificOptionsParam]]
    """
    An opaque object of octets,interpreted by vendor-specific code on the clients
    and servers.
    """


class DeviceEthernetDhcpv6InterfaceOptions(TypedDict, total=False):
    fqdn: DeviceEthernetDhcpv6InterfaceOptionsFqdn
    """
    DHCPv6 server needs to know the FQDN of the client for the addresses for the
    client's IA_NA bindings in order to update the IPv6-address-to-FQDN mapping.
    This option allows the client to convey its FQDN to the server. The Client FQDN
    option also contains Flags that DHCPv6 clients and servers use to negotiate who
    does which update.
    """

    server_identifier: DeviceEthernetDhcpv6InterfaceOptionsServerIdentifier
    """A client uses multicast to reach all servers or an individual server.

    An individual server is indicated by specifying that server's DUID in a Server
    Identifier option in the client's message (all servers will receive this message
    but only the indicated server will respond). All servers are indicated by not
    supplying this option.
    """

    vendor_class: DeviceEthernetDhcpv6InterfaceOptionsVendorClass
    """
    The vendor class option is used by a client to identify the vendor that
    manufactured the hardware on which the client is running. The information
    contained in the data area of this option is contained in one or more opaque
    fields that identify details of the hardware configuration.
    """

    vendor_info: DeviceEthernetDhcpv6InterfaceOptionsVendorInfo
    """
    This option is used by clients to exchange vendor-specific information with
    servers.
    """


class DeviceEthernetDhcpv6InterfaceOptionsRequestRequestCustom(TypedDict, total=False):
    type: Required[int]
    """The type of the Custom option TLV."""


class DeviceEthernetDhcpv6InterfaceOptionsRequestRequest(TypedDict, total=False):
    choice: Literal["vendor_information", "name_servers", "fqdn", "bootfile_url", "sztp", "custom"]
    """
    The Option Request option is used to identify a list of options in a message
    between a client and a server. The option code is 6. - Vendor_specific
    information option, requested by clients for vendor-specific informations from
    servers. - DNS Recursive Name Server Option, requested by clients to get the
    list ofIPv6 addresses of DNS recursive name servers to which DNS queries may be
    sent by the client resolver in order of preference.

    - Client FQDN option - indicates whether the client or the DHCP server should
      update DNS with the AAAA record corresponding to the assigned IPv6 address and
      the FQDN provided in this option. The DHCP server always updates the PTR
      record.
    - bootfile_url, if client is configured for network booting then the client must
      use this option to obtain the boot file url from the server.
    - sztp. Securely provision a networking device when it is booting in a
      factory-default state.
    """

    custom: DeviceEthernetDhcpv6InterfaceOptionsRequestRequestCustom
    """
    The Custom option is used to provide a not so well known option in the message
    between a client and a server.
    """


class DeviceEthernetDhcpv6InterfaceOptionsRequest(TypedDict, total=False):
    associated_dhcp_messages: Required[Dhcpv6ClientOptionsIncludedMessagesParam]
    """The list of dhcpv6 client messages where this option is included."""

    request: Required[Iterable[DeviceEthernetDhcpv6InterfaceOptionsRequestRequest]]
    """List of options requested by a client from a server."""


class DeviceEthernetDhcpv6Interface(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    duid_type: DeviceEthernetDhcpv6InterfaceDuidType
    """Each DHCP client and server has a DUID.

    DHCP clients and servers use DUIDs to identify each other.
    """

    ia_type: DeviceEthernetDhcpv6InterfaceIaType
    """Each IA has an associated IAID.

    Differnet IA options represent different types of IPv6 addresses and parameters
    accepted by DHCPv6 clients each used in different context by an IPv6 node.
    """

    options: DeviceEthernetDhcpv6InterfaceOptions
    """Optional DHCPv4 Client options that are sent in Dhcp client messages."""

    options_request: DeviceEthernetDhcpv6InterfaceOptionsRequest
    """The options requested by a client from a server in the options request option."""

    rapid_commit: bool
    """
    If Rapid Commit is set, client initiates Rapid Commit two-message exchange by
    including Rapid Commit option in Solicit message.
    """


class DeviceEthernetIpv4AddressGatewayMac(TypedDict, total=False):
    auto: str
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["auto", "value"]
    """auto or configured value."""

    value: str


class DeviceEthernetIpv4Address(TypedDict, total=False):
    address: Required[str]
    """The IPv4 address"""

    gateway: Required[str]
    """The IPv4 address of the gateway"""

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    gateway_mac: DeviceEthernetIpv4AddressGatewayMac
    """By default auto(resolved gateway mac) is set.

    Setting a value would mean that ARP will not be used for learning MAC of
    connected device. The user-configured MAC address will be used for auto-filling
    the destination MAC address in the control and data packets sent from this IPv4
    endpoint whenever applicable.
    """

    prefix: int
    """The prefix of the IPv4 address."""


class DeviceEthernetIpv6AddressGatewayMac(TypedDict, total=False):
    auto: str
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["auto", "value"]
    """auto or configured value."""

    value: str


class DeviceEthernetIpv6Address(TypedDict, total=False):
    address: Required[str]
    """The IPv6 address."""

    gateway: Required[str]
    """The IPv6 gateway address."""

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    gateway_mac: DeviceEthernetIpv6AddressGatewayMac
    """By default auto(resolved gateway mac) is set.

    Setting a value would mean that ND will not be used for learning MAC of
    connected device. The user-configured MAC address will be used for auto-filling
    the destination MAC address in the control and data packets sent from this IPv6
    endpoint whenever applicable.
    """

    prefix: int
    """The network prefix."""


class DeviceEthernet(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    connection: DeviceEthernetConnection
    """Device connection to physical, LAG or another device."""

    dhcpv4_interfaces: Iterable[DeviceEthernetDhcpv4Interface]
    """List of DHCPv4 Clients Configuration."""

    dhcpv6_interfaces: Iterable[DeviceEthernetDhcpv6Interface]
    """List of DHCPv6 Clients Configuration."""

    ipv4_addresses: Iterable[DeviceEthernetIpv4Address]
    """List of IPv4 addresses and their gateways."""

    ipv6_addresses: Iterable[DeviceEthernetIpv6Address]
    """
    List of global IPv6 addresses and their gateways. The Link Local IPv6 address
    will be automatically generated.
    """

    mac: str
    """
    Media Access Control address.The implementation should ensure that the 'mac'
    field is explicitly configured by the user for all types of interfaces as
    denoted by 'connection' attribute except 'simulated_link' where 'mac' is not
    mandatory.
    """

    mtu: int
    """Maximum Transmission Unit."""

    vlans: Iterable[DeviceVlanParam]
    """List of VLANs"""


class DeviceIpv4Loopback(TypedDict, total=False):
    eth_name: Required[str]
    """
    The unique name of the Ethernet interface behind which this Loopback interface
    will be created.

    x-constraint:

    - /components/schemas/Device.Ethernet/properties/name
    """

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    address: str
    """The IPv4 Loopback address with prefix length of 32."""


class DeviceIpv6Loopback(TypedDict, total=False):
    eth_name: Required[str]
    """
    The unique name of the Ethernet interface behind which this Loopback interface
    will be created.

    x-constraint:

    - /components/schemas/Device.Ethernet/properties/name
    """

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    address: str
    """The IPv6 Loopback address with prefix length of 128."""


class DeviceIsisInterfaceAdjacencySid(TypedDict, total=False):
    b_flag: bool
    """The backup flag. If set, the Adj-SID is eligible for protection."""

    choice: Literal["sid_values", "sid_indices"]
    """
    Choice of whether Adjacency-SID carries and absolute value or a relative index
    to the SRGB/SRLB Ranges. Please refer to
    device.isis.segment_routing.router_capability.sr_capability.srgb_ranges for the
    Segment Routing Global Block (SRGB) Descriptor and
    device.isis.segment_routing.router_capability.srlb_ranges for the SR Local Block
    (SRLB). A user needs to configure at least one entry of SID value or SID index.
    If no entry is configured, then an implementation may advertise appropriate
    default SID Value/Index based on the choice. e.g. the first value from the SRGB
    or SRLB range.

    - sid_values: Adjacency-SID carries one or more values and then v_flag is set by
      the implementation.
    - sid_indices: Adjacency-SID carries one or more indices and then v_flag is
      unset by the implementation.
    """

    f_flag: bool
    """The address family flag.

    If unset, then the Adj-SID refers to an adjacency with outgoing IPv4
    encapsulation. If set then the Adj-SID refers to an adjacency with outgoing IPv6
    encapsulation.
    """

    l_flag: bool
    """The local flag.

    If set, then the value/index carried by the Adj-SID has local significance. In
    this case, Adjacency_sid is from
    device.isis.segment_routing.router_capability.srlb_ranges.
    """

    p_flag: bool
    """The persistent flag.

    When set, the P-Flag indicates that the Adj-SID is persistently allocated, i.e.,
    the Adj-SID value remains consistent across router restart and/or interface
    flap.
    """

    s_flag: bool
    """The set flag.

    When set, the S-Flag indicates that the Adj-SID refers to a set of adjacencies
    (and therefore MAY be assigned to other adjacencies as well).
    """

    sid_indices: Iterable[int]
    """One or more adjacency Indices are relative to ranges defined for SRGB or SRLB."""

    sid_values: Iterable[int]
    """The corresponding Adjacency SID as one or more absolute Values for the link."""

    weight: int
    """
    The value represents the weight of the Adj-SID for the purpose of load
    balancing.
    """


class DeviceIsisInterfaceAdvanced(TypedDict, total=False):
    auto_adjust_area: bool
    """
    If a Level 1 Hello is received on this emulated router for an area not currently
    in its area list, an area from the received Hello is added to that list. This
    ensures an area match for all future Level 1 Hellos from the source L1 router.
    """

    auto_adjust_mtu: bool
    """
    If a padded Hello message is received on the interface, the length of the Hello
    packets sent out on that interface is adjusted to match.
    """

    auto_adjust_supported_protocols: bool
    """
    If a Hello message listing supported protocols is received on this emulated
    router, the supported protocols advertised by this router are changed to match
    exactly.
    """

    enable_3way_handshake: bool
    """
    If it is true, the Point-to-Point circuit will include 3-way TLV in its
    Point-to-Point IIH and attempt to establish the adjacency as specified in
    RFC 5303. This field is not applicable if network_type is set to 'broadcast'
    type in ISIS interface.
    """

    p2p_hellos_to_unicast_mac: bool
    """
    If it is true, the Point-to-Point Hello messages will be sent to the unicast MAC
    address.
    """


class DeviceIsisInterfaceAuthentication(TypedDict, total=False):
    auth_type: Required[Literal["md5", "password"]]
    """The circuit authentication method."""

    md5: str
    """MD5 key to be used for authentication."""

    password: str
    """The password, in clear text, to be used for Authentication."""


class DeviceIsisInterfaceLinkProtection(TypedDict, total=False):
    dedicated_1_plus_1: bool
    """Enabling this signifies that a dedicated disjoint link is protecting this link.

    However, the protecting link is not advertised in the link state database and is
    therefore not available for the routing of LSPs.
    """

    dedicated_1_to_1: bool
    """
    Enabling this signifies that there is one dedicated disjoint link of type Extra
    Traffic that is protecting this link.
    """

    enhanced: bool
    """
    Enabling this signifies that a protection scheme that is more reliable than
    Dedicated 1+1.
    """

    extra_traffic: bool
    """Enable this to protect other link or links.

    LSPs on a link of this type are lost if any of the links fail.
    """

    reserved_40: bool
    """This is a Protection Scheme with value 0x40."""

    reserved_80: bool
    """This is a Protection Scheme with value 0x80."""

    shared: bool
    """
    Enable this to share the Extra Traffic links between one or more links of type
    Shared.There are one or more disjoint links of type Extra Traffic that are
    protecting this link.
    """

    unprotected: bool
    """Enabling this signifies that there is no other link protecting this link.

    LSPs on a link of this type are lost if the link fails.
    """


class DeviceIsisInterfaceMultiTopologyID(TypedDict, total=False):
    link_metric: int
    """Specifies the link metric for this topology on the ISIS interface."""

    mt_id: int
    """
    The Multi Topology ID for one of the topologies supported on the ISIS interface.
    """


class DeviceIsisInterface(TypedDict, total=False):
    eth_name: Required[str]
    """The unique name of the Ethernet interface on which ISIS is running.

    Two ISIS interfaces cannot share the same Ethernet. The underlying Ethernet
    Interface can an emulated or simulated interface. A simulated ethernet interface
    can be assumed to be connected by a primary (internal to a simulated topology)
    or a secondary link (connected to a device behind a different simulated
    topology).

    x-constraint:

    - /components/schemas/Device.Ethernet/properties/name
    """

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    adjacency_sids: Iterable[DeviceIsisInterfaceAdjacencySid]
    """List of Adjacency Segment Identifier (Adj-SID) sub-TLVs."""

    advanced: DeviceIsisInterfaceAdvanced
    """Optional container for advanced interface properties."""

    authentication: DeviceIsisInterfaceAuthentication
    """
    The Circuit authentication method used for the interfaces on this emulated ISIS
    v4/v6 router.
    """

    l1_settings: IsisInterfaceLevelParam
    """Settings of Level 1 Hello."""

    l2_settings: IsisInterfaceLevelParam
    """Settings of Level 2 Hello."""

    level_type: Literal["level_1", "level_2", "level_1_2"]
    """
    This indicates whether this router is participating in Level-1 (L1), Level-2
    (L2) or both L1 and L2 domains on this interface.
    """

    link_protection: DeviceIsisInterfaceLinkProtection
    """Link protection on the ISIS link between two interfaces."""

    metric: int
    """The default metric cost for the interface."""

    multi_topology_ids: Iterable[DeviceIsisInterfaceMultiTopologyID]
    """Contains the properties of multiple topologies."""

    network_type: Literal["broadcast", "point_to_point"]
    """The type of network link."""

    srlg_values: Iterable[int]
    """This contains list of SRLG values for the link between two interfaces."""

    traffic_engineering: Iterable[LinkStateTeParam]
    """Contains a list of Traffic Engineering attributes."""


class DeviceIsisAdvanced(TypedDict, total=False):
    area_addresses: List[str]
    """
    Its combination of the ISP and HO-DSP.Usually all nodes within an area have the
    same area address. If no area addresses are configured, a default area of
    "490001" will be advertised.
    """

    csnp_interval: int
    """
    The number of milliseconds between transmissions of Partial Sequence Number PDU.
    """

    enable_attached_bit: bool
    """
    If the Attached bit is enabled, it indicates that the ISIS router is attached to
    another area or the Level 2 backbone. The purpose of an Attached-Bit is to
    accomplish Inter-Area Routing. When an L1/L2 router is connected to more than
    one area, it sets the Attached-bit on its L1 LSP. This can cause a default route
    ( 0.0.0.0/0 ) to be installed by the receiving router.
    """

    enable_hello_padding: bool
    """It enables padding of Hello message to MTU size."""

    lsp_lifetime: int
    """The MaxAge for retaining a learned LSP on this router in seconds."""

    lsp_mgroup_min_trans_interval: int
    """The number of seconds between transmissions of LSPs/MGROUP-PDUs."""

    lsp_refresh_rate: int
    """The rate at which LSPs are re-sent in seconds."""

    max_area_addresses: int
    """The Number of Area Addresses permitted, with a valid range from 0 to 254.

    A zero indicates a maximum of 3 addresses.
    """

    max_lsp_size: int
    """
    The maximum size in bytes of any LSP that can be transmitted over a link of
    equal or less than maximum MTU size.
    """

    psnp_interval: int
    """
    The number of milliseconds between transmissions of Partial Sequence Number PDU.
    """


class DeviceIsisBasic(TypedDict, total=False):
    enable_wide_metric: bool
    """
    When set to true, it allows sending of more detailed metric information for the
    routes using 32-bit wide values using TLV 135 IP reachability and more detailed
    reachability information for IS reachability by using TLV 22. The detailed usage
    is described in RFC3784.
    """

    hostname: str
    """Host name for the router.

    The host name is transmitted in all the packets sent from the router.
    """

    ipv4_te_router_id: str
    """IPv4 Traffic Engineering(TE) router id.

    This address should be configured as an IPv4 Loopback address in
    'ipv4_loopbacks' in the Device.
    """

    learned_lsp_filter: bool
    """
    Configuration for controlling storage of ISIS learned LSPs are received from the
    neighbors.
    """


class DeviceIsisInstance(TypedDict, total=False):
    iid: int
    """
    Instance Identifier (IID) TLV will associate a PDU with an ISIS instance by
    using a unique 16-bit number and including one or more Instance-Specific
    Topology Identifiers (ITIDs).
    """

    itids: Iterable[int]
    """This contains one or more ITIDs that will be advertised in IID TLV."""


class DeviceIsisRouterAuth(TypedDict, total=False):
    area_auth: IsisAuthenticationBaseParam
    """
    The Area authentication method used for the emulated ISIS router. This is used
    for L1 LSPs.
    """

    domain_auth: IsisAuthenticationBaseParam
    """
    The Domain authentication method used for the emulated ISIS router. This is used
    for L2 LSPs.
    """

    ignore_receive_md5: bool
    """Do not verify MD5 checksum in received LSPs."""


class DeviceIsisSegmentRoutingRouterCapabilitySrCapabilityFlags(TypedDict, total=False):
    ipv4_mpls: bool
    """I-Flag for the MPLS IPv4 Flag.

    If set, then the router is capable of processing SR-MPLS-encapsulated IPv4
    packets on all interfaces.
    """

    ipv6_mpls: bool
    """V-Flag for the MPLS IPv6 Flag.

    If set, then the router is capable of processing SR-MPLS-encapsulated IPv6
    packets on all interfaces.
    """


class DeviceIsisSegmentRoutingRouterCapabilitySrCapabilitySrgbRange(TypedDict, total=False):
    range: int
    """This represents the number of SID in a SRGB range."""

    starting_sid: int
    """
    The SID/Label sub-TLV contains the first value of the SRGB while the range
    contains the number of SRGB elements.
    """


class DeviceIsisSegmentRoutingRouterCapabilitySrCapability(TypedDict, total=False):
    flags: DeviceIsisSegmentRoutingRouterCapabilitySrCapabilityFlags
    """1 octet of flags."""

    srgb_ranges: Iterable[DeviceIsisSegmentRoutingRouterCapabilitySrCapabilitySrgbRange]
    """
    This contains the list of SRGB. If no SRGB range is configured, implementation
    should send one SRGB range with default values.
    """


class DeviceIsisSegmentRoutingRouterCapabilitySrlbRange(TypedDict, total=False):
    range: int
    """This represents the number of SIDs in a SRLB range."""

    starting_sid: int
    """
    The SID/Label sub-TLV contains the first value of the SRLB while the range
    contains the number of SRLB elements.
    """


class DeviceIsisSegmentRoutingRouterCapability(TypedDict, total=False):
    algorithms: Iterable[int]
    """
    This contains one or more Segment Routing Algorithm that a router may use
    various algorithms when calculating reachability to other nodes or to prefixes
    attached to these nodes. The Isis may use various algorithms when calculating
    reachability to other nodes or to prefixes attached to these nodes. Examples of
    these algorithms are metric-based SPF, various sorts of Constrained SPF, etc.

    - 0: SPF algorithm based on link metric.
    - 1: Strict SPF algorithm based on link metric. Reference:
      https://datatracker.ietf.org/doc/html/rfc8665#name-igp-algorithm-types-registr.
      When the originating router does not advertise the SR-Algorithm sub-TLV, it
      implies that algorithm 0 is the only algorithm supported by the routers. When
      the originating router does advertise the SR-Algorithm sub-TLV, then algorithm
      0 MUST be present while non-zero algorithms MAY be present.
    """

    choice: Literal["ipv4_te_router_id", "interface_ip", "custom_router_cap_id"]
    """
    The Router Capability ID SHOULD be identical to the value advertised in the
    Traffic Engineering Router ID TLV [RFC5305]. If no Traffic Engineering Router ID
    is assigned, the Router ID SHOULD be identical to an IP Interface Address
    [RFC1195] advertised by the originating IS. If the originating node does not
    support IPv4, then the reserved value 0.0.0.0 MUST be used in the Router ID
    field, and the IPv6 TE Router ID sub-TLV [RFC5316] MUST be present in the TLV.

    - ipv4_te_router_id: IPv4 Traffic Engineering(TE) router id (defined in
      isis.basic.ipv4_te_router_id) to be used as Router Capability ID.
    - interface_ip: When this is chosen the first IPv4 address of the first eth
      interface associated with this isis router instance should be assigned as the
      Router Capability ID.
    - custom_router_cap_id: This option should be chosen when Router Capability ID
      needs to be configured different from above two options.
    """

    custom_router_cap_id: str
    """Router Capability ID in IPv4 address format."""

    d_bit: Literal["down", "not_down"]
    """
    D bit (0x02): When the IS-IS Router CAPABILITY TLV is leaked from Level 2 (L2)
    to Level 1 (L1), the D bit MUST be set. Otherwise, this bit MUST be clear. IS-IS
    Router CAPABILITY TLVs with the D bit set MUST NOT be leaked from Level 1 to
    Level 2. This is to prevent TLV looping.
    """

    s_bit: Literal["flood", "not_flood"]
    """
    S bit (0x01): If the S bit is set(1), the IS-IS Router CAPABILITY TLV MUST be
    flooded across the entire routing domain. If the S bit is not set(0), the TLV
    MUST NOT be leaked between levels. This bit MUST NOT be altered during the TLV
    leaking.
    """

    sr_capability: DeviceIsisSegmentRoutingRouterCapabilitySrCapability
    """SR-Capabilities."""

    srlb_ranges: Iterable[DeviceIsisSegmentRoutingRouterCapabilitySrlbRange]
    """This contains the list of SR Local Block (SRLB)"""


class DeviceIsisSegmentRouting(TypedDict, total=False):
    router_capability: DeviceIsisSegmentRoutingRouterCapability
    """
    Optional IS-IS TLV named CAPABILITY, formed of multiple sub-TLVs, which allows a
    router to announce its capabilities within an IS-IS level or the entire routing
    domain.
    """


class DeviceIsisV4Route(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    addresses: Iterable[V4RouteAddressParam]
    """A list of group of IPv4 route addresses."""

    link_metric: int
    """The user-defined metric associated with this route range."""

    n_flag: bool
    """Node Flag (Bit 2)"""

    origin_type: Literal["internal", "external"]
    """The origin of the advertised route-internal or external to the ISIS area.

    Options include the following: Internal-for intra-area routes, through Level 1
    LSPs. External-for inter-area routes redistributed within L1, through Level 1
    LSPs.
    """

    prefix_attr_enabled: bool
    """
    Specifies whether the sub-TLV for IPv4/IPv6 Extended Reachability Attribute
    Flags will be advertised or not.
    """

    prefix_sids: Iterable[IsisSrPrefixSidParam]
    """A list of SID paramters for a group of IPv4 route addresses."""

    r_flag: bool
    """Re-advertisement Flag (Bit 1)"""

    redistribution_type: Literal["up", "down"]
    """
    Defines the Up/Down (Redistribution) bit defined for TLVs 128 and 130 by
    RFC 2966. It is used for domain-wide advertisement of prefix information.

    Up (0)-used when a prefix is initially advertised within the ISIS L3 hierarchy,
    and for all other prefixes in L1 and L2 LSPs. (default) Down (1)-used when an
    L1/L2 router advertises L2 prefixes in L1 LSPs.

    The prefixes are being advertised from a higher level (L2) down to a lower level
    (L1).
    """

    x_flag: bool
    """External Prefix Flag (Bit 0)"""


class DeviceIsisV6Route(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    addresses: Iterable[V6RouteAddressParam]
    """A list of group of IPv6 route addresses."""

    link_metric: int
    """The user-defined metric associated with this route range."""

    n_flag: bool
    """Node Flag (Bit 2)"""

    origin_type: Literal["internal", "external"]
    """The origin of the advertised route-internal or external to the ISIS area.

    Options include the following: Internal-for intra-area routes, through Level 1
    LSPs. External-for inter-area routes redistributed within L1, through Level 1
    LSPs.
    """

    prefix_attr_enabled: bool
    """
    Specifies whether the sub-TLV for IPv4/IPv6 Extended Reachability Attribute
    Flags will be advertised or not.
    """

    prefix_sids: Iterable[IsisSrPrefixSidParam]
    """A list of SID parameters for a group of IPv6 route addresses."""

    r_flag: bool
    """Re-advertisement Flag (Bit 1)"""

    redistribution_type: Literal["up", "down"]
    """
    Defines the Up/Down (Redistribution) bit defined for TLVs 128 and 130 by
    RFC 2966. It is used for domain-wide advertisement of prefix information.

    Up (0)-used when a prefix is initially advertised within the ISIS L3 hierarchy,
    and for all other prefixes in L1 and L2 LSPs. (default) Down (1)-used when an
    L1/L2 router advertises L2 prefixes in L1 LSPs.

    The prefixes are being advertised from a higher level (L2) down to a lower level
    (L1).
    """

    x_flag: bool
    """External Prefix Flag (Bit 0)"""


class DeviceIsis(TypedDict, total=False):
    interfaces: Required[Iterable[DeviceIsisInterface]]
    """List of ISIS interfaces for this router."""

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    system_id: Required[str]
    """The System ID for this emulated ISIS router, e.g. "640100010000"."""

    advanced: DeviceIsisAdvanced
    """Contains advance properties of an ISIS Router.."""

    basic: DeviceIsisBasic
    """Contains basic properties of an ISIS Router."""

    instance: DeviceIsisInstance
    """This contains the properties of a Multi-Instance-capable routers or MI-RTR.

    Each router can emulate one ISIS instance at a time.
    """

    router_auth: DeviceIsisRouterAuth
    """ISIS Router authentication properties."""

    segment_routing: DeviceIsisSegmentRouting
    """Optional Segment Routing (SR)."""

    v4_routes: Iterable[DeviceIsisV4Route]
    """Emulated ISIS IPv4 routes."""

    v6_routes: Iterable[DeviceIsisV6Route]
    """Emulated ISIS IPv6 routes."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySourcePskEndOffsetTime(
    TypedDict, total=False
):
    hh: int
    """Hours in HH format."""

    mm: int
    """Minutes in MM format."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySourcePskStartOffsetTime(
    TypedDict, total=False
):
    hh: int
    """Hours in HH format."""

    mm: int
    """Minutes in MM format."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySourcePsk(TypedDict, total=False):
    cak_name: str
    """Connectivity association key(CAK) name."""

    cak_value: str
    """Connectivity association key(CAK) value.

    It can be 128 bits or 256 bits long depending on the chosen MKA key derivation
    function.
    """

    end_offset_time: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySourcePskEndOffsetTime

    start_offset_time: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySourcePskStartOffsetTime


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySource(TypedDict, total=False):
    choice: Literal["psk", "msk"]
    """Key source. Choose one from PSK or MSK."""

    psks: Iterable[DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySourcePsk]
    """PSK chain."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicPskChainStartTimeUtc(
    TypedDict, total=False
):
    day: int
    """Day of the month in DD format."""

    hour: int
    """Hour of the day in HH format."""

    minute: int
    """Minute of the hour in MM format."""

    month: int
    """Month of the year in MM format."""

    second: int
    """Second of the minute in SS format."""

    year: int
    """Year from the start of common era(CE) in YYYY format."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicPskChainStartTime(TypedDict, total=False):
    choice: Literal["utc"]
    """Timezone choice. Currently only Coordinated Universal Time(UTC) is supported."""

    utc: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicPskChainStartTimeUtc
    """Coordinated Universal Time(UTC) time."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicRekeyModeTimerBased(TypedDict, total=False):
    choice: Literal["continuous", "fixed_count"]
    """Periodic Rekey count."""

    fixed_count: int
    """Fixed rekey attempts."""

    interval: int
    """Periodic rekey interval (sec)."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicRekeyMode(TypedDict, total=False):
    choice: Literal["dont_rekey", "timer_based", "pn_based"]
    """Mode choices."""

    timer_based: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicRekeyModeTimerBased
    """Container for timer based periodic rekey properties."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicSupportedCipherSuites(
    TypedDict, total=False
):
    gcm_aes_128: bool
    """GCM-AES-128."""

    gcm_aes_256: bool
    """GCM-AES-256."""

    gcm_aes_xpn_128: bool
    """GCM-AES-XPN-128."""

    gcm_aes_xpn_256: bool
    """GCM-AES-XPN-256."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasic(TypedDict, total=False):
    key_source: Required[DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicKeySource]
    """Key source."""

    actor_priority: str
    """Actor priority."""

    delay_protect: bool
    """Delay Protect or not.

    When delay protect is enabled, it guards against delaying the delivery of MACsec
    encrypted frames by an attacker to the recipient.
    """

    eapol_ethernet_type: str
    """EAPOL Ethernet type."""

    key_derivation_function: Literal["aes_cmac_128", "aes_cmac_256"]
    """Key Derivation Function."""

    macsec_capability: Literal[
        "macsec_not_implemented",
        "macsec_integrity_without_confidentiality",
        "macsec_integrity_with_no_confidentiality_offset",
        "macsec_integrity_with_confidentiality_offset",
    ]
    """MACSec Capability."""

    macsec_desired: bool
    """Determines whether MACsec is desired or not.

    It is advertised in periodic Hellos.
    """

    mka_hello_time: int
    """MKA Hello Time (msec)."""

    mka_life_time: int
    """MKA Life Time (sec)."""

    mka_version: int
    """MKA Version."""

    psk_chain_start_time: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicPskChainStartTime
    """Pre-shared key(PSK) chain start time in UTC time format DD-MM-YYYY HH:MM:SS.

    If this time is set, the key start time will be relative to this value.
    Otherwise if this value is not set, key start time will be relative to test
    start time.
    """

    rekey_mode: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicRekeyMode
    """Rekey Mode."""

    send_icv_indicatior_in_mkpdu: bool
    """Send ICV Indicator in MKPDU."""

    supported_cipher_suites: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasicSupportedCipherSuites
    """Supported Cipher Suites."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaTxSecureChannel(TypedDict, total=False):
    name: Required[str]
    """Tx SC name."""

    system_id: Required[str]
    """System ID."""

    port_id: int
    """Port ID."""

    starting_message_number: int
    """Starting Message Number."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaTx(TypedDict, total=False):
    secure_channels: Required[
        Iterable[DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaTxSecureChannel]
    ]
    """Tx secure channels."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaKeyServer(TypedDict, total=False):
    cipher_suite: Literal["gcm_aes_128", "gcm_aes_256", "gcm_aes_xpn_128", "gcm_aes_xpn_256"]
    """The cipher suite.

    Choose one from GCM-AES-128 GCM-AES-256 GCM-AES-XPN-128 GCM-AES-XPN-256
    """

    confidentialty_offset: Literal[
        "no_confidentiality",
        "no_confidentiality_offset",
        "confidentiality_offset_30_octets",
        "confidentiality_offset_50_octets",
    ]
    """Confidentiality Offset."""

    rekey_threshold_pn: str
    """Determines the PN rekey threshold."""

    rekey_threshold_xpn: str
    """Determines the XPN rekey threshold."""

    starting_distributed_an: int
    """Starting Distributed AN."""

    starting_key_number: int
    """Starting Key Number."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMka(TypedDict, total=False):
    basic: Required[DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaBasic]
    """This contains the basic properties of KaY."""

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    tx: Required[DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaTx]
    """Tx Properties."""

    key_server: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMkaKeyServer
    """Key server attributes."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyRxSecureChannel(TypedDict, total=False):
    dut_msb_xpn: int
    """DUT MSB of XPN.

    The 32 most significant bits of the XPN that DUT will be using to construct the
    64 bits XPN value when test starts.
    """

    dut_sci_port_id: int
    """Port ID in DUT SCI."""

    dut_sci_system_id: str
    """System ID in DUT SCI."""

    saks: Iterable[SecureEntityStaticKeySakParam]
    """Rx SAK pool."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyRx(TypedDict, total=False):
    secure_channels: Iterable[DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyRxSecureChannel]
    """Rx secure channels."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTxRekeyModeTimerBased(
    TypedDict, total=False
):
    choice: Literal["continuous", "fixed_count"]
    """Periodic rekey attempt choices."""

    fixed_count: int
    """Fixed rekey attempts."""

    interval: int
    """Periodic rekey interval (sec)."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTxRekeyMode(TypedDict, total=False):
    choice: Literal["dont_rekey", "timer_based", "pn_based"]
    """Rekey mode choices."""

    timer_based: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTxRekeyModeTimerBased
    """Container for timer based periodic rekey properties."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTxSecureChannel(TypedDict, total=False):
    port_id: int
    """Port ID."""

    saks: Iterable[SecureEntityStaticKeySakParam]
    """Tx SAK pool."""

    system_id: str
    """System ID."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTx(TypedDict, total=False):
    rekey_mode: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTxRekeyMode
    """Rekey mode."""

    secure_channels: Iterable[DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTxSecureChannel]
    """Tx secure channels."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKey(TypedDict, total=False):
    cipher_suite: Literal["gcm_aes_128", "gcm_aes_256", "gcm_aes_xpn_128", "gcm_aes_xpn_256"]
    """The cipher suite.

    Choose one from GCM-AES-128 GCM-AES-128 GCM-AES-256 GCM-AES-XPN-128
    GCM-AES-XPN-256
    """

    confidentiality: bool
    """Encrypt or not."""

    confidentiality_offset: Literal["zero", "thirty", "fifty"]
    """Confidentiality offset."""

    rx: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyRx
    """Rx properties of SecY."""

    tx: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKeyTx
    """Tx properties of SecY."""


class DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocol(TypedDict, total=False):
    choice: Literal["mka", "static_key"]
    """Key generation protocol choices.

    Choose "mka" for dynamic key distribution using MACsec key agreement(MKA)
    protocol. Choose "static_key" for static configuration of secure association
    key(SAK).
    """

    mka: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolMka
    """This contains the properties of Key Agreement Entity (KaY) in MKA supplicant."""

    static_key: DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocolStaticKey
    """Static key properties properties of SecY. Static key is used in absence MKA."""


class DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannelTxPnFixed(
    TypedDict, total=False
):
    pn: int
    """Fixed Tx packet number(PN). 4 bytes PN with which all packets will be sent out."""

    xpn: str
    """Fixed Tx extended packet number(XPN).

    8 bytes XPN with which all packets will be sent out.
    """


class DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannelTxPnIncrementing(
    TypedDict, total=False
):
    count: int
    """Count of packet numbers in series."""

    starting_pn: int
    """The starting packet number(PN)."""

    starting_xpn: str
    """The starting extended packet number(XPN)."""


class DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannelTxPn(
    TypedDict, total=False
):
    choice: Literal["fixed_pn", "incrementing_pn"]
    """Types of Tx packet number(PN) series.

    Supported choices: 1) fixed PN - MACsec packets will be sent out with the
    configured fixed PN or lower half of configured fixed XPN. 2) incrementing PN -
    MACsec packets will be sent out by single device with an incrementing PN or XPN.
    """

    fixed: DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannelTxPnFixed
    """Fixed packet number(PN) configuration."""

    incrementing: DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannelTxPnIncrementing
    """Incrementing packet number(PN) configuration."""


class DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannel(
    TypedDict, total=False
):
    tx_pn: DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannelTxPn
    """Tx packet number(PN) configuration."""


class DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlyTrafficOptions(
    TypedDict, total=False
):
    send_gratuitous_arp: bool
    """Send gratuitous ARP or not."""


class DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnly(TypedDict, total=False):
    secure_channels: Iterable[
        DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlySecureChannel
    ]

    traffic_options: (
        DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnlyTrafficOptions
    )
    """Encrypt only traffic options."""


class DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngine(TypedDict, total=False):
    choice: Literal["encrypt_only"]
    """Engine type based on encryption and/ or decryption capability.

    Supported types: encrypt_only - engine can only encrypt transmitted packets but
    it cannot decrypt packets upon arrival. As the packets cannot be decrypted on
    arrival, such packets cannot be delivered to the receiving device. Hence only
    stateless traffic can be sent.
    """

    encrypt_only: DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngineEncryptOnly
    """The container for encrypt only engine configuration."""


class DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationRx(TypedDict, total=False):
    replay_protection: bool
    """Enable replay protection on not."""

    replay_window: int
    """Replay window size."""


class DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationTx(TypedDict, total=False):
    end_station: bool
    """End station on not."""

    include_sci: bool
    """Include SCI on not."""


class DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulation(TypedDict, total=False):
    crypto_engine: Required[DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationCryptoEngine]
    """Crypto engine properties of SecY."""

    rx: DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationRx
    """Rx properties of SecY."""

    tx: DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulationTx
    """Tx properties of SecY."""


class DeviceMacsecEthernetInterfaceSecureEntityDataPlane(TypedDict, total=False):
    choice: Literal["encapsulation", "no_encapsulation"]
    """Choose "encapsulation" so that data packets are sent with MACsec encapsulation.

    Choose "no_encapsulation" so that data packets are sent without MACsec
    encapsulation.
    """

    encapsulation: DeviceMacsecEthernetInterfaceSecureEntityDataPlaneEncapsulation
    """A container of encapsulation properties for a secure entity(SecY)."""


class DeviceMacsecEthernetInterfaceSecureEntity(TypedDict, total=False):
    key_generation_protocol: Required[DeviceMacsecEthernetInterfaceSecureEntityKeyGenerationProtocol]
    """
    This contains the properties of key generation protocol of Secure Entity (SecY).
    """

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    data_plane: DeviceMacsecEthernetInterfaceSecureEntityDataPlane
    """This contains the properties of data plane of Secure Entity (SecY)."""


class DeviceMacsecEthernetInterface(TypedDict, total=False):
    eth_name: Required[str]
    """The unique name of the Ethernet interface on which MACsec is enabled.

    x-constraint:

    - /components/schemas/Device.Ethernet/properties/name
    """

    secure_entity: Required[DeviceMacsecEthernetInterfaceSecureEntity]
    """This contains the properties of Secure Entity (SecY)."""


class DeviceMacsec(TypedDict, total=False):
    ethernet_interfaces: Required[Iterable[DeviceMacsecEthernetInterface]]
    """Ethernet Interfaces"""


class DeviceOspfv2InterfaceAdvanced(TypedDict, total=False):
    dead_interval: int
    """
    The time interval in seconds before the router's neighbors will declare it down,
    when they stop hearing the router's Hello Packets. Advertised in Hello packets
    sent out this interface.
    """

    hello_interval: int
    """
    The time interval, in seconds, between the Hello packets that the router sends
    on the interface. Advertised in Hello packets sent out this interface.
    """

    priority: int
    """The Priority for (Backup) Designated Router election.

    This value is used in Hello packets for the Designated Router (DR) election
    process. The default is 0, which indicates that the router will not participate
    in the DR election process.
    """

    routing_metric: int
    """Routing metric associated with the interface.."""

    validate_received_mtu: bool
    """
    If this is set to true, then the MTU received from the neighbor during Database
    (DB) Exchange will be validated, otherwise it will be ignored.
    """


class DeviceOspfv2InterfaceArea(TypedDict, total=False):
    id: int
    """The Area ID."""

    choice: Literal["id", "ip"]
    """The OSPF Area ID identifies the routing area to which the host belongs.

    Area ID type can be following format.

    - id: A 32-bit number identifying the area.
    - ip: The Area ID in IPv4 address format.
    """

    ip: str
    """The Area ID in IPv4 address format."""


class DeviceOspfv2InterfaceAuthenticationMd5(TypedDict, total=False):
    key: str
    """
    An alphanumeric secret used to generate the 16 byte MD5 hash value added to the
    OSPFv2 PDU in the Authentication TLV.
    """

    key_id: int
    """The unique MD5 Key Identifier per-interface."""


class DeviceOspfv2InterfaceAuthentication(TypedDict, total=False):
    choice: Literal["md5s", "clear_text"]
    """The authentication method.

    - md5 - Cryptographic authentication.
    - clear_text - Simple password authentication. A 64-bit field is configured on a
      per-network basis. All packets sent on a particular network must have this
      configured value (in clear text) in their OSPF header 64-bit authentication
      field.
    """

    clear_text: str
    """The 8 Byte authentication field in the OSPF packet."""

    md5s: Iterable[DeviceOspfv2InterfaceAuthenticationMd5]
    """List of MD5 Key IDs and MD5 Keys."""


class DeviceOspfv2InterfaceLinkProtection(TypedDict, total=False):
    dedicated_1_plus_1: bool
    """Enabling this signifies that a dedicated disjoint link is protecting this link.

    However, the protecting link is not advertised in the link state database and is
    therefore not available for the routing of LSAs.
    """

    dedicated_1_to_1: bool
    """
    Enabling this signifies that there is one dedicated disjoint link of type Extra
    Traffic that is protecting this link.
    """

    enhanced: bool
    """
    Enabling this signifies that a protection scheme that is more reliable than
    Dedicated 1+1.
    """

    extra_traffic: bool
    """Enable this to protect other link or links.

    LSAs on a link of this type are lost if any of the links fail.
    """

    reserved_40: bool
    """This is a Protection Scheme with value 0x40."""

    reserved_80: bool
    """This is a Protection Scheme with value 0x80."""

    shared: bool
    """
    Enable this to share the Extra Traffic links between one or more links of type
    Shared.There are one or more disjoint links of type Extra Traffic that are
    protecting this link.
    """

    unprotected: bool
    """Enabling this signifies that there is no other link protecting this link.

    LSAs on a link of this type are lost if the link fails.
    """


class DeviceOspfv2InterfaceNetworkTypePointToMultipoint(TypedDict, total=False):
    neighbor_ip: str


class DeviceOspfv2InterfaceNetworkType(TypedDict, total=False):
    choice: Literal["broadcast", "point_to_point", "point_to_multipoint"]

    point_to_multipoint: Iterable[DeviceOspfv2InterfaceNetworkTypePointToMultipoint]
    """List of Neigbhors."""


class DeviceOspfv2Interface(TypedDict, total=False):
    ipv4_name: Required[str]
    """The globally unique name of the IPv4 interface connected to the DUT.

    x-constraint:

    - /components/schemas/Device.Ipv4/properties/name
    """

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    advanced: DeviceOspfv2InterfaceAdvanced
    """Optional container for advanced interface properties."""

    area: DeviceOspfv2InterfaceArea
    """
    The Area ID of the area to which the attached network belongs. All routing
    protocol packets originating from the interface are labelled with this Area ID.
    """

    authentication: DeviceOspfv2InterfaceAuthentication
    """
    OSPFv2 authentication properties. If the authentication is not configured, none
    OSPF packet exchange is authenticated.
    """

    link_protection: DeviceOspfv2InterfaceLinkProtection
    """Link protection on the OSPFv2 link between two interfaces."""

    network_type: DeviceOspfv2InterfaceNetworkType
    """The OSPF network link type."""

    srlg_values: Iterable[int]
    """
    A Shared Risk Link Group (SRLG) is represented by a 32-bit number unique within
    an IGP (OSPFv2 and IS-IS) domain. An SRLG is a set of links sharing a common
    resource, which affects all links in the set if the common resource fails. Links
    share the same risk of failure and are therefore considered to belong to the
    same SRLG.
    """

    traffic_engineering: Iterable[LinkStateTeParam]
    """Contains a list of Traffic Engineering attributes."""


class DeviceOspfv2Capabilities(TypedDict, total=False):
    dc_bit: bool
    """
    Demand Circuit: 5th-bit: describes the router's handling of demand circuits, as
    specified in [Ref21], rfc2328.
    """

    e_bit: bool
    """External Capability: 1st-bit: describes the way AS-external-LSAs are flooded."""

    ea_bit: bool
    """
    External Attribute: 4th-bit: describes the router's willingness to receive and
    forward External-Attributes-LSAs, as specified in [Ref20], rfc2328.
    """

    lsa_b_bit: bool
    """Set to indicate that the router acts as an Area Border Router."""

    lsa_e_bit: bool
    """Set to indicate that the router acts as an AS Boundary Router."""

    mc_bit: bool
    """
    Multicast Capability: 2nd-bit: describes whether IP multicast datagrams are
    forwarded according to the specifications in [Ref18], rfc2328.
    """

    np_bit: bool
    """
    NSSA Capability: 3rd-bit: describes the handling of Type-7 LSAs, as specified in
    [Ref19], rfc2328.
    """

    o_bit: bool
    """
    Opaque LSA's Forwarded: 6th-bit: describes the router's willingness to receive
    and forward Opaque-LSAs, rfc2370.
    """

    t_bit: bool
    """Type of Service: 0th-bit: describes OSPFv2's TOS capability."""

    unused_bit: bool
    """Opaque LSA's Forwarded: 7th-bit: unused bit."""


class DeviceOspfv2GracefulRestart(TypedDict, total=False):
    helper_mode: bool
    """Support of Graceful Restart in Helper Mode."""


class DeviceOspfv2RouterID(TypedDict, total=False):
    choice: Literal["interface_ip", "custom"]
    """IP address of Router ID for this emulated OSPFv2 router.

    - interface_ip: When IPv4 interface address to be assigned as Router ID.
    - custom: When, Router ID needs to be configured different from Interface IPv4
      address.
    """

    custom: str
    """Router ID in IPv4 address format."""


class DeviceOspfv2V4RouteRouteOriginExternalType1(TypedDict, total=False):
    flags: Ospfv2V4RrExtdPrefixFlagsParam
    """One-octet field contains flags applicable to the prefix."""


class DeviceOspfv2V4RouteRouteOriginExternalType2(TypedDict, total=False):
    flags: Ospfv2V4RrExtdPrefixFlagsParam
    """One-octet field contains flags applicable to the prefix."""


class DeviceOspfv2V4RouteRouteOriginInterArea(TypedDict, total=False):
    flags: Ospfv2V4RrExtdPrefixFlagsParam
    """One-octet field contains flags applicable to the prefix."""


class DeviceOspfv2V4RouteRouteOriginIntraArea(TypedDict, total=False):
    flags: Ospfv2V4RrExtdPrefixFlagsParam
    """One-octet field contains flags applicable to the prefix."""


class DeviceOspfv2V4RouteRouteOriginNssaExternal(TypedDict, total=False):
    flags: Ospfv2V4RrExtdPrefixFlagsParam
    """One-octet field contains flags applicable to the prefix."""

    propagation: bool
    """The flag is set True if LSA will be propagated between Areas."""


class DeviceOspfv2V4RouteRouteOrigin(TypedDict, total=False):
    choice: Literal["intra_area", "inter_area", "external_type_1", "external_type_2", "nssa_external"]
    """Supported types are: - intra_area: for Intra-Area.

    - inter_area: for Inter Area. - external_type_1: for Autonomous System (AS)
      External with internal AS metric. - external_type_2: for Autonomous System
      (AS) External with internal and external AS metric. - nssa_external: for 7
      Not-So-Stubby Area (NSSA) External.
    """

    external_type_1: DeviceOspfv2V4RouteRouteOriginExternalType1
    """Configuration for the External Type 1."""

    external_type_2: DeviceOspfv2V4RouteRouteOriginExternalType2
    """Configuration for the External Type 2."""

    inter_area: DeviceOspfv2V4RouteRouteOriginInterArea
    """Configuration for the Intra-Area."""

    intra_area: DeviceOspfv2V4RouteRouteOriginIntraArea
    """Configuration for the Intra-Area."""

    nssa_external: DeviceOspfv2V4RouteRouteOriginNssaExternal
    """Configuration for the External Type 2."""


class DeviceOspfv2V4Route(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    addresses: Iterable[V4RouteAddressParam]
    """A list of group of IPv4 route addresses."""

    metric: int
    """The user-defined metric associated with this route range."""

    route_origin: DeviceOspfv2V4RouteRouteOrigin
    """The type of the OSPFv2 routes."""


class DeviceOspfv2(TypedDict, total=False):
    interfaces: Required[Iterable[DeviceOspfv2Interface]]
    """List of OSPFv2 interfaces for this router."""

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    capabilities: DeviceOspfv2Capabilities
    """
    A router indicates the optional capabilities that it supports in its OSPF Hello
    packets, Database Description packets and in its LSAs.
    """

    graceful_restart: DeviceOspfv2GracefulRestart
    """Container of properties of OSPFv2 Graceful Retstart."""

    inter_burst_lsu_interval: int
    """The gap in miliseconds between each Flood Link State Update Burst"""

    lsa_refresh_time: int
    """The time in seconds required for LSA refresh."""

    lsa_retransmit_time: int
    """The time in seconds for LSA retransmission."""

    max_flood_lsu_per_burst: int
    """The maximum number of Flood LSUpdates for each burst"""

    router_id: DeviceOspfv2RouterID
    """OSPFv2 Router Id."""

    store_lsa: bool
    """
    Configuration for controlling storage of OSPFv2 learned LSAs received from the
    neighbors.
    """

    v4_routes: Iterable[DeviceOspfv2V4Route]
    """Emulated OSPFv4 IPv4 routes."""


class DeviceOspfv3InstanceInterfaceAdvanced(TypedDict, total=False):
    dead_interval: int
    """
    The time interval in seconds before the router's neighbors will declare it down,
    when they stop hearing the router's Hello Packets. Advertised in Hello packets
    sent out this interface.
    """

    hello_interval: int
    """
    The time interval, in seconds, between the Hello packets that the router sends
    on the interface. Advertised in Hello packets sent out this interface.
    """

    link_metric: int
    """The cost of transmitting data on this link."""

    validate_received_mtu: bool
    """
    If this is set to true, then the MTU received from the neighbor during Database
    (DB) Exchange will be validated, otherwise it will be ignored.
    """


class DeviceOspfv3InstanceInterfaceArea(TypedDict, total=False):
    id: int
    """The Area ID."""

    choice: Literal["id", "ip"]
    """The OSPFv3 Area ID identifies the routing area to which the host belongs.

    Area ID type can be following format.

    - id: A 32-bit number identifying the area.
    - ip: The Area ID in IPv4 address format.
    """

    ip: str
    """The Area ID in IPv4 address format."""


class DeviceOspfv3InstanceInterfaceNetworkTypeBroadcast(TypedDict, total=False):
    priority: int
    """The Priority for (Backup) Designated Router election.

    This value is used in Hello packets for the Designated Router (DR) election
    process. The default is 0, which indicates that the router will not participate
    in the DR election process.
    """


class DeviceOspfv3InstanceInterfaceNetworkType(TypedDict, total=False):
    broadcast: DeviceOspfv3InstanceInterfaceNetworkTypeBroadcast
    """Capabilities associated with network type broadcast."""

    choice: Literal["broadcast", "point_to_point"]


class DeviceOspfv3InstanceInterfaceOptions(TypedDict, total=False):
    dc_bit: bool
    """
    Demand Circuit: This bit describes the router's handling of demand circuits, as
    specified in [Ref10], rfc2740.
    """

    e_bit: bool
    """
    External Capability: This bit describes the router's willingness to receive and
    forward External-Attributes-LSAs, as specified in [Ref1], rfc2740.
    """

    n_bit: bool
    """
    NSSA Capability: This bit describes the handling of Type-7 LSAs, as specified in
    [Ref8], rfc2740.
    """

    r_bit: bool
    """Router: This bit indicates if the originator is an active router."""

    v6_bit: bool
    """V6: If set, the router/link should be included in IPv6 routing calculations."""


class DeviceOspfv3InstanceInterface(TypedDict, total=False):
    ipv6_name: Required[str]
    """The globally unique name of the IPv6 interface connected to the DUT.

    x-constraint:

    - /components/schemas/Device.Ipv6/properties/name
    """

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    advanced: DeviceOspfv3InstanceInterfaceAdvanced
    """Optional container for advanced interface properties."""

    area: DeviceOspfv3InstanceInterfaceArea
    """
    The Area ID of the area to which the attached network belongs. All routing
    protocol packets originating from the interface are labelled with this Area ID.
    """

    instance_id: int
    """
    Enables multiple instances of OSPF to be run over a single link. Each protocol
    instance should be assigned a separate Instance ID; the Instance ID has
    link-local significance only.
    """

    network_type: DeviceOspfv3InstanceInterfaceNetworkType
    """The OSPF network link type."""

    options: DeviceOspfv3InstanceInterfaceOptions
    """Container for OSPFv3 optional interface properties."""


class DeviceOspfv3InstanceCapabilities(TypedDict, total=False):
    lsa_b_bit: bool
    """Set to indicate that the router acts as an Area Border Router."""

    lsa_e_bit: bool
    """Set to indicate that the router acts as an AS Boundary Router."""


class DeviceOspfv3InstanceGracefulRestart(TypedDict, total=False):
    helper_mode: bool
    """Support of Graceful Restart in Helper Mode."""


class DeviceOspfv3InstanceV6RouteRouteOriginNssaExternalCapabilitiesForwardingAddress(TypedDict, total=False):
    choice: Literal["interface_ip", "custom"]
    """IPv6 forwarding address of Type 7 LSA Not-So-Stubby Area (NSSA) External.

    - interface_ip: if set, forwarding address is set with Interface IPv6 address.
    - custom: if set, forwarding address is set with a custom IPv6 address.
    """

    custom: str
    """Forwarding address in IPv6 format."""


class DeviceOspfv3InstanceV6RouteRouteOriginNssaExternalCapabilities(TypedDict, total=False):
    forwarding_address: DeviceOspfv3InstanceV6RouteRouteOriginNssaExternalCapabilitiesForwardingAddress
    """Configuration for forwarding address of NSSA External route origin."""

    propagation: bool
    """If set, LSAs will be propagated between Areas."""


class DeviceOspfv3InstanceV6RouteRouteOriginNssaExternal(TypedDict, total=False):
    capabilities: DeviceOspfv3InstanceV6RouteRouteOriginNssaExternalCapabilities
    """Configuration for capabilities associated with route origin."""


class DeviceOspfv3InstanceV6RouteRouteOrigin(TypedDict, total=False):
    choice: Literal["intra_area", "inter_area", "external_type_1", "external_type_2", "nssa_external"]
    """Supported types are: - intra_area: for Intra-Area.

    - inter_area: for Inter Area. - external_type_1: for Autonomous System (AS)
      External with internal AS metric. - external_type_2: for Autonomous System
      (AS) External with internal and external AS metric. - nssa_external: for type
      7 Not-So-Stubby Area (NSSA) External.
    """

    nssa_external: DeviceOspfv3InstanceV6RouteRouteOriginNssaExternal
    """Configuration for the type 7 Not-So-Stubby Area (NSSA) External."""


class DeviceOspfv3InstanceV6Route(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    addresses: Iterable[V6RouteAddressParam]
    """A list of group of IPv6 route addresses."""

    metric: int
    """The user-defined metric associated with this route range."""

    route_origin: DeviceOspfv3InstanceV6RouteRouteOrigin
    """The type of the OSPFv3 routes."""


class DeviceOspfv3Instance(TypedDict, total=False):
    interfaces: Required[Iterable[DeviceOspfv3InstanceInterface]]
    """List of OSPFv3 interfaces for this router."""

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    capabilities: DeviceOspfv3InstanceCapabilities
    """Optional container for OSPFv3 router capabilities."""

    graceful_restart: DeviceOspfv3InstanceGracefulRestart
    """Container of properties of OSPFv3 Graceful Retstart."""

    inter_burst_lsu_interval: int
    """The gap in miliseconds between each Flood Link State Update burst."""

    lsa_refresh_time: int
    """The time in seconds required for LSA refresh."""

    lsa_retransmit_time: int
    """The time in seconds for LSA retransmission."""

    store_lsa: bool
    """
    Configuration for controlling storage of OSPFv3 learned LSAs received from the
    neighbors.
    """

    v6_routes: Iterable[DeviceOspfv3InstanceV6Route]
    """Emulated OSPFv4 IPv6 routes."""


class DeviceOspfv3RouterID(TypedDict, total=False):
    choice: Literal["auto", "custom"]
    """IP address of Router ID for this emulated OSPFv3 router.

    - auto: When first IPv4 address on the router is attempted to be assigned as
      Router ID. If none are available for use, implementation should return an
      error.
    - custom: When, Router ID needs to be configured different from first IPv4
      address of the router.
    """

    custom: str
    """Router ID in IPv4 address format."""


class DeviceOspfv3(TypedDict, total=False):
    instances: Required[Iterable[DeviceOspfv3Instance]]
    """List of OSPFv3 router instances for this router."""

    router_id: DeviceOspfv3RouterID
    """OSPFv3 Router Id."""


class DeviceRocev2Ipv4InterfacePeer(TypedDict, total=False):
    destination_ip_address: Required[str]
    """Specify the destination ip address."""

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    qps: Iterable[Rocev2QPsParam]
    """
    This allows the user to set multiple QPs and its properties between a pair of
    source and destination RoCEv2 devices.
    """


class DeviceRocev2Ipv4Interface(TypedDict, total=False):
    ipv4_name: Required[str]
    """
    The unique name of the IPv4 interface, used as the source IP for this list of
    RoCEv2 peers.

    x-constraint:

    - /components/schemas/Device.Ipv4/properties/name
    """

    ib_mtu: int
    """
    The InfiniBand protocol defines several fixed sizes for the Maximum Transmission
    Unit (IB MTU): 256, 512, 1024, 2048, or 4096 bytes. RDMA messages will have a
    payload size that corresponds to the configured IB MTU. Additionally, it is
    possible to configure a custom size.
    """

    peers: Iterable[DeviceRocev2Ipv4InterfacePeer]
    """This contains the list of RoCEv2 peers configured on this interface."""


class DeviceRocev2Ipv6InterfacePeer(TypedDict, total=False):
    destination_ip_address: Required[str]
    """Specify the destination ip address."""

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    qps: Iterable[Rocev2QPsParam]
    """
    This allows the user to set multiple QPs and its properties between a pair of
    source and destination RoCEv2 devices.
    """


class DeviceRocev2Ipv6Interface(TypedDict, total=False):
    ipv6_name: Required[str]
    """The unique name of IPv6 used as the source IP for this list of RoCEv2 peers.

    x-constraint:

    - /components/schemas/Device.Ipv6/properties/name
    """

    ib_mtu: int
    """
    The InfiniBand protocol defines several fixed sizes for the Maximum Transmission
    Unit (IB MTU): 256, 512, 1024, 2048, or 4096 bytes. RDMA messages will have a
    payload size that corresponds to the configured IB MTU. Additionally, it is
    possible to configure a custom size.
    """

    peers: Iterable[DeviceRocev2Ipv6InterfacePeer]
    """This contains the list of RoCEv2 IPv6 peers configured on this interface."""


class DeviceRocev2(TypedDict, total=False):
    ipv4_interfaces: Iterable[DeviceRocev2Ipv4Interface]
    """
    This contains an array of references to IPv4 interfaces, each having a list of
    IPv4 peers to various destinations.
    """

    ipv6_interfaces: Iterable[DeviceRocev2Ipv6Interface]
    """
    This contains an array references to IPv6 interfaces, each with a list of IPv6
    peers for various destinations.
    """


class DeviceRsvpIpv4Interface(TypedDict, total=False):
    ipv4_name: Required[str]
    """The globally unique name of the IPv4 interface connected to the DUT.

    This name must match the "name" field of the "ipv4_addresses" on top which this
    RSVP interface is configured.

    x-constraint:

    - /components/schemas/Device.Ipv4/properties/name
    """

    neighbor_ip: Required[str]
    """IPv4 address of the RSVP neighbor on this interface."""

    bundle_threshold: int
    """
    The number of milliseconds to wait after which RSVP will bundle different RSVP
    messages and transmit Bundle messages.
    """

    enable_hello: bool
    """Enables sending of Hello Messages as per RFC3209."""

    enable_refresh_reduction: bool
    """Enables sending of Refresh Reduction as described in RFC2961."""

    hello_interval: int
    """
    If enable_hello is set to 'true', this specifies the minimum hello interval in
    seconds at which successive Hello Messages are sent as per RFC3209. There is no
    specification specified maximum value. For clarity, setting the maximum to 1
    hour.
    """

    label_space_end: int
    """
    The user-defined label space end value.The last label value that can be assigned
    to the LSPs for which this router acts as egress.
    """

    label_space_start: int
    """The user-defined label space start value.

    The LSPs for which this router acts as a egress are assigned labels from this
    label pool.The"label_space_start" and "label_space_end" together defines this
    label-pool.
    """

    send_bundle: bool
    """Enables aggregration of different RSVP messages within a single PDU."""

    summary_refresh_interval: int
    """The number of seconds between transmissions of successive Summary Refreshes.

    There is no specification specified maximum value. For clarity, setting the
    maximum to 1 hour.
    """

    timeout_multiplier: int
    """
    The number of missed hellos after which the node should consider RSVP Neighbor
    to have timed out. There is no specification specified maximum value. Setting
    the maximum allowed value to 10.
    """


class DeviceRsvpLspIpv4InterfaceP2pEgressIpv4Lsps(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    enable_fixed_label: bool
    """
    If enabled, a specific fixed label will be advertised by the egress or tail end
    for all Path messages received by this egress. This can be leveraged to
    advertise Explicit or Implicit null labels.
    """

    fixed_label_value: int
    """The fixed label value as advertised by egress in RESV message.

    Applicable only if 'fixed_label' is set to 'true'. Special values are '0 - IPv4
    Explicit NULL', '2 - IPv6 Explicit NULL' and '3 - Implicit NULL'. Outside of
    this, labels are expected to have a minimum value of 16.
    """

    refresh_interval: int
    """The time in seconds between successive transmissions of RESV Refreshes.

    The actual refresh interval is jittered by upto 50%. There is no specification
    specified maximum value. For clarity, setting the maximum to 1 hour.
    """

    reservation_style: Literal["shared_explicit", "fixed_filter", "auto"]
    """
    It determines how RSVP-TE enabled network devices set up reservations along the
    path between an end-to-end QOS-enabled connection. If 'auto' is enabled, the
    style is chosen based on whether the incoming Path has 'SE Desired' flag set.
    Otherwise, the style is chosen based on the value selected for this attribute.
    """

    timeout_multiplier: int
    """
    The number of missed PATH refreshes after which a recieving node should consider
    the LSP state to have timed out. There is no specification specified maximum
    value. Setting the maximum allowed value to 10.
    """


class DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspEroSubobject(TypedDict, total=False):
    as_number: int
    """
    Autonomous System number to be set in the ERO sub-object that this LSP should
    traverse through. This field is applicable only if the value of 'type' is set to
    'as_number'. Note that as per RFC3209, 4-byte AS encoding is not supported.
    """

    hop_type: Literal["strict", "loose"]
    """The hop type of the ERO sub-object, one of Strict or Loose."""

    ipv4_address: str
    """IPv4 address that this LSP should traverse through.

    This field is applicable only if the value of 'type' is set to 'ipv4'.
    """

    prefix_length: int
    """Prefix length for the IPv4 address in the ERO sub-object.

    This field is applicable only if the value of 'type' is set to 'ipv4'.
    """

    type: Literal["ipv4", "as_number"]
    """The type of the ERO sub-object, one of IPv4 Address or AS Number."""


class DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspEro(TypedDict, total=False):
    prefix_length: int
    """
    If prepend_egress_ip is set to one of 'prepend_loose' or 'prepend_strict', then
    set this value as the prefix length of the ERO sub-object containing egress IP
    address.
    """

    prepend_neighbor_ip: Literal["dont_prepend", "prepend_loose", "prepend_strict"]
    """
    Determines whether the IP address of the RSVP neighbor should be added as an ERO
    sub-object. If it is to be included, it can be included as a Loose hop or as a
    Strict hop.
    """

    subobjects: Iterable[DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspEroSubobject]
    """Array of sub-objects to be included in the ERO.

    These sub-objects contain the intermediate hops to be traversed by the LSP while
    being forwarded towards the egress endpoint. These sub-objects are included
    after the optional sub-object containing IP address of egress endpoint of the
    LSP (when present).
    """


class DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspFastReroute(TypedDict, total=False):
    bandwidth: float
    """
    Specifies the value of the Bandwidth field as a 32-bit IEEE floating point
    integer, in bytes per second, as desired for the LSP.
    """

    exclude_any: str
    """
    A 32-bit vector representing a set of attribute filters associated with a tunnel
    any of which renders a link unacceptable. A null set (all bits set to zero)
    doesn't render the link unacceptable. The most significant byte in the
    hex-string is the farthest to the left in the byte sequence. Leading zero bytes
    in the configured value may be omitted for brevity.
    """

    facility_backup_desired: bool
    """Requests protection via the facility backup method."""

    holding_priority: int
    """Specifies the value of the Holding Priority field.

    This controls whether a new LSP being created with certain Setup Priority should
    pre-empt this LSP set up with this Holding Priority. While setting up a new LSP,
    preemption of existing LSP can happen if resource limitation is encountered (e.g
    bandwidth availability).
    """

    hop_limit: int
    """Specifies the value of the Hop Limit field.

    This controls the maximum number of hops the LSP should traverse to reach the
    LSP end-point.
    """

    include_all: str
    """
    A 32-bit vector representing a set of attribute filters associated with a tunnel
    all of which must be present for a link to be acceptable. A null set (all bits
    set to zero) automatically passes. The most significant byte in the hex-string
    is the farthest to the left in the byte sequence. Leading zero bytes in the
    configured value may be omitted for brevity.
    """

    include_any: str
    """
    A 32-bit vector representing a set of attribute filters associated with a tunnel
    any of which renders a link acceptable. A null set (all bits set to zero)
    automatically passes. The most significant byte in the hex-string is the
    farthest to the left in the byte sequence. Leading zero bytes in the configured
    value may be omitted for brevity.
    """

    one_to_one_backup_desired: bool
    """Requests protection via the one-to-one backup method."""

    setup_priority: int
    """Specifies the value of the Setup Priority field.

    This controls whether the backup LSP should pre-empt existing LSP that is setup
    with certain Holding Priority. While setting up a backup LSP, preemption of
    existing LSP can happen if resource limitation is encountered (e.g bandwidth
    availability).
    """


class DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspSessionAttributeResourceAffinities(TypedDict, total=False):
    exclude_any: str
    """
    A 32-bit vector representing a set of attribute filters associated with a tunnel
    any of which renders a link unacceptable. A null set (all bits set to zero)
    doesn't render the link unacceptable. The most significant byte in the
    hex-string is the farthest to the left in the byte sequence. Leading zero bytes
    in the configured value may be omitted for brevity.
    """

    include_all: str
    """
    A 32-bit vector representing a set of attribute filters associated with a tunnel
    all of which must be present for a link to be acceptable. A null set (all bits
    set to zero) automatically passes. The most significant byte in the hex-string
    is the farthest to the left in the byte sequence. Leading zero bytes in the
    configured value may be omitted for brevity.
    """

    include_any: str
    """
    A 32-bit vector representing a set of attribute filters associated with a tunnel
    any of which renders a link acceptable. A null set (all bits set to zero)
    automatically passes. The most significant byte in the hex-string is the
    farthest to the left in the byte sequence. Leading zero bytes in the configured
    value may be omitted for brevity.
    """


class DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspSessionAttribute(TypedDict, total=False):
    auto_generate_session_name: bool
    """
    If this is enabled, an auto-generated Session Name is included in the
    SESSION_ATTRIBUTE object in the Path Message for this LSP.
    """

    bandwidth_protection_desired: bool
    """
    This flag in the SESSION_ATTRIBUTE object in the Path Message indicates to the
    PLRs along the protected LSP path that a backup path with a bandwidth guarantee
    is desired. This bandwidth has to be guaranteed for the protected LSP, if no
    FAST_REROUTE object is included in the PATH message. If a FAST_REROUTE object is
    present in the Path message, then the bandwidth specified therein is to be
    guaranteed.
    """

    holding_priority: int
    """Specifies the value of the Holding Priority field.

    This controls whether a new LSP being created with certain Setup Priority should
    pre-empt this LSP if resource limitation is encountered when setting up the LSP.
    (e.g. bandwidth availability). The value 0 is the highest priority while 7 is
    the lowest.
    """

    label_recording_desired: bool
    """
    This flag indicates that label information should be included when doing a route
    record.
    """

    local_protection_desired: bool
    """
    This flag permits transit routers to use a local repair mechanism which may
    result in violation of the explicit route object. When a fault is detected on an
    adjacent downstream link or node, a transit router can reroute traffic for fast
    service restoration.
    """

    node_protection_desired: bool
    """
    This flag in the SESSION_ATTRIBUTE object in the Path Message indicates to the
    PLRs along a protected LSP path that it is desired to have a backup path that
    bypasses at least the next node of the protected LSP.
    """

    resource_affinities: DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspSessionAttributeResourceAffinities
    """This is an optional object.

    If included the extended SESSION_ATTRIBUTE object is sent in the Path message
    containing the additional fields included in this object. This contains a set of
    three bitmaps using which further constraints can be set on the path calculated
    for the LSP based on the Admin Group settings in the IGP (e.g ISIS or OSPF
    interface).
    """

    se_style_desired: bool
    """
    This flag indicates that the tunnel ingress node may choose to reroute this
    tunnel without tearing it down. A tunnel egress node SHOULD use the Shared
    Explicit(SE) Style when responding with a Resv message.
    """

    session_name: str
    """
    If auto_generate_session_name is set to 'false', then the value of this field is
    used to fill the Session Name field of the SESSION_ATTRIBUTE object in the Path
    Message for this LSP. It is suggested to include the Local IP, Remote IP, Tunnel
    ID and LSP ID in the auto-generated Session Name to ensure uniqueness of the
    name in the test. The maximum length of session name is 254 bytes.
    """

    setup_priority: int
    """Specifies the value of the Setup Priority field.

    This controls whether the LSP should pre-empt existing LSP setup with certain
    Holding Priority if resource limitation is encountered when setting up the LSP.
    (e.g. bandwidth availability). The value 0 is the highest priority while 7 is
    the lowest.
    """


class DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspTspec(TypedDict, total=False):
    maximum_policed_unit: int
    """Specifies the maximum length of packet frames that will be policed."""

    minimum_policed_unit: int
    """Specifies the minium length of packet frames that will be policed."""

    peak_data_rate: float
    """
    The peak data rate of the traffic in bytes per second used to specify the Token
    Bucket characteristics of the traffic to be carried in the LSP. This is part of
    the Token Bucket specification defined for a traffic flow defined in RFC2215.
    """

    token_bucket_rate: float
    """The rate of the traffic to be carried in this LSP in bytes per second.

    This is part of the Token Bucket specification defined for a traffic flow
    defined in RFC2215.
    """

    token_bucket_size: float
    """
    The depth of the token bucket in bytes used to specify the Token Bucket
    characteristics of the traffic to be carried in the LSP. This is part of the
    Token Bucket specification defined for a traffic flow defined in RFC2215.
    """


class DeviceRsvpLspIpv4InterfaceP2pIngressIpv4Lsp(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    remote_address: Required[str]
    """IPv4 address of the remote endpoint of the LSP."""

    backup_lsp_id: int
    """
    The LSP id that will be used when creating a Make-Before-Break LSP when the
    active LSP is using lsp_id. If the active LSP on which Make-Before-Break is
    being done is using the backup_lsp_id, the new LSP created will toggle to use
    the lsp_id instead.
    """

    ero: DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspEro
    """
    This contains the values of the fields to be included in the ERO object in the
    Path Message sent for the LSP. This is an optional object . If this attribute is
    not included , the ERO object will not be included.
    """

    fast_reroute: DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspFastReroute
    """
    This contains the values of the fields to be included in the FAST_REROUTE object
    in the Path Message sent for the LSP. This is an optional object . If this
    attribute is not included , the FAST_REROUTE object will not be included.
    """

    lsp_id: int
    """The LSP ID of the RSVP LSP.

    Carried in the SENDER_TEMPLATE object in Path Messages.
    """

    lsp_switchover_delay: int
    """
    The amount of delay in milliseconds that an implementation should wait for
    before switching traffic to the new LSP created after a Make-Before-Break is
    done on an LSP. The default value is 0 which means to switch immediately. An
    implementation should support a minimum delay value of at least 50ms . There is
    no specification specified maximum value. Setting maximum allowed value to 1
    minute. If a delay value is supplied which is lesser than the minimum delay
    value supported, a warning should be provided indicating that the minimum value
    of LSP switchover delay is automatically increased to the supported minimum
    value. This warning should be included in the list of warnings in the
    'Response.Warning' attribute sent in the SetConfig 'Success' Response.
    """

    refresh_interval: int
    """The time in seconds between successive transmissions of PATH Refreshes.

    The actual refresh interval is jittered by upto 50%. There is no specification
    specified maximum value. For clarity, setting the maximum to 1 hour.
    """

    session_attribute: DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspSessionAttribute
    """
    This contains the values of the fields to be included in the SESSION_ATTRIBUTE
    object in the Path Message sent for the LSP.
    """

    timeout_multiplier: int
    """
    The number of missed RESV refreshes after which a recieving node should consider
    the LSP state to have timed out. There is no specification specified maximum
    value. Setting the maximum allowed value to 10.
    """

    tspec: DeviceRsvpLspIpv4InterfaceP2pIngressIpv4LspTspec
    """
    This contains the values of the fields to be included in the TSPEC object in the
    Path Message sent for the LSP.
    """

    tunnel_id: int
    """The Tunnel ID of the RSVP LSP. Carried in the SESSION object in Path Messages."""


class DeviceRsvpLspIpv4Interface(TypedDict, total=False):
    ipv4_name: Required[str]
    """
    The globally unique name of the IPv4 or Loopback IPv4 interface acting as the
    RSVP ingress and egress endpoint for the LSPs configured on this interface. This
    must match the "name" field of either "ipv4_addresses" or "ipv4_loopbacks" on
    which this LSP interface is configured.

    x-constraint:

    - /components/schemas/Device.Ipv4/properties/name
    - /components/schemas/Device.Ipv4Loopback/properties/name
    """

    p2p_egress_ipv4_lsps: DeviceRsvpLspIpv4InterfaceP2pEgressIpv4Lsps
    """Contains properties of Tail(Egress) LSPs."""

    p2p_ingress_ipv4_lsps: Iterable[DeviceRsvpLspIpv4InterfaceP2pIngressIpv4Lsp]
    """Array of point-to-point RSVP-TE P2P LSPs originating from this interface."""


class DeviceRsvp(TypedDict, total=False):
    ipv4_interfaces: Iterable[DeviceRsvpIpv4Interface]
    """List of IPv4 RSVP connected interfaces.

    At least one interface should be present for device connected to the DUT. For
    unconnected devices, this array must be empty.
    """

    lsp_ipv4_interfaces: Iterable[DeviceRsvpLspIpv4Interface]
    """
    List of IPv4 Loopback or IPv4 connected interfaces acting as RSVP ingress and
    egress endpoints.
    """

    name: str
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """


class DeviceVxlanV4TunnelDestinationIPModeMulticast(TypedDict, total=False):
    address: str
    """IPv4 Multicast address"""


class DeviceVxlanV4TunnelDestinationIPModeUnicastVtep(TypedDict, total=False):
    arp_suppression_cache: Iterable[VxlanTunnelDestinationIPModeUnicastArpSuppressionCacheParam]
    """
    Each VTEP maintains an ARP suppression cache table for known IP hosts and their
    associated MAC addresses in the VNI segment. When an end host in the VNI sends
    an ARP request for another end-host IP address, its local VTEP intercepts the
    ARP request and checks for the ARP-resolved IP address in its ARP suppression
    cache table. If it finds a match, the local VTEP sends an ARP response on behalf
    of the remote end host.
    """

    remote_vtep_address: str
    """Remote VXLAN Tunnel End Point address"""


class DeviceVxlanV4TunnelDestinationIPModeUnicast(TypedDict, total=False):
    vteps: Iterable[DeviceVxlanV4TunnelDestinationIPModeUnicastVtep]
    """List of VTEPs for member VNI(VXLAN Network Identifier)"""


class DeviceVxlanV4TunnelDestinationIPMode(TypedDict, total=False):
    choice: Literal["unicast", "multicast"]
    """unicast or multicast"""

    multicast: DeviceVxlanV4TunnelDestinationIPModeMulticast
    """Multicast Group address for member VNI(VXLAN Network Identifier)"""

    unicast: DeviceVxlanV4TunnelDestinationIPModeUnicast


class DeviceVxlanV4Tunnel(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects. Globally unique name of
    an object. It also serves as the primary key for arrays of objects.
    """

    source_interface: Required[str]
    """Determines the source interface.

    x-constraint:

    - /components/schemas/Device.Ipv4/properties/name
    - /components/schemas/Device.Ipv4Loopback/properties/name
    """

    vni: Required[int]
    """VXLAN Network Identifier (VNI) to distinguish network instances on the wire"""

    destination_ip_mode: DeviceVxlanV4TunnelDestinationIPMode
    """Communication mode between the VTEPs, either unicast or multicast."""


class DeviceVxlanV6TunnelDestinationIPModeMulticast(TypedDict, total=False):
    address: str
    """IPv6 Multicast address"""


class DeviceVxlanV6TunnelDestinationIPModeUnicastVtep(TypedDict, total=False):
    arp_suppression_cache: Iterable[VxlanTunnelDestinationIPModeUnicastArpSuppressionCacheParam]
    """
    Each VTEP maintains an ARP suppression cache table for known IP hosts and their
    associated MAC addresses in the VNI segment. When an end host in the VNI sends
    an ARP request for another end-host IP address, its local VTEP intercepts the
    ARP request and checks for the ARP-resolved IP address in its ARP suppression
    cache table. If it finds a match, the local VTEP sends an ARP response on behalf
    of the remote end host.
    """

    remote_vtep_address: str
    """Remote VXLAN Tunnel End Point address"""


class DeviceVxlanV6TunnelDestinationIPModeUnicast(TypedDict, total=False):
    vteps: Iterable[DeviceVxlanV6TunnelDestinationIPModeUnicastVtep]
    """List of VTEPs for member VNI(VXLAN Network Identifier)"""


class DeviceVxlanV6TunnelDestinationIPMode(TypedDict, total=False):
    choice: Literal["unicast", "multicast"]
    """unicast or multicast"""

    multicast: DeviceVxlanV6TunnelDestinationIPModeMulticast
    """Multicast Group address for member VNI(VXLAN Network Identifier)"""

    unicast: DeviceVxlanV6TunnelDestinationIPModeUnicast


class DeviceVxlanV6Tunnel(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects. Globally unique name of
    an object. It also serves as the primary key for arrays of objects.
    """

    source_interface: Required[str]
    """Determines the source interface.

    x-constraint:

    - /components/schemas/Device.Ipv6/properties/name
    - /components/schemas/Device.Ipv6Loopback/properties/name
    """

    vni: Required[int]
    """VXLAN Network Identifier (VNI) to distinguish network instances on the wire"""

    destination_ip_mode: DeviceVxlanV6TunnelDestinationIPMode
    """Communication mode between the VTEPs, either unicast or multicast."""


class DeviceVxlan(TypedDict, total=False):
    v4_tunnels: Iterable[DeviceVxlanV4Tunnel]
    """IPv4 VXLAN Tunnels"""

    v6_tunnels: Iterable[DeviceVxlanV6Tunnel]
    """IPv6 VXLAN Tunnels"""


class Device(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    bgp: DeviceBgp
    """
    The properties of BGP router and its children, such as BGPv4, BGPv6 peers and
    their route ranges.
    """

    dhcp_server: DeviceDhcpServer
    """The properties of DHCP Server and its children, such as DHCPv4, DHCPv6 servers."""

    ethernets: Iterable[DeviceEthernet]
    """
    Ethernet configuration for one or more emulated or simulated network interfaces.
    """

    ipv4_loopbacks: Iterable[DeviceIpv4Loopback]
    """
    IPv4 Loopback interface that can be attached to an Ethernet in the same device
    or to an Ethernet in another device.
    """

    ipv6_loopbacks: Iterable[DeviceIpv6Loopback]
    """
    IPv6 Loopback interface that can be attached to an Ethernet in the same device
    or to an Ethernet in another device.
    """

    isis: DeviceIsis
    """
    The properties of an IS-IS router and its children, such as IS-IS interfaces and
    route ranges.
    """

    macsec: DeviceMacsec
    """Configuration of MACsec device."""

    ospfv2: DeviceOspfv2
    """Configuration for OSPFv2 router."""

    ospfv3: DeviceOspfv3
    """Configuration for OSPFv3 router."""

    rocev2: DeviceRocev2
    """Configuration for RoCEv2."""

    rsvp: DeviceRsvp
    """The properties of an RSVP router and its children."""

    vxlan: DeviceVxlan
    """
    Configuration of VXLAN tunnel interfaces RFC Ref:
    https://datatracker.ietf.org/doc/html/rfc7348
    """


class EgressOnlyTrackingFilter(TypedDict, total=False):
    choice: Literal["none", "auto_macsec"]
    """
    If a packet does not match the filter it will not be considered for egress
    tracking. Currently two options are provided: none: All packets will be
    considered for egress only tracking. auto_macsec: This requires that MACsec
    enabled Ethernet interface should be configured on this port. This filter will
    ensure that only packets with Ethernet Type set to MACsec (0x88E5) and destined
    to traffic Rx device(s) will be considered for egress only tracking
    """


class EgressOnlyTrackingMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    The Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field.
    """

    offset: Required[int]
    """Offset in bits relative to start of the packet."""

    length: int
    """
    Number of bits to track for metrics starting from configured offset from start
    of the packet.
    """


class EgressOnlyTracking(TypedDict, total=False):
    port_name: Required[str]
    """
    Name of the received port this egress tracking rule/specification has to be
    applied.

    x-constraint:

    - /components/schemas/Port/properties/name
    """

    enable_timestamps: bool
    """Enables additional metric first and last timestamps."""

    filters: Iterable[EgressOnlyTrackingFilter]
    """
    Specifies a rule which will be used to first filter received packets on this
    port before applying the egress tracking metric_tags on them. If multiple
    filters are provided, then an incoming packet MUST pass all the filters. If the
    packet does not pass any filter, it is not considered for egress tracking.
    """

    metric_tags: Iterable[EgressOnlyTrackingMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding egress_only_tracking metrics.
    """


class EventsCpEvents(TypedDict, total=False):
    enable: bool
    """
    Setting to true enables start and end time for control_plane events associated
    with started flows to be recorded.
    """


class EventsDpEvents(TypedDict, total=False):
    enable: bool
    """
    Setting to true enables flow_rx_rate_above_threshold and
    flow_rx_rate_below_threshold timestamps to be recorded when data packets switch
    between multiple rx_ports on the receive ports for affected flows.
    """

    rx_rate_threshold: float
    """
    Setting to true enables timestamps to be recorded when the rx rate of a flow
    goes above or below the threshold value.
    """


class Events(TypedDict, total=False):
    cp_events: EventsCpEvents
    """Container for control plane(cp) event configuration."""

    dp_events: EventsDpEvents
    """
    Container for data plane(dp) event configuration. Enabling this option may
    affect the resultant packet payload due to additional instrumentation data.
    """


class LagPortEthernet(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    mac: str
    """
    Media Access Control address.The implementation should ensure that the 'mac'
    field is explicitly configured by the user for all types of interfaces as
    denoted by 'connection' attribute except 'simulated_link' where 'mac' is not
    mandatory.
    """

    mtu: int
    """Maximum Transmission Unit."""

    vlans: Iterable[DeviceVlanParam]
    """List of VLANs"""


class LagPortLacp(TypedDict, total=False):
    actor_activity: Literal["passive", "active"]
    """
    Sets the value of LACP actor activity as either passive or active. Passive
    indicates the port's preference for not transmitting LACPDUs unless its
    partner's control is Active. Active indicates the port's preference to
    participate in the protocol regardless of the partner's control value.
    """

    actor_port_number: int
    """The actor port number"""

    actor_port_priority: int
    """The actor port priority"""

    lacpdu_periodic_time_interval: int
    """This field defines how frequently LACPDUs are sent to the link partner"""

    lacpdu_timeout: int
    """This timer is used to detect whether received protocol information has expired"""


class LagPort(TypedDict, total=False):
    ethernet: Required[LagPortEthernet]
    """Base Ethernet interface."""

    port_name: Required[str]
    """The name of a port object that will be part of the LAG.

    x-constraint:

    - /components/schemas/Port/properties/name
    """

    lacp: LagPortLacp
    """
    The container for link aggregation control protocol settings of a LAG member
    (port).
    """


class LagProtocolLacp(TypedDict, total=False):
    actor_key: int
    """The actor key"""

    actor_system_id: str
    """The actor system id"""

    actor_system_priority: int
    """The actor system priority"""


class LagProtocolStatic(TypedDict, total=False):
    lag_id: int
    """The static lag id"""


class LagProtocol(TypedDict, total=False):
    choice: Literal["lacp", "static"]
    """The type of controlling protocol for the LAG (ports group)."""

    lacp: LagProtocolLacp
    """
    The container for link aggregation control protocol settings of a LAG (ports
    group).
    """

    static: LagProtocolStatic
    """The container for static link aggregation protocol settings."""


class Lag(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    min_links: int
    """
    Specifies the mininum number of member interfaces that must be active for the
    aggregate interface to be available. If the aggregate interface is not available
    due to min-links criterion not being met, LACPDUs continue to be transmitted and
    received by the member interfaces if LACP is enabled, but other PDUs are not
    transmitted or received.
    """

    ports: Iterable[LagPort]

    protocol: LagProtocol


class Layer1AutoNegotiation(TypedDict, total=False):
    advertise_10_fd_mbps: bool
    """
    If auto_negotiate is true and the interface supports this option then this speed
    will be advertised.
    """

    advertise_10_hd_mbps: bool
    """
    If auto_negotiate is true and the interface supports this option then this speed
    will be advertised.
    """

    advertise_100_fd_mbps: bool
    """
    If auto_negotiate is true and the interface supports this option then this speed
    will be advertised.
    """

    advertise_100_hd_mbps: bool
    """
    If auto_negotiate is true and the interface supports this option then this speed
    will be advertised.
    """

    advertise_1000_mbps: bool
    """
    If auto_negotiate is true and the interface supports this option then this speed
    will be advertised.
    """

    link_training: bool
    """Enable/disable gigabit ethernet link training."""

    rs_fec: bool
    """Enable/disable gigabit ethernet reed solomon forward error correction (RS FEC)."""


class Layer1FlowControlIeee802_1qbb(TypedDict, total=False):
    pfc_class_0: int
    """
    The valid values are null, 0 - 7. A null value indicates there is no setting for
    this pfc class.
    """

    pfc_class_1: int
    """
    The valid values are null, 0 - 7. A null value indicates there is no setting for
    this pfc class.
    """

    pfc_class_2: int
    """
    The valid values are null, 0 - 7. A null value indicates there is no setting for
    this pfc class.
    """

    pfc_class_3: int
    """
    The valid values are null, 0 - 7. A null value indicates there is no setting for
    this pfc class.
    """

    pfc_class_4: int
    """
    The valid values are null, 0 - 7. A null value indicates there is no setting for
    this pfc class.
    """

    pfc_class_5: int
    """
    The valid values are null, 0 - 7. A null value indicates there is no setting for
    this pfc class.
    """

    pfc_class_6: int
    """
    The valid values are null, 0 - 7. A null value indicates there is no setting for
    this pfc class.
    """

    pfc_class_7: int
    """
    The valid values are null, 0 - 7. A null value indicates there is no setting for
    this pfc class.
    """

    pfc_delay: int
    """
    The upper limit on the transmit time of a queue after receiving a message to
    pause a specified priority. A value of 0 or null indicates that pfc delay will
    not be enabled.
    """


class Layer1FlowControl(TypedDict, total=False):
    choice: Literal["ieee_802_1qbb", "ieee_802_3x"]
    """The type of priority flow control."""

    directed_address: str
    """
    The 48bit mac address that the layer1 port names will listen on for a directed
    pause.
    """

    ieee_802_1qbb: Layer1FlowControlIeee802_1qbb
    """
    These settings enhance the existing 802.3x pause priority capabilities to enable
    flow control based on 802.1p priorities (classes of service).
    """

    ieee_802_3x: object
    """A container for ieee 802.3x rx pause settings"""


class Layer1(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    port_names: Required[List[str]]
    """A list of unique names of port objects that will share the choice settings.

    x-constraint:

    - /components/schemas/Port/properties/name
    """

    auto_negotiate: bool
    """
    Under Review: This field is currently under review for pending exploration on
    use cases, given that a separate configuration called `AutoNegotiation` already
    exists.

    Enable/disable auto negotiation.
    """

    auto_negotiation: Layer1AutoNegotiation
    """Configuration for auto negotiation settings"""

    flow_control: Layer1FlowControl
    """
    A container for layer1 receive flow control settings. To enable flow control
    settings on ports this object must be a valid object not a null value.
    """

    ieee_media_defaults: bool
    """
    Under Review: This field is currently under review for pending exploration on
    use cases

    Set to true to override the auto_negotiate, link_training and rs_fec settings
    for gigabit ethernet interfaces.
    """

    media: Literal["copper", "fiber", "sgmii"]
    """Set the type of media for test interface if supported.

    When no media type is explicitly set, the current media type of underlying test
    interface shall be assumed.
    """

    mtu: int
    """Set the maximum transmission unit size.

    A warning shall be raised if the specified value is valid but not supported,
    ignoring the setting altogether.
    """

    promiscuous: bool
    """Enable promiscuous mode on test interface.

    A warning shall be raised if this field is set to `true`, even when it's not
    supported, ignoring the setting altogether.
    """

    speed: Literal[
        "speed_10_fd_mbps",
        "speed_10_hd_mbps",
        "speed_100_fd_mbps",
        "speed_100_hd_mbps",
        "speed_1_gbps",
        "speed_10_gbps",
        "speed_25_gbps",
        "speed_40_gbps",
        "speed_50_gbps",
        "speed_100_gbps",
        "speed_200_gbps",
        "speed_400_gbps",
        "speed_800_gbps",
    ]
    """Set the speed if supported.

    When no speed is explicitly set, the current speed of underlying test interface
    shall be assumed.
    """


class LldpConnection(TypedDict, total=False):
    choice: Literal["port_name"]
    """
    The name of the test port or other connection objects on which LLDP is
    configured.
    """

    port_name: str
    """Name of the test port on which LLDP is configured on.

    x-constraint:

    - /components/schemas/Port/properties/name
    """


class LldpChassisIDMacAddressSubtype(TypedDict, total=False):
    auto: str
    """The OTG implementation must provide a system generated value for this property."""

    choice: Literal["auto", "value"]
    """
    In auto mode the system generated value is set for this property, while if the
    choice is selected as value, a user configured value will be used for this
    property.
    """

    value: str
    """User must specify a value if mode is not auto."""


class LldpChassisID(TypedDict, total=False):
    choice: Literal["mac_address_subtype", "interface_name_subtype", "local_subtype"]
    """Chassis ID subtype to be used in Chassis ID TLV."""

    interface_name_subtype: str
    """Name of an interface of the chassis that uniquely identifies the chassis."""

    local_subtype: str
    """Locally assigned name of the chassis."""

    mac_address_subtype: LldpChassisIDMacAddressSubtype
    """The MAC address configured in the Chassis ID TLV."""


class LldpOrgInfoInformation(TypedDict, total=False):
    choice: Literal["info"]
    """
    In info mode the organizationally defined information contain either binary or
    alpha-numeric information encoded in UTF-8 (as specified in IETF RFC 3629).
    """

    info: str
    """
    The organizationally defined information encoded in UTF-8 (as specified in IETF
    RFC 3629). This byte stream can be of any length from 1 to 507 bytes. In the
    info byte stream, one byte is represented as string of 2 characters, for example
    2 character string (0x)AB represents value of a single byte. So the maximum
    length of this attribute is 1014 (507 \\** 2 hex characters per byte).
    """


class LldpOrgInfo(TypedDict, total=False):
    information: LldpOrgInfoInformation
    """Contains the organizationally defined information.

    The actual format of the organizationally defined information string field is
    organizationally specific and can contain either binary or alpha-numeric
    information that is instance specific for the particular TLV type and subtype.
    Alpha-numeric information are encoded in UTF-8 (as specified in IETF RFC 3629).
    Or include one or more information fields with their associated field-type
    identifiers, designators similar to those in the Management Address TLV.
    """

    oui: str
    """
    The organizationally unique identifier field shall contain the organization's
    OUI as defined in Clause 9 of IEEE Std 802. It is a 24 bit number that uniquely
    identifies a vendor, manufacturer, or other organizations.
    """

    subtype: int
    """
    The organizationally defined subtype field shall contain a unique subtype value
    assigned by the defining organization.
    """


class LldpPortIDInterfaceNameSubtype(TypedDict, total=False):
    auto: str
    """The OTG implementation must provide a system generated value for this property."""

    choice: Literal["auto", "value"]
    """
    In auto mode the system generated value is set for this property, while if the
    choice is selected as value, a user configured value will be used for this
    property.
    """

    value: str
    """User must specify a value if mode is not auto."""


class LldpPortID(TypedDict, total=False):
    choice: Literal["mac_address_subtype", "interface_name_subtype", "local_subtype"]
    """Port ID subtype to be used in Port ID TLV."""

    interface_name_subtype: LldpPortIDInterfaceNameSubtype
    """The interface name configured in the Port ID TLV."""

    local_subtype: str
    """The Locally assigned name configured in the Port ID TLV."""

    mac_address_subtype: str
    """The MAC Address configured in the Port ID TLV."""


class LldpSystemName(TypedDict, total=False):
    auto: str
    """The OTG implementation must provide a system generated value for this property."""

    choice: Literal["auto", "value"]
    """
    In auto mode the system generated value is set for this property, while if the
    choice is selected as value, a user configured value will be used for this
    property.
    """

    value: str
    """User must specify a value if mode is not auto."""


class Lldp(TypedDict, total=False):
    connection: Required[LldpConnection]
    """The unique name of the object on which LLDP is running."""

    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    advertisement_interval: int
    """Set the transmission frequency of LLDP updates in seconds."""

    chassis_id: LldpChassisID
    """
    The Chassis ID is a mandatory TLV which identifies the chassis component of the
    endpoint identifier associated with the transmitting LLDP agent. If mac address
    is specified it should be in colon seperated mac address format.
    """

    hold_time: int
    """
    Specifies the amount of time in seconds a receiving device should maintain LLDP
    information sent by the device before discarding it.
    """

    org_infos: Iterable[LldpOrgInfo]
    """The Organization Information is used to define the organization specific TLVs.

    The organization specific TLV is defined in IEEE 802.1AB-2016 specification.
    This category is provided to allow different organizations, such as IEEE 802.1,
    IEEE 802.3, IETF, as well as individual software and equipment vendors, to
    define TLVs that advertise information to remote entities attached to the same
    media.
    """

    port_id: LldpPortID
    """
    The Port ID is a mandatory TLV which identifies the port component of the
    endpoint identifier associated with the transmitting LLDP agent. If the
    specified port is an IEEE 802.3 Repeater port, then this TLV is optional.
    """

    system_name: LldpSystemName
    """
    The system name field shall contain an alpha-numeric string that indicates the
    system's administratively assigned name. The system name should be the system's
    fully qualified domain name. If implementations support IETF RFC 3418, the
    sysName object should be used for this field.
    """


class OptionsPerPortOptionProtocolRocev2Cnp(TypedDict, total=False):
    choice: Literal["ip_dscp"]

    cnp_delay_timer: int
    """
    The interval duration between the generation of successive CNP packets should be
    specified in microseconds.
    """

    ecn_value: Literal["non_ect", "ect_1", "ect_0", "ce"]
    """CNP ECN Value."""

    ip_dscp: Rocev2PriorityValueParam
    """IP DSCP value for the CNP packets."""


class OptionsPerPortOptionProtocolRocev2ConnectionTypeReliableConnectionAck(TypedDict, total=False):
    choice: Literal["ip_dscp"]

    ecn_value: Literal["non_ect", "ect_1", "ect_0", "ce"]
    """ACK ECN Value."""

    ip_dscp: Rocev2PriorityValueParam
    """IP DSCP value for the ACK packets."""


class OptionsPerPortOptionProtocolRocev2ConnectionTypeReliableConnectionNak(TypedDict, total=False):
    choice: Literal["ip_dscp"]

    ecn_value: Literal["non_ect", "ect_1", "ect_0", "ce"]
    """ECN Code point to add in NAK packets."""

    ip_dscp: Rocev2PriorityValueParam
    """IP DSCP value for the NAK packets."""


class OptionsPerPortOptionProtocolRocev2ConnectionTypeReliableConnection(TypedDict, total=False):
    ack: OptionsPerPortOptionProtocolRocev2ConnectionTypeReliableConnectionAck
    """ACK parameters."""

    enable_retransmission_timeout: bool
    """Enable Retransmission on ACK Timeout."""

    nak: OptionsPerPortOptionProtocolRocev2ConnectionTypeReliableConnectionNak
    """NAK parameters."""

    retransmission_retry_count: int
    """Number of retransmission attempts before stopping due to missing ACK/NAK."""

    retransmission_timeout_value: int
    """
    The duration to wait before retrying transmission upon not receiving an
    acknowledgment (ACK) or negative acknowledgment (NAK) is specified in
    milliseconds.
    """


class OptionsPerPortOptionProtocolRocev2ConnectionType(TypedDict, total=False):
    choice: Literal["reliable_connection"]

    reliable_connection: OptionsPerPortOptionProtocolRocev2ConnectionTypeReliableConnection
    """Defines the ACK and NAK settings for RoCEv2.

    This configuration ensures reliable data delivery by controlling how the system
    responds to successful and failed packet transmissions.
    """


class OptionsPerPortOptionProtocolRocev2DcqcnSettings(TypedDict, total=False):
    additive_increment_rate: float
    """
    This is the rate at which the target rates will increase when the DCQCN will be
    in the additive increase rate recovery mode.
    """

    alpha_g: int
    """Controls the increment / decrement of the alpha parameter in DCQCN algorithm."""

    alpha_update_period: int
    """timer after which the alpha parameter will update according to the algorithm.

    Unit is microseconds.
    """

    clamp_target_rate: bool
    """
    Is used to reduce the target rate by remembering the current rate. If it is not
    set, then only the target rate will be reduced for the first CNP after each rate
    increment otherwise if its set then the target rate will be reduced for each
    rate reduce.
    """

    enable_dcqcn: bool
    """Enable DCQCN port settigns."""

    hyper_increment_rate: float
    """
    This is the rate at which the target rates will increase when the DCQCN will be
    in the hyper increment rate recovery mode.
    """

    initial_alpha: int
    """Value of the alpha at the time when the first CNP is received."""

    initial_rate_after_first_cnp: float
    """This is the percentage of rate user wants to set on receiving the first CNP."""

    maximum_rate_decrement_at_time: int
    """
    This is the maximum that line rate can be decreased on triggering a rate reduce
    algorithm.
    """

    minimum_rate_limmit: float
    """This is the minimum line rate which user wants to restrict.

    Below this the algorithm cannot set the rate.
    """

    rate_increment_byte_counter: int
    """
    This is the bytes counter. After the expiry of this bytes also counter the rate
    recovery algorithms will be triggered, and the rate will be recovered.
    """

    rate_increment_threshold: int
    """
    This is the threshold value which will ensure how many times, each rate recovery
    algorithms will execute before moving to the next value.
    """

    rate_increment_time: int
    """After the expiry of this timer, the rate recovery algorithms will be triggered.

    Unit is microseconds.
    """

    rate_reduction_time_period: int
    """
    timer after which the algorithm will check if CNP is there or not and if CNP is
    present it will reduce the rate. Unit is microseconds.
    """


class OptionsPerPortOptionProtocolRocev2(TypedDict, total=False):
    cnp: OptionsPerPortOptionProtocolRocev2Cnp
    """CNP parameters."""

    connection_type: OptionsPerPortOptionProtocolRocev2ConnectionType
    """
    Specifies the connection type for the QP, determining what and how the QP
    transfers data.
    """

    dcqcn_settings: OptionsPerPortOptionProtocolRocev2DcqcnSettings
    """RoCEv2 DCQCN Settings."""


class OptionsPerPortOptionProtocol(TypedDict, total=False):
    choice: Literal["rocev2"]
    """list of protocols that have per port settings"""

    rocev2: OptionsPerPortOptionProtocolRocev2
    """Data plane traffic flow configuration for a test port."""


class OptionsPerPortOption(TypedDict, total=False):
    port_name: str
    """The name of port for which this settings will be applied to.

    x-constraint:

    - /components/schemas/Port/properties/name
    """

    protocols: Iterable[OptionsPerPortOptionProtocol]


class OptionsPortOptions(TypedDict, total=False):
    location_preemption: bool
    """
    Preempt all the test port locations as defined by the
    Port.Port.properties.location. If the test ports defined by their location
    values are in use and this value is true, the test ports will be preempted.
    """


class OptionsProtocolOptions(TypedDict, total=False):
    auto_start_all: bool
    """
    When set to true, all underlying resources for configured protocols and
    interfaces shall be created and corresponding protocol session negotiation shall
    be initiated. Otherwise, when set to false, corresponding protocol session
    negotiation will need to be initiated using a separate set_protocol_state API
    call.
    """


class Options(TypedDict, total=False):
    per_port_options: Iterable[OptionsPerPortOption]

    port_options: OptionsPortOptions
    """Common port options that apply to all configured Port objects."""

    protocol_options: OptionsProtocolOptions
    """Common options that apply to all configured protocols and interfaces."""


class Port(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    location: str
    """The location of a test port.

    It is the endpoint where packets will emit from. Test port locations can be the
    following:

    - physical appliance with multiple ports
    - physical chassis with multiple cards and ports
    - local interface
    - virtual machine, docker container, kubernetes cluster

    The test port location format is implementation specific. Use the
    /results/capabilities API to determine what formats an implementation supports
    for the location property. Get the configured location state by using the
    /results/port API.
    """


class StatefulFlowsRocev2TxPortTransmitTypeTargetLineRateFlowRocev2Verb(TypedDict, total=False):
    choice: Literal["write", "write_with_immediate", "send", "send_with_immediate", "read"]

    send_with_immediate: Rocev2ImmediateDataParam
    """Four bytes of immediate Data for SEND/WRITE with immediate."""

    write_with_immediate: Rocev2ImmediateDataParam
    """Four bytes of immediate Data for SEND/WRITE with immediate."""


class StatefulFlowsRocev2TxPortTransmitTypeTargetLineRateFlow(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    tx_endpoint: Required[str]
    """The unique name of an emulated device that will be transmitting the flows.

    x-constraint:

    - /components/schemas/Rocev2.QPs/properties/qp_name
    """

    message_size: int
    """Length of Message that needs to be transmitted to the remote end-point."""

    message_size_unit: Literal["bytes", "kb", "mb", "gb"]
    """Unit of the transfer message size.

    Available options are Bytes, KiloBtyes (KB), NegaBytes (MB) and GigaBytes (GB).
    """

    rocev2_verb: StatefulFlowsRocev2TxPortTransmitTypeTargetLineRateFlowRocev2Verb
    """RoCEv2 Verb.

    Available options are: WRITE, WRITE_With_Immediate, SEND, SEND_With_Immediate
    and READ.
    """

    rx_endpoint: str
    """
    The unique name of remote QP or port which be receiving the packets for the
    flow.

    x-constraint:

    - /components/schemas/Port/properties/name
    - /components/schemas/Rocev2.QPs/properties/qp_name
    """


class StatefulFlowsRocev2TxPortTransmitTypeTargetLineRate(TypedDict, total=False):
    flows: Iterable[StatefulFlowsRocev2TxPortTransmitTypeTargetLineRateFlow]

    value: int
    """Target Line Rate as percentage of max line rate."""


class StatefulFlowsRocev2TxPortTransmitType(TypedDict, total=False):
    choice: Literal["target_line_rate"]

    target_line_rate: StatefulFlowsRocev2TxPortTransmitTypeTargetLineRate
    """
    Configure target line rate of traffic rate on this port as percentage of link
    speed.
    """


class StatefulFlowsRocev2TxPort(TypedDict, total=False):
    port_name: str
    """The name of port for which this settings will be applied to.

    x-constraint:

    - /components/schemas/Port/properties/name
    """

    transmit_type: StatefulFlowsRocev2TxPortTransmitType
    """RoCEv2 flows can be configured to run in continuous mode or fixed iteration."""


class StatefulFlowsRocev2(TypedDict, total=False):
    tx_ports: Iterable[StatefulFlowsRocev2TxPort]
    """Specifies the list of transmit (TX) ports used for sending RoCEv2 traffic."""


class StatefulFlows(TypedDict, total=False):
    choice: Literal["rocev2"]
    """Stateful traffic flow configuration."""

    rocev2: Iterable[StatefulFlowsRocev2]
    """RoCEv2 Flow Groups."""
