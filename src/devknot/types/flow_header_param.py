# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .flow_ipv4_auto_param import FlowIpv4AutoParam
from .flow_ipv6_auto_param import FlowIpv6AutoParam
from .flow_snmpv2c_pdu_param import FlowSnmpv2cPduParam
from .flow_rsvp_object_length_param import FlowRsvpObjectLengthParam
from .flow_rsvp_lsp_tunnel_flag_param import FlowRsvpLspTunnelFlagParam
from .pattern_flow_vlan_id_counter_param import PatternFlowVlanIDCounterParam
from .flow_rsvp_route_record_length_param import FlowRsvpRouteRecordLengthParam
from .flow_snmpv2c_variable_binding_param import FlowSnmpv2cVariableBindingParam
from .pattern_flow_ipv4_dst_counter_param import PatternFlowIpv4DstCounterParam
from .pattern_flow_ipv4_src_counter_param import PatternFlowIpv4SrcCounterParam
from .pattern_flow_ipv6_dst_counter_param import PatternFlowIpv6DstCounterParam
from .pattern_flow_ipv6_src_counter_param import PatternFlowIpv6SrcCounterParam
from .pattern_flow_vlan_cfi_counter_param import PatternFlowVlanCfiCounterParam
from .pattern_flow_vlan_tpid_counter_param import PatternFlowVlanTpidCounterParam
from .pattern_flow_vxlan_vni_counter_param import PatternFlowVxlanVniCounterParam
from .pattern_flow_gtpv1_teid_counter_param import PatternFlowGtpv1TeidCounterParam
from .pattern_flow_gtpv2_teid_counter_param import PatternFlowGtpv2TeidCounterParam
from .pattern_flow_mpls_label_counter_param import PatternFlowMplsLabelCounterParam
from .pattern_flow_tcp_ecn_ns_counter_param import PatternFlowTcpEcnNsCounterParam
from .pattern_flow_tcp_window_counter_param import PatternFlowTcpWindowCounterParam
from .pattern_flow_udp_length_counter_param import PatternFlowUdpLengthCounterParam
from .pattern_flow_gre_version_counter_param import PatternFlowGreVersionCounterParam
from .pattern_flow_igmpv1_type_counter_param import PatternFlowIgmpv1TypeCounterParam
from .pattern_flow_ppp_address_counter_param import PatternFlowPppAddressCounterParam
from .pattern_flow_ppp_control_counter_param import PatternFlowPppControlCounterParam
from .pattern_flow_tcp_ack_num_counter_param import PatternFlowTcpAckNumCounterParam
from .pattern_flow_tcp_ctl_ack_counter_param import PatternFlowTcpCtlAckCounterParam
from .pattern_flow_tcp_ctl_fin_counter_param import PatternFlowTcpCtlFinCounterParam
from .pattern_flow_tcp_ctl_psh_counter_param import PatternFlowTcpCtlPshCounterParam
from .pattern_flow_tcp_ctl_rst_counter_param import PatternFlowTcpCtlRstCounterParam
from .pattern_flow_tcp_ctl_syn_counter_param import PatternFlowTcpCtlSynCounterParam
from .pattern_flow_tcp_ctl_urg_counter_param import PatternFlowTcpCtlUrgCounterParam
from .pattern_flow_tcp_ecn_cwr_counter_param import PatternFlowTcpEcnCwrCounterParam
from .pattern_flow_tcp_seq_num_counter_param import PatternFlowTcpSeqNumCounterParam
from .pattern_flow_vxlan_flags_counter_param import PatternFlowVxlanFlagsCounterParam
from .pattern_flow_ethernet_dst_counter_param import PatternFlowEthernetDstCounterParam
from .pattern_flow_ethernet_src_counter_param import PatternFlowEthernetSrcCounterParam
from .pattern_flow_gre_protocol_counter_param import PatternFlowGreProtocolCounterParam
from .pattern_flow_gtpv1_e_flag_counter_param import PatternFlowGtpv1EFlagCounterParam
from .pattern_flow_gtpv1_s_flag_counter_param import PatternFlowGtpv1SFlagCounterParam
from .pattern_flow_gtpv2_spare1_counter_param import PatternFlowGtpv2Spare1CounterParam
from .pattern_flow_gtpv2_spare2_counter_param import PatternFlowGtpv2Spare2CounterParam
from .pattern_flow_ipv4_version_counter_param import PatternFlowIpv4VersionCounterParam
from .pattern_flow_ipv6_version_counter_param import PatternFlowIpv6VersionCounterParam
from .pattern_flow_tcp_dst_port_counter_param import PatternFlowTcpDstPortCounterParam
from .pattern_flow_tcp_ecn_echo_counter_param import PatternFlowTcpEcnEchoCounterParam
from .pattern_flow_tcp_src_port_counter_param import PatternFlowTcpSrcPortCounterParam
from .pattern_flow_udp_dst_port_counter_param import PatternFlowUdpDstPortCounterParam
from .pattern_flow_udp_src_port_counter_param import PatternFlowUdpSrcPortCounterParam
from .pattern_flow_arp_operation_counter_param import PatternFlowArpOperationCounterParam
from .pattern_flow_gre_reserved0_counter_param import PatternFlowGreReserved0CounterParam
from .pattern_flow_gre_reserved1_counter_param import PatternFlowGreReserved1CounterParam
from .pattern_flow_gtpv1_pn_flag_counter_param import PatternFlowGtpv1PnFlagCounterParam
from .pattern_flow_gtpv1_version_counter_param import PatternFlowGtpv1VersionCounterParam
from .pattern_flow_gtpv2_version_counter_param import PatternFlowGtpv2VersionCounterParam
from .pattern_flow_igmpv1_unused_counter_param import PatternFlowIgmpv1UnusedCounterParam
from .pattern_flow_ipv4_dscp_ecn_counter_param import PatternFlowIpv4DscpEcnCounterParam
from .pattern_flow_ipv4_dscp_phb_counter_param import PatternFlowIpv4DscpPhbCounterParam
from .pattern_flow_ipv4_protocol_counter_param import PatternFlowIpv4ProtocolCounterParam
from .pattern_flow_ipv4_reserved_counter_param import PatternFlowIpv4ReservedCounterParam
from .pattern_flow_pfc_pause_dst_counter_param import PatternFlowPfcPauseDstCounterParam
from .pattern_flow_pfc_pause_src_counter_param import PatternFlowPfcPauseSrcCounterParam
from .pattern_flow_rsvp_reserved_counter_param import PatternFlowRsvpReservedCounterParam
from .pattern_flow_vlan_priority_counter_param import PatternFlowVlanPriorityCounterParam
from .pattern_flow_gtpv1_reserved_counter_param import PatternFlowGtpv1ReservedCounterParam
from .pattern_flow_icmp_echo_code_counter_param import PatternFlowIcmpEchoCodeCounterParam
from .pattern_flow_icmp_echo_type_counter_param import PatternFlowIcmpEchoTypeCounterParam
from .pattern_flow_igmpv1_version_counter_param import PatternFlowIgmpv1VersionCounterParam
from .pattern_flow_ipv4_tos_delay_counter_param import PatternFlowIpv4TosDelayCounterParam
from .pattern_flow_ipv6_hop_limit_counter_param import PatternFlowIpv6HopLimitCounterParam
from .pattern_flow_gtpv2_teid_flag_counter_param import PatternFlowGtpv2TeidFlagCounterParam
from .pattern_flow_ipv4_tos_unused_counter_param import PatternFlowIpv4TosUnusedCounterParam
from .pattern_flow_ipv6_flow_label_counter_param import PatternFlowIpv6FlowLabelCounterParam
from .pattern_flow_snmpv2c_version_counter_param import PatternFlowSnmpv2cVersionCounterParam
from .pattern_flow_tcp_data_offset_counter_param import PatternFlowTcpDataOffsetCounterParam
from .pattern_flow_vxlan_reserved0_counter_param import PatternFlowVxlanReserved0CounterParam
from .pattern_flow_vxlan_reserved1_counter_param import PatternFlowVxlanReserved1CounterParam
from .pattern_flow_icmpv6_echo_code_counter_param import PatternFlowIcmpv6EchoCodeCounterParam
from .pattern_flow_icmpv6_echo_type_counter_param import PatternFlowIcmpv6EchoTypeCounterParam
from .pattern_flow_ipv6_next_header_counter_param import PatternFlowIpv6NextHeaderCounterParam
from .pattern_flow_arp_hardware_type_counter_param import PatternFlowArpHardwareTypeCounterParam
from .pattern_flow_arp_protocol_type_counter_param import PatternFlowArpProtocolTypeCounterParam
from .pattern_flow_ipv4_priority_raw_counter_param import PatternFlowIpv4PriorityRawCounterParam
from .pattern_flow_ipv4_time_to_live_counter_param import PatternFlowIpv4TimeToLiveCounterParam
from .pattern_flow_ipv4_tos_monetary_counter_param import PatternFlowIpv4TosMonetaryCounterParam
from .pattern_flow_ipv4_total_length_counter_param import PatternFlowIpv4TotalLengthCounterParam
from .pattern_flow_mpls_time_to_live_counter_param import PatternFlowMplsTimeToLiveCounterParam
from .pattern_flow_ppp_protocol_type_counter_param import PatternFlowPppProtocolTypeCounterParam
from .pattern_flow_rsvp_time_to_live_counter_param import PatternFlowRsvpTimeToLiveCounterParam
from .flow_rsvp_session_attribute_name_length_param import FlowRsvpSessionAttributeNameLengthParam
from .pattern_flow_ethernet_pause_dst_counter_param import PatternFlowEthernetPauseDstCounterParam
from .pattern_flow_ethernet_pause_src_counter_param import PatternFlowEthernetPauseSrcCounterParam
from .pattern_flow_ethernet_pfc_queue_counter_param import PatternFlowEthernetPfcQueueCounterParam
from .pattern_flow_gtpv1_message_type_counter_param import PatternFlowGtpv1MessageTypeCounterParam
from .pattern_flow_gtpv1_n_pdu_number_counter_param import PatternFlowGtpv1NPduNumberCounterParam
from .pattern_flow_gtpv2_message_type_counter_param import PatternFlowGtpv2MessageTypeCounterParam
from .pattern_flow_ipv4_dont_fragment_counter_param import PatternFlowIpv4DontFragmentCounterParam
from .pattern_flow_ipv4_header_length_counter_param import PatternFlowIpv4HeaderLengthCounterParam
from .pattern_flow_ipv6_traffic_class_counter_param import PatternFlowIpv6TrafficClassCounterParam
from .pattern_flow_mpls_traffic_class_counter_param import PatternFlowMplsTrafficClassCounterParam
from .pattern_flow_arp_hardware_length_counter_param import PatternFlowArpHardwareLengthCounterParam
from .pattern_flow_arp_protocol_length_counter_param import PatternFlowArpProtocolLengthCounterParam
from .pattern_flow_ethernet_ether_type_counter_param import PatternFlowEthernetEtherTypeCounterParam
from .pattern_flow_ethernet_pause_time_counter_param import PatternFlowEthernetPauseTimeCounterParam
from .pattern_flow_gtpv1_protocol_type_counter_param import PatternFlowGtpv1ProtocolTypeCounterParam
from .pattern_flow_ipv4_identification_counter_param import PatternFlowIpv4IdentificationCounterParam
from .pattern_flow_ipv4_more_fragments_counter_param import PatternFlowIpv4MoreFragmentsCounterParam
from .pattern_flow_ipv4_tos_precedence_counter_param import PatternFlowIpv4TosPrecedenceCounterParam
from .pattern_flow_ipv4_tos_throughput_counter_param import PatternFlowIpv4TosThroughputCounterParam
from .pattern_flow_ipv6_payload_length_counter_param import PatternFlowIpv6PayloadLengthCounterParam
from .pattern_flow_gre_checksum_present_counter_param import PatternFlowGreChecksumPresentCounterParam
from .pattern_flow_gtpv1_message_length_counter_param import PatternFlowGtpv1MessageLengthCounterParam
from .pattern_flow_gtpv1_squence_number_counter_param import PatternFlowGtpv1SquenceNumberCounterParam
from .pattern_flow_gtpv2_message_length_counter_param import PatternFlowGtpv2MessageLengthCounterParam
from .pattern_flow_icmp_echo_identifier_counter_param import PatternFlowIcmpEchoIdentifierCounterParam
from .pattern_flow_igmpv1_group_address_counter_param import PatternFlowIgmpv1GroupAddressCounterParam
from .pattern_flow_ipv4_fragment_offset_counter_param import PatternFlowIpv4FragmentOffsetCounterParam
from .pattern_flow_ipv4_tos_reliability_counter_param import PatternFlowIpv4TosReliabilityCounterParam
from .pattern_flow_mpls_bottom_of_stack_counter_param import PatternFlowMplsBottomOfStackCounterParam
from .pattern_flow_pfc_pause_ether_type_counter_param import PatternFlowPfcPauseEtherTypeCounterParam
from .pattern_flow_gtpv2_sequence_number_counter_param import PatternFlowGtpv2SequenceNumberCounterParam
from .pattern_flow_gtp_extension_contents_counter_param import PatternFlowGtpExtensionContentsCounterParam
from .pattern_flow_icmpv6_echo_identifier_counter_param import PatternFlowIcmpv6EchoIdentifierCounterParam
from .pattern_flow_pfc_pause_pause_class0_counter_param import PatternFlowPfcPausePauseClass0CounterParam
from .pattern_flow_pfc_pause_pause_class1_counter_param import PatternFlowPfcPausePauseClass1CounterParam
from .pattern_flow_pfc_pause_pause_class2_counter_param import PatternFlowPfcPausePauseClass2CounterParam
from .pattern_flow_pfc_pause_pause_class3_counter_param import PatternFlowPfcPausePauseClass3CounterParam
from .pattern_flow_pfc_pause_pause_class4_counter_param import PatternFlowPfcPausePauseClass4CounterParam
from .pattern_flow_pfc_pause_pause_class5_counter_param import PatternFlowPfcPausePauseClass5CounterParam
from .pattern_flow_pfc_pause_pause_class6_counter_param import PatternFlowPfcPausePauseClass6CounterParam
from .pattern_flow_pfc_pause_pause_class7_counter_param import PatternFlowPfcPausePauseClass7CounterParam
from .pattern_flow_gtpv2_piggybacking_flag_counter_param import PatternFlowGtpv2PiggybackingFlagCounterParam
from .pattern_flow_arp_sender_hardware_addr_counter_param import PatternFlowArpSenderHardwareAddrCounterParam
from .pattern_flow_arp_sender_protocol_addr_counter_param import PatternFlowArpSenderProtocolAddrCounterParam
from .pattern_flow_arp_target_hardware_addr_counter_param import PatternFlowArpTargetHardwareAddrCounterParam
from .pattern_flow_arp_target_protocol_addr_counter_param import PatternFlowArpTargetProtocolAddrCounterParam
from .pattern_flow_ethernet_pause_ether_type_counter_param import PatternFlowEthernetPauseEtherTypeCounterParam
from .pattern_flow_icmp_echo_sequence_number_counter_param import PatternFlowIcmpEchoSequenceNumberCounterParam
from .pattern_flow_pfc_pause_control_op_code_counter_param import PatternFlowPfcPauseControlOpCodeCounterParam
from .pattern_flow_icmpv6_echo_sequence_number_counter_param import PatternFlowIcmpv6EchoSequenceNumberCounterParam
from .pattern_flow_snmpv2c_bulk_pdu_request_id_counter_param import PatternFlowSnmpv2cBulkPduRequestIDCounterParam
from .pattern_flow_pfc_pause_class_enable_vector_counter_param import PatternFlowPfcPauseClassEnableVectorCounterParam
from .pattern_flow_rsvp_path_objects_custom_type_counter_param import PatternFlowRsvpPathObjectsCustomTypeCounterParam
from .pattern_flow_ethernet_pause_control_op_code_counter_param import PatternFlowEthernetPauseControlOpCodeCounterParam
from .pattern_flow_gtp_extension_extension_length_counter_param import (
    PatternFlowGtpExtensionExtensionLengthCounterParam,
)
from .pattern_flow_gtpv1_next_extension_header_type_counter_param import (
    PatternFlowGtpv1NextExtensionHeaderTypeCounterParam,
)
from .pattern_flow_snmpv2c_bulk_pdu_max_repetitions_counter_param import (
    PatternFlowSnmpv2cBulkPduMaxRepetitionsCounterParam,
)
from .pattern_flow_gtp_extension_next_extension_header_counter_param import (
    PatternFlowGtpExtensionNextExtensionHeaderCounterParam,
)
from .pattern_flow_ipv4_options_custom_type_copied_flag_counter_param import (
    PatternFlowIpv4OptionsCustomTypeCopiedFlagCounterParam,
)
from .pattern_flow_rsvp_path_rsvp_hop_ipv4_ipv4_address_counter_param import (
    PatternFlowRsvpPathRsvpHopIpv4Ipv4AddressCounterParam,
)
from .pattern_flow_ipv4_options_custom_type_option_class_counter_param import (
    PatternFlowIpv4OptionsCustomTypeOptionClassCounterParam,
)
from .pattern_flow_ipv4_options_custom_type_option_number_counter_param import (
    PatternFlowIpv4OptionsCustomTypeOptionNumberCounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_version_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServVersionCounterParam,
)
from .pattern_flow_rsvp_path_session_ext_tunnel_id_as_ipv4_counter_param import (
    PatternFlowRsvpPathSessionExtTunnelIDAsIpv4CounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_zero_bit_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServZeroBitCounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_reserved1_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServReserved1CounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_reserved2_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServReserved2CounterParam,
)
from .pattern_flow_rsvp_path_session_ext_tunnel_id_as_integer_counter_param import (
    PatternFlowRsvpPathSessionExtTunnelIDAsIntegerCounterParam,
)
from .pattern_flow_rsvp_path_session_lsp_tunnel_ipv4_reserved_counter_param import (
    PatternFlowRsvpPathSessionLspTunnelIpv4ReservedCounterParam,
)
from .pattern_flow_rsvp_path_session_lsp_tunnel_ipv4_tunnel_id_counter_param import (
    PatternFlowRsvpPathSessionLspTunnelIpv4TunnelIDCounterParam,
)
from .pattern_flow_rsvp_path_time_values_type1_refresh_period_r_counter_param import (
    PatternFlowRsvpPathTimeValuesType1RefreshPeriodRCounterParam,
)
from .pattern_flow_rsvp_path_explicit_route_type1_as_number_l_bit_counter_param import (
    PatternFlowRsvpPathExplicitRouteType1AsNumberLBitCounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_overall_length_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServOverallLengthCounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_service_header_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServServiceHeaderCounterParam,
)
from .pattern_flow_rsvp_path_explicit_route_type1_ipv4_prefix_l_bit_counter_param import (
    PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixLBitCounterParam,
)
from .pattern_flow_rsvp_path_rsvp_hop_ipv4_logical_interface_handle_counter_param import (
    PatternFlowRsvpPathRsvpHopIpv4LogicalInterfaceHandleCounterParam,
)
from .pattern_flow_rsvp_path_sender_template_lsp_tunnel_ipv4_lsp_id_counter_param import (
    PatternFlowRsvpPathSenderTemplateLspTunnelIpv4LspIDCounterParam,
)
from .pattern_flow_rsvp_path_label_request_without_label_range_l3pid_counter_param import (
    PatternFlowRsvpPathLabelRequestWithoutLabelRangeL3pidCounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_parameter127_flag_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServParameter127FlagCounterParam,
)
from .pattern_flow_rsvp_path_sender_template_lsp_tunnel_ipv4_reserved_counter_param import (
    PatternFlowRsvpPathSenderTemplateLspTunnelIpv4ReservedCounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_maximum_packet_size_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServMaximumPacketSizeCounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_parameter127_length_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServParameter127LengthCounterParam,
)
from .pattern_flow_rsvp_path_label_request_without_label_range_reserved_counter_param import (
    PatternFlowRsvpPathLabelRequestWithoutLabelRangeReservedCounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_minimum_policed_unit_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServMinimumPolicedUnitCounterParam,
)
from .pattern_flow_rsvp_path_record_route_type1_ipv4_address_ipv4_address_counter_param import (
    PatternFlowRsvpPathRecordRouteType1Ipv4AddressIpv4AddressCounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_length_of_service_data_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServLengthOfServiceDataCounterParam,
)
from .pattern_flow_rsvp_path_explicit_route_type1_ipv4_prefix_ipv4_address_counter_param import (
    PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixIpv4AddressCounterParam,
)
from .pattern_flow_rsvp_path_record_route_type1_ipv4_address_prefix_length_counter_param import (
    PatternFlowRsvpPathRecordRouteType1Ipv4AddressPrefixLengthCounterParam,
)
from .pattern_flow_rsvp_path_sender_tspec_int_serv_parameter_id_token_bucket_tspec_counter_param import (
    PatternFlowRsvpPathSenderTspecIntServParameterIDTokenBucketTspecCounterParam,
)
from .pattern_flow_rsvp_path_session_lsp_tunnel_ipv4_ipv4_tunnel_end_point_address_counter_param import (
    PatternFlowRsvpPathSessionLspTunnelIpv4Ipv4TunnelEndPointAddressCounterParam,
)
from .pattern_flow_rsvp_path_sender_template_lsp_tunnel_ipv4_ipv4_tunnel_sender_address_counter_param import (
    PatternFlowRsvpPathSenderTemplateLspTunnelIpv4Ipv4TunnelSenderAddressCounterParam,
)

__all__ = [
    "FlowHeaderParam",
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


class ArpHardwareLengthMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class ArpHardwareLength(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowArpHardwareLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowArpHardwareLengthCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[ArpHardwareLengthMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class ArpHardwareTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class ArpHardwareType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowArpHardwareTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowArpHardwareTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[ArpHardwareTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class ArpOperationMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class ArpOperation(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowArpOperationCounterParam
    """integer counter pattern"""

    increment: PatternFlowArpOperationCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[ArpOperationMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class ArpProtocolLengthMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class ArpProtocolLength(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowArpProtocolLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowArpProtocolLengthCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[ArpProtocolLengthMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class ArpProtocolTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class ArpProtocolType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowArpProtocolTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowArpProtocolTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[ArpProtocolTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class ArpSenderHardwareAddrMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class ArpSenderHardwareAddr(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowArpSenderHardwareAddrCounterParam
    """mac counter pattern"""

    increment: PatternFlowArpSenderHardwareAddrCounterParam
    """mac counter pattern"""

    metric_tags: Iterable[ArpSenderHardwareAddrMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class ArpSenderProtocolAddrMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class ArpSenderProtocolAddr(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowArpSenderProtocolAddrCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowArpSenderProtocolAddrCounterParam
    """ipv4 counter pattern"""

    metric_tags: Iterable[ArpSenderProtocolAddrMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class ArpTargetHardwareAddrMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class ArpTargetHardwareAddr(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowArpTargetHardwareAddrCounterParam
    """mac counter pattern"""

    increment: PatternFlowArpTargetHardwareAddrCounterParam
    """mac counter pattern"""

    metric_tags: Iterable[ArpTargetHardwareAddrMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class ArpTargetProtocolAddrMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class ArpTargetProtocolAddr(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowArpTargetProtocolAddrCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowArpTargetProtocolAddrCounterParam
    """ipv4 counter pattern"""

    metric_tags: Iterable[ArpTargetProtocolAddrMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class Arp(TypedDict, total=False):
    hardware_length: ArpHardwareLength
    """Length (in octets) of a hardware address"""

    hardware_type: ArpHardwareType
    """Network link protocol type"""

    operation: ArpOperation
    """The operation that the sender is performing"""

    protocol_length: ArpProtocolLength
    """Length (in octets) of internetwork addresses"""

    protocol_type: ArpProtocolType
    """The internetwork protocol for which the ARP request is intended"""

    sender_hardware_addr: ArpSenderHardwareAddr
    """Media address of the sender"""

    sender_protocol_addr: ArpSenderProtocolAddr
    """Internetwork address of the sender"""

    target_hardware_addr: ArpTargetHardwareAddr
    """Media address of the target"""

    target_protocol_addr: ArpTargetProtocolAddr
    """Internetwork address of the target"""


class CustomMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Custom(TypedDict, total=False):
    bytes: Required[str]
    """A custom packet header defined as a string of hex bytes.

    The string MUST contain sequence of valid hex bytes. Spaces or colons can be
    part of the bytes but will be discarded. This packet header can be used in
    multiple places in the packet.
    """

    metric_tags: Iterable[CustomMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """


class EthernetDstMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class EthernetDst(TypedDict, total=False):
    auto: str
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowEthernetDstCounterParam
    """mac counter pattern"""

    increment: PatternFlowEthernetDstCounterParam
    """mac counter pattern"""

    metric_tags: Iterable[EthernetDstMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class EthernetEtherTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class EthernetEtherType(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowEthernetEtherTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowEthernetEtherTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[EthernetEtherTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class EthernetPfcQueueMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class EthernetPfcQueue(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowEthernetPfcQueueCounterParam
    """integer counter pattern"""

    increment: PatternFlowEthernetPfcQueueCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[EthernetPfcQueueMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class EthernetSrcMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class EthernetSrc(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowEthernetSrcCounterParam
    """mac counter pattern"""

    increment: PatternFlowEthernetSrcCounterParam
    """mac counter pattern"""

    metric_tags: Iterable[EthernetSrcMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class Ethernet(TypedDict, total=False):
    dst: EthernetDst
    """Destination MAC address"""

    ether_type: EthernetEtherType
    """Ethernet type"""

    pfc_queue: EthernetPfcQueue
    """Priority flow control queue"""

    src: EthernetSrc
    """Source MAC address"""


class EthernetpauseControlOpCodeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class EthernetpauseControlOpCode(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowEthernetPauseControlOpCodeCounterParam
    """integer counter pattern"""

    increment: PatternFlowEthernetPauseControlOpCodeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[EthernetpauseControlOpCodeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class EthernetpauseDstMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class EthernetpauseDst(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowEthernetPauseDstCounterParam
    """mac counter pattern"""

    increment: PatternFlowEthernetPauseDstCounterParam
    """mac counter pattern"""

    metric_tags: Iterable[EthernetpauseDstMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class EthernetpauseEtherTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class EthernetpauseEtherType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowEthernetPauseEtherTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowEthernetPauseEtherTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[EthernetpauseEtherTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class EthernetpauseSrcMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class EthernetpauseSrc(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowEthernetPauseSrcCounterParam
    """mac counter pattern"""

    increment: PatternFlowEthernetPauseSrcCounterParam
    """mac counter pattern"""

    metric_tags: Iterable[EthernetpauseSrcMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class EthernetpauseTimeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class EthernetpauseTime(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowEthernetPauseTimeCounterParam
    """integer counter pattern"""

    increment: PatternFlowEthernetPauseTimeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[EthernetpauseTimeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ethernetpause(TypedDict, total=False):
    control_op_code: EthernetpauseControlOpCode
    """Control operation code"""

    dst: EthernetpauseDst
    """Destination MAC address"""

    ether_type: EthernetpauseEtherType
    """Ethernet type"""

    src: EthernetpauseSrc
    """Source MAC address"""

    time: EthernetpauseTime
    """Time"""


class GreChecksum(TypedDict, total=False):
    choice: Literal["generated", "custom"]
    """The type of checksum"""

    custom: int
    """A custom checksum value"""

    generated: Literal["good", "bad"]
    """A system generated checksum value"""


class GreChecksumPresentMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class GreChecksumPresent(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGreChecksumPresentCounterParam
    """integer counter pattern"""

    increment: PatternFlowGreChecksumPresentCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[GreChecksumPresentMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class GreProtocolMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class GreProtocol(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "increment", "decrement", "auto"]

    decrement: PatternFlowGreProtocolCounterParam
    """integer counter pattern"""

    increment: PatternFlowGreProtocolCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[GreProtocolMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class GreReserved0MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class GreReserved0(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGreReserved0CounterParam
    """integer counter pattern"""

    increment: PatternFlowGreReserved0CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[GreReserved0MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class GreReserved1MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class GreReserved1(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGreReserved1CounterParam
    """integer counter pattern"""

    increment: PatternFlowGreReserved1CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[GreReserved1MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class GreVersionMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class GreVersion(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGreVersionCounterParam
    """integer counter pattern"""

    increment: PatternFlowGreVersionCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[GreVersionMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gre(TypedDict, total=False):
    checksum: GreChecksum
    """Optional checksum of GRE header and payload.

    Only present if the checksum_present bit is set.
    """

    checksum_present: GreChecksumPresent
    """Checksum present bit"""

    protocol: GreProtocol
    """Protocol type of encapsulated payload"""

    reserved0: GreReserved0
    """Reserved bits"""

    reserved1: GreReserved1
    """Optional reserved field. Only present if the checksum_present bit is set."""

    version: GreVersion
    """GRE version number"""


class Gtpv1EFlagMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1EFlag(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1EFlagCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1EFlagCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1EFlagMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1ExtensionHeaderContentsMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1ExtensionHeaderContents(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpExtensionContentsCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpExtensionContentsCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1ExtensionHeaderContentsMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1ExtensionHeaderExtensionLengthMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1ExtensionHeaderExtensionLength(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpExtensionExtensionLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpExtensionExtensionLengthCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1ExtensionHeaderExtensionLengthMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1ExtensionHeaderNextExtensionHeaderMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1ExtensionHeaderNextExtensionHeader(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpExtensionNextExtensionHeaderCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpExtensionNextExtensionHeaderCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1ExtensionHeaderNextExtensionHeaderMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1ExtensionHeader(TypedDict, total=False):
    contents: Gtpv1ExtensionHeaderContents
    """The extension header contents"""

    extension_length: Gtpv1ExtensionHeaderExtensionLength
    """
    This field states the length of this extension header, including the length, the
    contents, and the next extension header field, in 4-octet units, so the length
    of the extension must always be a multiple of 4.
    """

    next_extension_header: Gtpv1ExtensionHeaderNextExtensionHeader
    """It states the type of the next extension, or 0 if no next extension exists.

    This permits chaining several next extension headers.
    """


class Gtpv1MessageLengthMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1MessageLength(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1MessageLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1MessageLengthCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1MessageLengthMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1MessageTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1MessageType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1MessageTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1MessageTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1MessageTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1NPduNumberMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1NPduNumber(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1NPduNumberCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1NPduNumberCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1NPduNumberMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1NextExtensionHeaderTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1NextExtensionHeaderType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1NextExtensionHeaderTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1NextExtensionHeaderTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1NextExtensionHeaderTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1PnFlagMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1PnFlag(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1PnFlagCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1PnFlagCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1PnFlagMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1ProtocolTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1ProtocolType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1ProtocolTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1ProtocolTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1ProtocolTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1ReservedMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1Reserved(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1ReservedCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1ReservedCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1ReservedMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1SFlagMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1SFlag(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1SFlagCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1SFlagCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1SFlagMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1SquenceNumberMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1SquenceNumber(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1SquenceNumberCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1SquenceNumberCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1SquenceNumberMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1TeidMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1Teid(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1TeidCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1TeidCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1TeidMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1VersionMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv1Version(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv1VersionCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv1VersionCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv1VersionMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv1(TypedDict, total=False):
    e_flag: Gtpv1EFlag
    """Extension header field present"""

    extension_headers: Iterable[Gtpv1ExtensionHeader]
    """A list of optional extension headers."""

    message_length: Gtpv1MessageLength
    """
    The length of the payload (the bytes following the mandatory 8-byte GTP header)
    in bytes that includes any optional fields
    """

    message_type: Gtpv1MessageType
    """
    The type of GTP message Different types of messages are defined in 3GPP TS
    29.060 section 7.1
    """

    n_pdu_number: Gtpv1NPduNumber
    """N-PDU number.

    Exists if any of the e_flag, s_flag, or pn_flag bits are on. Must be interpreted
    only if the pn_flag bit is on.
    """

    next_extension_header_type: Gtpv1NextExtensionHeaderType
    """Next extension header.

    Exists if any of the e_flag, s_flag, or pn_flag bits are on. Must be interpreted
    only if the e_flag bit is on.
    """

    pn_flag: Gtpv1PnFlag
    """N-PDU field present"""

    protocol_type: Gtpv1ProtocolType
    """Protocol type, GTP is 1, GTP' is 0"""

    reserved: Gtpv1Reserved
    """Reserved field"""

    s_flag: Gtpv1SFlag
    """Sequence number field present"""

    squence_number: Gtpv1SquenceNumber
    """Sequence number.

    Exists if any of the e_flag, s_flag, or pn_flag bits are on. Must be interpreted
    only if the s_flag bit is on.
    """

    teid: Gtpv1Teid
    """
    Tunnel endpoint identifier (TEID) used to multiplex connections in the same GTP
    tunnel
    """

    version: Gtpv1Version
    """GTPv1 version"""


class Gtpv2MessageLengthMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2MessageLength(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv2MessageLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv2MessageLengthCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv2MessageLengthMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv2MessageTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2MessageType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv2MessageTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv2MessageTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv2MessageTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv2PiggybackingFlagMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2PiggybackingFlag(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv2PiggybackingFlagCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv2PiggybackingFlagCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv2PiggybackingFlagMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv2SequenceNumberMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2SequenceNumber(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv2SequenceNumberCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv2SequenceNumberCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv2SequenceNumberMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv2Spare1MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2Spare1(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv2Spare1CounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv2Spare1CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv2Spare1MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv2Spare2MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2Spare2(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv2Spare2CounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv2Spare2CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv2Spare2MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv2TeidMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2Teid(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv2TeidCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv2TeidCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv2TeidMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv2TeidFlagMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2TeidFlag(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv2TeidFlagCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv2TeidFlagCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv2TeidFlagMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv2VersionMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Gtpv2Version(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowGtpv2VersionCounterParam
    """integer counter pattern"""

    increment: PatternFlowGtpv2VersionCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Gtpv2VersionMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Gtpv2(TypedDict, total=False):
    message_length: Gtpv2MessageLength
    """
    A 16-bit field that indicates the length of the payload in bytes, excluding the
    mandatory GTP-c header (first 4 bytes). Includes the TEID and sequence_number if
    they are present.
    """

    message_type: Gtpv2MessageType
    """An 8-bit field that indicates the type of GTP message.

    Different types of messages are defined in 3GPP TS 29.060 section 7.1
    """

    piggybacking_flag: Gtpv2PiggybackingFlag
    """
    If piggybacking_flag is set to 1 then another GTP-C message with its own header
    shall be present at the end of the current message
    """

    sequence_number: Gtpv2SequenceNumber
    """The sequence number"""

    spare1: Gtpv2Spare1
    """A 3-bit reserved field (must be 0)."""

    spare2: Gtpv2Spare2
    """Reserved field"""

    teid: Gtpv2Teid
    """Tunnel endpoint identifier.

    A 32-bit (4-octet) field used to multiplex different connections in the same GTP
    tunnel. Is present only if the teid_flag is set.
    """

    teid_flag: Gtpv2TeidFlag
    """
    If teid_flag is set to 1 then the TEID field will be present between the message
    length and the sequence number. All messages except Echo and Echo reply require
    TEID to be present
    """

    version: Gtpv2Version
    """Version number"""


class IcmpEchoChecksum(TypedDict, total=False):
    choice: Literal["generated", "custom"]
    """The type of checksum"""

    custom: int
    """A custom checksum value"""

    generated: Literal["good", "bad"]
    """A system generated checksum value"""


class IcmpEchoCodeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class IcmpEchoCode(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIcmpEchoCodeCounterParam
    """integer counter pattern"""

    increment: PatternFlowIcmpEchoCodeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[IcmpEchoCodeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class IcmpEchoIdentifierMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class IcmpEchoIdentifier(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIcmpEchoIdentifierCounterParam
    """integer counter pattern"""

    increment: PatternFlowIcmpEchoIdentifierCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[IcmpEchoIdentifierMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class IcmpEchoSequenceNumberMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class IcmpEchoSequenceNumber(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIcmpEchoSequenceNumberCounterParam
    """integer counter pattern"""

    increment: PatternFlowIcmpEchoSequenceNumberCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[IcmpEchoSequenceNumberMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class IcmpEchoTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class IcmpEchoType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIcmpEchoTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowIcmpEchoTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[IcmpEchoTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class IcmpEcho(TypedDict, total=False):
    checksum: IcmpEchoChecksum
    """ICMP checksum"""

    code: IcmpEchoCode
    """The ICMP subtype. The default code for ICMP echo request and reply is 0."""

    identifier: IcmpEchoIdentifier
    """ICMP identifier"""

    sequence_number: IcmpEchoSequenceNumber
    """ICMP sequence number"""

    type: IcmpEchoType
    """The type of ICMP echo packet"""


class Icmp(TypedDict, total=False):
    choice: Literal["echo"]

    echo: IcmpEcho
    """Packet Header for ICMP echo request"""


class Icmpv6EchoChecksum(TypedDict, total=False):
    choice: Literal["generated", "custom"]
    """The type of checksum"""

    custom: int
    """A custom checksum value"""

    generated: Literal["good", "bad"]
    """A system generated checksum value"""


class Icmpv6EchoCodeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Icmpv6EchoCode(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIcmpv6EchoCodeCounterParam
    """integer counter pattern"""

    increment: PatternFlowIcmpv6EchoCodeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Icmpv6EchoCodeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Icmpv6EchoIdentifierMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Icmpv6EchoIdentifier(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIcmpv6EchoIdentifierCounterParam
    """integer counter pattern"""

    increment: PatternFlowIcmpv6EchoIdentifierCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Icmpv6EchoIdentifierMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Icmpv6EchoSequenceNumberMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Icmpv6EchoSequenceNumber(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIcmpv6EchoSequenceNumberCounterParam
    """integer counter pattern"""

    increment: PatternFlowIcmpv6EchoSequenceNumberCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Icmpv6EchoSequenceNumberMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Icmpv6EchoTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Icmpv6EchoType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIcmpv6EchoTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowIcmpv6EchoTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Icmpv6EchoTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Icmpv6Echo(TypedDict, total=False):
    checksum: Icmpv6EchoChecksum
    """ICMPv6 checksum"""

    code: Icmpv6EchoCode
    """ICMPv6 echo sub type"""

    identifier: Icmpv6EchoIdentifier
    """ICMPv6 echo identifier"""

    sequence_number: Icmpv6EchoSequenceNumber
    """ICMPv6 echo sequence number"""

    type: Icmpv6EchoType
    """ICMPv6 echo type"""


class Icmpv6(TypedDict, total=False):
    choice: Literal["echo"]

    echo: Icmpv6Echo
    """Packet Header for ICMPv6 Echo"""


class Igmpv1Checksum(TypedDict, total=False):
    choice: Literal["generated", "custom"]
    """The type of checksum"""

    custom: int
    """A custom checksum value"""

    generated: Literal["good", "bad"]
    """A system generated checksum value"""


class Igmpv1GroupAddressMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Igmpv1GroupAddress(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIgmpv1GroupAddressCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowIgmpv1GroupAddressCounterParam
    """ipv4 counter pattern"""

    metric_tags: Iterable[Igmpv1GroupAddressMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class Igmpv1TypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Igmpv1Type(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIgmpv1TypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowIgmpv1TypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Igmpv1TypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Igmpv1UnusedMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Igmpv1Unused(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIgmpv1UnusedCounterParam
    """integer counter pattern"""

    increment: PatternFlowIgmpv1UnusedCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Igmpv1UnusedMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Igmpv1VersionMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Igmpv1Version(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIgmpv1VersionCounterParam
    """integer counter pattern"""

    increment: PatternFlowIgmpv1VersionCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Igmpv1VersionMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Igmpv1(TypedDict, total=False):
    checksum: Igmpv1Checksum
    """Checksum"""

    group_address: Igmpv1GroupAddress
    """Group address"""

    type: Igmpv1Type
    """Type of message"""

    unused: Igmpv1Unused
    """Unused"""

    version: Igmpv1Version
    """Version number"""


class Ipv4DontFragmentMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4DontFragment(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4DontFragmentCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4DontFragmentCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4DontFragmentMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4DstMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4DstRandom(TypedDict, total=False):
    count: int
    """The total number of values to be generated by the random value generator."""

    max: str
    """The maximum possible value generated by the random value generator."""

    min: str
    """The minimum possible value generated by the random value generator."""

    seed: int
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class Ipv4Dst(TypedDict, total=False):
    auto: FlowIpv4AutoParam
    """The OTG implementation can provide a system generated, value for this property."""

    choice: Literal["value", "values", "increment", "decrement", "auto", "random"]

    decrement: PatternFlowIpv4DstCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowIpv4DstCounterParam
    """ipv4 counter pattern"""

    metric_tags: Iterable[Ipv4DstMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: Ipv4DstRandom
    """ipv4 random pattern"""

    value: str

    values: List[str]


class Ipv4FragmentOffsetMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4FragmentOffset(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4FragmentOffsetCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4FragmentOffsetCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4FragmentOffsetMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4HeaderChecksum(TypedDict, total=False):
    choice: Literal["generated", "custom"]
    """The type of checksum"""

    custom: int
    """A custom checksum value"""

    generated: Literal["good", "bad"]
    """A system generated checksum value"""


class Ipv4HeaderLengthMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4HeaderLength(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowIpv4HeaderLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4HeaderLengthCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4HeaderLengthMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4IdentificationMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4Identification(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4IdentificationCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4IdentificationCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4IdentificationMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4MoreFragmentsMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4MoreFragments(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4MoreFragmentsCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4MoreFragmentsCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4MoreFragmentsMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4OptionCustomLength(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["auto", "value"]
    """auto or configured value."""

    value: int


class Ipv4OptionCustomTypeCopiedFlag(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4OptionsCustomTypeCopiedFlagCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4OptionsCustomTypeCopiedFlagCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class Ipv4OptionCustomTypeOptionClass(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4OptionsCustomTypeOptionClassCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4OptionsCustomTypeOptionClassCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class Ipv4OptionCustomTypeOptionNumber(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4OptionsCustomTypeOptionNumberCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4OptionsCustomTypeOptionNumberCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class Ipv4OptionCustomType(TypedDict, total=False):
    copied_flag: Ipv4OptionCustomTypeCopiedFlag
    """This flag indicates this option is copied to all fragments on fragmentations."""

    option_class: Ipv4OptionCustomTypeOptionClass
    """
    Option class
    [Ref:https://www.iana.org/assignments/ip-parameters/ip-parameters.xhtml#ip-parameters-1].
    """

    option_number: Ipv4OptionCustomTypeOptionNumber
    """
    Option Number
    [Ref:https://www.iana.org/assignments/ip-parameters/ip-parameters.xhtml#ip-parameters-1].
    """


class Ipv4OptionCustom(TypedDict, total=False):
    length: Ipv4OptionCustomLength
    """Length for custom options."""

    type: Ipv4OptionCustomType
    """Type options for custom options."""

    value: str
    """
    Value of the option field should not excced 38 bytes since maximum 40 bytes can
    be added as options in IPv4 header. For type and length requires 2 bytes, hence
    maximum of 38 bytes are expected. Maximum length of this attribute is 76 (38 \\**
    2 hex character per byte).
    """


class Ipv4Option(TypedDict, total=False):
    choice: Literal["router_alert", "custom"]

    custom: Ipv4OptionCustom
    """User defined IP options to be appended to the IPv4 header."""


class Ipv4PriorityDscpEcnMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityDscpEcn(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4DscpEcnCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4DscpEcnCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4PriorityDscpEcnMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4PriorityDscpPhbMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityDscpPhb(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4DscpPhbCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4DscpPhbCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4PriorityDscpPhbMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4PriorityDscp(TypedDict, total=False):
    ecn: Ipv4PriorityDscpEcn
    """Explicit congestion notification"""

    phb: Ipv4PriorityDscpPhb
    """Per hop behavior"""


class Ipv4PriorityRawMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityRaw(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4PriorityRawCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4PriorityRawCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4PriorityRawMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4PriorityTosDelayMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosDelay(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4TosDelayCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4TosDelayCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4PriorityTosDelayMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4PriorityTosMonetaryMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosMonetary(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4TosMonetaryCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4TosMonetaryCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4PriorityTosMonetaryMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4PriorityTosPrecedenceMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosPrecedence(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4TosPrecedenceCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4TosPrecedenceCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4PriorityTosPrecedenceMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4PriorityTosReliabilityMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosReliability(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4TosReliabilityCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4TosReliabilityCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4PriorityTosReliabilityMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4PriorityTosThroughputMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosThroughput(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4TosThroughputCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4TosThroughputCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4PriorityTosThroughputMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4PriorityTosUnusedMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4PriorityTosUnused(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4TosUnusedCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4TosUnusedCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4PriorityTosUnusedMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4PriorityTos(TypedDict, total=False):
    delay: Ipv4PriorityTosDelay
    """Delay"""

    monetary: Ipv4PriorityTosMonetary
    """Monetary"""

    precedence: Ipv4PriorityTosPrecedence
    """Precedence"""

    reliability: Ipv4PriorityTosReliability
    """Reliability"""

    throughput: Ipv4PriorityTosThroughput
    """Throughput"""

    unused: Ipv4PriorityTosUnused
    """Unused"""


class Ipv4Priority(TypedDict, total=False):
    choice: Literal["raw", "tos", "dscp"]

    dscp: Ipv4PriorityDscp
    """Differentiated services code point (DSCP) packet field."""

    raw: Ipv4PriorityRaw
    """Raw priority"""

    tos: Ipv4PriorityTos
    """Type of service (TOS) packet field."""


class Ipv4ProtocolMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4Protocol(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowIpv4ProtocolCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4ProtocolCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4ProtocolMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4ReservedMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4Reserved(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4ReservedCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4ReservedCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4ReservedMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4SrcMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4SrcRandom(TypedDict, total=False):
    count: int
    """The total number of values to be generated by the random value generator."""

    max: str
    """The maximum possible value generated by the random value generator."""

    min: str
    """The minimum possible value generated by the random value generator."""

    seed: int
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class Ipv4Src(TypedDict, total=False):
    auto: FlowIpv4AutoParam
    """The OTG implementation can provide a system generated, value for this property."""

    choice: Literal["value", "values", "increment", "decrement", "auto", "random"]

    decrement: PatternFlowIpv4SrcCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowIpv4SrcCounterParam
    """ipv4 counter pattern"""

    metric_tags: Iterable[Ipv4SrcMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: Ipv4SrcRandom
    """ipv4 random pattern"""

    value: str

    values: List[str]


class Ipv4TimeToLiveMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4TimeToLive(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4TimeToLiveCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4TimeToLiveCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4TimeToLiveMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4TotalLengthMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4TotalLength(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowIpv4TotalLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4TotalLengthCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4TotalLengthMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4VersionMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv4Version(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv4VersionCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv4VersionCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv4VersionMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv4(TypedDict, total=False):
    dont_fragment: Ipv4DontFragment
    """
    Dont fragment flag If the dont_fragment flag is set and fragmentation is
    required to route the packet then the packet is dropped.
    """

    dst: Ipv4Dst
    """Destination address"""

    fragment_offset: Ipv4FragmentOffset
    """Fragment offset"""

    header_checksum: Ipv4HeaderChecksum
    """Header checksum"""

    header_length: Ipv4HeaderLength
    """Header length"""

    identification: Ipv4Identification
    """Identification"""

    more_fragments: Ipv4MoreFragments
    """More fragments flag"""

    options: Iterable[Ipv4Option]

    priority: Ipv4Priority
    """A container for ipv4 raw, tos, dscp ip priorities."""

    protocol: Ipv4Protocol
    """Protocol, default is 61 any host internal protocol"""

    reserved: Ipv4Reserved
    """Reserved flag."""

    src: Ipv4Src
    """Source address"""

    time_to_live: Ipv4TimeToLive
    """Time to live"""

    total_length: Ipv4TotalLength
    """Total length"""

    version: Ipv4Version
    """Version"""


class Ipv6DstMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv6Dst(TypedDict, total=False):
    auto: FlowIpv6AutoParam
    """The OTG implementation can provide a system generated, value for this property."""

    choice: Literal["value", "values", "increment", "decrement", "auto"]

    decrement: PatternFlowIpv6DstCounterParam
    """ipv6 counter pattern"""

    increment: PatternFlowIpv6DstCounterParam
    """ipv6 counter pattern"""

    metric_tags: Iterable[Ipv6DstMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class Ipv6FlowLabelMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv6FlowLabelRandom(TypedDict, total=False):
    count: int
    """The total number of values to be generated by the random value generator."""

    max: int
    """The maximum possible value generated by the random value generator."""

    min: int
    """The minimum possible value generated by the random value generator."""

    seed: int
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class Ipv6FlowLabel(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement", "random"]

    decrement: PatternFlowIpv6FlowLabelCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv6FlowLabelCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv6FlowLabelMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: Ipv6FlowLabelRandom
    """integer random pattern"""

    value: int

    values: Iterable[int]


class Ipv6HopLimitMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv6HopLimit(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv6HopLimitCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv6HopLimitCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv6HopLimitMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv6NextHeaderMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv6NextHeader(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowIpv6NextHeaderCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv6NextHeaderCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv6NextHeaderMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv6PayloadLengthMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv6PayloadLength(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowIpv6PayloadLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv6PayloadLengthCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv6PayloadLengthMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv6SrcMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv6Src(TypedDict, total=False):
    auto: FlowIpv6AutoParam
    """The OTG implementation can provide a system generated, value for this property."""

    choice: Literal["value", "values", "increment", "decrement", "auto"]

    decrement: PatternFlowIpv6SrcCounterParam
    """ipv6 counter pattern"""

    increment: PatternFlowIpv6SrcCounterParam
    """ipv6 counter pattern"""

    metric_tags: Iterable[Ipv6SrcMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class Ipv6TrafficClassMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv6TrafficClass(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv6TrafficClassCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv6TrafficClassCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv6TrafficClassMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv6VersionMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class Ipv6Version(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowIpv6VersionCounterParam
    """integer counter pattern"""

    increment: PatternFlowIpv6VersionCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[Ipv6VersionMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ipv6(TypedDict, total=False):
    dst: Ipv6Dst
    """Destination address"""

    flow_label: Ipv6FlowLabel
    """Flow label"""

    hop_limit: Ipv6HopLimit
    """Hop limit"""

    next_header: Ipv6NextHeader
    """Next header"""

    payload_length: Ipv6PayloadLength
    """Payload length"""

    src: Ipv6Src
    """Source address"""

    traffic_class: Ipv6TrafficClass
    """Traffic class"""

    version: Ipv6Version
    """Version number"""


class Macsec(TypedDict, total=False):
    choice: Literal["auto"]
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


class MplsBottomOfStackMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class MplsBottomOfStack(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowMplsBottomOfStackCounterParam
    """integer counter pattern"""

    increment: PatternFlowMplsBottomOfStackCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[MplsBottomOfStackMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class MplsLabelMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class MplsLabel(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowMplsLabelCounterParam
    """integer counter pattern"""

    increment: PatternFlowMplsLabelCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[MplsLabelMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class MplsTimeToLiveMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class MplsTimeToLive(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowMplsTimeToLiveCounterParam
    """integer counter pattern"""

    increment: PatternFlowMplsTimeToLiveCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[MplsTimeToLiveMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class MplsTrafficClassMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class MplsTrafficClass(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowMplsTrafficClassCounterParam
    """integer counter pattern"""

    increment: PatternFlowMplsTrafficClassCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[MplsTrafficClassMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Mpls(TypedDict, total=False):
    bottom_of_stack: MplsBottomOfStack
    """Bottom of stack"""

    label: MplsLabel
    """Label of routers"""

    time_to_live: MplsTimeToLive
    """Time to live"""

    traffic_class: MplsTrafficClass
    """Traffic class"""


class PfcpauseClassEnableVectorMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpauseClassEnableVector(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPauseClassEnableVectorCounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPauseClassEnableVectorCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpauseClassEnableVectorMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpauseControlOpCodeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpauseControlOpCode(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPauseControlOpCodeCounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPauseControlOpCodeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpauseControlOpCodeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpauseDstMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpauseDst(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPauseDstCounterParam
    """mac counter pattern"""

    increment: PatternFlowPfcPauseDstCounterParam
    """mac counter pattern"""

    metric_tags: Iterable[PfcpauseDstMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class PfcpauseEtherTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpauseEtherType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPauseEtherTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPauseEtherTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpauseEtherTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpausePauseClass0MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass0(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPausePauseClass0CounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPausePauseClass0CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpausePauseClass0MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpausePauseClass1MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass1(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPausePauseClass1CounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPausePauseClass1CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpausePauseClass1MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpausePauseClass2MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass2(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPausePauseClass2CounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPausePauseClass2CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpausePauseClass2MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpausePauseClass3MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass3(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPausePauseClass3CounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPausePauseClass3CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpausePauseClass3MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpausePauseClass4MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass4(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPausePauseClass4CounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPausePauseClass4CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpausePauseClass4MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpausePauseClass5MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass5(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPausePauseClass5CounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPausePauseClass5CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpausePauseClass5MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpausePauseClass6MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass6(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPausePauseClass6CounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPausePauseClass6CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpausePauseClass6MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpausePauseClass7MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpausePauseClass7(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPausePauseClass7CounterParam
    """integer counter pattern"""

    increment: PatternFlowPfcPausePauseClass7CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PfcpausePauseClass7MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PfcpauseSrcMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PfcpauseSrc(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPfcPauseSrcCounterParam
    """mac counter pattern"""

    increment: PatternFlowPfcPauseSrcCounterParam
    """mac counter pattern"""

    metric_tags: Iterable[PfcpauseSrcMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: str

    values: List[str]


class Pfcpause(TypedDict, total=False):
    class_enable_vector: PfcpauseClassEnableVector
    """Destination"""

    control_op_code: PfcpauseControlOpCode
    """Control operation code"""

    dst: PfcpauseDst
    """Destination MAC address"""

    ether_type: PfcpauseEtherType
    """Ethernet type"""

    pause_class_0: PfcpausePauseClass0
    """Pause class 0"""

    pause_class_1: PfcpausePauseClass1
    """Pause class 1"""

    pause_class_2: PfcpausePauseClass2
    """Pause class 2"""

    pause_class_3: PfcpausePauseClass3
    """Pause class 3"""

    pause_class_4: PfcpausePauseClass4
    """Pause class 4"""

    pause_class_5: PfcpausePauseClass5
    """Pause class 5"""

    pause_class_6: PfcpausePauseClass6
    """Pause class 6"""

    pause_class_7: PfcpausePauseClass7
    """Pause class 7"""

    src: PfcpauseSrc
    """Source MAC address"""


class PppAddressMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PppAddress(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPppAddressCounterParam
    """integer counter pattern"""

    increment: PatternFlowPppAddressCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PppAddressMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PppControlMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PppControl(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowPppControlCounterParam
    """integer counter pattern"""

    increment: PatternFlowPppControlCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PppControlMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class PppProtocolTypeMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class PppProtocolType(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowPppProtocolTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowPppProtocolTypeCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[PppProtocolTypeMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Ppp(TypedDict, total=False):
    address: PppAddress
    """PPP address"""

    control: PppControl
    """PPP control"""

    protocol_type: PppProtocolType
    """PPP protocol type"""


class RsvpMessageTypePathObjectClassNumCustomType(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathObjectsCustomTypeCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathObjectsCustomTypeCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumCustom(TypedDict, total=False):
    bytes: str
    """A custom packet header defined as a string of hex bytes.

    The string MUST contain sequence of valid hex bytes. Spaces or colons can be
    part of the bytes but will be discarded. Value of the this field should not
    excced 65525 bytes since maximum 65528 bytes can be added as object-contents in
    RSVP header. For type and length requires 3 bytes, hence maximum of 65524 bytes
    are expected. Maximum length of this attribute is 131050 (65525 \\** 2 hex
    character per byte).
    """

    length: FlowRsvpObjectLengthParam

    type: RsvpMessageTypePathObjectClassNumCustomType
    """User defined object type."""


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumberLBit(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathExplicitRouteType1AsNumberLBitCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathExplicitRouteType1AsNumberLBitCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumberLength(TypedDict, total=False):
    auto: int
    """The OTG implementation will provide a system generated value for this property.

    If the OTG implementation is unable to generate a value the default value must
    be used.
    """

    choice: Literal["auto", "value"]
    """auto or configured value."""

    value: int


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumber(TypedDict, total=False):
    as_number: int
    """
    Autonomous System number to be set in the ERO sub-object that this LSP should
    traverse through. This field is applicable only if the value of 'type' is set to
    'as_number'.
    """

    l_bit: RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumberLBit
    """The L bit is an attribute of the subobject.

    The L bit is set if the subobject represents a loose hop in the explicit route.
    If the bit is not set, the subobject represents a strict hop in the explicit
    route.
    """

    length: RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumberLength
    """
    The Length contains the total length of the subobject in bytes,including L, Type
    and Length fields. The Length MUST be atleast 4, and MUST be a multiple of 4.
    """


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixIpv4Address(
    TypedDict, total=False
):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixIpv4AddressCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixIpv4AddressCounterParam
    """ipv4 counter pattern"""

    value: str

    values: List[str]


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixLBit(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixLBitCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathExplicitRouteType1Ipv4PrefixLBitCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixLength(TypedDict, total=False):
    auto: int
    """The OTG implementation will provide a system generated value for this property.

    If the OTG implementation is unable to generate a value the default value must
    be used.
    """

    choice: Literal["auto", "value"]
    """auto or configured value."""

    value: int


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4Prefix(TypedDict, total=False):
    ipv4_address: RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixIpv4Address
    """This IPv4 address is treated as a prefix based on the prefix length value below.

    Bits beyond the prefix are ignored on receipt and SHOULD be set to zero on
    transmission.
    """

    l_bit: RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixLBit
    """The L bit is an attribute of the subobject.

    The L bit is set if the subobject represents a loose hop in the explicit route.
    If the bit is not set, the subobject represents a strict hop in the explicit
    route.
    """

    length: RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4PrefixLength
    """
    The Length contains the total length of the subobject in bytes,including L,Type
    and Length fields. The Length MUST be atleast 4, and MUST be a multiple of 4.
    """

    prefix: int
    """The prefix length of the IPv4 address."""


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectType(TypedDict, total=False):
    as_number: RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeAsNumber
    """
    Class = EXPLICIT_ROUTE, Type1 ROUTE_RECORD C-Type = 1 Subobject: Autonomous
    system number, C-Type: 32
    """

    choice: Literal["ipv4_prefix", "as_number"]

    ipv4_prefix: RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectTypeIpv4Prefix
    """
    Class = EXPLICIT_ROUTE, Type1 ROUTE_RECORD C-Type = 1 Subobject: IPv4 Prefix,
    C-Type: 1
    """


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1Subobject(TypedDict, total=False):
    type: RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1SubobjectType
    """
    Currently supported subobjects are IPv4 address(1) and Autonomous system
    number(32).
    """


class RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1(TypedDict, total=False):
    subobjects: Iterable[RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1Subobject]


class RsvpMessageTypePathObjectClassNumExplicitRouteCType(TypedDict, total=False):
    choice: Literal["type_1"]

    type_1: RsvpMessageTypePathObjectClassNumExplicitRouteCTypeType1
    """Type1 Explicit Route has subobjects.

    Currently supported subobjects are IPv4 prefix and Autonomous system number.
    """


class RsvpMessageTypePathObjectClassNumExplicitRoute(TypedDict, total=False):
    c_type: RsvpMessageTypePathObjectClassNumExplicitRouteCType
    """Object for EXPLICIT_ROUTE class and c-type is Type 1 Explicit Route (1)."""

    length: FlowRsvpObjectLengthParam
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRangeL3pid(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathLabelRequestWithoutLabelRangeL3pidCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathLabelRequestWithoutLabelRangeL3pidCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRangeReserved(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathLabelRequestWithoutLabelRangeReservedCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathLabelRequestWithoutLabelRangeReservedCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRange(TypedDict, total=False):
    l3pid: RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRangeL3pid
    """An identifier of the layer 3 protocol using this path.

    Standard Ethertype values are used e.g. The default value of 2048 ( 0x0800 )
    represents Ethertype for IPv4.
    """

    reserved: RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRangeReserved
    """This field is reserved.

    It MUST be set to zero on transmission and MUST be ignored on receipt.
    """


class RsvpMessageTypePathObjectClassNumLabelRequestCType(TypedDict, total=False):
    choice: Literal["without_label_range"]

    without_label_range: RsvpMessageTypePathObjectClassNumLabelRequestCTypeWithoutLabelRange
    """Class = LABEL_REQUEST, Without Label Range C-Type = 1"""


class RsvpMessageTypePathObjectClassNumLabelRequest(TypedDict, total=False):
    c_type: RsvpMessageTypePathObjectClassNumLabelRequestCType
    """Object for LABEL_REQUEST class.

    Currently supported c-type is Without Label Range (1).
    """

    length: FlowRsvpObjectLengthParam
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressFlags(TypedDict, total=False):
    choice: Literal["local_protection_available", "local_protection_in_use"]


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressIpv4Address(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathRecordRouteType1Ipv4AddressIpv4AddressCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowRsvpPathRecordRouteType1Ipv4AddressIpv4AddressCounterParam
    """ipv4 counter pattern"""

    value: str

    values: List[str]


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressPrefixLength(
    TypedDict, total=False
):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathRecordRouteType1Ipv4AddressPrefixLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathRecordRouteType1Ipv4AddressPrefixLengthCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4Address(TypedDict, total=False):
    flags: RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressFlags
    """0x01 local_protection_available, 0x02 local_protection_in_use"""

    ipv4_address: RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressIpv4Address
    """A 32-bit unicast, host address.

    Any network-reachable interface address is allowed here. Illegal addresses, such
    as certain loopback addresses, SHOULD NOT be used.
    """

    length: FlowRsvpRouteRecordLengthParam
    """
    The Length contains the total length of the subobject in bytes, including the
    Type and Length fields. The Length MUST be atleast 4, and MUST be a multiple
    of 4.
    """

    prefix_length: RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4AddressPrefixLength
    """Prefix-length of IPv4 address."""


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelCType(TypedDict, total=False):
    choice: Literal["value", "values"]

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelFlags(TypedDict, total=False):
    choice: Literal["value", "values"]

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelLabel(TypedDict, total=False):
    as_hex: str
    """Value of the this field should not excced 4 bytes.

    Maximum length of this attribute is 8 (4 \\** 2 hex character per byte).
    """

    as_integer: int

    choice: Literal["as_integer", "as_hex"]
    """32 bit integer or hex value."""


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabel(TypedDict, total=False):
    c_type: RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelCType
    """The C-Type of the included Label Object. Copied from the Label object."""

    flags: RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelFlags
    """0x01 = Global label.

    This flag indicates that the label will be understood if received on any
    interface.
    """

    label: RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabelLabel
    """The contents of the Label Object. Copied from the Label Object."""

    length: FlowRsvpRouteRecordLengthParam
    """
    The Length contains the total length of the subobject in bytes, including the
    Type and Length fields. The Length MUST be atleast 4, and MUST be a multiple
    of 4.
    """


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectType(TypedDict, total=False):
    choice: Literal["ipv4_address", "label"]

    ipv4_address: RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeIpv4Address
    """
    Class = RECORD_ROUTE, Type1 ROUTE_RECORD C-Type = 1 Subobject: IPv4 Address,
    C-Type: 1
    """

    label: RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectTypeLabel
    """Class = RECORD_ROUTE, Type1 ROUTE_RECORD C-Type = 1 Subobject: Label, C-Type: 3"""


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1Subobject(TypedDict, total=False):
    type: RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1SubobjectType
    """Currently supported subobjects are IPv4 address(1) and Label(3)."""


class RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1(TypedDict, total=False):
    subobjects: Iterable[RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1Subobject]


class RsvpMessageTypePathObjectClassNumRecordRouteCType(TypedDict, total=False):
    choice: Literal["type_1"]

    type_1: RsvpMessageTypePathObjectClassNumRecordRouteCTypeType1
    """Type1 record route has list of subobjects.

    Currently supported subobjects are IPv4 address(1) and Label(3).
    """


class RsvpMessageTypePathObjectClassNumRecordRoute(TypedDict, total=False):
    c_type: RsvpMessageTypePathObjectClassNumRecordRouteCType
    """Object for RECORD_ROUTE class. c-type is Type 1 Route Record (1)."""

    length: FlowRsvpObjectLengthParam
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4Ipv4Address(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathRsvpHopIpv4Ipv4AddressCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowRsvpPathRsvpHopIpv4Ipv4AddressCounterParam
    """ipv4 counter pattern"""

    value: str

    values: List[str]


class RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4LogicalInterfaceHandle(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathRsvpHopIpv4LogicalInterfaceHandleCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathRsvpHopIpv4LogicalInterfaceHandleCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4(TypedDict, total=False):
    ipv4_address: RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4Ipv4Address
    """
    The IPv4 address of the interface through which the last RSVP-knowledgeable hop
    forwarded this message.
    """

    logical_interface_handle: RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4LogicalInterfaceHandle
    """
    Logical Interface Handle (LIH) is used to distinguish logical outgoing
    interfaces. A node receiving an LIH in a Path message saves its value and
    returns it in the HOP objects of subsequent Resv messages sent to the node that
    originated the LIH. The LIH should be identically zero if there is no logical
    interface handle.
    """


class RsvpMessageTypePathObjectClassNumRsvpHopCType(TypedDict, total=False):
    choice: Literal["ipv4"]

    ipv4: RsvpMessageTypePathObjectClassNumRsvpHopCTypeIpv4
    """IPv4 RSVP_HOP object: Class = 3, C-Type = 1"""


class RsvpMessageTypePathObjectClassNumRsvpHop(TypedDict, total=False):
    c_type: RsvpMessageTypePathObjectClassNumRsvpHopCType
    """Object for RSVP_HOP class. Currently supported c-type is IPv4 (1)."""

    length: FlowRsvpObjectLengthParam
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4Ipv4TunnelSenderAddress(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTemplateLspTunnelIpv4Ipv4TunnelSenderAddressCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowRsvpPathSenderTemplateLspTunnelIpv4Ipv4TunnelSenderAddressCounterParam
    """ipv4 counter pattern"""

    value: str

    values: List[str]


class RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4LspID(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTemplateLspTunnelIpv4LspIDCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTemplateLspTunnelIpv4LspIDCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4Reserved(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTemplateLspTunnelIpv4ReservedCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTemplateLspTunnelIpv4ReservedCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4(TypedDict, total=False):
    ipv4_tunnel_sender_address: RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4Ipv4TunnelSenderAddress
    """IPv4 address for a sender node."""

    lsp_id: RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4LspID
    """
    A 16-bit identifier used in the SENDER_TEMPLATE that can be changed to allow a
    sender to share resources with itself.
    """

    reserved: RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4Reserved
    """Reserved field, MUST be zero."""


class RsvpMessageTypePathObjectClassNumSenderTemplateCType(TypedDict, total=False):
    choice: Literal["lsp_tunnel_ipv4"]

    lsp_tunnel_ipv4: RsvpMessageTypePathObjectClassNumSenderTemplateCTypeLspTunnelIpv4
    """Class = SENDER_TEMPLATE, LSP_TUNNEL_IPv4 C-Type = 7"""


class RsvpMessageTypePathObjectClassNumSenderTemplate(TypedDict, total=False):
    c_type: RsvpMessageTypePathObjectClassNumSenderTemplateCType
    """Object for SENDER_TEMPLATE class.

    Currently supported c-type is LSP Tunnel IPv4 (7).
    """

    length: FlowRsvpObjectLengthParam
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServLengthOfServiceData(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServLengthOfServiceDataCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServLengthOfServiceDataCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServMaximumPacketSize(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServMaximumPacketSizeCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServMaximumPacketSizeCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServMinimumPolicedUnit(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServMinimumPolicedUnitCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServMinimumPolicedUnitCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServOverallLength(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServOverallLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServOverallLengthCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameter127Flag(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServParameter127FlagCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServParameter127FlagCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameter127Length(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServParameter127LengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServParameter127LengthCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameterIDTokenBucketTspec(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServParameterIDTokenBucketTspecCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServParameterIDTokenBucketTspecCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServReserved1(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServReserved1CounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServReserved1CounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServReserved2(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServReserved2CounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServReserved2CounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServServiceHeader(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServServiceHeaderCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServServiceHeaderCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServVersion(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServVersionCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServVersionCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServZeroBit(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSenderTspecIntServZeroBitCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSenderTspecIntServZeroBitCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServ(TypedDict, total=False):
    length_of_service_data: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServLengthOfServiceData
    """Length of service data, 6 words not including per-service header."""

    maximum_packet_size: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServMaximumPacketSize
    """
    The maximum packet size parameter should be set to the size of the largest
    packet the application might wish to generate. This value must, by definition,
    be equal to or larger than the value of The minimum policed unit.
    """

    minimum_policed_unit: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServMinimumPolicedUnit
    """
    The minimum policed unit parameter should generally be set equal to the size of
    the smallest packet generated by the application.
    """

    overall_length: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServOverallLength
    """Overall length (7 words not including header)."""

    parameter_127_flag: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameter127Flag
    """Parameter 127 flags (none set)"""

    parameter_127_length: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameter127Length
    """Parameter 127 length, 5 words not including per-service header"""

    parameter_id_token_bucket_tspec: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServParameterIDTokenBucketTspec
    """Parameter ID, parameter 127 (Token Bucket TSpec)"""

    peak_data_rate: float
    """
    The peak rate may be set to the sender's peak traffic generation rate (if known
    and controlled), the physical interface line rate (if known), or positive
    infinity (if no better value is available).
    """

    reserved1: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServReserved1
    """Reserved."""

    reserved2: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServReserved2
    """Reserved."""

    service_header: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServServiceHeader
    """
    Service header, service number - '1' (Generic information) if in a PATH message.
    """

    token_bucket_rate: float
    """Token bucket rate is set to sender's view of its generated traffic."""

    token_bucket_size: float
    """Token bucket size is set to sender's view of its generated traffic."""

    version: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServVersion
    """Message format version number."""

    zero_bit: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServZeroBit
    """MUST be 0."""


class RsvpMessageTypePathObjectClassNumSenderTspecCType(TypedDict, total=False):
    choice: Literal["int_serv"]

    int_serv: RsvpMessageTypePathObjectClassNumSenderTspecCTypeIntServ
    """int-serv SENDER_TSPEC object: Class = 12, C-Type = 2"""


class RsvpMessageTypePathObjectClassNumSenderTspec(TypedDict, total=False):
    c_type: RsvpMessageTypePathObjectClassNumSenderTspecCType
    """Object for SENDER_TSPEC class. Currently supported c-type is int-serv (2)."""

    length: FlowRsvpObjectLengthParam
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelIDAsInteger(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSessionExtTunnelIDAsIntegerCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSessionExtTunnelIDAsIntegerCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelIDAsIpv4(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSessionExtTunnelIDAsIpv4CounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowRsvpPathSessionExtTunnelIDAsIpv4CounterParam
    """ipv4 counter pattern"""

    value: str

    values: List[str]


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelID(TypedDict, total=False):
    as_integer: RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelIDAsInteger
    """TBD"""

    as_ipv4: RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelIDAsIpv4
    """IPv4 address of the ingress endpoint for the tunnel."""

    choice: Literal["as_integer", "as_ipv4"]
    """32 bit integer or IPv4 address."""


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4Ipv4TunnelEndPointAddress(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSessionLspTunnelIpv4Ipv4TunnelEndPointAddressCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowRsvpPathSessionLspTunnelIpv4Ipv4TunnelEndPointAddressCounterParam
    """ipv4 counter pattern"""

    value: str

    values: List[str]


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4Reserved(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSessionLspTunnelIpv4ReservedCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSessionLspTunnelIpv4ReservedCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4TunnelID(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathSessionLspTunnelIpv4TunnelIDCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathSessionLspTunnelIpv4TunnelIDCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4(TypedDict, total=False):
    extended_tunnel_id: RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4ExtendedTunnelID
    """
    A 32-bit identifier used in the SESSION that remains constant over the life of
    the tunnel. Normally set to all zeros. Ingress nodes that wish to narrow the
    scope of a SESSION to the ingress-egress pair may place their IPv4 address here
    as a globally unique identifier.
    """

    ipv4_tunnel_end_point_address: RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4Ipv4TunnelEndPointAddress
    """IPv4 address of the egress node for the tunnel."""

    reserved: RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4Reserved
    """Reserved field, MUST be zero."""

    tunnel_id: RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4TunnelID
    """
    A 16-bit identifier used in the SESSION that remains constant over the life of
    the tunnel.
    """


class RsvpMessageTypePathObjectClassNumSessionCType(TypedDict, total=False):
    choice: Literal["lsp_tunnel_ipv4"]

    lsp_tunnel_ipv4: RsvpMessageTypePathObjectClassNumSessionCTypeLspTunnelIpv4
    """Class = SESSION, LSP_TUNNEL_IPv4 C-Type = 7."""


class RsvpMessageTypePathObjectClassNumSession(TypedDict, total=False):
    c_type: RsvpMessageTypePathObjectClassNumSessionCType
    """The body of an object corresponding to the class number and c-type.

    Currently supported c-type for SESSION object is LSP Tunnel IPv4 (7).
    """

    length: FlowRsvpObjectLengthParam
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumSessionAttributeCTypeLspTunnel(TypedDict, total=False):
    flags: FlowRsvpLspTunnelFlagParam
    """
    0x01 Local protection desired, 0x02 Label recording desired, 0x04 SE Style
    desired
    """

    holding_priority: int
    """
    The priority of the session with respect to holding resources,in the range of 0
    to 7. The value 0 is the highest priority. The Setup Priority is used in
    deciding whether this session can preempt another session.
    """

    name_length: FlowRsvpSessionAttributeNameLengthParam
    """The length of the display string before padding, in bytes."""

    session_name: str
    """A null padded string of characters."""

    setup_priority: int
    """
    The priority of the session with respect to taking resources,in the range of 0
    to 7. The value 0 is the highest priority. The Setup Priority is used in
    deciding whether this session can preempt another session.
    """


class RsvpMessageTypePathObjectClassNumSessionAttributeCTypeLspTunnelRa(TypedDict, total=False):
    exclude_any: str
    """
    A 32-bit vector representing a set of attribute filters associated with a tunnel
    any of which renders a link unacceptable. A null set (all bits set to zero)
    doesn't render the link unacceptable. The most significant byte in the
    hex-string is the farthest to the left in the byte sequence. Leading zero bytes
    in the configured value may be omitted for brevity.
    """

    flags: FlowRsvpLspTunnelFlagParam
    """
    0x01 Local protection desired, 0x02 Label recording desired, 0x04 SE Style
    desired
    """

    holding_priority: int
    """
    The priority of the session with respect to holding resources,in the range of 0
    to 7. The value 0 is the highest priority. The Setup Priority is used in
    deciding whether this session can preempt another session.
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

    name_length: FlowRsvpSessionAttributeNameLengthParam
    """The length of the display string before padding, in bytes."""

    session_name: str
    """A null padded string of characters."""

    setup_priority: int
    """
    The priority of the session with respect to taking resources,in the range of 0
    to 7. The value 0 is the highest priority. The Setup Priority is used in
    deciding whether this session can preempt another session.
    """


class RsvpMessageTypePathObjectClassNumSessionAttributeCType(TypedDict, total=False):
    choice: Literal["lsp_tunnel", "lsp_tunnel_ra"]

    lsp_tunnel: RsvpMessageTypePathObjectClassNumSessionAttributeCTypeLspTunnel
    """
    SESSION_ATTRIBUTE class = 207, LSP_TUNNEL_RA C-Type = 7, resource affinity
    information.
    """

    lsp_tunnel_ra: RsvpMessageTypePathObjectClassNumSessionAttributeCTypeLspTunnelRa
    """
    SESSION_ATTRIBUTE class = 207, LSP_TUNNEL_RA C-Type = 1, it carries resource
    affinity information.
    """


class RsvpMessageTypePathObjectClassNumSessionAttribute(TypedDict, total=False):
    c_type: RsvpMessageTypePathObjectClassNumSessionAttributeCType
    """Object for SESSION_ATTRIBUTE class.

    Currently supported c-type is LSP_Tunnel_RA (1) and LSP_Tunnel (7).
    """

    length: FlowRsvpObjectLengthParam
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNumTimeValuesCTypeType1RefreshPeriodR(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpPathTimeValuesType1RefreshPeriodRCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpPathTimeValuesType1RefreshPeriodRCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpMessageTypePathObjectClassNumTimeValuesCTypeType1(TypedDict, total=False):
    refresh_period_r: RsvpMessageTypePathObjectClassNumTimeValuesCTypeType1RefreshPeriodR
    """The refresh timeout period R used to generate this message;in milliseconds."""


class RsvpMessageTypePathObjectClassNumTimeValuesCType(TypedDict, total=False):
    choice: Literal["type_1"]

    type_1: RsvpMessageTypePathObjectClassNumTimeValuesCTypeType1
    """TIME_VALUES Object: Class = 5, C-Type = 1"""


class RsvpMessageTypePathObjectClassNumTimeValues(TypedDict, total=False):
    c_type: RsvpMessageTypePathObjectClassNumTimeValuesCType
    """Object for TIME_VALUES class.

    Currently supported c-type is Type 1 Time Value (1).
    """

    length: FlowRsvpObjectLengthParam
    """A 16-bit field containing the total object length in bytes.

    Must always be a multiple of 4 or at least 4.
    """


class RsvpMessageTypePathObjectClassNum(TypedDict, total=False):
    choice: Required[
        Literal[
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
    ]

    custom: RsvpMessageTypePathObjectClassNumCustom
    """Custom packet header"""

    explicit_route: RsvpMessageTypePathObjectClassNumExplicitRoute
    """C-Type is specific to a class num."""

    label_request: RsvpMessageTypePathObjectClassNumLabelRequest
    """C-Type is specific to a class num."""

    record_route: RsvpMessageTypePathObjectClassNumRecordRoute
    """C-Type is specific to a class num."""

    rsvp_hop: RsvpMessageTypePathObjectClassNumRsvpHop
    """C-Type is specific to a class num."""

    sender_template: RsvpMessageTypePathObjectClassNumSenderTemplate
    """C-Type is specific to a class num."""

    sender_tspec: RsvpMessageTypePathObjectClassNumSenderTspec
    """C-Type is specific to a class num."""

    session: RsvpMessageTypePathObjectClassNumSession
    """C-Type is specific to a class num."""

    session_attribute: RsvpMessageTypePathObjectClassNumSessionAttribute
    """C-Type is specific to a class num."""

    time_values: RsvpMessageTypePathObjectClassNumTimeValues
    """C-Type is specific to a class num."""


class RsvpMessageTypePathObject(TypedDict, total=False):
    class_num: RsvpMessageTypePathObjectClassNum
    """The class number is used to identify the class of an object.

    Defined in
    https://www.iana.org/assignments/rsvp-parameters/rsvp-parameters.xhtml#rsvp-parameters-4
    . Curently supported class numbers are for "Path" message type. "Path" message:
    Supported Class numbers and it's value: SESSION: 1, RSVP_HOP: 3, TIME_VALUES: 5,
    EXPLICIT_ROUTE: 20, LABEL_REQUEST: 19, SESSION_ATTRIBUTE: 207, SENDER_TEMPLATE:
    11, SENDER_TSPEC: 12, RECORD_ROUTE: 21, Custom: User defined bytes based on
    class and c-types not supported in above options.
    """


class RsvpMessageTypePath(TypedDict, total=False):
    objects: Iterable[RsvpMessageTypePathObject]
    """
    "Path" message requires atleast SESSION, RSVP_HOP, TIME_VALUES, LABEL_REQUEST,
    SENDER_TEMPLATE and SENDER_TSPEC objects in order.
    """


class RsvpMessageType(TypedDict, total=False):
    choice: Literal["path"]

    path: RsvpMessageTypePath
    """
    "Path" message requires the following list of objects in order as defined in
    https://www.rfc-editor.org/rfc/rfc3209.html#page-15: 1. SESSION 2. RSVP_HOP 3.
    TIME_VALUES 4. EXPLICIT_ROUTE [optional] 5. LABEL_REQUEST 6. SESSION_ATTRIBUTE
    [optional] 7. SENDER_TEMPLATE 8. SENDER_TSPEC 9. RECORD_ROUTE [optional]
    """


class RsvpReserved(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpReservedCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpReservedCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RsvpRsvpChecksum(TypedDict, total=False):
    choice: Literal["generated", "custom"]
    """The type of checksum"""

    custom: int
    """A custom checksum value"""

    generated: Literal["good", "bad"]
    """A system generated checksum value"""


class RsvpRsvpLength(TypedDict, total=False):
    auto: int
    """The OTG implementation will provide a system generated value for this property.

    If the OTG implementation is unable to generate a value the default value must
    be used.
    """

    choice: Literal["auto", "value"]
    """auto or configured value."""

    value: int


class RsvpTimeToLive(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowRsvpTimeToLiveCounterParam
    """integer counter pattern"""

    increment: PatternFlowRsvpTimeToLiveCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class Rsvp(TypedDict, total=False):
    flag: Literal["not_refresh_reduction_capable", "refresh_reduction_capable"]
    """Flag, 0x01-0x08: Reserved."""

    message_type: RsvpMessageType
    """An 8-bit number that identifies the function of the RSVP message.

    There are aound 20 message types defined in
    https://www.iana.org/assignments/rsvp-parameters/rsvp-parameters.xhtml#rsvp-parameters-2
    . Among these presently supported is "Path"(value: 1) message type.
    """

    reserved: RsvpReserved
    """Reserved"""

    rsvp_checksum: RsvpRsvpChecksum
    """
    The one's complement of the one's complement sum of the message, with the
    checksum field replaced by zero for the purpose of computing the checksum. An
    all-zero value means that no checksum was transmitted.
    """

    rsvp_length: RsvpRsvpLength
    """
    The sum of the lengths of the common header and all objects included in the
    message.
    """

    time_to_live: RsvpTimeToLive
    """The IP time-to-live(TTL) value with which the message was sent."""

    version: int
    """RSVP Protocol Version."""


class Snmpv2cDataGetBulkRequestMaxRepetitions(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cBulkPduMaxRepetitionsCounterParam
    """integer counter pattern"""

    increment: PatternFlowSnmpv2cBulkPduMaxRepetitionsCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class Snmpv2cDataGetBulkRequestNonRepeaters(TypedDict, total=False):
    choice: Literal["value", "values"]

    value: int

    values: Iterable[int]


class Snmpv2cDataGetBulkRequestRequestID(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cBulkPduRequestIDCounterParam
    """integer counter pattern"""

    increment: PatternFlowSnmpv2cBulkPduRequestIDCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class Snmpv2cDataGetBulkRequest(TypedDict, total=False):
    max_repetitions: Snmpv2cDataGetBulkRequestMaxRepetitions
    """
    A maximum of max_repetitions variable bindings are requested in the Response-PDU
    for each of the remaining variable bindings in the GetBulkRequest after the
    non_repeaters variable bindings.
    """

    non_repeaters: Snmpv2cDataGetBulkRequestNonRepeaters
    """
    One variable binding in the Response-PDU is requested for the first
    non_repeaters variable bindings in the GetBulkRequest.
    """

    request_id: Snmpv2cDataGetBulkRequestRequestID
    """Identifies a particular SNMP request.

    This index is echoed back in the response from the SNMP agent, allowing the SNMP
    manager to match an incoming response to the appropriate request.

    - Encoding of this field follows ASN.1 X.690(section 8.3) specification. Refer:
      http://www.itu.int/ITU-T/asn1/
    """

    variable_bindings: Iterable[FlowSnmpv2cVariableBindingParam]
    """A Sequence of variable_bindings."""


class Snmpv2cData(TypedDict, total=False):
    choice: Required[
        Literal[
            "get_request",
            "get_next_request",
            "response",
            "set_request",
            "get_bulk_request",
            "inform_request",
            "snmpv2_trap",
            "report",
        ]
    ]

    get_bulk_request: Snmpv2cDataGetBulkRequest
    """
    The purpose of the GetBulkRequest-PDU is to request the transfer of a
    potentially large amount of data, including, but not limited to, the efficient
    and rapid retrieval of large tables.
    """

    get_next_request: FlowSnmpv2cPduParam
    """This contains the body of the SNMPv2C PDU."""

    get_request: FlowSnmpv2cPduParam
    """This contains the body of the SNMPv2C PDU."""

    inform_request: FlowSnmpv2cPduParam
    """This contains the body of the SNMPv2C PDU."""

    report: FlowSnmpv2cPduParam
    """This contains the body of the SNMPv2C PDU."""

    response: FlowSnmpv2cPduParam
    """This contains the body of the SNMPv2C PDU."""

    set_request: FlowSnmpv2cPduParam
    """This contains the body of the SNMPv2C PDU."""

    snmpv2_trap: FlowSnmpv2cPduParam
    """This contains the body of the SNMPv2C PDU."""


class Snmpv2cVersion(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cVersionCounterParam
    """integer counter pattern"""

    increment: PatternFlowSnmpv2cVersionCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class Snmpv2c(TypedDict, total=False):
    data: Required[Snmpv2cData]
    """This contains the body of the SNMPv2C message.

    - Encoding of subsequent fields follow ASN.1 specification. Refer:
      http://www.itu.int/ITU-T/asn1/
    """

    community: str
    """
    It is an ASCII based octet string which identifies the SNMP community in which
    the sender and recipient of this message are located. It should match the
    read-only or read-write community string configured on the recipient for the PDU
    to be accepted.
    """

    version: Snmpv2cVersion
    """Version"""


class TcpAckNumMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpAckNum(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpAckNumCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpAckNumCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpAckNumMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpChecksum(TypedDict, total=False):
    choice: Literal["generated", "custom"]
    """The type of checksum"""

    custom: int
    """A custom checksum value"""

    generated: Literal["good", "bad"]
    """A system generated checksum value"""


class TcpCtlAckMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlAck(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpCtlAckCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpCtlAckCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpCtlAckMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpCtlFinMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlFin(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpCtlFinCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpCtlFinCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpCtlFinMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpCtlPshMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlPsh(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpCtlPshCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpCtlPshCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpCtlPshMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpCtlRstMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlRst(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpCtlRstCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpCtlRstCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpCtlRstMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpCtlSynMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlSyn(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpCtlSynCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpCtlSynCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpCtlSynMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpCtlUrgMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpCtlUrg(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpCtlUrgCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpCtlUrgCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpCtlUrgMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpDataOffsetMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpDataOffset(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpDataOffsetCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpDataOffsetCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpDataOffsetMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpDstPortMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpDstPortRandom(TypedDict, total=False):
    count: int
    """The total number of values to be generated by the random value generator."""

    max: int
    """The maximum possible value generated by the random value generator."""

    min: int
    """The minimum possible value generated by the random value generator."""

    seed: int
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class TcpDstPort(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement", "random"]

    decrement: PatternFlowTcpDstPortCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpDstPortCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpDstPortMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: TcpDstPortRandom
    """integer random pattern"""

    value: int

    values: Iterable[int]


class TcpEcnCwrMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpEcnCwr(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpEcnCwrCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpEcnCwrCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpEcnCwrMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpEcnEchoMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpEcnEcho(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpEcnEchoCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpEcnEchoCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpEcnEchoMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpEcnNsMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpEcnNs(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpEcnNsCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpEcnNsCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpEcnNsMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpSeqNumMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpSeqNum(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpSeqNumCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpSeqNumCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpSeqNumMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class TcpSrcPortMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpSrcPortRandom(TypedDict, total=False):
    count: int
    """The total number of values to be generated by the random value generator."""

    max: int
    """The maximum possible value generated by the random value generator."""

    min: int
    """The minimum possible value generated by the random value generator."""

    seed: int
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class TcpSrcPort(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement", "random"]

    decrement: PatternFlowTcpSrcPortCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpSrcPortCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpSrcPortMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: TcpSrcPortRandom
    """integer random pattern"""

    value: int

    values: Iterable[int]


class TcpWindowMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class TcpWindow(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowTcpWindowCounterParam
    """integer counter pattern"""

    increment: PatternFlowTcpWindowCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[TcpWindowMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Tcp(TypedDict, total=False):
    ack_num: TcpAckNum
    """Acknowledgement number"""

    checksum: TcpChecksum
    """
    The one's complement of the one's complement sum of all 16 bit words in header
    and text. An all-zero value means that no checksum will be transmitted. While
    computing the checksum, the checksum field itself is replaced with zeros.
    """

    ctl_ack: TcpCtlAck
    """A value of 1 indicates that the ackknowledgment field is significant."""

    ctl_fin: TcpCtlFin
    """Last packet from the sender."""

    ctl_psh: TcpCtlPsh
    """Asks to push the buffered data to the receiving application."""

    ctl_rst: TcpCtlRst
    """Reset the connection."""

    ctl_syn: TcpCtlSyn
    """Synchronize sequenece numbers."""

    ctl_urg: TcpCtlUrg
    """A value of 1 indicates that the urgent pointer field is significant."""

    data_offset: TcpDataOffset
    """The number of 32 bit words in the TCP header.

    This indicates where the data begins.
    """

    dst_port: TcpDstPort
    """Destination port"""

    ecn_cwr: TcpEcnCwr
    """Explicit congestion notification, congestion window reduced."""

    ecn_echo: TcpEcnEcho
    """Explicit congestion notification, echo.

    1 indicates the peer is ecn capable. 0 indicates that a packet with ipv4.ecn =
    11 in the ip header was received during normal transmission.
    """

    ecn_ns: TcpEcnNs
    """Explicit congestion notification, concealment protection."""

    seq_num: TcpSeqNum
    """Sequence number"""

    src_port: TcpSrcPort
    """Source port"""

    window: TcpWindow
    """Tcp connection window."""


class UdpChecksum(TypedDict, total=False):
    choice: Literal["generated", "custom"]
    """The type of checksum"""

    custom: int
    """A custom checksum value"""

    generated: Literal["good", "bad"]
    """A system generated checksum value"""


class UdpDstPortMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class UdpDstPortRandom(TypedDict, total=False):
    count: int
    """The total number of values to be generated by the random value generator."""

    max: int
    """The maximum possible value generated by the random value generator."""

    min: int
    """The minimum possible value generated by the random value generator."""

    seed: int
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class UdpDstPort(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement", "random"]

    decrement: PatternFlowUdpDstPortCounterParam
    """integer counter pattern"""

    increment: PatternFlowUdpDstPortCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[UdpDstPortMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: UdpDstPortRandom
    """integer random pattern"""

    value: int

    values: Iterable[int]


class UdpLengthMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class UdpLength(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowUdpLengthCounterParam
    """integer counter pattern"""

    increment: PatternFlowUdpLengthCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[UdpLengthMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class UdpSrcPortMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class UdpSrcPortRandom(TypedDict, total=False):
    count: int
    """The total number of values to be generated by the random value generator."""

    max: int
    """The maximum possible value generated by the random value generator."""

    min: int
    """The minimum possible value generated by the random value generator."""

    seed: int
    """
    The seed value is used to initialize the random number generator to a
    deterministic state. If the user provides a seed value of 0, the implementation
    will generate a sequence of non-deterministic random values. For any other seed
    value, the sequence of random numbers will be generated in a deterministic
    manner (specific to the implementation).
    """


class UdpSrcPort(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement", "random"]

    decrement: PatternFlowUdpSrcPortCounterParam
    """integer counter pattern"""

    increment: PatternFlowUdpSrcPortCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[UdpSrcPortMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    random: UdpSrcPortRandom
    """integer random pattern"""

    value: int

    values: Iterable[int]


class Udp(TypedDict, total=False):
    checksum: UdpChecksum
    """UDP checksum"""

    dst_port: UdpDstPort
    """Destination port"""

    length: UdpLength
    """Length"""

    src_port: UdpSrcPort
    """Source port"""


class VlanIDMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class VlanID(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowVlanIDCounterParam
    """integer counter pattern"""

    increment: PatternFlowVlanIDCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[VlanIDMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class VlanCfiMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class VlanCfi(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowVlanCfiCounterParam
    """integer counter pattern"""

    increment: PatternFlowVlanCfiCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[VlanCfiMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class VlanPriorityMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class VlanPriority(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowVlanPriorityCounterParam
    """integer counter pattern"""

    increment: PatternFlowVlanPriorityCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[VlanPriorityMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class VlanTpidMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class VlanTpid(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowVlanTpidCounterParam
    """integer counter pattern"""

    increment: PatternFlowVlanTpidCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[VlanTpidMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Vlan(TypedDict, total=False):
    id: VlanID
    """Vlan identifier"""

    cfi: VlanCfi
    """Canonical format indicator or drop elegible indicator"""

    priority: VlanPriority
    """Priority code point"""

    tpid: VlanTpid
    """Protocol identifier"""


class VxlanFlagsMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class VxlanFlags(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowVxlanFlagsCounterParam
    """integer counter pattern"""

    increment: PatternFlowVxlanFlagsCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[VxlanFlagsMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class VxlanReserved0MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class VxlanReserved0(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowVxlanReserved0CounterParam
    """integer counter pattern"""

    increment: PatternFlowVxlanReserved0CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[VxlanReserved0MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class VxlanReserved1MetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class VxlanReserved1(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowVxlanReserved1CounterParam
    """integer counter pattern"""

    increment: PatternFlowVxlanReserved1CounterParam
    """integer counter pattern"""

    metric_tags: Iterable[VxlanReserved1MetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class VxlanVniMetricTag(TypedDict, total=False):
    name: Required[str]
    """
    Name used to identify the metrics associated with the values applicable for
    configured offset and length inside corresponding header field
    """

    length: int
    """
    Number of bits to track for metrics starting from configured offset of
    corresponding header field
    """

    offset: int
    """Offset in bits relative to start of corresponding header field"""


class VxlanVni(TypedDict, total=False):
    auto: int
    """The OTG implementation can provide a system generated value for this property.

    If the OTG is unable to generate a value the default value must be used.
    """

    choice: Literal["value", "values", "auto", "increment", "decrement"]

    decrement: PatternFlowVxlanVniCounterParam
    """integer counter pattern"""

    increment: PatternFlowVxlanVniCounterParam
    """integer counter pattern"""

    metric_tags: Iterable[VxlanVniMetricTag]
    """
    One or more metric tags can be used to enable tracking portion of or all bits in
    a corresponding header field for metrics per each applicable value. These would
    appear as tagged metrics in corresponding flow metrics.
    """

    value: int

    values: Iterable[int]


class Vxlan(TypedDict, total=False):
    flags: VxlanFlags
    """Flags field with a bit format of RRRRIRRR.

    The I flag MUST be set to 1 for a valid vxlan network id (VNI). The other 7 bits
    (designated "R") are reserved fields and MUST be set to zero on transmission and
    ignored on receipt.
    """

    reserved0: VxlanReserved0
    """Reserved field"""

    reserved1: VxlanReserved1
    """Reserved field"""

    vni: VxlanVni
    """VXLAN network id"""


class FlowHeaderParam(TypedDict, total=False):
    arp: Arp
    """ARP packet header"""

    choice: Literal[
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
    """The available types of flow headers.

    If one is not provided the default ethernet packet header MUST be provided.
    """

    custom: Custom
    """Custom packet header"""

    ethernet: Ethernet
    """Ethernet packet header"""

    ethernetpause: Ethernetpause
    """IEEE 802.3x global ethernet pause packet header"""

    gre: Gre
    """Standard GRE packet header (RFC2784)"""

    gtpv1: Gtpv1
    """GTPv1 packet header"""

    gtpv2: Gtpv2
    """GTPv2 packet header"""

    icmp: Icmp
    """ICMP packet header"""

    icmpv6: Icmpv6
    """ICMPv6 packet header"""

    igmpv1: Igmpv1
    """IGMPv1 packet header"""

    ipv4: Ipv4
    """IPv4 packet header"""

    ipv6: Ipv6
    """IPv6 packet header"""

    macsec: Macsec
    """MACsec packet header."""

    mpls: Mpls
    """
    MPLS packet header; When configuring multiple such headers, the count shall not
    exceed 20.
    """

    pfcpause: Pfcpause
    """IEEE 802.1Qbb PFC Pause packet header."""

    ppp: Ppp
    """PPP packet header"""

    rsvp: Rsvp
    """RSVP packet header as defined in RFC2205 and RFC3209.

    Currently only supported message type is "Path" with mandatory objects and
    sub-objects.
    """

    snmpv2c: Snmpv2c
    """SNMPv2C packet header as defined in RFC1901 and RFC3416."""

    tcp: Tcp
    """TCP packet header"""

    udp: Udp
    """UDP packet header"""

    vlan: Vlan
    """VLAN packet header"""

    vxlan: Vxlan
    """VXLAN packet header"""
