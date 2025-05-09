# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .flow_ipv4_auto import FlowIpv4Auto
from .flow_ipv6_auto import FlowIpv6Auto
from .flow_snmpv2c_pdu import FlowSnmpv2cPdu
from .flow_rsvp_object_length import FlowRsvpObjectLength
from .flow_rsvp_lsp_tunnel_flag import FlowRsvpLspTunnelFlag
from .pattern_flow_vlan_id_counter import PatternFlowVlanIDCounter
from .flow_rsvp_route_record_length import FlowRsvpRouteRecordLength
from .flow_snmpv2c_variable_binding import FlowSnmpv2cVariableBinding
from .pattern_flow_ipv4_dst_counter import PatternFlowIpv4DstCounter
from .pattern_flow_ipv4_src_counter import PatternFlowIpv4SrcCounter
from .pattern_flow_ipv6_dst_counter import PatternFlowIpv6DstCounter
from .pattern_flow_ipv6_src_counter import PatternFlowIpv6SrcCounter
from .pattern_flow_vlan_cfi_counter import PatternFlowVlanCfiCounter
from .pattern_flow_vlan_tpid_counter import PatternFlowVlanTpidCounter
from .pattern_flow_vxlan_vni_counter import PatternFlowVxlanVniCounter
from .pattern_flow_gtpv1_teid_counter import PatternFlowGtpv1TeidCounter
from .pattern_flow_gtpv2_teid_counter import PatternFlowGtpv2TeidCounter
from .pattern_flow_mpls_label_counter import PatternFlowMplsLabelCounter
from .pattern_flow_tcp_ecn_ns_counter import PatternFlowTcpEcnNsCounter
from .pattern_flow_tcp_window_counter import PatternFlowTcpWindowCounter
from .pattern_flow_udp_length_counter import PatternFlowUdpLengthCounter
from .pattern_flow_gre_version_counter import PatternFlowGreVersionCounter
from .pattern_flow_igmpv1_type_counter import PatternFlowIgmpv1TypeCounter
from .pattern_flow_ppp_address_counter import PatternFlowPppAddressCounter
from .pattern_flow_ppp_control_counter import PatternFlowPppControlCounter
from .pattern_flow_tcp_ack_num_counter import PatternFlowTcpAckNumCounter
from .pattern_flow_tcp_ctl_ack_counter import PatternFlowTcpCtlAckCounter
from .pattern_flow_tcp_ctl_fin_counter import PatternFlowTcpCtlFinCounter
from .pattern_flow_tcp_ctl_psh_counter import PatternFlowTcpCtlPshCounter
from .pattern_flow_tcp_ctl_rst_counter import PatternFlowTcpCtlRstCounter
from .pattern_flow_tcp_ctl_syn_counter import PatternFlowTcpCtlSynCounter
from .pattern_flow_tcp_ctl_urg_counter import PatternFlowTcpCtlUrgCounter
from .pattern_flow_tcp_ecn_cwr_counter import PatternFlowTcpEcnCwrCounter
from .pattern_flow_tcp_seq_num_counter import PatternFlowTcpSeqNumCounter
from .pattern_flow_vxlan_flags_counter import PatternFlowVxlanFlagsCounter
from .pattern_flow_ethernet_dst_counter import PatternFlowEthernetDstCounter
from .pattern_flow_ethernet_src_counter import PatternFlowEthernetSrcCounter
from .pattern_flow_gre_protocol_counter import PatternFlowGreProtocolCounter
from .pattern_flow_gtpv1_e_flag_counter import PatternFlowGtpv1EFlagCounter
from .pattern_flow_gtpv1_s_flag_counter import PatternFlowGtpv1SFlagCounter
from .pattern_flow_gtpv2_spare1_counter import PatternFlowGtpv2Spare1Counter
from .pattern_flow_gtpv2_spare2_counter import PatternFlowGtpv2Spare2Counter
from .pattern_flow_ipv4_version_counter import PatternFlowIpv4VersionCounter
from .pattern_flow_ipv6_version_counter import PatternFlowIpv6VersionCounter
from .pattern_flow_tcp_dst_port_counter import PatternFlowTcpDstPortCounter
from .pattern_flow_tcp_ecn_echo_counter import PatternFlowTcpEcnEchoCounter
from .pattern_flow_tcp_src_port_counter import PatternFlowTcpSrcPortCounter
from .pattern_flow_udp_dst_port_counter import PatternFlowUdpDstPortCounter
from .pattern_flow_udp_src_port_counter import PatternFlowUdpSrcPortCounter
from .pattern_flow_arp_operation_counter import PatternFlowArpOperationCounter
from .pattern_flow_gre_reserved0_counter import PatternFlowGreReserved0Counter
from .pattern_flow_gre_reserved1_counter import PatternFlowGreReserved1Counter
from .pattern_flow_gtpv1_pn_flag_counter import PatternFlowGtpv1PnFlagCounter
from .pattern_flow_gtpv1_version_counter import PatternFlowGtpv1VersionCounter
from .pattern_flow_gtpv2_version_counter import PatternFlowGtpv2VersionCounter
from .pattern_flow_igmpv1_unused_counter import PatternFlowIgmpv1UnusedCounter
from .pattern_flow_ipv4_dscp_ecn_counter import PatternFlowIpv4DscpEcnCounter
from .pattern_flow_ipv4_dscp_phb_counter import PatternFlowIpv4DscpPhbCounter
from .pattern_flow_ipv4_protocol_counter import PatternFlowIpv4ProtocolCounter
from .pattern_flow_ipv4_reserved_counter import PatternFlowIpv4ReservedCounter
from .pattern_flow_pfc_pause_dst_counter import PatternFlowPfcPauseDstCounter
from .pattern_flow_pfc_pause_src_counter import PatternFlowPfcPauseSrcCounter
from .pattern_flow_rsvp_reserved_counter import PatternFlowRsvpReservedCounter
from .pattern_flow_vlan_priority_counter import PatternFlowVlanPriorityCounter
from .pattern_flow_gtpv1_reserved_counter import PatternFlowGtpv1ReservedCounter
from .pattern_flow_icmp_echo_code_counter import PatternFlowIcmpEchoCodeCounter
from .pattern_flow_icmp_echo_type_counter import PatternFlowIcmpEchoTypeCounter
from .pattern_flow_igmpv1_version_counter import PatternFlowIgmpv1VersionCounter
from .pattern_flow_ipv4_tos_delay_counter import PatternFlowIpv4TosDelayCounter
from .pattern_flow_ipv6_hop_limit_counter import PatternFlowIpv6HopLimitCounter
from .pattern_flow_gtpv2_teid_flag_counter import PatternFlowGtpv2TeidFlagCounter
from .pattern_flow_ipv4_tos_unused_counter import PatternFlowIpv4TosUnusedCounter
from .pattern_flow_ipv6_flow_label_counter import PatternFlowIpv6FlowLabelCounter
from .pattern_flow_snmpv2c_version_counter import PatternFlowSnmpv2cVersionCounter
from .pattern_flow_tcp_data_offset_counter import PatternFlowTcpDataOffsetCounter
from .pattern_flow_vxlan_reserved0_counter import PatternFlowVxlanReserved0Counter
from .pattern_flow_vxlan_reserved1_counter import PatternFlowVxlanReserved1Counter
from .pattern_flow_icmpv6_echo_code_counter import PatternFlowIcmpv6EchoCodeCounter
from .pattern_flow_icmpv6_echo_type_counter import PatternFlowIcmpv6EchoTypeCounter
from .pattern_flow_ipv6_next_header_counter import PatternFlowIpv6NextHeaderCounter
from .pattern_flow_arp_hardware_type_counter import PatternFlowArpHardwareTypeCounter
from .pattern_flow_arp_protocol_type_counter import PatternFlowArpProtocolTypeCounter
from .pattern_flow_ipv4_priority_raw_counter import PatternFlowIpv4PriorityRawCounter
from .pattern_flow_ipv4_time_to_live_counter import PatternFlowIpv4TimeToLiveCounter
from .pattern_flow_ipv4_tos_monetary_counter import PatternFlowIpv4TosMonetaryCounter
from .pattern_flow_ipv4_total_length_counter import PatternFlowIpv4TotalLengthCounter
from .pattern_flow_mpls_time_to_live_counter import PatternFlowMplsTimeToLiveCounter
from .pattern_flow_ppp_protocol_type_counter import PatternFlowPppProtocolTypeCounter
from .pattern_flow_rsvp_time_to_live_counter import PatternFlowRsvpTimeToLiveCounter
from .flow_rsvp_session_attribute_name_length import FlowRsvpSessionAttributeNameLength
from .pattern_flow_ethernet_pause_dst_counter import PatternFlowEthernetPauseDstCounter
from .pattern_flow_ethernet_pause_src_counter import PatternFlowEthernetPauseSrcCounter
from .pattern_flow_ethernet_pfc_queue_counter import PatternFlowEthernetPfcQueueCounter
from .pattern_flow_gtpv1_message_type_counter import PatternFlowGtpv1MessageTypeCounter
from .pattern_flow_gtpv1_n_pdu_number_counter import PatternFlowGtpv1NPduNumberCounter
from .pattern_flow_gtpv2_message_type_counter import PatternFlowGtpv2MessageTypeCounter
from .pattern_flow_ipv4_dont_fragment_counter import PatternFlowIpv4DontFragmentCounter
from .pattern_flow_ipv4_header_length_counter import PatternFlowIpv4HeaderLengthCounter
from .pattern_flow_ipv6_traffic_class_counter import PatternFlowIpv6TrafficClassCounter
from .pattern_flow_mpls_traffic_class_counter import PatternFlowMplsTrafficClassCounter
from .pattern_flow_arp_hardware_length_counter import PatternFlowArpHardwareLengthCounter
from .pattern_flow_arp_protocol_length_counter import PatternFlowArpProtocolLengthCounter
from .pattern_flow_ethernet_ether_type_counter import PatternFlowEthernetEtherTypeCounter
from .pattern_flow_ethernet_pause_time_counter import PatternFlowEthernetPauseTimeCounter
from .pattern_flow_gtpv1_protocol_type_counter import PatternFlowGtpv1ProtocolTypeCounter
from .pattern_flow_ipv4_identification_counter import PatternFlowIpv4IdentificationCounter
from .pattern_flow_ipv4_more_fragments_counter import PatternFlowIpv4MoreFragmentsCounter
from .pattern_flow_ipv4_tos_precedence_counter import PatternFlowIpv4TosPrecedenceCounter
from .pattern_flow_ipv4_tos_throughput_counter import PatternFlowIpv4TosThroughputCounter
from .pattern_flow_ipv6_payload_length_counter import PatternFlowIpv6PayloadLengthCounter
from .pattern_flow_gre_checksum_present_counter import PatternFlowGreChecksumPresentCounter
from .pattern_flow_gtpv1_message_length_counter import PatternFlowGtpv1MessageLengthCounter
from .pattern_flow_gtpv1_squence_number_counter import PatternFlowGtpv1SquenceNumberCounter
from .pattern_flow_gtpv2_message_length_counter import PatternFlowGtpv2MessageLengthCounter
from .pattern_flow_icmp_echo_identifier_counter import PatternFlowIcmpEchoIdentifierCounter
from .pattern_flow_igmpv1_group_address_counter import PatternFlowIgmpv1GroupAddressCounter
from .pattern_flow_ipv4_fragment_offset_counter import PatternFlowIpv4FragmentOffsetCounter
from .pattern_flow_ipv4_tos_reliability_counter import PatternFlowIpv4TosReliabilityCounter
from .pattern_flow_mpls_bottom_of_stack_counter import PatternFlowMplsBottomOfStackCounter
from .pattern_flow_pfc_pause_ether_type_counter import PatternFlowPfcPauseEtherTypeCounter
from .pattern_flow_gtpv2_sequence_number_counter import PatternFlowGtpv2SequenceNumberCounter
from .pattern_flow_gtp_extension_contents_counter import PatternFlowGtpExtensionContentsCounter
from .pattern_flow_icmpv6_echo_identifier_counter import PatternFlowIcmpv6EchoIdentifierCounter
from .pattern_flow_pfc_pause_pause_class0_counter import PatternFlowPfcPausePauseClass0Counter
from .pattern_flow_pfc_pause_pause_class1_counter import PatternFlowPfcPausePauseClass1Counter
from .pattern_flow_pfc_pause_pause_class2_counter import PatternFlowPfcPausePauseClass2Counter
from .pattern_flow_pfc_pause_pause_class3_counter import PatternFlowPfcPausePauseClass3Counter
from .pattern_flow_pfc_pause_pause_class4_counter import PatternFlowPfcPausePauseClass4Counter
from .pattern_flow_pfc_pause_pause_class5_counter import PatternFlowPfcPausePauseClass5Counter
from .pattern_flow_pfc_pause_pause_class6_counter import PatternFlowPfcPausePauseClass6Counter
from .pattern_flow_pfc_pause_pause_class7_counter import PatternFlowPfcPausePauseClass7Counter
from .pattern_flow_gtpv2_piggybacking_flag_counter import PatternFlowGtpv2PiggybackingFlagCounter
from .pattern_flow_arp_sender_hardware_addr_counter import PatternFlowArpSenderHardwareAddrCounter
from .pattern_flow_arp_sender_protocol_addr_counter import PatternFlowArpSenderProtocolAddrCounter
from .pattern_flow_arp_target_hardware_addr_counter import PatternFlowArpTargetHardwareAddrCounter
from .pattern_flow_arp_target_protocol_addr_counter import PatternFlowArpTargetProtocolAddrCounter
from .pattern_flow_ethernet_pause_ether_type_counter import PatternFlowEthernetPauseEtherTypeCounter
from .pattern_flow_icmp_echo_sequence_number_counter import PatternFlowIcmpEchoSequenceNumberCounter
from .pattern_flow_pfc_pause_control_op_code_counter import PatternFlowPfcPauseControlOpCodeCounter
from .pattern_flow_icmpv6_echo_sequence_number_counter import PatternFlowIcmpv6EchoSequenceNumberCounter
from .pattern_flow_snmpv2c_bulk_pdu_request_id_counter import PatternFlowSnmpv2cBulkPduRequestIDCounter
from .pattern_flow_pfc_pause_class_enable_vector_counter import PatternFlowPfcPauseClassEnableVectorCounter
from .pattern_flow_rsvp_path_objects_custom_type_counter import PatternFlowRsvpPathObjectsCustomTypeCounter
from .pattern_flow_ethernet_pause_control_op_code_counter import PatternFlowEthernetPauseControlOpCodeCounter
from .pattern_flow_gtp_extension_extension_length_counter import PatternFlowGtpExtensionExtensionLengthCounter
from .pattern_flow_gtpv1_next_extension_header_type_counter import PatternFlowGtpv1NextExtensionHeaderTypeCounter
from .pattern_flow_snmpv2c_bulk_pdu_max_repetitions_counter import PatternFlowSnmpv2cBulkPduMaxRepetitionsCounter
from .pattern_flow_gtp_extension_next_extension_header_counter import PatternFlowGtpExtensionNextExtensionHeaderCounter
from .pattern_flow_ipv4_options_custom_type_copied_flag_counter import PatternFlowIpv4OptionsCustomTypeCopiedFlagCounter
from .pattern_flow_rsvp_path_rsvp_hop_ipv4_ipv4_address_counter import PatternFlowRsvpPathRsvpHopIpv4Ipv4AddressCounter
from .pattern_flow_ipv4_options_custom_type_option_class_counter import (
    PatternFlowIpv4OptionsCustomTypeOptionClassCounter,
)
from .pattern_flow_ipv4_options_custom_type_option_number_counter import (
    PatternFlowIpv4OptionsCustomTypeOptionNumberCounter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_version_counter import (
    PatternFlowRsvpPathSenderTspecIntServVersionCounter,
)
from .pattern_flow_rsvp_path_session_ext_tunnel_id_as_ipv4_counter import (
    PatternFlowRsvpPathSessionExtTunnelIDAsIpv4Counter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_zero_bit_counter import (
    PatternFlowRsvpPathSenderTspecIntServZeroBitCounter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_reserved1_counter import (
    PatternFlowRsvpPathSenderTspecIntServReserved1Counter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_reserved2_counter import (
    PatternFlowRsvpPathSenderTspecIntServReserved2Counter,
)
from .pattern_flow_rsvp_path_session_ext_tunnel_id_as_integer_counter import (
    PatternFlowRsvpPathSessionExtTunnelIDAsIntegerCounter,
)
from .pattern_flow_rsvp_path_session_lsp_tunnel_ipv4_reserved_counter import (
    PatternFlowRsvpPathSessionLspTunnelIpv4ReservedCounter,
)
from .pattern_flow_rsvp_path_session_lsp_tunnel_ipv4_tunnel_id_counter import (
    PatternFlowRsvpPathSessionLspTunnelIpv4TunnelIDCounter,
)
from .pattern_flow_rsvp_path_time_values_type1_refresh_period_r_counter import (
    PatternFlowRsvpPathTimeValuesType1RefreshPeriodRCounter,
)
from .pattern_flow_rsvp_path_explicit_route_type1_as_number_l_bit_counter import (
    PatternFlowRsvpPathExplicitRouteType1AsNumberLBitCounter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_overall_length_counter import (
    PatternFlowRsvpPathSenderTspecIntServOverallLengthCounter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_service_header_counter import (
    PatternFlowRsvpPathSenderTspecIntServServiceHeaderCounter,
)
from .pattern_flow_rsvp_path_explicit_route_type1_ipv4_prefix_l_bit_counter import (
    PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixLBitCounter,
)
from .pattern_flow_rsvp_path_rsvp_hop_ipv4_logical_interface_handle_counter import (
    PatternFlowRsvpPathRsvpHopIpv4LogicalInterfaceHandleCounter,
)
from .pattern_flow_rsvp_path_sender_template_lsp_tunnel_ipv4_lsp_id_counter import (
    PatternFlowRsvpPathSenderTemplateLspTunnelIpv4LspIDCounter,
)
from .pattern_flow_rsvp_path_label_request_without_label_range_l3pid_counter import (
    PatternFlowRsvpPathLabelRequestWithoutLabelRangeL3pidCounter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_parameter127_flag_counter import (
    PatternFlowRsvpPathSenderTspecIntServParameter127FlagCounter,
)
from .pattern_flow_rsvp_path_sender_template_lsp_tunnel_ipv4_reserved_counter import (
    PatternFlowRsvpPathSenderTemplateLspTunnelIpv4ReservedCounter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_maximum_packet_size_counter import (
    PatternFlowRsvpPathSenderTspecIntServMaximumPacketSizeCounter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_parameter127_length_counter import (
    PatternFlowRsvpPathSenderTspecIntServParameter127LengthCounter,
)
from .pattern_flow_rsvp_path_label_request_without_label_range_reserved_counter import (
    PatternFlowRsvpPathLabelRequestWithoutLabelRangeReservedCounter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_minimum_policed_unit_counter import (
    PatternFlowRsvpPathSenderTspecIntServMinimumPolicedUnitCounter,
)
from .pattern_flow_rsvp_path_record_route_type1_ipv4_address_ipv4_address_counter import (
    PatternFlowRsvpPathRecordRouteType1Ipv4AddressIpv4AddressCounter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_length_of_service_data_counter import (
    PatternFlowRsvpPathSenderTspecIntServLengthOfServiceDataCounter,
)
from .pattern_flow_rsvp_path_explicit_route_type1_ipv4_prefix_ipv4_address_counter import (
    PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixIpv4AddressCounter,
)
from .pattern_flow_rsvp_path_record_route_type1_ipv4_address_prefix_length_counter import (
    PatternFlowRsvpPathRecordRouteType1Ipv4AddressPrefixLengthCounter,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_parameter_id_token_bucket_tspec_counter import (
    PatternFlowRsvpPathSenderTspecIntServParameterIDTokenBucketTspecCounter,
)
from .pattern_flow_rsvp_path_session_lsp_tunnel_ipv4_ipv4_tunnel_end_point_address_counter import (
    PatternFlowRsvpPathSessionLspTunnelIpv4Ipv4TunnelEndPointAddressCounter,
)
from .pattern_flow_rsvp_path_sender_template_lsp_tunnel_ipv4_ipv4_tunnel_sender_address_counter import (
    PatternFlowRsvpPathSenderTemplateLspTunnelIpv4Ipv4TunnelSenderAddressCounter,
)

__all__ = [
    "FlowHeader",
    "Arp",
    "ArpHardwareLength",
    "ArpHardwareLengthMetricTag",
    "ArpHardwareType",
    "ArpHardwareTypeMetricTag",
    "ArpOperation",
    "ArpOperationMetricTag",
    "ArpProtocolLength",
    "ArpProtocolLengthMetricTag",
    "ArpProtocolType",
    "ArpProtocolTypeMetricTag",
    "ArpSenderHardwareAddr",
    "ArpSenderHardwareAddrMetricTag",
    "ArpSenderProtocolAddr",
    "ArpSenderProtocolAddrMetricTag",
    "ArpTargetHardwareAddr",
    "ArpTargetHardwareAddrMetricTag",
    "ArpTargetProtocolAddr",
    "ArpTargetProtocolAddrMetricTag",
    "Custom",
    "CustomMetricTag",
    "Ethernet",
    "EthernetDst",
    "EthernetDstMetricTag",
    "EthernetEtherType",
    "EthernetEtherTypeMetricTag",
    "EthernetPfcQueue",
    "EthernetPfcQueueMetricTag",
    "EthernetSrc",
    "EthernetSrcMetricTag",
    "Ethernetpause",
    "EthernetpauseControlOpCode",
    "EthernetpauseControlOpCodeMetricTag",
    "EthernetpauseDst",
    "EthernetpauseDstMetricTag",
    "EthernetpauseEtherType",
    "EthernetpauseEtherTypeMetricTag",
    "EthernetpauseSrc",
    "EthernetpauseSrcMetricTag",
    "EthernetpauseTime",
    "EthernetpauseTimeMetricTag",
    "Gre",
    "GreChecksum",
    "GreChecksumPresent",
    "GreChecksumPresentMetricTag",
    "GreProtocol",
    "GreProtocolMetricTag",
    "GreReserved0",
    "GreReserved0MetricTag",
    "GreReserved1",
    "GreReserved1MetricTag",
    "GreVersion",
    "GreVersionMetricTag",
    "Gtpv1",
    "Gtpv1EFlag",
    "Gtpv1EFlagMetricTag",
    "Gtpv1ExtensionHeader",
    "Gtpv1ExtensionHeaderContents",
    "Gtpv1ExtensionHeaderContentsMetricTag",
    "Gtpv1ExtensionHeaderExtensionLength",
    "Gtpv1ExtensionHeaderExtensionLengthMetricTag",
    "Gtpv1ExtensionHeaderNextExtensionHeader",
    "Gtpv1ExtensionHeaderNextExtensionHeaderMetricTag",
    "Gtpv1MessageLength",
    "Gtpv1MessageLengthMetricTag",
    "Gtpv1MessageType",
    "Gtpv1MessageTypeMetricTag",
    "Gtpv1NPduNumber",
    "Gtpv1NPduNumberMetricTag",
    "Gtpv1NextExtensionHeaderType",
    "Gtpv1NextExtensionHeaderTypeMetricTag",
    "Gtpv1PnFlag",
    "Gtpv1PnFlagMetricTag",
    "Gtpv1ProtocolType",
    "Gtpv1ProtocolTypeMetricTag",
    "Gtpv1Reserved",
    "Gtpv1ReservedMetricTag",
    "Gtpv1SFlag",
    "Gtpv1SFlagMetricTag",
    "Gtpv1SquenceNumber",
    "Gtpv1SquenceNumberMetricTag",
    "Gtpv1Teid",
    "Gtpv1TeidMetricTag",
    "Gtpv1Version",
    "Gtpv1VersionMetricTag",
    "Gtpv2",
    "Gtpv2MessageLength",
    "Gtpv2MessageLengthMetricTag",
    "Gtpv2MessageType",
    "Gtpv2MessageTypeMetricTag",
    "Gtpv2PiggybackingFlag",
    "Gtpv2PiggybackingFlagMetricTag",
    "Gtpv2SequenceNumber",
    "Gtpv2SequenceNumberMetricTag",
    "Gtpv2Spare1",
    "Gtpv2Spare1MetricTag",
    "Gtpv2Spare2",
    "Gtpv2Spare2MetricTag",
    "Gtpv2Teid",
    "Gtpv2TeidMetricTag",
    "Gtpv2TeidFlag",
    "Gtpv2TeidFlagMetricTag",
    "Gtpv2Version",
    "Gtpv2VersionMetricTag",
    "Icmp",
    "IcmpEcho",
    "IcmpEchoChecksum",
    "IcmpEchoCode",
    "IcmpEchoCodeMetricTag",
    "IcmpEchoIdentifier",
    "IcmpEchoIdentifierMetricTag",
    "IcmpEchoSequenceNumber",
    "IcmpEchoSequenceNumberMetricTag",
    "IcmpEchoType",
    "IcmpEchoTypeMetricTag",
    "Icmpv6",
    "Icmpv6Echo",
    "Icmpv6EchoChecksum",
    "Icmpv6EchoCode",
    "Icmpv6EchoCodeMetricTag",
    "Icmpv6EchoIdentifier",
    "Icmpv6EchoIdentifierMetricTag",
    "Icmpv6EchoSequenceNumber",
    "Icmpv6EchoSequenceNumberMetricTag",
    "Icmpv6EchoType",
    "Icmpv6EchoTypeMetricTag",
    "Igmpv1",
    "Igmpv1Checksum",
    "Igmpv1GroupAddress",
    "Igmpv1GroupAddressMetricTag",
    "Igmpv1Type",
    "Igmpv1TypeMetricTag",
    "Igmpv1Unused",
    "Igmpv1UnusedMetricTag",
    "Igmpv1Version",
    "Igmpv1VersionMetricTag",
    "Ipv4",
    "Ipv4DontFragment",
    "Ipv4DontFragmentMetricTag",
    "Ipv4Dst",
    "Ipv4DstMetricTag",
    "Ipv4DstRandom",
    "Ipv4FragmentOffset",
    "Ipv4FragmentOffsetMetricTag",
    "Ipv4HeaderChecksum",
    "Ipv4HeaderLength",
    "Ipv4HeaderLengthMetricTag",
    "Ipv4Identification",
    "Ipv4IdentificationMetricTag",
    "Ipv4MoreFragments",
    "Ipv4MoreFragmentsMetricTag",
    "Ipv4Option",
    "Ipv4OptionCustom",
    "Ipv4OptionCustomLength",
    "Ipv4OptionCustomType",
    "Ipv4OptionCustomTypeCopiedFlag",
    "Ipv4OptionCustomTypeOptionClass",
    "Ipv4OptionCustomTypeOptionNumber",
    "Ipv4Priority",
    "Ipv4PriorityDscp",
    "Ipv4PriorityDscpEcn",
    "Ipv4PriorityDscpEcnMetricTag",
    "Ipv4PriorityDscpPhb",
    "Ipv4PriorityDscpPhbMetricTag",
    "Ipv4PriorityRaw",
    "Ipv4PriorityRawMetricTag",
    "Ipv4PriorityTos",
    "Ipv4PriorityTosDelay",
    "Ipv4PriorityTosDelayMetricTag",
    "Ipv4PriorityTosMonetary",
    "Ipv4PriorityTosMonetaryMetricTag",
    "Ipv4PriorityTosPrecedence",
    "Ipv4PriorityTosPrecedenceMetricTag",
    "Ipv4PriorityTosReliability",
    "Ipv4PriorityTosReliabilityMetricTag",
    "Ipv4PriorityTosThroughput",
    "Ipv4PriorityTosThroughputMetricTag",
    "Ipv4PriorityTosUnused",
    "Ipv4PriorityTosUnusedMetricTag",
    "Ipv4Protocol",
    "Ipv4ProtocolMetricTag",
    "Ipv4Reserved",
    "Ipv4ReservedMetricTag",
    "Ipv4Src",
    "Ipv4SrcMetricTag",
    "Ipv4SrcRandom",
    "Ipv4TimeToLive",
    "Ipv4TimeToLiveMetricTag",
    "Ipv4TotalLength",
    "Ipv4TotalLengthMetricTag",
    "Ipv4Version",
    "Ipv4VersionMetricTag",
    "Ipv6",
    "Ipv6Dst",
    "Ipv6DstMetricTag",
    "Ipv6FlowLabel",
    "Ipv6FlowLabelMetricTag",
    "Ipv6FlowLabelRandom",
    "Ipv6HopLimit",
    "Ipv6HopLimitMetricTag",
    "Ipv6NextHeader",
    "Ipv6NextHeaderMetricTag",
    "Ipv6PayloadLength",
    "Ipv6PayloadLengthMetricTag",
    "Ipv6Src",
    "Ipv6SrcMetricTag",
    "Ipv6TrafficClass",
    "Ipv6TrafficClassMetricTag",
    "Ipv6Version",
    "Ipv6VersionMetricTag",
    "Macsec",
    "Mpls",
    "MplsBottomOfStack",
    "MplsBottomOfStackMetricTag",
    "MplsLabel",
    "MplsLabelMetricTag",
    "MplsTimeToLive",
    "MplsTimeToLiveMetricTag",
    "MplsTrafficClass",
    "MplsTrafficClassMetricTag",
    "Pfcpause",
    "PfcpauseClassEnableVector",
    "PfcpauseClassEnableVectorMetricTag",
    "PfcpauseControlOpCode",
    "PfcpauseControlOpCodeMetricTag",
    "PfcpauseDst",
    "PfcpauseDstMetricTag",
    "PfcpauseEtherType",
    "PfcpauseEtherTypeMetricTag",
    "PfcpausePauseClass0",
    "PfcpausePauseClass0MetricTag",
    "PfcpausePauseClass1",
    "PfcpausePauseClass1MetricTag",
    "PfcpausePauseClass2",
    "PfcpausePauseClass2MetricTag",
    "PfcpausePauseClass3",
    "PfcpausePauseClass3MetricTag",
    "PfcpausePauseClass4",
    "PfcpausePauseClass4MetricTag",
    "PfcpausePauseClass5",
    "PfcpausePauseClass5MetricTag",
    "PfcpausePauseClass6",
    "PfcpausePauseClass6MetricTag",
    "PfcpausePauseClass7",
    "PfcpausePauseClass7MetricTag",
    "PfcpauseSrc",
    "PfcpauseSrcMetricTag",
    "Ppp",
    "PppAddress",
    "PppAddressMetricTag",
    "PppControl",
    "PppControlMetricTag",
    "PppProtocolType",
    "PppProtocolTypeMetricTag",
    "Rsvp",
    "RsvpMessageType",
    "RsvpMessageTypePath",
    "RsvpMessageTypePathObject",
    "RsvpMessageTypePathObjectClassNum",
    "RsvpMessageTypePathObjectClassNumCustom",
    "RsvpMessageTypePathObjectClassNumCustomType",
    "RsvpMessageTypePathObjectClassNumExplicitRoute",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCType",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1Subobject",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectType",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumber",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumberLBit",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumberLength",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4Prefix",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixIpv4Address",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixLBit",
    "RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixLength",
    "RsvpMessageTypePathObjectClassNumLabelRequest",
    "RsvpMessageTypePathObjectClassNumLabelRequestCType",
    "RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRange",
    "RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRangeL3pid",
    "RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRangeReserved",
    "RsvpMessageTypePathObjectClassNumRecordRoute",
    "RsvpMessageTypePathObjectClassNumRecordRouteCType",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1Subobject",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectType",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4Address",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressFlags",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressIpv4Address",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressPrefixLength",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabel",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelCType",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelFlags",
    "RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelLabel",
    "RsvpMessageTypePathObjectClassNumRsvpHop",
    "RsvpMessageTypePathObjectClassNumRsvpHopCType",
    "RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4",
    "RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4Ipv4Address",
    "RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4LogicalInterfaceHandle",
    "RsvpMessageTypePathObjectClassNumSenderTemplate",
    "RsvpMessageTypePathObjectClassNumSenderTemplateCType",
    "RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4",
    "RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4Ipv4TunnelSenderAddress",
    "RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4LspID",
    "RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4Reserved",
    "RsvpMessageTypePathObjectClassNumSenderTspec",
    "RsvpMessageTypePathObjectClassNumSenderTspecCType",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServ",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServLengthOfServiceData",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServMaximumPacketSize",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServMinimumPolicedUnit",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServOverallLength",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameter127Flag",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameter127Length",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameterIDTokenBucketTspec",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServReserved1",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServReserved2",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServServiceHeader",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServVersion",
    "RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServZeroBit",
    "RsvpMessageTypePathObjectClassNumSession",
    "RsvpMessageTypePathObjectClassNumSessionCType",
    "RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4",
    "RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelID",
    "RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelIDAsInteger",
    "RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelIDAsIpv4",
    "RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4Ipv4TunnelEndPointAddress",
    "RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4Reserved",
    "RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4TunnelID",
    "RsvpMessageTypePathObjectClassNumSessionAttribute",
    "RsvpMessageTypePathObjectClassNumSessionAttributeCType",
    "RsvpMessageTypePathObjectClassNumSessionAttributeCTypeLspTunnel",
    "RsvpMessageTypePathObjectClassNumSessionAttributeCTypeLspTunnelRa",
    "RsvpMessageTypePathObjectClassNumTimeValues",
    "RsvpMessageTypePathObjectClassNumTimeValuesCType",
    "RsvpMessageTypePathObjectClassNumTimeValuesCTypeType1",
    "RsvpMessageTypePathObjectClassNumTimeValuesCTypeType1RefreshPeriodR",
    "RsvpReserved",
    "RsvpRsvpChecksum",
    "RsvpRsvpLength",
    "RsvpTimeToLive",
    "Snmpv2c",
    "Snmpv2cData",
    "Snmpv2cDataGetBulkRequest",
    "Snmpv2cDataGetBulkRequestMaxRepetitions",
    "Snmpv2cDataGetBulkRequestNonRepeaters",
    "Snmpv2cDataGetBulkRequestRequestID",
    "Snmpv2cVersion",
    "Tcp",
    "TcpAckNum",
    "TcpAckNumMetricTag",
    "TcpChecksum",
    "TcpCtlAck",
    "TcpCtlAckMetricTag",
    "TcpCtlFin",
    "TcpCtlFinMetricTag",
    "TcpCtlPsh",
    "TcpCtlPshMetricTag",
    "TcpCtlRst",
    "TcpCtlRstMetricTag",
    "TcpCtlSyn",
    "TcpCtlSynMetricTag",
    "TcpCtlUrg",
    "TcpCtlUrgMetricTag",
    "TcpDataOffset",
    "TcpDataOffsetMetricTag",
    "TcpDstPort",
    "TcpDstPortMetricTag",
    "TcpDstPortRandom",
    "TcpEcnCwr",
    "TcpEcnCwrMetricTag",
    "TcpEcnEcho",
    "TcpEcnEchoMetricTag",
    "TcpEcnNs",
    "TcpEcnNsMetricTag",
    "TcpSeqNum",
    "TcpSeqNumMetricTag",
    "TcpSrcPort",
    "TcpSrcPortMetricTag",
    "TcpSrcPortRandom",
    "TcpWindow",
    "TcpWindowMetricTag",
    "Udp",
    "UdpChecksum",
    "UdpDstPort",
    "UdpDstPortMetricTag",
    "UdpDstPortRandom",
    "UdpLength",
    "UdpLengthMetricTag",
    "UdpSrcPort",
    "UdpSrcPortMetricTag",
    "UdpSrcPortRandom",
    "Vlan",
    "VlanID",
    "VlanIDMetricTag",
    "VlanCfi",
    "VlanCfiMetricTag",
    "VlanPriority",
    "VlanPriorityMetricTag",
    "VlanTpid",
    "VlanTpidMetricTag",
    "Vxlan",
    "VxlanFlags",
    "VxlanFlagsMetricTag",
    "VxlanReserved0",
    "VxlanReserved0MetricTag",
    "VxlanReserved1",
    "VxlanReserved1MetricTag",
    "VxlanVni",
    "VxlanVniMetricTag",
]


class ArpHardwareLengthMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class ArpHardwareLength(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowArpHardwareLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowArpHardwareLengthCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[ArpHardwareLengthMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class ArpHardwareTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class ArpHardwareType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowArpHardwareTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowArpHardwareTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[ArpHardwareTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class ArpOperationMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class ArpOperation(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowArpOperationCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowArpOperationCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[ArpOperationMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class ArpProtocolLengthMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class ArpProtocolLength(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowArpProtocolLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowArpProtocolLengthCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[ArpProtocolLengthMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class ArpProtocolTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class ArpProtocolType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowArpProtocolTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowArpProtocolTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[ArpProtocolTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class ArpSenderHardwareAddrMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class ArpSenderHardwareAddr(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowArpSenderHardwareAddrCounter] = None
    """mac counter pattern"""

    increment: Optional[PatternFlowArpSenderHardwareAddrCounter] = None
    """mac counter pattern"""

    metric_tags: Optional[List[ArpSenderHardwareAddrMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class ArpSenderProtocolAddrMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class ArpSenderProtocolAddr(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowArpSenderProtocolAddrCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowArpSenderProtocolAddrCounter] = None
    """ipv4 counter pattern"""

    metric_tags: Optional[List[ArpSenderProtocolAddrMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class ArpTargetHardwareAddrMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class ArpTargetHardwareAddr(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowArpTargetHardwareAddrCounter] = None
    """mac counter pattern"""

    increment: Optional[PatternFlowArpTargetHardwareAddrCounter] = None
    """mac counter pattern"""

    metric_tags: Optional[List[ArpTargetHardwareAddrMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class ArpTargetProtocolAddrMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class ArpTargetProtocolAddr(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowArpTargetProtocolAddrCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowArpTargetProtocolAddrCounter] = None
    """ipv4 counter pattern"""

    metric_tags: Optional[List[ArpTargetProtocolAddrMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class Arp(BaseModel):
    hardware_length: Optional[ArpHardwareLength] = None
    """Length (in octets) of a hardware address"""

    hardware_type: Optional[ArpHardwareType] = None
    """Network link protocol type"""

    operation: Optional[ArpOperation] = None
    """The operation that the sender is performing"""

    protocol_length: Optional[ArpProtocolLength] = None
    """Length (in octets) of internetwork addresses"""

    protocol_type: Optional[ArpProtocolType] = None
    """The internetwork protocol for which the ARP request is intended"""

    sender_hardware_addr: Optional[ArpSenderHardwareAddr] = None
    """Media address of the sender"""

    sender_protocol_addr: Optional[ArpSenderProtocolAddr] = None
    """Internetwork address of the sender"""

    target_hardware_addr: Optional[ArpTargetHardwareAddr] = None
    """Media address of the target"""

    target_protocol_addr: Optional[ArpTargetProtocolAddr] = None
    """Internetwork address of the target"""


class CustomMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Custom(BaseModel):
    bytes: str
    """A custom packet header defined as a string of hex bytes.

    The string MUST contain sequence of valid hex bytes. Spaces or colons can be
    part of the bytes but will be discarded. This packet header can be used in
    multiple places in the packet.
    """

    metric_tags: Optional[List[CustomMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """


class EthernetDstMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class EthernetDst(BaseModel):
    auto: Optional[str] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowEthernetDstCounter] = None
    """mac counter pattern"""

    increment: Optional[PatternFlowEthernetDstCounter] = None
    """mac counter pattern"""

    metric_tags: Optional[List[EthernetDstMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class EthernetEtherTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class EthernetEtherType(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowEthernetEtherTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowEthernetEtherTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[EthernetEtherTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class EthernetPfcQueueMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class EthernetPfcQueue(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowEthernetPfcQueueCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowEthernetPfcQueueCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[EthernetPfcQueueMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class EthernetSrcMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class EthernetSrc(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowEthernetSrcCounter] = None
    """mac counter pattern"""

    increment: Optional[PatternFlowEthernetSrcCounter] = None
    """mac counter pattern"""

    metric_tags: Optional[List[EthernetSrcMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class Ethernet(BaseModel):
    dst: Optional[EthernetDst] = None
    """Destination MAC address"""

    ether_type: Optional[EthernetEtherType] = None
    """Ethernet type"""

    pfc_queue: Optional[EthernetPfcQueue] = None
    """Priority flow control queue"""

    src: Optional[EthernetSrc] = None
    """Source MAC address"""


class EthernetpauseControlOpCodeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class EthernetpauseControlOpCode(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowEthernetPauseControlOpCodeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowEthernetPauseControlOpCodeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[EthernetpauseControlOpCodeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class EthernetpauseDstMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class EthernetpauseDst(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowEthernetPauseDstCounter] = None
    """mac counter pattern"""

    increment: Optional[PatternFlowEthernetPauseDstCounter] = None
    """mac counter pattern"""

    metric_tags: Optional[List[EthernetpauseDstMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class EthernetpauseEtherTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class EthernetpauseEtherType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowEthernetPauseEtherTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowEthernetPauseEtherTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[EthernetpauseEtherTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class EthernetpauseSrcMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class EthernetpauseSrc(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowEthernetPauseSrcCounter] = None
    """mac counter pattern"""

    increment: Optional[PatternFlowEthernetPauseSrcCounter] = None
    """mac counter pattern"""

    metric_tags: Optional[List[EthernetpauseSrcMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class EthernetpauseTimeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class EthernetpauseTime(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowEthernetPauseTimeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowEthernetPauseTimeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[EthernetpauseTimeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ethernetpause(BaseModel):
    control_op_code: Optional[EthernetpauseControlOpCode] = None
    """Control operation code"""

    dst: Optional[EthernetpauseDst] = None
    """Destination MAC address"""

    ether_type: Optional[EthernetpauseEtherType] = None
    """Ethernet type"""

    src: Optional[EthernetpauseSrc] = None
    """Source MAC address"""

    time: Optional[EthernetpauseTime] = None
    """Time"""


class GreChecksum(BaseModel):
    choice: Optional[Literal["generated", "custom"]] = None
    """The type of checksum"""

    custom: Optional[int] = None
    """A custom checksum value"""

    generated: Optional[Literal["good", "bad"]] = None
    """A system generated checksum value"""


class GreChecksumPresentMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class GreChecksumPresent(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGreChecksumPresentCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGreChecksumPresentCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[GreChecksumPresentMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class GreProtocolMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class GreProtocol(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "increment", "decrement", "auto"]] = None

    decrement: Optional[PatternFlowGreProtocolCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGreProtocolCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[GreProtocolMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class GreReserved0MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class GreReserved0(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGreReserved0Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGreReserved0Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[GreReserved0MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class GreReserved1MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class GreReserved1(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGreReserved1Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGreReserved1Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[GreReserved1MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class GreVersionMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class GreVersion(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGreVersionCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGreVersionCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[GreVersionMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gre(BaseModel):
    checksum: Optional[GreChecksum] = None
    """Optional checksum of GRE header and payload.

    Only present if the checksum_present bit is set.
    """

    checksum_present: Optional[GreChecksumPresent] = None
    """Checksum present bit"""

    protocol: Optional[GreProtocol] = None
    """Protocol type of encapsulated payload"""

    reserved0: Optional[GreReserved0] = None
    """Reserved bits"""

    reserved1: Optional[GreReserved1] = None
    """Optional reserved field. Only present if the checksum_present bit is set."""

    version: Optional[GreVersion] = None
    """GRE version number"""


class Gtpv1EFlagMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1EFlag(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1EFlagCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1EFlagCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1EFlagMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1ExtensionHeaderContentsMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1ExtensionHeaderContents(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpExtensionContentsCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpExtensionContentsCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1ExtensionHeaderContentsMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1ExtensionHeaderExtensionLengthMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1ExtensionHeaderExtensionLength(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpExtensionExtensionLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpExtensionExtensionLengthCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1ExtensionHeaderExtensionLengthMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1ExtensionHeaderNextExtensionHeaderMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1ExtensionHeaderNextExtensionHeader(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpExtensionNextExtensionHeaderCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpExtensionNextExtensionHeaderCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1ExtensionHeaderNextExtensionHeaderMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1ExtensionHeader(BaseModel):
    contents: Optional[Gtpv1ExtensionHeaderContents] = None
    """The extension header contents"""

    extension_length: Optional[Gtpv1ExtensionHeaderExtensionLength] = None
    """
    This field states the length of this extension header, including the length, the
    contents, and the next extension header field, in 4-octet units, so the length
    of the extension must always be a multiple of 4.
    """

    next_extension_header: Optional[Gtpv1ExtensionHeaderNextExtensionHeader] = None
    """It states the type of the next extension, or 0 if no next extension exists.

    This permits chaining several next extension headers.
    """


class Gtpv1MessageLengthMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1MessageLength(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1MessageLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1MessageLengthCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1MessageLengthMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1MessageTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1MessageType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1MessageTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1MessageTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1MessageTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1NPduNumberMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1NPduNumber(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1NPduNumberCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1NPduNumberCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1NPduNumberMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1NextExtensionHeaderTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1NextExtensionHeaderType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1NextExtensionHeaderTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1NextExtensionHeaderTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1NextExtensionHeaderTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1PnFlagMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1PnFlag(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1PnFlagCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1PnFlagCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1PnFlagMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1ProtocolTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1ProtocolType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1ProtocolTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1ProtocolTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1ProtocolTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1ReservedMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1Reserved(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1ReservedCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1ReservedCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1ReservedMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1SFlagMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1SFlag(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1SFlagCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1SFlagCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1SFlagMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1SquenceNumberMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1SquenceNumber(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1SquenceNumberCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1SquenceNumberCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1SquenceNumberMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1TeidMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1Teid(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1TeidCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1TeidCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1TeidMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1VersionMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1Version(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv1VersionCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv1VersionCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv1VersionMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv1(BaseModel):
    e_flag: Optional[Gtpv1EFlag] = None
    """Extension header field present"""

    extension_headers: Optional[List[Gtpv1ExtensionHeader]] = None
    """A list of optional extension headers."""

    message_length: Optional[Gtpv1MessageLength] = None
    """
    The length of the payload (the bytes following the mandatory 8-byte GTP header)
    in bytes that includes any optional fields
    """

    message_type: Optional[Gtpv1MessageType] = None
    """
    The type of GTP message Different types of messages are defined in 3GPP TS
    29.060 section 7.1
    """

    n_pdu_number: Optional[Gtpv1NPduNumber] = None
    """N-PDU number.

    Exists if any of the e_flag, s_flag, or pn_flag bits are on. Must be interpreted
    only if the pn_flag bit is on.
    """

    next_extension_header_type: Optional[Gtpv1NextExtensionHeaderType] = None
    """Next extension header.

    Exists if any of the e_flag, s_flag, or pn_flag bits are on. Must be interpreted
    only if the e_flag bit is on.
    """

    pn_flag: Optional[Gtpv1PnFlag] = None
    """N-PDU field present"""

    protocol_type: Optional[Gtpv1ProtocolType] = None
    """Protocol type, GTP is 1, GTP' is 0"""

    reserved: Optional[Gtpv1Reserved] = None
    """Reserved field"""

    s_flag: Optional[Gtpv1SFlag] = None
    """Sequence number field present"""

    squence_number: Optional[Gtpv1SquenceNumber] = None
    """Sequence number.

    Exists if any of the e_flag, s_flag, or pn_flag bits are on. Must be interpreted
    only if the s_flag bit is on.
    """

    teid: Optional[Gtpv1Teid] = None
    """
    Tunnel endpoint identifier (TEID) used to multiplex connections in the same GTP
    tunnel
    """

    version: Optional[Gtpv1Version] = None
    """GTPv1 version"""


class Gtpv2MessageLengthMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2MessageLength(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv2MessageLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv2MessageLengthCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv2MessageLengthMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv2MessageTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2MessageType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv2MessageTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv2MessageTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv2MessageTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv2PiggybackingFlagMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2PiggybackingFlag(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv2PiggybackingFlagCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv2PiggybackingFlagCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv2PiggybackingFlagMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv2SequenceNumberMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2SequenceNumber(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv2SequenceNumberCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv2SequenceNumberCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv2SequenceNumberMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv2Spare1MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2Spare1(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv2Spare1Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv2Spare1Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv2Spare1MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv2Spare2MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2Spare2(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv2Spare2Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv2Spare2Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv2Spare2MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv2TeidMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2Teid(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv2TeidCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv2TeidCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv2TeidMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv2TeidFlagMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2TeidFlag(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv2TeidFlagCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv2TeidFlagCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv2TeidFlagMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv2VersionMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2Version(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowGtpv2VersionCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowGtpv2VersionCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Gtpv2VersionMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Gtpv2(BaseModel):
    message_length: Optional[Gtpv2MessageLength] = None
    """
    A 16-bit field that indicates the length of the payload in bytes, excluding the
    mandatory GTP-c header (first 4 bytes). Includes the TEID and sequence_number if
    they are present.
    """

    message_type: Optional[Gtpv2MessageType] = None
    """An 8-bit field that indicates the type of GTP message.

    Different types of messages are defined in 3GPP TS 29.060 section 7.1
    """

    piggybacking_flag: Optional[Gtpv2PiggybackingFlag] = None
    """
    If piggybacking_flag is set to 1 then another GTP-C message with its own header
    shall be present at the end of the current message
    """

    sequence_number: Optional[Gtpv2SequenceNumber] = None
    """The sequence number"""

    spare1: Optional[Gtpv2Spare1] = None
    """A 3-bit reserved field (must be 0)."""

    spare2: Optional[Gtpv2Spare2] = None
    """Reserved field"""

    teid: Optional[Gtpv2Teid] = None
    """Tunnel endpoint identifier.

    A 32-bit (4-octet) field used to multiplex different connections in the same GTP
    tunnel. Is present only if the teid_flag is set.
    """

    teid_flag: Optional[Gtpv2TeidFlag] = None
    """
    If teid_flag is set to 1 then the TEID field will be present between the message
    length and the sequence number. All messages except Echo and Echo reply require
    TEID to be present
    """

    version: Optional[Gtpv2Version] = None
    """Version number"""


class IcmpEchoChecksum(BaseModel):
    choice: Optional[Literal["generated", "custom"]] = None
    """The type of checksum"""

    custom: Optional[int] = None
    """A custom checksum value"""

    generated: Optional[Literal["good", "bad"]] = None
    """A system generated checksum value"""


class IcmpEchoCodeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class IcmpEchoCode(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIcmpEchoCodeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIcmpEchoCodeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[IcmpEchoCodeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class IcmpEchoIdentifierMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class IcmpEchoIdentifier(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIcmpEchoIdentifierCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIcmpEchoIdentifierCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[IcmpEchoIdentifierMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class IcmpEchoSequenceNumberMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class IcmpEchoSequenceNumber(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIcmpEchoSequenceNumberCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIcmpEchoSequenceNumberCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[IcmpEchoSequenceNumberMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class IcmpEchoTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class IcmpEchoType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIcmpEchoTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIcmpEchoTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[IcmpEchoTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class IcmpEcho(BaseModel):
    checksum: Optional[IcmpEchoChecksum] = None
    """ICMP checksum"""

    code: Optional[IcmpEchoCode] = None
    """The ICMP subtype. The default code for ICMP echo request and reply is 0."""

    identifier: Optional[IcmpEchoIdentifier] = None
    """ICMP identifier"""

    sequence_number: Optional[IcmpEchoSequenceNumber] = None
    """ICMP sequence number"""

    type: Optional[IcmpEchoType] = None
    """The type of ICMP echo packet"""


class Icmp(BaseModel):
    choice: Optional[Literal["echo"]] = None

    echo: Optional[IcmpEcho] = None
    """Packet Header for ICMP echo request"""


class Icmpv6EchoChecksum(BaseModel):
    choice: Optional[Literal["generated", "custom"]] = None
    """The type of checksum"""

    custom: Optional[int] = None
    """A custom checksum value"""

    generated: Optional[Literal["good", "bad"]] = None
    """A system generated checksum value"""


class Icmpv6EchoCodeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Icmpv6EchoCode(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIcmpv6EchoCodeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIcmpv6EchoCodeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Icmpv6EchoCodeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Icmpv6EchoIdentifierMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Icmpv6EchoIdentifier(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIcmpv6EchoIdentifierCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIcmpv6EchoIdentifierCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Icmpv6EchoIdentifierMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Icmpv6EchoSequenceNumberMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Icmpv6EchoSequenceNumber(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIcmpv6EchoSequenceNumberCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIcmpv6EchoSequenceNumberCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Icmpv6EchoSequenceNumberMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Icmpv6EchoTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Icmpv6EchoType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIcmpv6EchoTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIcmpv6EchoTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Icmpv6EchoTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Icmpv6Echo(BaseModel):
    checksum: Optional[Icmpv6EchoChecksum] = None
    """ICMPv6 checksum"""

    code: Optional[Icmpv6EchoCode] = None
    """ICMPv6 echo sub type"""

    identifier: Optional[Icmpv6EchoIdentifier] = None
    """ICMPv6 echo identifier"""

    sequence_number: Optional[Icmpv6EchoSequenceNumber] = None
    """ICMPv6 echo sequence number"""

    type: Optional[Icmpv6EchoType] = None
    """ICMPv6 echo type"""


class Icmpv6(BaseModel):
    choice: Optional[Literal["echo"]] = None

    echo: Optional[Icmpv6Echo] = None
    """Packet Header for ICMPv6 Echo"""


class Igmpv1Checksum(BaseModel):
    choice: Optional[Literal["generated", "custom"]] = None
    """The type of checksum"""

    custom: Optional[int] = None
    """A custom checksum value"""

    generated: Optional[Literal["good", "bad"]] = None
    """A system generated checksum value"""


class Igmpv1GroupAddressMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Igmpv1GroupAddress(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIgmpv1GroupAddressCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowIgmpv1GroupAddressCounter] = None
    """ipv4 counter pattern"""

    metric_tags: Optional[List[Igmpv1GroupAddressMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class Igmpv1TypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Igmpv1Type(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIgmpv1TypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIgmpv1TypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Igmpv1TypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Igmpv1UnusedMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Igmpv1Unused(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIgmpv1UnusedCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIgmpv1UnusedCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Igmpv1UnusedMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Igmpv1VersionMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Igmpv1Version(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIgmpv1VersionCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIgmpv1VersionCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Igmpv1VersionMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Igmpv1(BaseModel):
    checksum: Optional[Igmpv1Checksum] = None
    """Checksum"""

    group_address: Optional[Igmpv1GroupAddress] = None
    """Group address"""

    type: Optional[Igmpv1Type] = None
    """Type of message"""

    unused: Optional[Igmpv1Unused] = None
    """Unused"""

    version: Optional[Igmpv1Version] = None
    """Version number"""


class Ipv4DontFragmentMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4DontFragment(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4DontFragmentCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4DontFragmentCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4DontFragmentMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4DstMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4DstRandom(BaseModel):
    count: Optional[int] = None
    """The total number of values to be generated by the random value generator."""

    max: Optional[str] = None
    """The maximum possible value generated by the random value generator."""

    min: Optional[str] = None
    """The minimum possible value generated by the random value generator."""

    seed: Optional[int] = None
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class Ipv4Dst(BaseModel):
    auto: Optional[FlowIpv4Auto] = None
    """The OTG implementation can provide a system generated, value for this property."""

    choice: Optional[Literal["value", "values", "increment", "decrement", "auto", "random"]] = None

    decrement: Optional[PatternFlowIpv4DstCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowIpv4DstCounter] = None
    """ipv4 counter pattern"""

    metric_tags: Optional[List[Ipv4DstMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: Optional[Ipv4DstRandom] = None
    """ipv4 random pattern"""

    value: Optional[str] = None

    values: Optional[List[str]] = None


class Ipv4FragmentOffsetMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4FragmentOffset(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4FragmentOffsetCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4FragmentOffsetCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4FragmentOffsetMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4HeaderChecksum(BaseModel):
    choice: Optional[Literal["generated", "custom"]] = None
    """The type of checksum"""

    custom: Optional[int] = None
    """A custom checksum value"""

    generated: Optional[Literal["good", "bad"]] = None
    """A system generated checksum value"""


class Ipv4HeaderLengthMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4HeaderLength(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4HeaderLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4HeaderLengthCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4HeaderLengthMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4IdentificationMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4Identification(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4IdentificationCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4IdentificationCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4IdentificationMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4MoreFragmentsMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4MoreFragments(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4MoreFragmentsCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4MoreFragmentsCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4MoreFragmentsMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4OptionCustomLength(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["auto", "value"]] = None
    """auto or configured value."""

    value: Optional[int] = None


class Ipv4OptionCustomTypeCopiedFlag(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4OptionsCustomTypeCopiedFlagCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4OptionsCustomTypeCopiedFlagCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4OptionCustomTypeOptionClass(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4OptionsCustomTypeOptionClassCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4OptionsCustomTypeOptionClassCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4OptionCustomTypeOptionNumber(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4OptionsCustomTypeOptionNumberCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4OptionsCustomTypeOptionNumberCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4OptionCustomType(BaseModel):
    copied_flag: Optional[Ipv4OptionCustomTypeCopiedFlag] = None
    """This flag indicates this option is copied to all fragments on fragmentations."""

    option_class: Optional[Ipv4OptionCustomTypeOptionClass] = None
    """
    Option class
    [Ref:https://www.iana.org/assignments/ip-parameters/ip-parameters.xhtml#ip-parameters-1].
    """

    option_number: Optional[Ipv4OptionCustomTypeOptionNumber] = None
    """
    Option Number
    [Ref:https://www.iana.org/assignments/ip-parameters/ip-parameters.xhtml#ip-parameters-1].
    """


class Ipv4OptionCustom(BaseModel):
    length: Optional[Ipv4OptionCustomLength] = None
    """Length for custom options."""

    type: Optional[Ipv4OptionCustomType] = None
    """Type options for custom options."""

    value: Optional[str] = None
    """
    Value of the option field should not excced 38 bytes since maximum 40 bytes can
    be added as options in IPv4 header. For type and length requires 2 bytes, hence
    maximum of 38 bytes are expected. Maximum length of this attribute is 76 (38 \\**
    2 hex character per byte).
    """


class Ipv4Option(BaseModel):
    choice: Optional[Literal["router_alert", "custom"]] = None

    custom: Optional[Ipv4OptionCustom] = None
    """User defined IP options to be appended to the IPv4 header."""


class Ipv4PriorityDscpEcnMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityDscpEcn(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4DscpEcnCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4DscpEcnCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4PriorityDscpEcnMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4PriorityDscpPhbMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityDscpPhb(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4DscpPhbCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4DscpPhbCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4PriorityDscpPhbMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4PriorityDscp(BaseModel):
    ecn: Optional[Ipv4PriorityDscpEcn] = None
    """Explicit congestion notification"""

    phb: Optional[Ipv4PriorityDscpPhb] = None
    """Per hop behavior"""


class Ipv4PriorityRawMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityRaw(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4PriorityRawCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4PriorityRawCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4PriorityRawMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4PriorityTosDelayMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosDelay(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4TosDelayCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4TosDelayCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4PriorityTosDelayMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4PriorityTosMonetaryMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosMonetary(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4TosMonetaryCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4TosMonetaryCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4PriorityTosMonetaryMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4PriorityTosPrecedenceMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosPrecedence(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4TosPrecedenceCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4TosPrecedenceCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4PriorityTosPrecedenceMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4PriorityTosReliabilityMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosReliability(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4TosReliabilityCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4TosReliabilityCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4PriorityTosReliabilityMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4PriorityTosThroughputMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosThroughput(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4TosThroughputCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4TosThroughputCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4PriorityTosThroughputMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4PriorityTosUnusedMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosUnused(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4TosUnusedCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4TosUnusedCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4PriorityTosUnusedMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4PriorityTos(BaseModel):
    delay: Optional[Ipv4PriorityTosDelay] = None
    """Delay"""

    monetary: Optional[Ipv4PriorityTosMonetary] = None
    """Monetary"""

    precedence: Optional[Ipv4PriorityTosPrecedence] = None
    """Precedence"""

    reliability: Optional[Ipv4PriorityTosReliability] = None
    """Reliability"""

    throughput: Optional[Ipv4PriorityTosThroughput] = None
    """Throughput"""

    unused: Optional[Ipv4PriorityTosUnused] = None
    """Unused"""


class Ipv4Priority(BaseModel):
    choice: Optional[Literal["raw", "tos", "dscp"]] = None

    dscp: Optional[Ipv4PriorityDscp] = None
    """Differentiated services code point (DSCP) packet field."""

    raw: Optional[Ipv4PriorityRaw] = None
    """Raw priority"""

    tos: Optional[Ipv4PriorityTos] = None
    """Type of service (TOS) packet field."""


class Ipv4ProtocolMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4Protocol(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4ProtocolCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4ProtocolCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4ProtocolMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4ReservedMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4Reserved(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4ReservedCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4ReservedCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4ReservedMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4SrcMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4SrcRandom(BaseModel):
    count: Optional[int] = None
    """The total number of values to be generated by the random value generator."""

    max: Optional[str] = None
    """The maximum possible value generated by the random value generator."""

    min: Optional[str] = None
    """The minimum possible value generated by the random value generator."""

    seed: Optional[int] = None
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class Ipv4Src(BaseModel):
    auto: Optional[FlowIpv4Auto] = None
    """The OTG implementation can provide a system generated, value for this property."""

    choice: Optional[Literal["value", "values", "increment", "decrement", "auto", "random"]] = None

    decrement: Optional[PatternFlowIpv4SrcCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowIpv4SrcCounter] = None
    """ipv4 counter pattern"""

    metric_tags: Optional[List[Ipv4SrcMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: Optional[Ipv4SrcRandom] = None
    """ipv4 random pattern"""

    value: Optional[str] = None

    values: Optional[List[str]] = None


class Ipv4TimeToLiveMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4TimeToLive(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4TimeToLiveCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4TimeToLiveCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4TimeToLiveMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4TotalLengthMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4TotalLength(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4TotalLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4TotalLengthCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4TotalLengthMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4VersionMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv4Version(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv4VersionCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv4VersionCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv4VersionMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv4(BaseModel):
    dont_fragment: Optional[Ipv4DontFragment] = None
    """
    Dont fragment flag If the dont_fragment flag is set and fragmentation is
    required to route the packet then the packet is dropped.
    """

    dst: Optional[Ipv4Dst] = None
    """Destination address"""

    fragment_offset: Optional[Ipv4FragmentOffset] = None
    """Fragment offset"""

    header_checksum: Optional[Ipv4HeaderChecksum] = None
    """Header checksum"""

    header_length: Optional[Ipv4HeaderLength] = None
    """Header length"""

    identification: Optional[Ipv4Identification] = None
    """Identification"""

    more_fragments: Optional[Ipv4MoreFragments] = None
    """More fragments flag"""

    options: Optional[List[Ipv4Option]] = None

    priority: Optional[Ipv4Priority] = None
    """A container for ipv4 raw, tos, dscp ip priorities."""

    protocol: Optional[Ipv4Protocol] = None
    """Protocol, default is 61 any host internal protocol"""

    reserved: Optional[Ipv4Reserved] = None
    """Reserved flag."""

    src: Optional[Ipv4Src] = None
    """Source address"""

    time_to_live: Optional[Ipv4TimeToLive] = None
    """Time to live"""

    total_length: Optional[Ipv4TotalLength] = None
    """Total length"""

    version: Optional[Ipv4Version] = None
    """Version"""


class Ipv6DstMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv6Dst(BaseModel):
    auto: Optional[FlowIpv6Auto] = None
    """The OTG implementation can provide a system generated, value for this property."""

    choice: Optional[Literal["value", "values", "increment", "decrement", "auto"]] = None

    decrement: Optional[PatternFlowIpv6DstCounter] = None
    """ipv6 counter pattern"""

    increment: Optional[PatternFlowIpv6DstCounter] = None
    """ipv6 counter pattern"""

    metric_tags: Optional[List[Ipv6DstMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class Ipv6FlowLabelMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv6FlowLabelRandom(BaseModel):
    count: Optional[int] = None
    """The total number of values to be generated by the random value generator."""

    max: Optional[int] = None
    """The maximum possible value generated by the random value generator."""

    min: Optional[int] = None
    """The minimum possible value generated by the random value generator."""

    seed: Optional[int] = None
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class Ipv6FlowLabel(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement", "random"]] = None

    decrement: Optional[PatternFlowIpv6FlowLabelCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv6FlowLabelCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv6FlowLabelMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: Optional[Ipv6FlowLabelRandom] = None
    """integer random pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv6HopLimitMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv6HopLimit(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv6HopLimitCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv6HopLimitCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv6HopLimitMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv6NextHeaderMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv6NextHeader(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv6NextHeaderCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv6NextHeaderCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv6NextHeaderMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv6PayloadLengthMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv6PayloadLength(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv6PayloadLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv6PayloadLengthCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv6PayloadLengthMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv6SrcMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv6Src(BaseModel):
    auto: Optional[FlowIpv6Auto] = None
    """The OTG implementation can provide a system generated, value for this property."""

    choice: Optional[Literal["value", "values", "increment", "decrement", "auto"]] = None

    decrement: Optional[PatternFlowIpv6SrcCounter] = None
    """ipv6 counter pattern"""

    increment: Optional[PatternFlowIpv6SrcCounter] = None
    """ipv6 counter pattern"""

    metric_tags: Optional[List[Ipv6SrcMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class Ipv6TrafficClassMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv6TrafficClass(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv6TrafficClassCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv6TrafficClassCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv6TrafficClassMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv6VersionMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class Ipv6Version(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowIpv6VersionCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowIpv6VersionCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[Ipv6VersionMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ipv6(BaseModel):
    dst: Optional[Ipv6Dst] = None
    """Destination address"""

    flow_label: Optional[Ipv6FlowLabel] = None
    """Flow label"""

    hop_limit: Optional[Ipv6HopLimit] = None
    """Hop limit"""

    next_header: Optional[Ipv6NextHeader] = None
    """Next header"""

    payload_length: Optional[Ipv6PayloadLength] = None
    """Payload length"""

    src: Optional[Ipv6Src] = None
    """Source address"""

    traffic_class: Optional[Ipv6TrafficClass] = None
    """Traffic class"""

    version: Optional[Ipv6Version] = None
    """Version number"""


class Macsec(BaseModel):
    choice: Optional[Literal["auto"]] = None
    """Currently only auto choice is allowed.

    If choice is auto, MACsec header is autogenerated. If auto choice is selected,
    MACsec protocol must be configured in device; flow.tx_rx.choice must be of type
    'device' and flow.tx_rx.device.tx_names[0] must be chosen to be an endpoint that
    is on or behind a MACSec enabled ethernet to be able to correctly auto-fill the
    fields of the MACsec header. If one of the conditions is not true, the
    implementation should return an error specifying the issue. A custom choice can
    be added in future to allow user to set specific MACsec header fields and/ or to
    generate flow.tx_rx.port type of traffic with MACSec header fields explicitly
    specified by the user.
    """


class MplsBottomOfStackMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class MplsBottomOfStack(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowMplsBottomOfStackCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowMplsBottomOfStackCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[MplsBottomOfStackMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class MplsLabelMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class MplsLabel(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowMplsLabelCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowMplsLabelCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[MplsLabelMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class MplsTimeToLiveMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class MplsTimeToLive(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowMplsTimeToLiveCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowMplsTimeToLiveCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[MplsTimeToLiveMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class MplsTrafficClassMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class MplsTrafficClass(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowMplsTrafficClassCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowMplsTrafficClassCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[MplsTrafficClassMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Mpls(BaseModel):
    bottom_of_stack: Optional[MplsBottomOfStack] = None
    """Bottom of stack"""

    label: Optional[MplsLabel] = None
    """Label of routers"""

    time_to_live: Optional[MplsTimeToLive] = None
    """Time to live"""

    traffic_class: Optional[MplsTrafficClass] = None
    """Traffic class"""


class PfcpauseClassEnableVectorMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpauseClassEnableVector(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPauseClassEnableVectorCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPauseClassEnableVectorCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpauseClassEnableVectorMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpauseControlOpCodeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpauseControlOpCode(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPauseControlOpCodeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPauseControlOpCodeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpauseControlOpCodeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpauseDstMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpauseDst(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPauseDstCounter] = None
    """mac counter pattern"""

    increment: Optional[PatternFlowPfcPauseDstCounter] = None
    """mac counter pattern"""

    metric_tags: Optional[List[PfcpauseDstMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class PfcpauseEtherTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpauseEtherType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPauseEtherTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPauseEtherTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpauseEtherTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpausePauseClass0MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass0(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPausePauseClass0Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPausePauseClass0Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpausePauseClass0MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpausePauseClass1MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass1(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPausePauseClass1Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPausePauseClass1Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpausePauseClass1MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpausePauseClass2MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass2(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPausePauseClass2Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPausePauseClass2Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpausePauseClass2MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpausePauseClass3MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass3(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPausePauseClass3Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPausePauseClass3Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpausePauseClass3MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpausePauseClass4MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass4(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPausePauseClass4Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPausePauseClass4Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpausePauseClass4MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpausePauseClass5MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass5(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPausePauseClass5Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPausePauseClass5Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpausePauseClass5MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpausePauseClass6MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass6(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPausePauseClass6Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPausePauseClass6Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpausePauseClass6MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpausePauseClass7MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass7(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPausePauseClass7Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPfcPausePauseClass7Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PfcpausePauseClass7MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PfcpauseSrcMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PfcpauseSrc(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPfcPauseSrcCounter] = None
    """mac counter pattern"""

    increment: Optional[PatternFlowPfcPauseSrcCounter] = None
    """mac counter pattern"""

    metric_tags: Optional[List[PfcpauseSrcMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[str] = None

    values: Optional[List[str]] = None


class Pfcpause(BaseModel):
    class_enable_vector: Optional[PfcpauseClassEnableVector] = None
    """Destination"""

    control_op_code: Optional[PfcpauseControlOpCode] = None
    """Control operation code"""

    dst: Optional[PfcpauseDst] = None
    """Destination MAC address"""

    ether_type: Optional[PfcpauseEtherType] = None
    """Ethernet type"""

    pause_class_0: Optional[PfcpausePauseClass0] = None
    """Pause class 0"""

    pause_class_1: Optional[PfcpausePauseClass1] = None
    """Pause class 1"""

    pause_class_2: Optional[PfcpausePauseClass2] = None
    """Pause class 2"""

    pause_class_3: Optional[PfcpausePauseClass3] = None
    """Pause class 3"""

    pause_class_4: Optional[PfcpausePauseClass4] = None
    """Pause class 4"""

    pause_class_5: Optional[PfcpausePauseClass5] = None
    """Pause class 5"""

    pause_class_6: Optional[PfcpausePauseClass6] = None
    """Pause class 6"""

    pause_class_7: Optional[PfcpausePauseClass7] = None
    """Pause class 7"""

    src: Optional[PfcpauseSrc] = None
    """Source MAC address"""


class PppAddressMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PppAddress(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPppAddressCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPppAddressCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PppAddressMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PppControlMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PppControl(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPppControlCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPppControlCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PppControlMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class PppProtocolTypeMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class PppProtocolType(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowPppProtocolTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowPppProtocolTypeCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[PppProtocolTypeMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Ppp(BaseModel):
    address: Optional[PppAddress] = None
    """PPP address"""

    control: Optional[PppControl] = None
    """PPP control"""

    protocol_type: Optional[PppProtocolType] = None
    """PPP protocol type"""


class RsvpMessageTypePathObjectClassNumCustomType(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathObjectsCustomTypeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathObjectsCustomTypeCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumCustom(BaseModel):
    bytes: Optional[str] = None
    """A custom packet header defined as a string of hex bytes.

    The string MUST contain sequence of valid hex bytes. Spaces or colons can be
    part of the bytes but will be discarded. Value of the this field should not
    excced 65525 bytes since maximum 65528 bytes can be added as object-contents in
    RSVP header. For type and length requires 3 bytes, hence maximum of 65524 bytes
    are expected. Maximum length of this attribute is 131050 (65525 \\** 2 hex
    character per byte).
    """

    length: Optional[FlowRsvpObjectLength] = None

    type: Optional[RsvpMessageTypePathObjectClassNumCustomType] = None
    """User defined object type."""


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumberLBit(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathExplicitRouteType1AsNumberLBitCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathExplicitRouteType1AsNumberLBitCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumberLength(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation will provide a system generated value for this property.

    If the OTG implementation is unable to generate a value the default value must
    be used.
    """

    choice: Optional[Literal["auto", "value"]] = None
    """auto or configured value."""

    value: Optional[int] = None


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumber(BaseModel):
    as_number: Optional[int] = None
    """
    Autonomous System number to be set in the ERO sub-object that this LSP should
    traverse through. This field is applicable only if the value of 'type' is set to
    'as_number'.
    """

    l_bit: Optional[RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumberLBit] = None
    """The L bit is an attribute of the subobject.

    The L bit is set if the subobject represents a loose hop in the explicit route.
    If the bit is not set, the subobject represents a strict hop in the explicit
    route.
    """

    length: Optional[RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumberLength] = None
    """
    The Length contains the total length of the subobject in bytes,including L, Type
    and Length fields. The Length MUST be atleast 4, and MUST be a multiple of 4.
    """


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixIpv4Address(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixIpv4AddressCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixIpv4AddressCounter] = None
    """ipv4 counter pattern"""

    value: Optional[str] = None

    values: Optional[List[str]] = None


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixLBit(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixLBitCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixLBitCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixLength(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation will provide a system generated value for this property.

    If the OTG implementation is unable to generate a value the default value must
    be used.
    """

    choice: Optional[Literal["auto", "value"]] = None
    """auto or configured value."""

    value: Optional[int] = None


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4Prefix(BaseModel):
    ipv4_address: Optional[
        RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixIpv4Address
    ] = None
    """This IPv4 address is treated as a prefix based on the prefix length value below.

    Bits beyond the prefix are ignored on receipt and SHOULD be set to zero on
    transmission.
    """

    l_bit: Optional[RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixLBit] = None
    """The L bit is an attribute of the subobject.

    The L bit is set if the subobject represents a loose hop in the explicit route.
    If the bit is not set, the subobject represents a strict hop in the explicit
    route.
    """

    length: Optional[RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixLength] = None
    """
    The Length contains the total length of the subobject in bytes,including L,Type
    and Length fields. The Length MUST be atleast 4, and MUST be a multiple of 4.
    """

    prefix: Optional[int] = None
    """The prefix length of the IPv4 address."""


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectType(BaseModel):
    as_number: Optional[RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumber] = None
    """
    Class = EXPLICIT_ROUTE, Type1 ROUTE_RECORD C-Type = 1 Subobject: Autonomous
    system number, C-Type: 32
    """

    choice: Optional[Literal["ipv4_prefix", "as_number"]] = None

    ipv4_prefix: Optional[RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4Prefix] = None
    """
    Class = EXPLICIT_ROUTE, Type1 ROUTE_RECORD C-Type = 1 Subobject: IPv4 Prefix,
    C-Type: 1
    """


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1Subobject(BaseModel):
    type: Optional[RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectType] = None
    """
    Currently supported subobjects are IPv4 address(1) and Autonomous system
    number(32).
    """


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1(BaseModel):
    subobjects: Optional[List[RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1Subobject]] = None


class RsvpMessageTypePathObjectClassNumExplicitRouteCType(BaseModel):
    choice: Optional[Literal["type_1"]] = None

    type_1: Optional[RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1] = None
    """Type1 Explicit Route has subobjects.

    Currently supported subobjects are IPv4 prefix and Autonomous system number.
    """


class RsvpMessageTypePathObjectClassNumExplicitRoute(BaseModel):
    c_type: Optional[RsvpMessageTypePathObjectClassNumExplicitRouteCType] = None
    """Object for EXPLICIT_ROUTE class and c-type is Type 1 Explicit Route (1)."""

    length: Optional[FlowRsvpObjectLength] = None
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRangeL3pid(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathLabelRequestWithoutLabelRangeL3pidCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathLabelRequestWithoutLabelRangeL3pidCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRangeReserved(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathLabelRequestWithoutLabelRangeReservedCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathLabelRequestWithoutLabelRangeReservedCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRange(BaseModel):
    l3pid: Optional[RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRangeL3pid] = None
    """An identifier of the layer 3 protocol using this path.

    Standard Ethertype values are used e.g. The default value of 2048 ( 0x0800 )
    represents Ethertype for IPv4.
    """

    reserved: Optional[RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRangeReserved] = None
    """This field is reserved.

    It MUST be set to zero on transmission and MUST be ignored on receipt.
    """


class RsvpMessageTypePathObjectClassNumLabelRequestCType(BaseModel):
    choice: Optional[Literal["without_label_range"]] = None

    without_label_range: Optional[RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRange] = None
    """Class = LABEL_REQUEST, Without Label Range C-Type = 1"""


class RsvpMessageTypePathObjectClassNumLabelRequest(BaseModel):
    c_type: Optional[RsvpMessageTypePathObjectClassNumLabelRequestCType] = None
    """Object for LABEL_REQUEST class.

    Currently supported c-type is Without Label Range (1).
    """

    length: Optional[FlowRsvpObjectLength] = None
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressFlags(BaseModel):
    choice: Optional[Literal["local_protection_available", "local_protection_in_use"]] = None


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressIpv4Address(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathRecordRouteType1Ipv4AddressIpv4AddressCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowRsvpPathRecordRouteType1Ipv4AddressIpv4AddressCounter] = None
    """ipv4 counter pattern"""

    value: Optional[str] = None

    values: Optional[List[str]] = None


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressPrefixLength(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathRecordRouteType1Ipv4AddressPrefixLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathRecordRouteType1Ipv4AddressPrefixLengthCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4Address(BaseModel):
    flags: Optional[RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressFlags] = None
    """0x01 local_protection_available, 0x02 local_protection_in_use"""

    ipv4_address: Optional[
        RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressIpv4Address
    ] = None
    """A 32-bit unicast, host address.

    Any network-reachable interface address is allowed here. Illegal addresses, such
    as certain loopback addresses, SHOULD NOT be used.
    """

    length: Optional[FlowRsvpRouteRecordLength] = None
    """
    The Length contains the total length of the subobject in bytes, including the
    Type and Length fields. The Length MUST be atleast 4, and MUST be a multiple
    of 4.
    """

    prefix_length: Optional[
        RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressPrefixLength
    ] = None
    """Prefix-length of IPv4 address."""


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelCType(BaseModel):
    choice: Optional[Literal["value", "values"]] = None

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelFlags(BaseModel):
    choice: Optional[Literal["value", "values"]] = None

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelLabel(BaseModel):
    as_hex: Optional[str] = None
    """Value of the this field should not excced 4 bytes.

    Maximum length of this attribute is 8 (4 \\** 2 hex character per byte).
    """

    as_integer: Optional[int] = None

    choice: Optional[Literal["as_integer", "as_hex"]] = None
    """32 bit integer or hex value."""


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabel(BaseModel):
    c_type: Optional[RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelCType] = None
    """The C-Type of the included Label Object. Copied from the Label object."""

    flags: Optional[RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelFlags] = None
    """0x01 = Global label.

    This flag indicates that the label will be understood if received on any
    interface.
    """

    label: Optional[RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelLabel] = None
    """The contents of the Label Object. Copied from the Label Object."""

    length: Optional[FlowRsvpRouteRecordLength] = None
    """
    The Length contains the total length of the subobject in bytes, including the
    Type and Length fields. The Length MUST be atleast 4, and MUST be a multiple
    of 4.
    """


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectType(BaseModel):
    choice: Optional[Literal["ipv4_address", "label"]] = None

    ipv4_address: Optional[RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4Address] = None
    """
    Class = RECORD_ROUTE, Type1 ROUTE_RECORD C-Type = 1 Subobject: IPv4 Address,
    C-Type: 1
    """

    label: Optional[RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabel] = None
    """Class = RECORD_ROUTE, Type1 ROUTE_RECORD C-Type = 1 Subobject: Label, C-Type: 3"""


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1Subobject(BaseModel):
    type: Optional[RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectType] = None
    """Currently supported subobjects are IPv4 address(1) and Label(3)."""


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1(BaseModel):
    subobjects: Optional[List[RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1Subobject]] = None


class RsvpMessageTypePathObjectClassNumRecordRouteCType(BaseModel):
    choice: Optional[Literal["type_1"]] = None

    type_1: Optional[RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1] = None
    """Type1 record route has list of subobjects.

    Currently supported subobjects are IPv4 address(1) and Label(3).
    """


class RsvpMessageTypePathObjectClassNumRecordRoute(BaseModel):
    c_type: Optional[RsvpMessageTypePathObjectClassNumRecordRouteCType] = None
    """Object for RECORD_ROUTE class. c-type is Type 1 Route Record (1)."""

    length: Optional[FlowRsvpObjectLength] = None
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4Ipv4Address(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathRsvpHopIpv4Ipv4AddressCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowRsvpPathRsvpHopIpv4Ipv4AddressCounter] = None
    """ipv4 counter pattern"""

    value: Optional[str] = None

    values: Optional[List[str]] = None


class RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4LogicalInterfaceHandle(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathRsvpHopIpv4LogicalInterfaceHandleCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathRsvpHopIpv4LogicalInterfaceHandleCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4(BaseModel):
    ipv4_address: Optional[RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4Ipv4Address] = None
    """
    The IPv4 address of the interface through which the last RSVP-knowledgeable hop
    forwarded this message.
    """

    logical_interface_handle: Optional[RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4LogicalInterfaceHandle] = None
    """
    Logical Interface Handle (LIH) is used to distinguish logical outgoing
    interfaces. A node receiving an LIH in a Path message saves its value and
    returns it in the HOP objects of subsequent Resv messages sent to the node that
    originated the LIH. The LIH should be identically zero if there is no logical
    interface handle.
    """


class RsvpMessageTypePathObjectClassNumRsvpHopCType(BaseModel):
    choice: Optional[Literal["ipv4"]] = None

    ipv4: Optional[RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4] = None
    """IPv4 RSVP_HOP object: Class = 3, C-Type = 1"""


class RsvpMessageTypePathObjectClassNumRsvpHop(BaseModel):
    c_type: Optional[RsvpMessageTypePathObjectClassNumRsvpHopCType] = None
    """Object for RSVP_HOP class. Currently supported c-type is IPv4 (1)."""

    length: Optional[FlowRsvpObjectLength] = None
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4Ipv4TunnelSenderAddress(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTemplateLspTunnelIpv4Ipv4TunnelSenderAddressCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTemplateLspTunnelIpv4Ipv4TunnelSenderAddressCounter] = None
    """ipv4 counter pattern"""

    value: Optional[str] = None

    values: Optional[List[str]] = None


class RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4LspID(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTemplateLspTunnelIpv4LspIDCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTemplateLspTunnelIpv4LspIDCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4Reserved(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTemplateLspTunnelIpv4ReservedCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTemplateLspTunnelIpv4ReservedCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4(BaseModel):
    ipv4_tunnel_sender_address: Optional[
        RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4Ipv4TunnelSenderAddress
    ] = None
    """IPv4 address for a sender node."""

    lsp_id: Optional[RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4LspID] = None
    """
    A 16-bit identifier used in the SENDER_TEMPLATE that can be changed to allow a
    sender to share resources with itself.
    """

    reserved: Optional[RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4Reserved] = None
    """Reserved field, MUST be zero."""


class RsvpMessageTypePathObjectClassNumSenderTemplateCType(BaseModel):
    choice: Optional[Literal["lsp_tunnel_ipv4"]] = None

    lsp_tunnel_ipv4: Optional[RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4] = None
    """Class = SENDER_TEMPLATE, LSP_TUNNEL_IPv4 C-Type = 7"""


class RsvpMessageTypePathObjectClassNumSenderTemplate(BaseModel):
    c_type: Optional[RsvpMessageTypePathObjectClassNumSenderTemplateCType] = None
    """Object for SENDER_TEMPLATE class.

    Currently supported c-type is LSP Tunnel IPv4 (7).
    """

    length: Optional[FlowRsvpObjectLength] = None
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServLengthOfServiceData(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServLengthOfServiceDataCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServLengthOfServiceDataCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServMaximumPacketSize(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServMaximumPacketSizeCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServMaximumPacketSizeCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServMinimumPolicedUnit(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServMinimumPolicedUnitCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServMinimumPolicedUnitCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServOverallLength(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServOverallLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServOverallLengthCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameter127Flag(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServParameter127FlagCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServParameter127FlagCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameter127Length(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServParameter127LengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServParameter127LengthCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameterIDTokenBucketTspec(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServParameterIDTokenBucketTspecCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServParameterIDTokenBucketTspecCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServReserved1(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServReserved1Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServReserved1Counter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServReserved2(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServReserved2Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServReserved2Counter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServServiceHeader(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServServiceHeaderCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServServiceHeaderCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServVersion(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServVersionCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServVersionCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServZeroBit(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSenderTspecIntServZeroBitCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSenderTspecIntServZeroBitCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServ(BaseModel):
    length_of_service_data: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServLengthOfServiceData] = None
    """Length of service data, 6 words not including per-service header."""

    maximum_packet_size: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServMaximumPacketSize] = None
    """
    The maximum packet size parameter should be set to the size of the largest
    packet the application might wish to generate. This value must, by definition,
    be equal to or larger than the value of The minimum policed unit.
    """

    minimum_policed_unit: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServMinimumPolicedUnit] = None
    """
    The minimum policed unit parameter should generally be set equal to the size of
    the smallest packet generated by the application.
    """

    overall_length: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServOverallLength] = None
    """Overall length (7 words not including header)."""

    parameter_127_flag: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameter127Flag] = None
    """Parameter 127 flags (none set)"""

    parameter_127_length: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameter127Length] = None
    """Parameter 127 length, 5 words not including per-service header"""

    parameter_id_token_bucket_tspec: Optional[
        RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameterIDTokenBucketTspec
    ] = None
    """Parameter ID, parameter 127 (Token Bucket TSpec)"""

    peak_data_rate: Optional[float] = None
    """
    The peak rate may be set to the sender's peak traffic generation rate (if known
    and controlled), the physical interface line rate (if known), or positive
    infinity (if no better value is available).
    """

    reserved1: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServReserved1] = None
    """Reserved."""

    reserved2: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServReserved2] = None
    """Reserved."""

    service_header: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServServiceHeader] = None
    """
    Service header, service number - '1' (Generic information) if in a PATH message.
    """

    token_bucket_rate: Optional[float] = None
    """Token bucket rate is set to sender's view of its generated traffic."""

    token_bucket_size: Optional[float] = None
    """Token bucket size is set to sender's view of its generated traffic."""

    version: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServVersion] = None
    """Message format version number."""

    zero_bit: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServZeroBit] = None
    """MUST be 0."""


class RsvpMessageTypePathObjectClassNumSenderTspecCType(BaseModel):
    choice: Optional[Literal["int_serv"]] = None

    int_serv: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServ] = None
    """int-serv SENDER_TSPEC object: Class = 12, C-Type = 2"""


class RsvpMessageTypePathObjectClassNumSenderTspec(BaseModel):
    c_type: Optional[RsvpMessageTypePathObjectClassNumSenderTspecCType] = None
    """Object for SENDER_TSPEC class. Currently supported c-type is int-serv (2)."""

    length: Optional[FlowRsvpObjectLength] = None
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelIDAsInteger(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSessionExtTunnelIDAsIntegerCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSessionExtTunnelIDAsIntegerCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelIDAsIpv4(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSessionExtTunnelIDAsIpv4Counter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowRsvpPathSessionExtTunnelIDAsIpv4Counter] = None
    """ipv4 counter pattern"""

    value: Optional[str] = None

    values: Optional[List[str]] = None


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelID(BaseModel):
    as_integer: Optional[RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelIDAsInteger] = None
    """TBD"""

    as_ipv4: Optional[RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelIDAsIpv4] = None
    """IPv4 address of the ingress endpoint for the tunnel."""

    choice: Optional[Literal["as_integer", "as_ipv4"]] = None
    """32 bit integer or IPv4 address."""


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4Ipv4TunnelEndPointAddress(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSessionLspTunnelIpv4Ipv4TunnelEndPointAddressCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowRsvpPathSessionLspTunnelIpv4Ipv4TunnelEndPointAddressCounter] = None
    """ipv4 counter pattern"""

    value: Optional[str] = None

    values: Optional[List[str]] = None


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4Reserved(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSessionLspTunnelIpv4ReservedCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSessionLspTunnelIpv4ReservedCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4TunnelID(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathSessionLspTunnelIpv4TunnelIDCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathSessionLspTunnelIpv4TunnelIDCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4(BaseModel):
    extended_tunnel_id: Optional[RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelID] = None
    """
    A 32-bit identifier used in the SESSION that remains constant over the life of
    the tunnel. Normally set to all zeros. Ingress nodes that wish to narrow the
    scope of a SESSION to the ingress-egress pair may place their IPv4 address here
    as a globally unique identifier.
    """

    ipv4_tunnel_end_point_address: Optional[
        RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4Ipv4TunnelEndPointAddress
    ] = None
    """IPv4 address of the egress node for the tunnel."""

    reserved: Optional[RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4Reserved] = None
    """Reserved field, MUST be zero."""

    tunnel_id: Optional[RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4TunnelID] = None
    """
    A 16-bit identifier used in the SESSION that remains constant over the life of
    the tunnel.
    """


class RsvpMessageTypePathObjectClassNumSessionCType(BaseModel):
    choice: Optional[Literal["lsp_tunnel_ipv4"]] = None

    lsp_tunnel_ipv4: Optional[RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4] = None
    """Class = SESSION, LSP_TUNNEL_IPv4 C-Type = 7."""


class RsvpMessageTypePathObjectClassNumSession(BaseModel):
    c_type: Optional[RsvpMessageTypePathObjectClassNumSessionCType] = None
    """The body of an object corresponding to the class number and c-type.

    Currently supported c-type for SESSION object is LSP Tunnel IPv4 (7).
    """

    length: Optional[FlowRsvpObjectLength] = None
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumSessionAttributeCTypeLspTunnel(BaseModel):
    flags: Optional[FlowRsvpLspTunnelFlag] = None
    """
    0x01 Local protection desired, 0x02 Label recording desired, 0x04 SE Style
    desired
    """

    holding_priority: Optional[int] = None
    """
    The priority of the session with respect to holding resources,in the range of 0
    to 7. The value 0 is the highest priority. The Setup Priority is used in
    deciding whether this session can preempt another session.
    """

    name_length: Optional[FlowRsvpSessionAttributeNameLength] = None
    """The length of the display string before padding, in bytes."""

    session_name: Optional[str] = None
    """A null padded string of characters."""

    setup_priority: Optional[int] = None
    """
    The priority of the session with respect to taking resources,in the range of 0
    to 7. The value 0 is the highest priority. The Setup Priority is used in
    deciding whether this session can preempt another session.
    """


class RsvpMessageTypePathObjectClassNumSessionAttributeCTypeLspTunnelRa(BaseModel):
    exclude_any: Optional[str] = None
    """
    A 32-bit vector representing a set of attribute filters associated with a tunnel
    any of which renders a link unacceptable. A null set (all bits set to zero)
    doesn't render the link unacceptable. The most significant byte in the
    hex-string is the farthest to the left in the byte sequence. Leading zero bytes
    in the configured value may be omitted for brevity.
    """

    flags: Optional[FlowRsvpLspTunnelFlag] = None
    """
    0x01 Local protection desired, 0x02 Label recording desired, 0x04 SE Style
    desired
    """

    holding_priority: Optional[int] = None
    """
    The priority of the session with respect to holding resources,in the range of 0
    to 7. The value 0 is the highest priority. The Setup Priority is used in
    deciding whether this session can preempt another session.
    """

    include_all: Optional[str] = None
    """
    A 32-bit vector representing a set of attribute filters associated with a tunnel
    all of which must be present for a link to be acceptable. A null set (all bits
    set to zero) automatically passes. The most significant byte in the hex-string
    is the farthest to the left in the byte sequence. Leading zero bytes in the
    configured value may be omitted for brevity.
    """

    include_any: Optional[str] = None
    """
    A 32-bit vector representing a set of attribute filters associated with a tunnel
    any of which renders a link acceptable. A null set (all bits set to zero)
    automatically passes. The most significant byte in the hex-string is the
    farthest to the left in the byte sequence. Leading zero bytes in the configured
    value may be omitted for brevity.
    """

    name_length: Optional[FlowRsvpSessionAttributeNameLength] = None
    """The length of the display string before padding, in bytes."""

    session_name: Optional[str] = None
    """A null padded string of characters."""

    setup_priority: Optional[int] = None
    """
    The priority of the session with respect to taking resources,in the range of 0
    to 7. The value 0 is the highest priority. The Setup Priority is used in
    deciding whether this session can preempt another session.
    """


class RsvpMessageTypePathObjectClassNumSessionAttributeCType(BaseModel):
    choice: Optional[Literal["lsp_tunnel", "lsp_tunnel_ra"]] = None

    lsp_tunnel: Optional[RsvpMessageTypePathObjectClassNumSessionAttributeCTypeLspTunnel] = None
    """
    SESSION_ATTRIBUTE class = 207, LSP_TUNNEL_RA C-Type = 7, resource affinity
    information.
    """

    lsp_tunnel_ra: Optional[RsvpMessageTypePathObjectClassNumSessionAttributeCTypeLspTunnelRa] = None
    """
    SESSION_ATTRIBUTE class = 207, LSP_TUNNEL_RA C-Type = 1, it carries resource
    affinity information.
    """


class RsvpMessageTypePathObjectClassNumSessionAttribute(BaseModel):
    c_type: Optional[RsvpMessageTypePathObjectClassNumSessionAttributeCType] = None
    """Object for SESSION_ATTRIBUTE class.

    Currently supported c-type is LSP_Tunnel_RA (1) and LSP_Tunnel (7).
    """

    length: Optional[FlowRsvpObjectLength] = None
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumTimeValuesCTypeType1RefreshPeriodR(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpPathTimeValuesType1RefreshPeriodRCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpPathTimeValuesType1RefreshPeriodRCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpMessageTypePathObjectClassNumTimeValuesCTypeType1(BaseModel):
    refresh_period_r: Optional[RsvpMessageTypePathObjectClassNumTimeValuesCTypeType1RefreshPeriodR] = None
    """The refresh timeout period R used to generate this message;in milliseconds."""


class RsvpMessageTypePathObjectClassNumTimeValuesCType(BaseModel):
    choice: Optional[Literal["type_1"]] = None

    type_1: Optional[RsvpMessageTypePathObjectClassNumTimeValuesCTypeType1] = None
    """TIME_VALUES Object: Class = 5, C-Type = 1"""


class RsvpMessageTypePathObjectClassNumTimeValues(BaseModel):
    c_type: Optional[RsvpMessageTypePathObjectClassNumTimeValuesCType] = None
    """Object for TIME_VALUES class.

    Currently supported c-type is Type 1 Time Value (1).
    """

    length: Optional[FlowRsvpObjectLength] = None
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNum(BaseModel):
    choice: Literal[
        "session",
        "rsvp_hop",
        "time_values",
        "explicit_route",
        "label_request",
        "session_attribute",
        "sender_template",
        "sender_tspec",
        "record_route",
        "custom",
    ]

    custom: Optional[RsvpMessageTypePathObjectClassNumCustom] = None
    """Custom packet header"""

    explicit_route: Optional[RsvpMessageTypePathObjectClassNumExplicitRoute] = None
    """C-Type is specific to a class num."""

    label_request: Optional[RsvpMessageTypePathObjectClassNumLabelRequest] = None
    """C-Type is specific to a class num."""

    record_route: Optional[RsvpMessageTypePathObjectClassNumRecordRoute] = None
    """C-Type is specific to a class num."""

    rsvp_hop: Optional[RsvpMessageTypePathObjectClassNumRsvpHop] = None
    """C-Type is specific to a class num."""

    sender_template: Optional[RsvpMessageTypePathObjectClassNumSenderTemplate] = None
    """C-Type is specific to a class num."""

    sender_tspec: Optional[RsvpMessageTypePathObjectClassNumSenderTspec] = None
    """C-Type is specific to a class num."""

    session: Optional[RsvpMessageTypePathObjectClassNumSession] = None
    """C-Type is specific to a class num."""

    session_attribute: Optional[RsvpMessageTypePathObjectClassNumSessionAttribute] = None
    """C-Type is specific to a class num."""

    time_values: Optional[RsvpMessageTypePathObjectClassNumTimeValues] = None
    """C-Type is specific to a class num."""


class RsvpMessageTypePathObject(BaseModel):
    class_num: Optional[RsvpMessageTypePathObjectClassNum] = None
    """The class number is used to identify the class of an object.

    Defined in
    https://www.iana.org/assignments/rsvp-parameters/rsvp-parameters.xhtml#rsvp-parameters-4
    . Curently supported class numbers are for "Path" message type. "Path" message:
    Supported Class numbers and it's value: SESSION: 1, RSVP_HOP: 3, TIME_VALUES: 5,
    EXPLICIT_ROUTE: 20, LABEL_REQUEST: 19, SESSION_ATTRIBUTE: 207, SENDER_TEMPLATE:
    11, SENDER_TSPEC: 12, RECORD_ROUTE: 21, Custom: User defined bytes based on
    class and c-types not supported in above options.
    """


class RsvpMessageTypePath(BaseModel):
    objects: Optional[List[RsvpMessageTypePathObject]] = None
    """
    "Path" message requires atleast SESSION, RSVP_HOP, TIME_VALUES, LABEL_REQUEST,
    SENDER_TEMPLATE and SENDER_TSPEC objects in order.
    """


class RsvpMessageType(BaseModel):
    choice: Optional[Literal["path"]] = None

    path: Optional[RsvpMessageTypePath] = None
    """
    "Path" message requires the following list of objects in order as defined in
    https://www.rfc-editor.org/rfc/rfc3209.html#page-15: 1. SESSION 2. RSVP_HOP 3.
    TIME_VALUES 4. EXPLICIT_ROUTE [optional] 5. LABEL_REQUEST 6. SESSION_ATTRIBUTE
    [optional] 7. SENDER_TEMPLATE 8. SENDER_TSPEC 9. RECORD_ROUTE [optional]
    """


class RsvpReserved(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpReservedCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpReservedCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RsvpRsvpChecksum(BaseModel):
    choice: Optional[Literal["generated", "custom"]] = None
    """The type of checksum"""

    custom: Optional[int] = None
    """A custom checksum value"""

    generated: Optional[Literal["good", "bad"]] = None
    """A system generated checksum value"""


class RsvpRsvpLength(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation will provide a system generated value for this property.

    If the OTG implementation is unable to generate a value the default value must
    be used.
    """

    choice: Optional[Literal["auto", "value"]] = None
    """auto or configured value."""

    value: Optional[int] = None


class RsvpTimeToLive(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowRsvpTimeToLiveCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowRsvpTimeToLiveCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Rsvp(BaseModel):
    flag: Optional[Literal["not_refresh_reduction_capable", "refresh_reduction_capable"]] = None
    """Flag, 0x01-0x08: Reserved."""

    message_type: Optional[RsvpMessageType] = None
    """An 8-bit number that identifies the function of the RSVP message.

    There are aound 20 message types defined in
    https://www.iana.org/assignments/rsvp-parameters/rsvp-parameters.xhtml#rsvp-parameters-2
    . Among these presently supported is "Path"(value: 1) message type.
    """

    reserved: Optional[RsvpReserved] = None
    """Reserved"""

    rsvp_checksum: Optional[RsvpRsvpChecksum] = None
    """
    The one's complement of the one's complement sum of the message, with the
    checksum field replaced by zero for the purpose of computing the checksum. An
    all-zero value means that no checksum was transmitted.
    """

    rsvp_length: Optional[RsvpRsvpLength] = None
    """
    The sum of the lengths of the common header and all objects included in the
    message.
    """

    time_to_live: Optional[RsvpTimeToLive] = None
    """The IP time-to-live(TTL) value with which the message was sent."""

    version: Optional[int] = None
    """RSVP Protocol Version."""


class Snmpv2cDataGetBulkRequestMaxRepetitions(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cBulkPduMaxRepetitionsCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowSnmpv2cBulkPduMaxRepetitionsCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Snmpv2cDataGetBulkRequestNonRepeaters(BaseModel):
    choice: Optional[Literal["value", "values"]] = None

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Snmpv2cDataGetBulkRequestRequestID(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cBulkPduRequestIDCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowSnmpv2cBulkPduRequestIDCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Snmpv2cDataGetBulkRequest(BaseModel):
    max_repetitions: Optional[Snmpv2cDataGetBulkRequestMaxRepetitions] = None
    """
    A maximum of max_repetitions variable bindings are requested in the Response-PDU
    for each of the remaining variable bindings in the GetBulkRequest after the
    non_repeaters variable bindings.
    """

    non_repeaters: Optional[Snmpv2cDataGetBulkRequestNonRepeaters] = None
    """
    One variable binding in the Response-PDU is requested for the first
    non_repeaters variable bindings in the GetBulkRequest.
    """

    request_id: Optional[Snmpv2cDataGetBulkRequestRequestID] = None
    """Identifies a particular SNMP request.

    This index is echoed back in the response from the SNMP agent, allowing the SNMP
    manager to match an incoming response to the appropriate request.

    - Encoding of this field follows ASN.1 X.690(section 8.3) specification. Refer:
      http://www.itu.int/ITU-T/asn1/
    """

    variable_bindings: Optional[List[FlowSnmpv2cVariableBinding]] = None
    """A Sequence of variable_bindings."""


class Snmpv2cData(BaseModel):
    choice: Literal[
        "get_request",
        "get_next_request",
        "response",
        "set_request",
        "get_bulk_request",
        "inform_request",
        "snmpv2_trap",
        "report",
    ]

    get_bulk_request: Optional[Snmpv2cDataGetBulkRequest] = None
    """
    The purpose of the GetBulkRequest-PDU is to request the transfer of a
    potentially large amount of data, including, but not limited to, the efficient
    and rapid retrieval of large tables.
    """

    get_next_request: Optional[FlowSnmpv2cPdu] = None
    """This contains the body of the SNMPv2C PDU."""

    get_request: Optional[FlowSnmpv2cPdu] = None
    """This contains the body of the SNMPv2C PDU."""

    inform_request: Optional[FlowSnmpv2cPdu] = None
    """This contains the body of the SNMPv2C PDU."""

    report: Optional[FlowSnmpv2cPdu] = None
    """This contains the body of the SNMPv2C PDU."""

    response: Optional[FlowSnmpv2cPdu] = None
    """This contains the body of the SNMPv2C PDU."""

    set_request: Optional[FlowSnmpv2cPdu] = None
    """This contains the body of the SNMPv2C PDU."""

    snmpv2_trap: Optional[FlowSnmpv2cPdu] = None
    """This contains the body of the SNMPv2C PDU."""


class Snmpv2cVersion(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cVersionCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowSnmpv2cVersionCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Snmpv2c(BaseModel):
    data: Snmpv2cData
    """This contains the body of the SNMPv2C message.

    - Encoding of subsequent fields follow ASN.1 specification. Refer:
      http://www.itu.int/ITU-T/asn1/
    """

    community: Optional[str] = None
    """
    It is an ASCII based octet string which identifies the SNMP community in which
    the sender and recipient of this message are located. It should match the
    read-only or read-write community string configured on the recipient for the PDU
    to be accepted.
    """

    version: Optional[Snmpv2cVersion] = None
    """Version"""


class TcpAckNumMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpAckNum(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpAckNumCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpAckNumCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpAckNumMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpChecksum(BaseModel):
    choice: Optional[Literal["generated", "custom"]] = None
    """The type of checksum"""

    custom: Optional[int] = None
    """A custom checksum value"""

    generated: Optional[Literal["good", "bad"]] = None
    """A system generated checksum value"""


class TcpCtlAckMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlAck(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpCtlAckCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpCtlAckCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpCtlAckMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpCtlFinMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlFin(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpCtlFinCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpCtlFinCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpCtlFinMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpCtlPshMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlPsh(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpCtlPshCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpCtlPshCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpCtlPshMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpCtlRstMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlRst(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpCtlRstCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpCtlRstCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpCtlRstMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpCtlSynMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlSyn(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpCtlSynCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpCtlSynCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpCtlSynMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpCtlUrgMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlUrg(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpCtlUrgCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpCtlUrgCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpCtlUrgMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpDataOffsetMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpDataOffset(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpDataOffsetCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpDataOffsetCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpDataOffsetMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpDstPortMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpDstPortRandom(BaseModel):
    count: Optional[int] = None
    """The total number of values to be generated by the random value generator."""

    max: Optional[int] = None
    """The maximum possible value generated by the random value generator."""

    min: Optional[int] = None
    """The minimum possible value generated by the random value generator."""

    seed: Optional[int] = None
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class TcpDstPort(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement", "random"]] = None

    decrement: Optional[PatternFlowTcpDstPortCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpDstPortCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpDstPortMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: Optional[TcpDstPortRandom] = None
    """integer random pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpEcnCwrMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpEcnCwr(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpEcnCwrCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpEcnCwrCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpEcnCwrMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpEcnEchoMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpEcnEcho(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpEcnEchoCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpEcnEchoCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpEcnEchoMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpEcnNsMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpEcnNs(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpEcnNsCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpEcnNsCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpEcnNsMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpSeqNumMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpSeqNum(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpSeqNumCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpSeqNumCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpSeqNumMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpSrcPortMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpSrcPortRandom(BaseModel):
    count: Optional[int] = None
    """The total number of values to be generated by the random value generator."""

    max: Optional[int] = None
    """The maximum possible value generated by the random value generator."""

    min: Optional[int] = None
    """The minimum possible value generated by the random value generator."""

    seed: Optional[int] = None
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class TcpSrcPort(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement", "random"]] = None

    decrement: Optional[PatternFlowTcpSrcPortCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpSrcPortCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpSrcPortMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: Optional[TcpSrcPortRandom] = None
    """integer random pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class TcpWindowMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class TcpWindow(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowTcpWindowCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowTcpWindowCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[TcpWindowMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Tcp(BaseModel):
    ack_num: Optional[TcpAckNum] = None
    """Acknowledgement number"""

    checksum: Optional[TcpChecksum] = None
    """
    The one's complement of the one's complement sum of all 16 bit words in header
    and text. An all-zero value means that no checksum will be transmitted. While
    computing the checksum, the checksum field itself is replaced with zeros.
    """

    ctl_ack: Optional[TcpCtlAck] = None
    """A value of 1 indicates that the ackknowledgment field is significant."""

    ctl_fin: Optional[TcpCtlFin] = None
    """Last packet from the sender."""

    ctl_psh: Optional[TcpCtlPsh] = None
    """Asks to push the buffered data to the receiving application."""

    ctl_rst: Optional[TcpCtlRst] = None
    """Reset the connection."""

    ctl_syn: Optional[TcpCtlSyn] = None
    """Synchronize sequenece numbers."""

    ctl_urg: Optional[TcpCtlUrg] = None
    """A value of 1 indicates that the urgent pointer field is significant."""

    data_offset: Optional[TcpDataOffset] = None
    """The number of 32 bit words in the TCP header.

    This indicates where the data begins.
    """

    dst_port: Optional[TcpDstPort] = None
    """Destination port"""

    ecn_cwr: Optional[TcpEcnCwr] = None
    """Explicit congestion notification, congestion window reduced."""

    ecn_echo: Optional[TcpEcnEcho] = None
    """Explicit congestion notification, echo.

    1 indicates the peer is ecn capable. 0 indicates that a packet with ipv4.ecn =
    11 in the ip header was received during normal transmission.
    """

    ecn_ns: Optional[TcpEcnNs] = None
    """Explicit congestion notification, concealment protection."""

    seq_num: Optional[TcpSeqNum] = None
    """Sequence number"""

    src_port: Optional[TcpSrcPort] = None
    """Source port"""

    window: Optional[TcpWindow] = None
    """Tcp connection window."""


class UdpChecksum(BaseModel):
    choice: Optional[Literal["generated", "custom"]] = None
    """The type of checksum"""

    custom: Optional[int] = None
    """A custom checksum value"""

    generated: Optional[Literal["good", "bad"]] = None
    """A system generated checksum value"""


class UdpDstPortMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class UdpDstPortRandom(BaseModel):
    count: Optional[int] = None
    """The total number of values to be generated by the random value generator."""

    max: Optional[int] = None
    """The maximum possible value generated by the random value generator."""

    min: Optional[int] = None
    """The minimum possible value generated by the random value generator."""

    seed: Optional[int] = None
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class UdpDstPort(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement", "random"]] = None

    decrement: Optional[PatternFlowUdpDstPortCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowUdpDstPortCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[UdpDstPortMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: Optional[UdpDstPortRandom] = None
    """integer random pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class UdpLengthMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class UdpLength(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowUdpLengthCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowUdpLengthCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[UdpLengthMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class UdpSrcPortMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class UdpSrcPortRandom(BaseModel):
    count: Optional[int] = None
    """The total number of values to be generated by the random value generator."""

    max: Optional[int] = None
    """The maximum possible value generated by the random value generator."""

    min: Optional[int] = None
    """The minimum possible value generated by the random value generator."""

    seed: Optional[int] = None
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class UdpSrcPort(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement", "random"]] = None

    decrement: Optional[PatternFlowUdpSrcPortCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowUdpSrcPortCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[UdpSrcPortMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: Optional[UdpSrcPortRandom] = None
    """integer random pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Udp(BaseModel):
    checksum: Optional[UdpChecksum] = None
    """UDP checksum"""

    dst_port: Optional[UdpDstPort] = None
    """Destination port"""

    length: Optional[UdpLength] = None
    """Length"""

    src_port: Optional[UdpSrcPort] = None
    """Source port"""


class VlanIDMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class VlanID(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowVlanIDCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowVlanIDCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[VlanIDMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class VlanCfiMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class VlanCfi(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowVlanCfiCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowVlanCfiCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[VlanCfiMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class VlanPriorityMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class VlanPriority(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowVlanPriorityCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowVlanPriorityCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[VlanPriorityMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class VlanTpidMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class VlanTpid(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowVlanTpidCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowVlanTpidCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[VlanTpidMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Vlan(BaseModel):
    id: Optional[VlanID] = None
    """Vlan identifier"""

    cfi: Optional[VlanCfi] = None
    """Canonical format indicator or drop elegible indicator"""

    priority: Optional[VlanPriority] = None
    """Priority code point"""

    tpid: Optional[VlanTpid] = None
    """Protocol identifier"""


class VxlanFlagsMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class VxlanFlags(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowVxlanFlagsCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowVxlanFlagsCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[VxlanFlagsMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class VxlanReserved0MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class VxlanReserved0(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowVxlanReserved0Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowVxlanReserved0Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[VxlanReserved0MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class VxlanReserved1MetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class VxlanReserved1(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowVxlanReserved1Counter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowVxlanReserved1Counter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[VxlanReserved1MetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class VxlanVniMetricTag(BaseModel):
    name: str
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: Optional[int] = None
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: Optional[int] = None
    """Offset in bits relative to start of corresponding header field"""


class VxlanVni(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Optional[Literal["value", "values", "auto", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowVxlanVniCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowVxlanVniCounter] = None
    """integer counter pattern"""

    metric_tags: Optional[List[VxlanVniMetricTag]] = None
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Vxlan(BaseModel):
    flags: Optional[VxlanFlags] = None
    """Flags field with a bit format of RRRRIRRR.

    The I flag MUST be set to 1 for a valid vxlan network id (VNI). The other 7 bits
    (designated "R") are reserved fields and MUST be set to zero on transmission and
    ignored on receipt.
    """

    reserved0: Optional[VxlanReserved0] = None
    """Reserved field"""

    reserved1: Optional[VxlanReserved1] = None
    """Reserved field"""

    vni: Optional[VxlanVni] = None
    """VXLAN network id"""


class FlowHeader(BaseModel):
    arp: Optional[Arp] = None
    """ARP packet header"""

    choice: Optional[
        Literal[
            "custom",
            "ethernet",
            "vlan",
            "vxlan",
            "ipv4",
            "ipv6",
            "pfcpause",
            "ethernetpause",
            "tcp",
            "udp",
            "gre",
            "gtpv1",
            "gtpv2",
            "arp",
            "icmp",
            "icmpv6",
            "ppp",
            "igmpv1",
            "mpls",
            "snmpv2c",
            "rsvp",
            "macsec",
        ]
    ] = None
    """The available types of flow headers.

    If one is not provided the default ethernet packet header MUST be provided.
    """

    custom: Optional[Custom] = None
    """Custom packet header"""

    ethernet: Optional[Ethernet] = None
    """Ethernet packet header"""

    ethernetpause: Optional[Ethernetpause] = None
    """IEEE 802.3x global ethernet pause packet header"""

    gre: Optional[Gre] = None
    """Standard GRE packet header (RFC2784)"""

    gtpv1: Optional[Gtpv1] = None
    """GTPv1 packet header"""

    gtpv2: Optional[Gtpv2] = None
    """GTPv2 packet header"""

    icmp: Optional[Icmp] = None
    """ICMP packet header"""

    icmpv6: Optional[Icmpv6] = None
    """ICMPv6 packet header"""

    igmpv1: Optional[Igmpv1] = None
    """IGMPv1 packet header"""

    ipv4: Optional[Ipv4] = None
    """IPv4 packet header"""

    ipv6: Optional[Ipv6] = None
    """IPv6 packet header"""

    macsec: Optional[Macsec] = None
    """MACsec packet header."""

    mpls: Optional[Mpls] = None
    """
    MPLS packet header; When configuring multiple such headers, the count shall not
    exceed 20.
    """

    pfcpause: Optional[Pfcpause] = None
    """IEEE 802.1Qbb PFC Pause packet header."""

    ppp: Optional[Ppp] = None
    """PPP packet header"""

    rsvp: Optional[Rsvp] = None
    """RSVP packet header as defined in RFC2205 and RFC3209.

    Currently only supported message type is "Path" with mandatory objects and
    sub-objects.
    """

    snmpv2c: Optional[Snmpv2c] = None
    """SNMPv2C packet header as defined in RFC1901 and RFC3416."""

    tcp: Optional[Tcp] = None
    """TCP packet header"""

    udp: Optional[Udp] = None
    """UDP packet header"""

    vlan: Optional[Vlan] = None
    """VLAN packet header"""

    vxlan: Optional[Vxlan] = None
    """VXLAN packet header"""
