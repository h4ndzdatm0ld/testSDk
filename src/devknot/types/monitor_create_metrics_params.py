# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

__all__ = [
    "MonitorCreateMetricsParams",
    "Bgpv4",
    "Bgpv6",
    "Convergence",
    "Dhcpv4Client",
    "Dhcpv4Server",
    "Dhcpv6Client",
    "Dhcpv6Server",
    "EgressOnlyTracking",
    "EgressOnlyTrackingTaggedMetrics",
    "Flow",
    "FlowTaggedMetrics",
    "FlowTaggedMetricsFilter",
    "Isis",
    "Lacp",
    "Lag",
    "Lldp",
    "Macsec",
    "Mka",
    "Ospfv2",
    "Ospfv3",
    "Port",
    "Rocev2Flow",
    "Rocev2FlowPerQp",
    "Rocev2Ipv4",
    "Rocev2Ipv4PerPeer",
    "Rocev2Ipv6",
    "Rocev2Ipv6PerPeer",
    "Rsvp",
]


class MonitorCreateMetricsParams(TypedDict, total=False):
    bgpv4: Bgpv4
    """The request to retrieve BGPv4 per peer metrics/statistics."""

    bgpv6: Bgpv6
    """The request to retrieve BGPv6 per peer metrics/statistics."""

    choice: Literal[
        "port",
        "flow",
        "bgpv4",
        "bgpv6",
        "isis",
        "lag",
        "lacp",
        "lldp",
        "rsvp",
        "dhcpv4_client",
        "dhcpv4_server",
        "dhcpv6_client",
        "dhcpv6_server",
        "ospfv2",
        "convergence",
        "macsec",
        "mka",
        "ospfv3",
        "rocev2_ipv4",
        "rocev2_ipv6",
        "rocev2_flow",
        "egress_only_tracking",
    ]

    convergence: Convergence
    """
    Under Review: Convergence metrics is currently under review for pending
    exploration on use cases.

    Container for requesting control-plane and data-plane convergence time metrics
    for flows.
    """

    dhcpv4_client: Dhcpv4Client
    """The request to retrieve DHCPv4 per client metrics/statistics."""

    dhcpv4_server: Dhcpv4Server
    """The request to retrieve DHCPv4 per Server metrics/statistics."""

    dhcpv6_client: Dhcpv6Client
    """The request to retrieve DHCPv6 per client metrics/statistics."""

    dhcpv6_server: Dhcpv6Server
    """The request to retrieve DHCPv6 per Server metrics/statistics."""

    egress_only_tracking: EgressOnlyTracking
    """The container for a egress only tracking metric request."""

    flow: Flow
    """The container for a flow metric request."""

    isis: Isis
    """The request to retrieve ISIS per Router metrics/statistics."""

    lacp: Lacp
    """The request to retrieve LACP per LAG member metrics/statistics."""

    lag: Lag
    """The request to retrieve per LAG metrics/statistics."""

    lldp: Lldp
    """The request to retrieve LLDP per instance metrics/statistics."""

    macsec: Macsec
    """The request to retrieve MACsec per secure entity(secY) metrics/statistics."""

    mka: Mka
    """The request to retrieve MKA per peer metrics/statistics."""

    ospfv2: Ospfv2
    """The request to retrieve OSPFv2 per Router metrics/statistics."""

    ospfv3: Ospfv3
    """The request to retrieve OSPFv3 per router metrics/statistics."""

    port: Port
    """The port result request to the traffic generator"""

    rocev2_flow: Rocev2Flow
    """Request to retrieve RoCEv2 FLow statistics."""

    rocev2_ipv4: Rocev2Ipv4
    """Request to retrieve RoCEv2 over IPv4 per peer metrics/statistics."""

    rocev2_ipv6: Rocev2Ipv6
    """Request to retrieve RoCEv2 over IPv6 per peer metrics/statistics."""

    rsvp: Rsvp
    """The request to retrieve RSVP-TE per Router metrics/statistics."""


class Bgpv4(TypedDict, total=False):
    column_names: List[
        Literal[
            "session_state",
            "session_flap_count",
            "routes_advertised",
            "routes_received",
            "route_withdraws_sent",
            "route_withdraws_received",
            "updates_sent",
            "updates_received",
            "opens_sent",
            "opens_received",
            "keepalives_sent",
            "keepalives_received",
            "notifications_sent",
            "notifications_received",
            "fsm_state",
            "end_of_rib_received",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned except for any
    result_groups. The name of the BGPv4 peer cannot be excluded.
    """

    peer_names: List[str]
    """The names of BGPv4 peers to return results for.

    An empty list will return results for all BGPv4 peers.

    x-constraint:

    - /components/schemas/Bgp.V4peer/properties/name
    """


class Bgpv6(TypedDict, total=False):
    column_names: List[
        Literal[
            "session_state",
            "session_flap_count",
            "routes_advertised",
            "routes_received",
            "route_withdraws_sent",
            "route_withdraws_received",
            "updates_sent",
            "updates_received",
            "opens_sent",
            "opens_received",
            "keepalives_sent",
            "keepalives_received",
            "notifications_sent",
            "notifications_received",
            "fsm_state",
            "end_of_rib_received",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned except for any
    result_groups. The name of the BGPv6 peer cannot be excluded.
    """

    peer_names: List[str]
    """The names of BGPv6 peers to return results for.

    An empty list will return results for all BGPv6 peers.

    x-constraint:

    - /components/schemas/Bgp.V6peer/properties/name
    """


class Convergence(TypedDict, total=False):
    flow_names: List[str]
    """
    Convergence metrics will be retrieved for these flow names. If no flow names are
    specified then convergence metrics for all flows will be returned.

    x-constraint:

    - /components/schemas/Flow/properties/name
    """


class Dhcpv4Client(TypedDict, total=False):
    client_names: List[str]
    """The names of DHCPv4 clients to return results for.

    An empty list will return results for all DHCPv4 client.

    x-constraint:

    - /components/schemas/Device.Dhcpv4client/properties/name
    """

    column_names: List[
        Literal[
            "discovers_sent",
            "offers_received",
            "requests_sent",
            "acks_received",
            "nacks_received",
            "releases_sent",
            "declines_sent",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned. The name of the DHCPv4
    client cannot be excluded.
    """


class Dhcpv4Server(TypedDict, total=False):
    column_names: List[
        Literal[
            "discovers_received",
            "offers_sent",
            "requests_received",
            "acks_sent",
            "nacks_sent",
            "releases_received",
            "declines_received",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned. The name of the DHCPv4
    server cannot be excluded.
    """

    server_names: List[str]
    """The names of DHCPv4 Servers to return results for.

    An empty list will return results for all DHCPv4 Server.

    x-constraint:

    - /components/schemas/Device.Dhcpv4Server/properties/name
    """


class Dhcpv6Client(TypedDict, total=False):
    client_names: List[str]
    """The names of DHCPv6 clients to return results for.

    An empty list will return results for all DHCPv6 client.

    x-constraint:

    - /components/schemas/Device.Dhcpv6client/properties/name
    """

    column_names: List[
        Literal[
            "solicits_sent",
            "advertisements_received",
            "advertisements_ignored",
            "requests_sent",
            "nacks_received",
            "replies_received",
            "information_requests_sent",
            "renews_sent",
            "rebinds_sent",
            "releases_sent",
            "reconfigures_received",
            "rapid_commit_solicits_sent",
            "rapid_commit_replies_received",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned except for any
    result_groups. The name of the DHCPv6 client cannot be excluded.
    """


class Dhcpv6Server(TypedDict, total=False):
    column_names: List[
        Literal[
            "solicits_received",
            "solicits_ignored",
            "advertisements_sent",
            "requests_received",
            "nacks_sent",
            "confirms_received",
            "renewals_received",
            "rebinds_received",
            "replies_sent",
            "releases_received",
            "declines_received",
            "information_requests_received",
            "relay_forwards_received",
            "relay_replies_sent",
            "reconfigures_sent",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned except for any
    result_groups. The name of the DHCPv6 server cannot be excluded.
    """

    server_names: List[str]
    """The names of DHCPv6 Servers to return results for.

    An empty list will return results for all DHCPv6 Server.

    x-constraint:

    - /components/schemas/Device.Dhcpv6Server/properties/name
    """


class EgressOnlyTrackingTaggedMetrics(TypedDict, total=False):
    include_empty_metrics: bool
    """
    Controls inclusion/exclusion of tagged metrics where each underlying attribute
    has zero value or absent value.
    """

    metric_names: List[
        Literal[
            "frames_rx",
            "bytes_rx",
            "frames_rx_rate",
            "rx_l1_rate_bps",
            "rx_rate_bytes",
            "rx_rate_bps",
            "rx_rate_kbps",
            "rx_rate_mbps",
            "tx_metrics",
        ]
    ]
    """The list of metric names that the returned result set will contain.

    If the list is empty then all metrics will be returned. Note: tx_metrics is
    optional, it is applicable where implementation is able to retrieve transmitter
    information. In order to get Tx metrics, tx_metric must be added in metric_names
    and all supported Tx metrics will be returned as listed in metric response.
    """


class EgressOnlyTracking(TypedDict, total=False):
    port_names: List[str]
    """
    Egress only tracking metrics will be retrieved for these port names. If no
    port-names are provided, egress_only_tracking metrics will be returned for all
    ports which have one or more egress_only_tracking enabled.

    x-constraint:

    - /components/schemas/EgressOnlyTracking/properties/port_name
    """

    tagged_metrics: EgressOnlyTrackingTaggedMetrics
    """Filter for tagged metrics"""


class FlowTaggedMetricsFilter(TypedDict, total=False):
    name: str
    """
    A metric tag name that MUST exist in a flow packet or flow egress_packet
    configuration
    """

    values: List[str]
    """
    A list of filters that can be applied to the metric tag name. By default all
    values will be included in the flow metric results.
    """


class FlowTaggedMetrics(TypedDict, total=False):
    filters: Iterable[FlowTaggedMetricsFilter]
    """
    List of filters to selectively fetch tagged metrics with certain tag and
    corresponding value.
    """

    include: bool
    """Controls inclusion/exclusion of tagged metrics when fetching flow metrics."""

    include_empty_metrics: bool
    """
    Controls inclusion/exclusion of tagged metrics where each underlying attributes
    has zero value or absent value.
    """

    metric_names: List[
        Literal[
            "frames_tx",
            "frames_rx",
            "bytes_tx",
            "bytes_rx",
            "frames_tx_rate",
            "frames_rx_rate",
            "tx_l1_rate_bps",
            "rx_l1_rate_bps",
            "tx_rate_bytes",
            "rx_rate_bytes",
            "tx_rate_bps",
            "rx_rate_bps",
            "tx_rate_kbps",
            "rx_rate_kbps",
            "tx_rate_mbps",
            "rx_rate_mbps",
        ]
    ]
    """The list of metric names that the returned result set will contain.

    If the list is empty then all metrics will be returned.
    """


class Flow(TypedDict, total=False):
    flow_names: List[str]
    """
    Flow metrics will be retrieved for these flow names. If no flow names are
    specified then all flows will be returned.

    x-constraint:

    - /components/schemas/Flow/properties/name
    """

    metric_names: List[
        Literal[
            "transmit",
            "frames_tx",
            "frames_rx",
            "bytes_tx",
            "bytes_rx",
            "frames_tx_rate",
            "frames_rx_rate",
            "tx_l1_rate_bps",
            "rx_l1_rate_bps",
            "tx_rate_bytes",
            "rx_rate_bytes",
            "tx_rate_bps",
            "rx_rate_bps",
            "tx_rate_kbps",
            "rx_rate_kbps",
            "tx_rate_mbps",
            "rx_rate_mbps",
        ]
    ]
    """The list of metric names that the returned result set will contain.

    If the list is empty then all metrics will be returned.
    """

    tagged_metrics: FlowTaggedMetrics
    """Filter for tagged metrics"""


class Isis(TypedDict, total=False):
    column_names: List[
        Literal[
            "l1_sessions_up",
            "l1_session_flap",
            "l1_database_size",
            "l1_broadcast_hellos_sent",
            "l1_broadcast_hellos_received",
            "l1_point_to_point_hellos_sent",
            "l1_point_to_point_hellos_received",
            "l1_psnp_sent",
            "l1_psnp_received",
            "l1_csnp_sent",
            "l1_csnp_received",
            "l1_lsp_sent",
            "l1_lsp_received",
            "l2_sessions_up",
            "l2_session_flap",
            "l2_database_size",
            "l2_broadcast_hellos_sent",
            "l2_broadcast_hellos_received",
            "l2_point_to_point_hellos_sent",
            "l2_point_to_point_hellos_received",
            "l2_psnp_sent",
            "l2_psnp_received",
            "l2_csnp_sent",
            "l2_csnp_received",
            "l2_lsp_sent",
            "l2_lsp_received",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned except for any
    result_groups. The name of the ISIS Router cannot be excluded.
    """

    router_names: List[str]
    """The names of ISIS Routers to return results for.

    An empty list will return results for all ISIS router.

    x-constraint:

    - /components/schemas/Device.IsisRouter/properties/name
    """


class Lacp(TypedDict, total=False):
    column_names: List[
        Literal[
            "lacp_packets_rx",
            "lacp_packets_tx",
            "lacp_rx_errors",
            "activity",
            "timeout",
            "synchronization",
            "aggregatable",
            "collecting",
            "distributing",
            "system_id",
            "oper_key",
            "partner_id",
            "partner_key",
            "port_num",
            "partner_port_num",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned. The name of LAG and LAG
    member can not be excluded.
    """

    lag_member_port_names: List[str]
    """The names of LAG members (ports) for which LACP metrics to be returned.

    An empty list will return metrics for all LAG members.

    x-constraint:

    - /components/schemas/Port/properties/name
    """

    lag_names: List[str]
    """The names of LAG (ports group) for which LACP metrics to be returned.

    An empty list will return metrics for all LAGs.

    x-constraint:

    - /components/schemas/Lag/properties/name
    """


class Lag(TypedDict, total=False):
    column_names: List[
        Literal[
            "oper_status",
            "member_ports_up",
            "frames_tx",
            "frames_rx",
            "bytes_tx",
            "bytes_rx",
            "frames_tx_rate",
            "frames_rx_rate",
            "bytes_tx_rate",
            "bytes_rx_rate",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned. The name of the LAG
    cannot be excluded.
    """

    lag_names: List[str]
    """The names of LAGs to return results for.

    An empty list will return results for all LAGs.

    x-constraint:

    - /components/schemas/Lag/properties/name
    """


class Lldp(TypedDict, total=False):
    column_names: List[
        Literal["frames_rx", "frames_tx", "frames_error_rx", "frames_discard", "tlvs_discard", "tlvs_unknown"]
    ]
    """The requested list of column names for the result set.

    If the list is empty then metrics for all columns will be returned. The name of
    LLDP instance can not be excluded.
    """

    lldp_names: List[str]
    """The names of LLDP instances to return results for.

    An empty list will return results for all LLDP instances.

    x-constraint:

    - /components/schemas/Lldp/properties/name
    """


class Macsec(TypedDict, total=False):
    column_names: List[
        Literal[
            "session_state",
            "session_flap_count",
            "out_pkts_protected",
            "out_pkts_encrypted",
            "in_pkts_ok",
            "in_pkts_bad",
            "in_pkts_bad_tag",
            "in_pkts_late",
            "in_pkts_no_sci",
            "in_pkts_not_using_sa",
            "in_pkts_not_valid",
            "in_pkts_unknown_sci",
            "in_pkts_unused_sa",
            "in_pkts_invalid",
            "in_pkts_untagged",
            "out_octets_protected",
            "out_octets_encrypted",
            "in_octets_validated",
            "in_octets_decrypted",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned except for any
    result_groups. The name of the secure entity(secY) cannot be excluded.
    """

    secure_entity_names: List[str]
    """The names of secure entities(secYs) to return results for.

    An empty list will return results for all secYs.

    x-constraint:

    - /components/schemas/Macsec/properties/name
    """


class Mka(TypedDict, total=False):
    column_names: List[
        Literal[
            "session_state",
            "session_flap_count",
            "mkpdu_tx",
            "mkpdu_rx",
            "live_peer_count",
            "potential_peer_count",
            "latest_key_tx_peer_count",
            "latest_key_rx_peer_count",
            "malformed_mkpdu",
            "icv_mismatch",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned except for any
    result_groups. The name of the peer cannot be excluded.
    """

    peer_names: List[str]
    """The names of peers to return results for.

    An empty list will return results for all peers.

    x-constraint:

    - /components/schemas/Mka/properties/name
    """


class Ospfv2(TypedDict, total=False):
    column_names: List[
        Literal[
            "full_state_count",
            "down_state_count",
            "sessions_flap",
            "hellos_sent",
            "hellos_received",
            "dbd_sent",
            "dbd_received",
            "ls_request_sent",
            "ls_request_received",
            "ls_update_sent",
            "ls_update_received",
            "ls_ack_sent",
            "ls_ack_received",
            "lsa_sent",
            "lsa_received",
            "lsa_ack_sent",
            "lsa_ack_received",
            "router_lsa_sent",
            "router_lsa_received",
            "network_lsa_sent",
            "network_lsa_received",
            "summary_lsa_sent",
            "summary_lsa_received",
            "external_lsa_sent",
            "external_lsa_received",
            "nssa_lsa_sent",
            "nssa_lsa_received",
            "opaque_local_sent",
            "opaque_local_received",
            "opaque_area_sent",
            "opaque_area_received",
            "opaque_domain_sent",
            "opaque_domain_received",
        ]
    ]
    """
    The list of column names that the returned result set will contain. If the list
    is empty then all columns will be returned except for any result_groups. The
    name of the OSPFv2 Router cannot be excluded.
    """

    router_names: List[str]
    """The names of OSPFv2 routers to return results for.

    An empty list will return results for all OSPFv2 router.

    x-constraint:

    - /components/schemas/Device.Ospfv2/properties/name
    """


class Ospfv3(TypedDict, total=False):
    column_names: List[
        Literal[
            "full_state_count",
            "down_state_count",
            "sessions_flap",
            "hellos_sent",
            "hellos_received",
            "dbd_sent",
            "dbd_received",
            "ls_request_sent",
            "ls_request_received",
            "ls_update_sent",
            "ls_update_received",
            "ls_ack_sent",
            "ls_ack_received",
            "lsa_sent",
            "lsa_received",
            "router_lsa_sent",
            "router_lsa_received",
            "network_lsa_sent",
            "network_lsa_received",
            "inter_area_prefix_lsa_sent",
            "inter_area_prefix_lsa_received",
            "inter_area_router_lsa_sent",
            "inter_area_router_lsa_received",
            "external_lsa_sent",
            "external_lsa_received",
            "nssa_lsa_sent",
            "nssa_lsa_received",
            "link_lsa_sent",
            "link_lsa_received",
            "intra_area_prefix_lsa_sent",
            "intra_area_prefix_lsa_received",
        ]
    ]
    """
    The list of column names that the returned result set will contain. If the list
    is empty then all columns will be returned except for any result_groups. The
    name of the OSPFv3 Router cannot be excluded.
    """

    router_names: List[str]
    """The names of OSPFv3 routers to return results for.

    An empty list will return results for all OSPFv3 routers.

    x-constraint:

    - /components/schemas/Ospfv3.RouterInstance/properties/name
    """


class Port(TypedDict, total=False):
    column_names: List[
        Literal[
            "transmit",
            "location",
            "link",
            "capture",
            "frames_tx",
            "frames_rx",
            "bytes_tx",
            "bytes_rx",
            "frames_tx_rate",
            "frames_rx_rate",
            "bytes_tx_rate",
            "bytes_rx_rate",
            "last_change",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned. The name of the port
    cannot be excluded.
    """

    port_names: List[str]
    """The names of objects to return results for.

    An empty list will return all port row results.

    x-constraint:

    - /components/schemas/Port/properties/name
    """


class Rocev2FlowPerQp(TypedDict, total=False):
    column_names: List[
        Literal[
            "flow_name",
            "port_tx",
            "port_rx",
            "src_qp",
            "dest_qp",
            "src_ipv4",
            "dest_ipv4",
            "data_frames_tx",
            "data_frames_rx",
            "frame_delta",
            "data_frames_retransmitted",
            "frame_sequence_error",
            "tx_bytes",
            "rx_bytes",
            "data_tx_rate",
            "data_rx_rate",
            "message_tx",
            "message_complete_rx",
            "message_fail",
            "flow_completion_time",
            "avg_latency",
            "min_latency",
            "max_latency",
            "ecn_ce_rx",
            "cnp_tx",
            "cnp_rx",
            "ack_tx",
            "ack_rx",
            "nak_tx",
            "nak_rx",
            "first_timestamp",
            "last_timestamp",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned except for any
    result_groups. The name of the Flow cannot be excluded.
    """


class Rocev2Flow(TypedDict, total=False):
    choice: Literal["per_qp"]
    """Fetch stats per QP"""

    per_qp: Rocev2FlowPerQp
    """The names of RoCEv2 flows.

    An empty list will return results for all RoCEv2 flows.
    """


class Rocev2Ipv4PerPeer(TypedDict, total=False):
    column_names: List[
        Literal[
            "qp_configured",
            "qp_up",
            "qp_down",
            "connect_request_tx",
            "connect_request_rx",
            "connect_reply_tx",
            "connect_reply_rx",
            "ready_tx",
            "ready_rx",
            "disconnect_request_tx",
            "disconnect_request_rx",
            "disconnect_reply_tx",
            "disconnect_reply_rx",
            "reject_tx",
            "reject_rx",
            "unknown_msg_rx",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned except for any
    result_groups. The name of the RoCEv2 peer cannot be excluded.
    """

    peer_names: List[str]
    """The names of RoCEv2 over IPv4 peers to return results for.

    An empty list will return results for all RoCEv2 peers.

    x-constraint:

    - /components/schemas/Rocev2.V4peer/properties/name
    """


class Rocev2Ipv4(TypedDict, total=False):
    choice: Literal["per_peer"]
    """Fetch stats per_peer"""

    per_peer: Rocev2Ipv4PerPeer
    """The names of RoCEv2 over IPv4 peers to return results for.

    An empty list will return results for all RoCEv2 peers.
    """


class Rocev2Ipv6PerPeer(TypedDict, total=False):
    column_names: List[
        Literal[
            "qp_configured",
            "qp_up",
            "qp_down",
            "connect_request_tx",
            "connect_request_rx",
            "connect_reply_tx",
            "connect_reply_rx",
            "ready_tx",
            "ready_rx",
            "disconnect_request_tx",
            "disconnect_request_rx",
            "disconnect_reply_tx",
            "disconnect_reply_rx",
            "reject_tx",
            "reject_rx",
            "unknown_msg_rx",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the list is empty then all columns will be returned except for any
    result_groups. The name of the RoCEv2 peer cannot be excluded.
    """

    peer_names: List[str]
    """The names of RoCEv2 over IPv6 peers to return results for.

    An empty list will return results for all RoCEv2 peers.

    x-constraint:

    - /components/schemas/Rocev2.V6peer/properties/name
    """


class Rocev2Ipv6(TypedDict, total=False):
    choice: Literal["per_peer"]
    """Fetch stats per_peer"""

    per_peer: Rocev2Ipv6PerPeer
    """The names of RoCEv2 over IPv6 peers to return results for.

    An empty list will return results for all RoCEv2 peers.
    """


class Rsvp(TypedDict, total=False):
    column_names: List[
        Literal[
            "ingress_p2p_lsps_configured",
            "ingress_p2p_lsps_up",
            "egress_p2p_lsps_up",
            "lsp_flap_count",
            "paths_tx",
            "paths_rx",
            "resvs_tx",
            "resvs_rx",
            "path_tears_tx",
            "path_tears_rx",
            "resv_tears_tx",
            "resv_tears_rx",
            "path_errors_tx",
            "path_errors_rx",
            "resv_errors_tx",
            "resv_errors_rx",
            "resv_conf_tx",
            "resv_conf_rx",
            "hellos_tx",
            "hellos_rx",
            "acks_tx",
            "acks_rx",
            "nacks_tx",
            "nacks_rx",
            "srefresh_tx",
            "srefresh_rx",
            "bundle_tx",
            "bundle_rx",
            "path_reevaluation_request_tx",
            "path_reoptimizations",
        ]
    ]
    """The list of column names that the returned result set will contain.

    If the input list is empty then all columns will be returned except for any
    result_groups.
    """

    router_names: List[str]
    """The names of RSVP-TE Routers to return results for.

    An empty list as input will return results for all RSVP-TE routers.

    x-constraint:

    - /components/schemas/Device.Rsvp/properties/name
    """
