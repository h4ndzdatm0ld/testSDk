# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .metric_latency import MetricLatency
from .metric_timestamp import MetricTimestamp

__all__ = [
    "MonitorCreateMetricsResponse",
    "Bgpv4Metric",
    "Bgpv6Metric",
    "ConvergenceMetric",
    "ConvergenceMetricEvent",
    "Dhcpv4clientMetric",
    "Dhcpv4serverMetric",
    "Dhcpv6clientMetric",
    "Dhcpv6serverMetric",
    "EgressOnlyTrackingMetric",
    "EgressOnlyTrackingMetricTaggedMetric",
    "EgressOnlyTrackingMetricTaggedMetricTag",
    "EgressOnlyTrackingMetricTaggedMetricTimestamps",
    "EgressOnlyTrackingMetricTaggedMetricTxMetrics",
    "FlowMetric",
    "FlowMetricTaggedMetric",
    "FlowMetricTaggedMetricTag",
    "FlowMetricTaggedMetricTagValue",
    "IsisMetric",
    "LacpMetric",
    "LagMetric",
    "LldpMetric",
    "MacsecMetric",
    "MkaMetric",
    "Ospfv2Metric",
    "Ospfv3Metric",
    "PortMetric",
    "Rocev2FlowPerQpMetric",
    "Rocev2Ipv4PerPeerMetric",
    "Rocev2Ipv6PerPeerMetric",
    "RsvpMetric",
]


class Bgpv4Metric(BaseModel):
    end_of_rib_received: Optional[int] = None
    """
    Number of End-of-RIB markers received indicating the completion of the initial
    routing update for a particular <AFI, SAFI> address family after the session is
    established. For the IPv4 unicast address family, the End-of-RIB marker is an
    UPDATE message with the minimum length. For any other address family, it is an
    UPDATE message that contains only the MP_UNREACH_NLRI attribute with no
    withdrawn routes for that <AFI, SAFI>.
    """

    fsm_state: Optional[Literal["idle", "connect", "active", "opensent", "openconfirm", "established"]] = None
    """
    BGP peer FSM (Finite State Machine) state as Idle, Connect, Active, OpenSent,
    OpenConfirm and Established. In all the states except Established the BGP
    session is down. Idle refers to the Idle state of the FSM. Connect refers to the
    state where the session is waiting for the underlying transport session to be
    established. Active refers to the state where the session is awaiting for a
    connection from the remote peer. OpenSent refers to the state where the session
    is in the process of being established. The local system has sent an OPEN
    message. OpenConfirm refers to the state where the session is in the process of
    being established. The local system has sent and received an OPEN message and is
    awaiting a NOTIFICATION or KEEPALIVE message from remote peer. Established
    refers to the state where the BGP session with the peer is established.
    """

    keepalives_received: Optional[int] = None
    """Number of Keepalive messages received."""

    keepalives_sent: Optional[int] = None
    """Number of Keepalive messages sent."""

    name: Optional[str] = None
    """The name of a configured BGPv4 peer."""

    notifications_received: Optional[int] = None
    """Number of Notification messages received."""

    notifications_sent: Optional[int] = None
    """Number of Notification messages sent."""

    opens_received: Optional[int] = None
    """Number of Open messages received."""

    opens_sent: Optional[int] = None
    """Number of Open messages sent."""

    route_withdraws_received: Optional[int] = None
    """Number of route withdraws received."""

    route_withdraws_sent: Optional[int] = None
    """Number of route withdraws sent."""

    routes_advertised: Optional[int] = None
    """Number of routes advertised."""

    routes_received: Optional[int] = None
    """Number of routes received."""

    session_flap_count: Optional[int] = None
    """Number of times the session went from Up to Down state."""

    session_state: Optional[Literal["up", "down"]] = None
    """Session state as up or down.

    Up refers to an Established state and Down refers to any other state.
    """

    updates_received: Optional[int] = None
    """Number of Update messages received."""

    updates_sent: Optional[int] = None
    """Number of Update messages sent."""


class Bgpv6Metric(BaseModel):
    end_of_rib_received: Optional[int] = None
    """
    Number of End-of-RIB markers received indicating the completion of the initial
    routing update for a particular <AFI, SAFI> address family after the session is
    established. For the IPv4 unicast address family, the End-of-RIB marker is an
    UPDATE message with the minimum length. For any other address family, it is an
    UPDATE message that contains only the MP_UNREACH_NLRI attribute with no
    withdrawn routes for that <AFI, SAFI>.
    """

    fsm_state: Optional[Literal["idle", "connect", "active", "opensent", "openconfirm", "established"]] = None
    """
    BGP peer FSM (Finite State Machine) state as Idle, Connect, Active, OpenSent,
    OpenConfirm and Established. In all the states except Established the BGP
    session is down. Idle refers to the Idle state of the FSM. Connect refers to the
    state where the session is waiting for the underlying transport session to be
    established. Active refers to the state where the session is awaiting for a
    connection from the remote peer. OpenSent refers to the state where the session
    is in the process of being established. The local system has sent an OPEN
    message. OpenConfirm refers to the state where the session is in the process of
    being established. The local system has sent and received an OPEN message and is
    awaiting a NOTIFICATION or KEEPALIVE message from remote peer. Established
    refers to the state where the BGP session with the peer is established.
    """

    keepalives_received: Optional[int] = None
    """Number of Keepalive messages received."""

    keepalives_sent: Optional[int] = None
    """Number of Keepalive messages sent."""

    name: Optional[str] = None
    """The name of a configured BGPv6 peer."""

    notifications_received: Optional[int] = None
    """Number of Notification messages received."""

    notifications_sent: Optional[int] = None
    """Number of Notification messages sent."""

    opens_received: Optional[int] = None
    """Number of Open messages received."""

    opens_sent: Optional[int] = None
    """Number of Open messages sent."""

    route_withdraws_received: Optional[int] = None
    """Number of route withdraws received."""

    route_withdraws_sent: Optional[int] = None
    """Number of route withdraws sent."""

    routes_advertised: Optional[int] = None
    """Number of routes advertised."""

    routes_received: Optional[int] = None
    """Number of routes received."""

    session_flap_count: Optional[int] = None
    """Number of times the session went from Up to Down state."""

    session_state: Optional[Literal["up", "down"]] = None
    """Session state as up or down.

    Up refers to an Established state and Down refers to any other state.
    """

    updates_received: Optional[int] = None
    """Number of Update messages received."""

    updates_sent: Optional[int] = None
    """Number of Update messages sent."""


class ConvergenceMetricEvent(BaseModel):
    begin_timestamp_ns: Optional[float] = None
    """The timestamp(nanoseconds) of the starting event that triggers convergence."""

    end_timestamp_ns: Optional[float] = None
    """The timestamp(nanoseconds) of the end event that triggers convergence."""

    source: Optional[str] = None
    """The source of the event.

    The source MUST be the value of one of the x-constraint paths, which means the
    source MUST be a unique name in the configuration.

    x-constraint:

    - /components/schemas/Port/properties/name
    - /components/schemas/Flow/properties/name
    - /components/schemas/Device.Bgpv4Route/properties/name
    - /components/schemas/Device.Bgpv6Route/properties/name
    """

    type: Optional[
        Literal[
            "link_down",
            "link_up",
            "route_withdraw",
            "route_advertise",
            "flow_rx_rate_above_threshold",
            "flow_rx_rate_below_threshold",
        ]
    ] = None
    """The type of control plane or data plane event that occurred."""


class ConvergenceMetric(BaseModel):
    control_plane_data_plane_convergence_us: Optional[float] = None
    """
    The total convergence time(microseconds), between the event that caused the
    switchover until an acceptable amount of traffic was received at time Above
    Threshold Timestamp, when the rate crosses above the configured
    rx_rate_threshold.
    """

    data_plane_convergence_us: Optional[float] = None
    """The convergence time(microseconds) measured from the data plane perspective
    only.

    It measures the time w.r.t. last start of the traffic of the affected flow from
    Below Threshold Timestamp, when the rate on Test Port 2 crosses below the Rx
    Threshold until an acceptable amount of traffic was received at time Above
    Threshold Timestamp, when the rate crosses above the configured
    rx_rate_threshold.
    """

    events: Optional[List[ConvergenceMetricEvent]] = None
    """The events that were used to determine the convergence analytics."""

    name: Optional[str] = None
    """The name of a flow."""


class Dhcpv4clientMetric(BaseModel):
    acks_received: Optional[int] = None
    """Number of lease DHCPACK messages received."""

    declines_sent: Optional[int] = None
    """Number of DHCPDECLINE messages sent."""

    discovers_sent: Optional[int] = None
    """Number of DHCPDISCOVER messages sent."""

    nacks_received: Optional[int] = None
    """Number of negative lease DHCPNACK messages received."""

    name: Optional[str] = None
    """The name of a configured DHCPv4 client."""

    offers_received: Optional[int] = None
    """Number of DHCPOFFER messages received."""

    releases_sent: Optional[int] = None
    """Number of DHCPRELEASE messages sent."""

    requests_sent: Optional[int] = None
    """Number of DHCPREQUEST messages sent."""


class Dhcpv4serverMetric(BaseModel):
    acks_sent: Optional[int] = None
    """Number of lease DHCPACK messages sent."""

    declines_received: Optional[int] = None
    """Number of DHCPDECLINE messages received."""

    discovers_received: Optional[int] = None
    """Number of DHCPDISCOVER messages received."""

    nacks_sent: Optional[int] = None
    """Number of negative lease DHCPNACK messages sent."""

    name: Optional[str] = None
    """The name of a configured DHCPv4 Server."""

    offers_sent: Optional[int] = None
    """Number of DHCPOFFER messages sent."""

    releases_received: Optional[int] = None
    """Number of DHCPRELEASE messages received."""

    requests_received: Optional[int] = None
    """Number of DHCPOFFER messages received."""


class Dhcpv6clientMetric(BaseModel):
    advertisements_ignored: Optional[int] = None
    """Number of DHCPADVERTISE messages ignored."""

    advertisements_received: Optional[int] = None
    """Number of DHCPADVERTISE messages received."""

    information_requests_sent: Optional[int] = None
    """Number of DHCP Inform requests sent."""

    nacks_received: Optional[int] = None
    """Number of negative lease DHCPNACK messages received."""

    name: Optional[str] = None
    """The name of a configured DHCPv6 client."""

    rapid_commit_replies_received: Optional[int] = None
    """Number of rapid commit DHCP Reply messages received."""

    rapid_commit_solicits_sent: Optional[int] = None
    """Number of rapid commit DHCPSOLICIT messages sent."""

    rebinds_sent: Optional[int] = None
    """Number of DHCP rebind messages sent."""

    reconfigures_received: Optional[int] = None
    """Number of DHCP Reconfigure messages received."""

    releases_sent: Optional[int] = None
    """Number of DHCP Release messages sent."""

    renews_sent: Optional[int] = None
    """Number of DHCP renew messages sent."""

    replies_received: Optional[int] = None
    """Number of DHCPOFFER messages received."""

    requests_sent: Optional[int] = None
    """Number of DHCPREQUEST messages sent."""

    solicits_sent: Optional[int] = None
    """Number of DHCPSOLICIT messages sent."""


class Dhcpv6serverMetric(BaseModel):
    advertisements_sent: Optional[int] = None
    """Number of DHCP Advertise messages sent."""

    confirms_received: Optional[int] = None
    """Number of DHCP Confirm messages received."""

    declines_received: Optional[int] = None
    """Number of DHCP Decline messages received."""

    information_requests_received: Optional[int] = None
    """Number of DHCP Information Request messages received."""

    nacks_sent: Optional[int] = None
    """Number of naks sent for DHCPREQUEST messages."""

    name: Optional[str] = None
    """The name of a configured DHCPv6 Server."""

    rebinds_received: Optional[int] = None
    """Number of DHCP Rebind messages received."""

    reconfigures_sent: Optional[int] = None
    """Number of DHCP Reconfigure messages sent."""

    relay_forwards_received: Optional[int] = None
    """Number of DHCP Relay agent forward messages received."""

    relay_replies_sent: Optional[int] = None
    """Number of DHCP reply messages sent to Relay agent."""

    releases_received: Optional[int] = None
    """Number of DHCP Release messages received."""

    renewals_received: Optional[int] = None
    """Number of DHCP Renewal messages received."""

    replies_sent: Optional[int] = None
    """Number of DHCP Reply messages sent."""

    requests_received: Optional[int] = None
    """Number of DHCPREQUEST messages received."""

    solicits_ignored: Optional[int] = None
    """Number of DHCPSOLICIT messages ignored."""

    solicits_received: Optional[int] = None
    """Number of DHCPSOLICIT messages received."""


class EgressOnlyTrackingMetricTaggedMetricTag(BaseModel):
    name: Optional[str] = None
    """Name of packet field metric tag"""

    value: Optional[str] = None
    """Value of packet field metric tag in hexadecimal format"""


class EgressOnlyTrackingMetricTaggedMetricTimestamps(BaseModel):
    first_timestamp_ns: Optional[float] = None
    """First timestamp in nanoseconds"""

    last_timestamp_ns: Optional[float] = None
    """Last timestamp in nanoseconds"""


class EgressOnlyTrackingMetricTaggedMetricTxMetrics(BaseModel):
    bytes_tx: Optional[int] = None
    """The current total number of bytes transmitted"""

    frames_tx: Optional[int] = None
    """The current total number of frames transmitted"""

    frames_tx_rate: Optional[float] = None
    """The current rate of frames transmitted"""

    loss: Optional[float] = None
    """The percentage of lost frames"""

    port_tx: Optional[str] = None
    """The name of the transmit port"""

    tx_l1_rate_bps: Optional[float] = None
    """The Layer 1 transmission rate in bits per second."""

    tx_rate_bps: Optional[float] = None
    """The transmission rate in bits per second."""

    tx_rate_bytes: Optional[float] = None
    """The transmission rate in bytes per second."""

    tx_rate_kbps: Optional[float] = None
    """The transmission rate in Kilobits per second."""

    tx_rate_mbps: Optional[float] = None
    """The transmission rate in Megabits per second."""


class EgressOnlyTrackingMetricTaggedMetric(BaseModel):
    bytes_rx: Optional[int] = None
    """The current total number of bytes received"""

    frames_rx: Optional[int] = None
    """The current total number of valid frames received"""

    frames_rx_rate: Optional[float] = None
    """The current rate of valid frames received"""

    rx_l1_rate_bps: Optional[float] = None
    """The Layer 1 receive rate in bits per second."""

    rx_rate_bps: Optional[float] = None
    """The receive rate in bits per second."""

    rx_rate_bytes: Optional[float] = None
    """The receive rate in bytes per second."""

    rx_rate_kbps: Optional[float] = None
    """The receive rate in Kilobits per second."""

    rx_rate_mbps: Optional[float] = None
    """The receive rate in Megabits per second."""

    tags: Optional[List[EgressOnlyTrackingMetricTaggedMetricTag]] = None
    """List of tag and value pairs"""

    timestamps: Optional[EgressOnlyTrackingMetricTaggedMetricTimestamps] = None
    """
    The container for timestamp metrics. The container will be empty if the
    timestamp has not been configured for the flow.
    """

    tx_metrics: Optional[EgressOnlyTrackingMetricTaggedMetricTxMetrics] = None
    """
    The container for tx metrics. The container will be empty if the tx metrics has
    not been configured.
    """


class EgressOnlyTrackingMetric(BaseModel):
    port_rx: Optional[str] = None
    """The name of the receive port"""

    tagged_metrics: Optional[List[EgressOnlyTrackingMetricTaggedMetric]] = None
    """
    List of metrics corresponding to a set of values applicable for configured
    metric tags in egress packet header fields. The container is keyed by list of
    tag-value pairs.
    """


class FlowMetricTaggedMetricTagValue(BaseModel):
    choice: Optional[Literal["hex", "str"]] = None
    """Available formats for metric tag value"""

    hex: Optional[str] = None
    """Value represented in hexadecimal format"""

    str: Optional[builtins.str] = None
    """Value represented in string format"""


class FlowMetricTaggedMetricTag(BaseModel):
    name: Optional[str] = None
    """Name of packet field metric tag"""

    value: Optional[FlowMetricTaggedMetricTagValue] = None
    """A container for metric tag value"""


class FlowMetricTaggedMetric(BaseModel):
    bytes_rx: Optional[int] = None
    """The current total number of bytes received"""

    bytes_tx: Optional[int] = None
    """The current total number of bytes transmitted"""

    frames_rx: Optional[int] = None
    """The current total number of valid frames received"""

    frames_rx_rate: Optional[float] = None
    """The current rate of valid frames received"""

    frames_tx: Optional[int] = None
    """The current total number of frames transmitted"""

    frames_tx_rate: Optional[float] = None
    """The current rate of frames transmitted"""

    latency: Optional[MetricLatency] = None
    """The container for latency metrics.

    The min/max/avg values are dependent on the type of latency measurement mode
    that is configured. The container will be empty if the latency has not been
    configured for the flow.
    """

    loss: Optional[float] = None
    """The percentage of lost frames"""

    rx_l1_rate_bps: Optional[float] = None
    """The Layer 1 receive rate in bits per second."""

    rx_rate_bps: Optional[float] = None
    """The receive rate in bits per second."""

    rx_rate_bytes: Optional[float] = None
    """The receive rate in bytes per second."""

    rx_rate_kbps: Optional[float] = None
    """The receive rate in Kilobits per second."""

    rx_rate_mbps: Optional[float] = None
    """The receive rate in Megabits per second."""

    tags: Optional[List[FlowMetricTaggedMetricTag]] = None
    """List of tag and value pairs"""

    timestamps: Optional[MetricTimestamp] = None
    """
    The container for timestamp metrics. The container will be empty if the
    timestamp has not been configured for the flow.
    """

    tx_l1_rate_bps: Optional[float] = None
    """The Layer 1 transmission rate in bits per second."""

    tx_rate_bps: Optional[float] = None
    """The transmission rate in bits per second."""

    tx_rate_bytes: Optional[float] = None
    """The transmission rate in bytes per second."""

    tx_rate_kbps: Optional[float] = None
    """The transmission rate in Kilobits per second."""

    tx_rate_mbps: Optional[float] = None
    """The transmission rate in Megabits per second."""


class FlowMetric(BaseModel):
    bytes_rx: Optional[int] = None
    """The current total number of bytes received"""

    bytes_tx: Optional[int] = None
    """The current total number of bytes transmitted"""

    frames_rx: Optional[int] = None
    """The current total number of valid frames received"""

    frames_rx_rate: Optional[float] = None
    """The current rate of valid frames received"""

    frames_tx: Optional[int] = None
    """The current total number of frames transmitted"""

    frames_tx_rate: Optional[float] = None
    """The current rate of frames transmitted"""

    latency: Optional[MetricLatency] = None
    """The container for latency metrics.

    The min/max/avg values are dependent on the type of latency measurement mode
    that is configured. The container will be empty if the latency has not been
    configured for the flow.
    """

    loss: Optional[float] = None
    """The percentage of lost frames"""

    name: Optional[str] = None
    """The name of the flow"""

    port_rx: Optional[str] = None
    """The name of the receive port"""

    port_tx: Optional[str] = None
    """The name of the transmit port"""

    rx_l1_rate_bps: Optional[float] = None
    """The Layer 1 receive rate in bits per second."""

    rx_rate_bps: Optional[float] = None
    """The receive rate in bits per second."""

    rx_rate_bytes: Optional[float] = None
    """The receive rate in bytes per second."""

    rx_rate_kbps: Optional[float] = None
    """The receive rate in Kilobits per second."""

    rx_rate_mbps: Optional[float] = None
    """The receive rate in Megabits per second."""

    tagged_metrics: Optional[List[FlowMetricTaggedMetric]] = None
    """
    List of metrics corresponding to a set of values applicable for configured
    metric tags in ingress or egress packet header fields of corresponding flow. The
    container is keyed by list of tag-value pairs.
    """

    timestamps: Optional[MetricTimestamp] = None
    """
    The container for timestamp metrics. The container will be empty if the
    timestamp has not been configured for the flow.
    """

    transmit: Optional[Literal["started", "stopped", "paused"]] = None
    """The transmit state of the flow."""

    tx_l1_rate_bps: Optional[float] = None
    """The Layer 1 transmission rate in bits per second."""

    tx_rate_bps: Optional[float] = None
    """The transmission rate in bits per second."""

    tx_rate_bytes: Optional[float] = None
    """The transmission rate in bytes per second."""

    tx_rate_kbps: Optional[float] = None
    """The transmission rate in Kilobits per second."""

    tx_rate_mbps: Optional[float] = None
    """The transmission rate in Megabits per second."""


class IsisMetric(BaseModel):
    l1_broadcast_hellos_received: Optional[int] = None
    """Number of Level 1 Hello messages received."""

    l1_broadcast_hellos_sent: Optional[int] = None
    """Number of Level 1 Hello messages sent."""

    l1_csnp_received: Optional[int] = None
    """Number of Level 1 (L1) Complete Sequence Number Packet (CSNPs) received."""

    l1_csnp_sent: Optional[int] = None
    """Number of Level 1 (L1) Complete Sequence Number Packet (CSNPs) sent."""

    l1_database_size: Optional[int] = None
    """Number of Link State Updates (LSPs) in the Level 1 LSP Databases."""

    l1_lsp_received: Optional[int] = None
    """Number of Level 1 (L1) Link State Protocol Data Units (LSPs) received."""

    l1_lsp_sent: Optional[int] = None
    """Number of Level 1 (L1) Link State Protocol Data Units (LSPs) sent."""

    l1_point_to_point_hellos_received: Optional[int] = None
    """Number of Level 1 Point-to-Point(P2P) Hello messages received."""

    l1_point_to_point_hellos_sent: Optional[int] = None
    """Number of Level 1 Point-to-Point(P2P) Hello messages sent."""

    l1_psnp_received: Optional[int] = None
    """Number of Level 1 (L1) Complete Sequence Number Packet (PSNPs) received."""

    l1_psnp_sent: Optional[int] = None
    """Number of Level 1 (L1) Partial Sequence Number Packet (PSNPs) sent."""

    l1_session_flap: Optional[int] = None
    """The number of Level 1 Sessions Flap."""

    l1_sessions_up: Optional[int] = None
    """The number of Level 1 (L1) sessions that are fully up."""

    l2_broadcast_hellos_received: Optional[int] = None
    """Number of Level 2 Hello messages received."""

    l2_broadcast_hellos_sent: Optional[int] = None
    """Number of Level 2 Hello messages sent."""

    l2_csnp_received: Optional[int] = None
    """Number of Level 2 (L2) Complete Sequence Number Packet (CSNPs) received."""

    l2_csnp_sent: Optional[int] = None
    """Number of Level 2 (L2) Complete Sequence Number Packet (CSNPs) sent."""

    l2_database_size: Optional[int] = None
    """Number of Link State Updates (LSPs) in the Level 2 LSP Databases."""

    l2_lsp_received: Optional[int] = None
    """Number of Level 2 (L2) Link State Protocol Data Units (LSPs) received."""

    l2_lsp_sent: Optional[int] = None
    """Number of Level 2 (L2) Link State Protocol Data Units (LSPs) sent."""

    l2_point_to_point_hellos_received: Optional[int] = None
    """Number of Level 2 Point-to-Point(P2P) Hello messages received."""

    l2_point_to_point_hellos_sent: Optional[int] = None
    """Number of Level 2 Point-to-Point(P2P) Hello messages sent."""

    l2_psnp_received: Optional[int] = None
    """Number of Level 2 (L2) Complete Sequence Number Packet (PSNPs) received."""

    l2_psnp_sent: Optional[int] = None
    """Number of Level 2 (L2) Partial Sequence Number Packet (PSNPs) sent."""

    l2_session_flap: Optional[int] = None
    """The number of Level 2 Sessions Flap."""

    l2_sessions_up: Optional[int] = None
    """The number of Level 2 (L2) sessions that are fully up."""

    name: Optional[str] = None
    """The name of a configured ISIS router."""


class LacpMetric(BaseModel):
    activity: Optional[Literal["active", "passive"]] = None
    """Indicates participant is active or passive."""

    aggregatable: Optional[bool] = None
    """
    A true value indicates that the participant will allow the link to be used as
    part of the aggregate. A false value indicates the link should be used as an
    individual link.
    """

    collecting: Optional[bool] = None
    """
    If true, the participant is collecting incoming frames on the link, otherwise
    false.
    """

    distributing: Optional[bool] = None
    """
    When true, the participant is distributing outgoing frames; when false,
    distribution is disabled.
    """

    lacp_packets_rx: Optional[int] = None
    """Number of LACPDUs received."""

    lacp_packets_tx: Optional[int] = None
    """Number of LACPDUs transmitted."""

    lacp_rx_errors: Optional[int] = None
    """Number of LACPDUs receive packet errors."""

    lag_member_port_name: Optional[str] = None
    """The name of a LAG member (port) configured with LACP."""

    lag_name: Optional[str] = None
    """The name of a LAG (ports group) configured with LACP."""

    oper_key: Optional[int] = None
    """Current operational value of the key for the aggregate interface."""

    partner_id: Optional[str] = None
    """MAC address representing the protocol partner's interface system ID."""

    partner_key: Optional[int] = None
    """Operational value of the protocol partner's key."""

    partner_port_num: Optional[int] = None
    """Port number of the partner (remote) port for this member port."""

    port_num: Optional[int] = None
    """Port number of the local (actor) aggregation member."""

    synchronization: Optional[Literal["in_sync", "out_sync"]] = None
    """Indicates whether the participant is in-sync or out-of-sync."""

    system_id: Optional[str] = None
    """MAC address that defines the local system ID for the aggregate interface."""

    timeout: Optional[Literal["short", "long"]] = None
    """The timeout type (short or long) used by the participant."""


class LagMetric(BaseModel):
    bytes_rx: Optional[int] = None
    """The current total number of valid bytes received."""

    bytes_rx_rate: Optional[float] = None
    """The current rate of bytes received."""

    bytes_tx: Optional[int] = None
    """The current total number of bytes transmitted."""

    bytes_tx_rate: Optional[float] = None
    """The current rate of bytes transmitted."""

    frames_rx: Optional[int] = None
    """The current total number of valid frames received."""

    frames_rx_rate: Optional[float] = None
    """The current rate of valid frames received."""

    frames_tx: Optional[int] = None
    """The current total number of frames transmitted."""

    frames_tx_rate: Optional[float] = None
    """The current rate of frames transmitted."""

    member_ports_up: Optional[int] = None
    """The number of LAG member ports up."""

    name: Optional[str] = None
    """The name of a configured LAG

    x-constraint:

    - /components/schemas/Lag/properties/name
    """

    oper_status: Optional[Literal["up", "down"]] = None
    """The current operational state of the LAG.

    The state can be up or down. State 'up' indicates member_ports_up >= min_links.
    """


class LldpMetric(BaseModel):
    frames_discard: Optional[int] = None
    """Number of LLDP frames received that are discarded.

    This stat should be incremented when one or more of the three mandatory TLVs at
    the beginning of the LLDPDU is missing, out of order or contains an out of range
    information string length. This stat should follow the validation rules in
    section 10.3.2 of IEEE Std 802.1 AB-2005.
    """

    frames_error_rx: Optional[int] = None
    """Number of LLDP frames received with packet errors.

    This stat should be incremented based on statsFramesInErrorsTotal increment rule
    in section 10.3.2 of IEEE Std 802.1 AB-2005.
    """

    frames_rx: Optional[int] = None
    """Number of LLDP frames received."""

    frames_tx: Optional[int] = None
    """Number of LLDP frames transmitted."""

    name: Optional[str] = None
    """The name of the configured LLDP instance."""

    tlvs_discard: Optional[int] = None
    """Number of LLDP tlvs received that are discarded.

    If any TLV contains an error condition specific for that particular TLV or if
    any TLV extends past the physical end of the frame then these TLVs will be
    discarded.
    """

    tlvs_unknown: Optional[int] = None
    """Number of LLDP unknown tlvs received.

    If the OUI of the organizationlly specific TLV and/or organizationally defined
    subtype are not recognized,or if TLV type value is in the range of reserved TLV
    types then these TLVs will be considered as unknown TLVs.
    """


class MacsecMetric(BaseModel):
    in_octets_decrypted: Optional[int] = None
    """InOctetsDecrypted, the number of received bytes decrypted."""

    in_octets_validated: Optional[int] = None
    """InOctetsValidated, the number of received bytes validated."""

    in_pkts_bad: Optional[int] = None
    """
    The total number of received bad packets that failed atleast one validation
    check.
    """

    in_pkts_bad_tag: Optional[int] = None
    """InPktsBadTag, the number of packets discarded due to bad tag/ICV."""

    in_pkts_invalid: Optional[int] = None
    """InPktsInvalid, the number of packets received with invalid ICV."""

    in_pkts_late: Optional[int] = None
    """InPktsLate, the number of packets discarded out of window."""

    in_pkts_no_sci: Optional[int] = None
    """InPktsNoSCI,the number of packets discarded due to unknown SCI."""

    in_pkts_not_using_sa: Optional[int] = None
    """InPktsNotUsingSA, the number of packets discarded due to unused SA."""

    in_pkts_not_valid: Optional[int] = None
    """InPktsNotValid, the number of packets discarded due to invalid ICV."""

    in_pkts_ok: Optional[int] = None
    """InPktsOk, the number of valid packets received."""

    in_pkts_unknown_sci: Optional[int] = None
    """InPktsUnknownSCI, the number of packets received with unknown SCI."""

    in_pkts_untagged: Optional[int] = None
    """InPktsUntagged, the number of non-MACsec packets received."""

    in_pkts_unused_sa: Optional[int] = None
    """InPktsUnusedSA, the number of packets received with unused SA."""

    name: Optional[str] = None
    """The name of a configured MACsec secure entity(secY)."""

    out_octets_encrypted: Optional[int] = None
    """OutOctetsEncrypted, the number of bytes transmitted as encrypted."""

    out_octets_protected: Optional[int] = None
    """OutOctetsProtected, the number of bytes transmitted as protected."""

    out_pkts_encrypted: Optional[int] = None
    """OutPktsEncrypted, the number of encrypted packets transmitted."""

    out_pkts_protected: Optional[int] = None
    """OutPktsProtected, the number of protected packets transmitted."""

    session_flap_count: Optional[int] = None
    """Number of times the session went from Up to Down state."""

    session_state: Optional[Literal["up", "down"]] = None
    """Session state as up or down.

    Up refers to an Established state and Down refers to any other state.
    """


class MkaMetric(BaseModel):
    icv_mismatch: Optional[int] = None
    """Number of MKA Protocol Data Unit(MKPDU) frames with ICV mismatch Rx."""

    latest_key_rx_peer_count: Optional[int] = None
    """Number of MKA latest key Rx peers."""

    latest_key_tx_peer_count: Optional[int] = None
    """Number of MKA latest key Tx peers."""

    live_peer_count: Optional[int] = None
    """Number of MKA live peers."""

    malformed_mkpdu: Optional[int] = None
    """Number of malformed MKA Protocol Data Unit(MKPDU) frames Rx."""

    mkpdu_rx: Optional[int] = None
    """Number of MKA protocol data unit(MKPDU) frames Rx."""

    mkpdu_tx: Optional[int] = None
    """Number of MKA protocol data unit(MKPDU) frames Tx."""

    name: Optional[str] = None
    """The name of a configured MKA peer."""

    potential_peer_count: Optional[int] = None
    """Number of MKA potential peers."""

    session_flap_count: Optional[int] = None
    """Number of times the session went from Up to Down state."""

    session_state: Optional[Literal["up", "down"]] = None
    """Session state as up or down.

    Up refers to an Established state and Down refers to any other state.
    """


class Ospfv2Metric(BaseModel):
    dbd_received: Optional[int] = None
    """The number of OSPFv2 Database Description (DBD) messages received."""

    dbd_sent: Optional[int] = None
    """The number of OSPFv2 Database Description (DBD) messages transmitted."""

    down_state_count: Optional[int] = None
    """The number of OSPFv2 sessions in down state."""

    external_lsa_received: Optional[int] = None
    """The number of OSPFv2 External (Type 5) LSAs received."""

    external_lsa_sent: Optional[int] = None
    """The number of OSPFv2 External (Type 5) LSAs transmitted."""

    full_state_count: Optional[int] = None
    """The number of OSPFv2 sessions in up state."""

    hellos_received: Optional[int] = None
    """The number of OSPFv2 Hello messages received."""

    hellos_sent: Optional[int] = None
    """The number of OSPFv2 Hello messages transmitted."""

    ls_ack_received: Optional[int] = None
    """The number of OSPFv2 LinkState (LS) Acknowledgement messages received."""

    ls_ack_sent: Optional[int] = None
    """The number of OSPFv2 LinkState (LS) Acknowledgement messages transmitted."""

    ls_request_received: Optional[int] = None
    """The number of OSPFv2 LinkState (LS) Request messages received."""

    ls_request_sent: Optional[int] = None
    """The number of OSPFv2 LinkState (LS) Request messages transmitted."""

    ls_update_received: Optional[int] = None
    """The number of OSPFv2 LinkState (LS) Update messages received."""

    ls_update_sent: Optional[int] = None
    """The number of OSPFv2 LinkState (LS) Update messages transmitted."""

    lsa_ack_received: Optional[int] = None
    """
    The total number of OSPFv2 LinkState Advertisement (LSA) acknowledge messages
    received .
    """

    lsa_ack_sent: Optional[int] = None
    """The total number of OSPFv2 LinkState Advertisement (LSA) messages acknowledged."""

    lsa_received: Optional[int] = None
    """The total number of OSPFv2 LinkState Advertisement (LSA) messages received."""

    lsa_sent: Optional[int] = None
    """The total number of OSPFv2 LinkState Advertisement (LSA) messages transmitted."""

    name: Optional[str] = None
    """The name of a configured OSPFv2 router."""

    network_lsa_received: Optional[int] = None
    """The number of OSPFv2 Network (Type 2) LSAs transmitted."""

    network_lsa_sent: Optional[int] = None
    """The number of OSPFv2 Network (Type 2) LSAs transmitted."""

    nssa_lsa_received: Optional[int] = None
    """The number of OSPFv2 NSSA (Type 7) LSAs received."""

    nssa_lsa_sent: Optional[int] = None
    """The number of OSPFv2 NSSA (Type 7) LSAs transmitted."""

    opaque_area_received: Optional[int] = None
    """The number of OSPFv2 Opaque Area (Type 10) LSAs received."""

    opaque_area_sent: Optional[int] = None
    """The number of OSPF Opaque Area (Type 10) LSAs transmitted."""

    opaque_domain_received: Optional[int] = None
    """The number of OSPFv2 Opaque Domain (Type 11) LSAs received."""

    opaque_domain_sent: Optional[int] = None
    """The number of OSPFv2 Opaque Domain (Type 11) LSAs transmitted."""

    opaque_local_received: Optional[int] = None
    """The number of OSPFv2 Opaque Local (Type 9) LSAs received."""

    opaque_local_sent: Optional[int] = None
    """The number of OSPFv2 Opaque Local (Type 9) LSAs transmitted."""

    router_lsa_received: Optional[int] = None
    """The number of OSPFv2 Router (Type 1) LSAs received."""

    router_lsa_sent: Optional[int] = None
    """The number of OSPFv2 Router (Type 1) LSAs transmitted."""

    sessions_flap: Optional[int] = None
    """The number of change of OSPFv2 sessions from up to down state."""

    summary_lsa_received: Optional[int] = None
    """The number of OSPFv2 Summary IP (Type 3) LSA received."""

    summary_lsa_sent: Optional[int] = None
    """The number of OSPFv2 Summary IP (Type 3) LSAs transmitted."""


class Ospfv3Metric(BaseModel):
    dbd_received: Optional[int] = None
    """The number of OSPFv3 Database Description (DBD) messages received."""

    dbd_sent: Optional[int] = None
    """The number of OSPFv3 Database Description (DBD) messages transmitted."""

    down_state_count: Optional[int] = None
    """The number of OSPFv3 sessions in down state."""

    external_lsa_received: Optional[int] = None
    """The number of OSPFv3 External (Type 5) LSAs received."""

    external_lsa_sent: Optional[int] = None
    """The number of OSPFv3 External (Type 5) LSAs transmitted."""

    full_state_count: Optional[int] = None
    """The number of OSPFv3 sessions in up state."""

    hellos_received: Optional[int] = None
    """The number of OSPFv3 Hello messages received."""

    hellos_sent: Optional[int] = None
    """The number of OSPFv3 Hello messages transmitted."""

    inter_area_prefix_lsa_received: Optional[int] = None
    """The number of OSPFv3 Inter-Area-Prefix (Type 3) LSAs received."""

    inter_area_prefix_lsa_sent: Optional[int] = None
    """The number of OSPFv3 Inter-Area-Prefix (Type 3) LSAs transmitted."""

    inter_area_router_lsa_received: Optional[int] = None
    """The number of OSPFv3 Inter-Area-Router (Type 4) LSAs received."""

    inter_area_router_lsa_sent: Optional[int] = None
    """The number of OSPFv3 Inter-Area-Router (Type 4) LSAs transmitted."""

    intra_area_prefix_lsa_received: Optional[int] = None
    """The number of OSPFv3 Intra-Area-Prefix (Type 9) LSAs received."""

    intra_area_prefix_lsa_sent: Optional[int] = None
    """The number of OSPFv3 Intra-Area-Prefix (Type 9) LSAs transmitted."""

    link_lsa_received: Optional[int] = None
    """The number of OSPFv3 Link (Type 8) LSAs received."""

    link_lsa_sent: Optional[int] = None
    """The number of OSPFv3 Link (Type 8) LSAs transmitted."""

    ls_ack_received: Optional[int] = None
    """The number of OSPFv3 LinkState (LS) Acknowledgement messages received."""

    ls_ack_sent: Optional[int] = None
    """The number of OSPFv3 LinkState (LS) Acknowledgement messages transmitted."""

    ls_request_received: Optional[int] = None
    """The number of OSPFv3 LinkState (LS) Request messages received."""

    ls_request_sent: Optional[int] = None
    """The number of OSPFv3 LinkState (LS) Request messages transmitted."""

    ls_update_received: Optional[int] = None
    """The number of OSPFv3 LinkState (LS) Update messages received."""

    ls_update_sent: Optional[int] = None
    """The number of OSPFv3 LinkState (LS) Update messages transmitted."""

    lsa_received: Optional[int] = None
    """The total number of OSPFv3 LinkState Advertisement (LSA) messages received."""

    lsa_sent: Optional[int] = None
    """The total number of OSPFv3 LinkState Advertisement (LSA) messages transmitted."""

    name: Optional[str] = None
    """The name of a configured OSPFv3 router."""

    network_lsa_received: Optional[int] = None
    """The number of OSPFv3 Network (Type 2) LSAs received."""

    network_lsa_sent: Optional[int] = None
    """The number of OSPFv3 Network (Type 2) LSAs transmitted."""

    nssa_lsa_received: Optional[int] = None
    """The number of OSPFv3 NSSA (Type 7) LSAs received."""

    nssa_lsa_sent: Optional[int] = None
    """The number of OSPFv3 NSSA (Type 7) LSAs transmitted."""

    router_lsa_received: Optional[int] = None
    """The number of OSPFv3 Router (Type 1) LSAs received."""

    router_lsa_sent: Optional[int] = None
    """The number of OSPFv3 Router (Type 1) LSAs transmitted."""

    sessions_flap: Optional[int] = None
    """The number of change of OSPFv3 sessions from up to down state."""


class PortMetric(BaseModel):
    bytes_rx: Optional[int] = None
    """The current total number of valid bytes received"""

    bytes_rx_rate: Optional[float] = None
    """The current rate of bytes received"""

    bytes_tx: Optional[int] = None
    """The current total number of bytes transmitted"""

    bytes_tx_rate: Optional[float] = None
    """The current rate of bytes transmitted"""

    capture: Optional[Literal["started", "stopped"]] = None
    """The state of the test port capture infrastructure.

    The string can be started, stopped or a custom error message.
    """

    frames_rx: Optional[int] = None
    """The current total number of valid frames received"""

    frames_rx_rate: Optional[float] = None
    """The current rate of valid frames received"""

    frames_tx: Optional[int] = None
    """The current total number of frames transmitted"""

    frames_tx_rate: Optional[float] = None
    """The current rate of frames transmitted"""

    last_change: Optional[int] = None
    """
    The timestamp indicates the absolute time of the last link state change of the
    test port (e.g., up-to-down transition).

    The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1,
    1970 00:00:00 UTC).
    """

    link: Optional[Literal["up", "down"]] = None
    """
    The state of the test port link The string can be up, down or a custom error
    message.
    """

    location: Optional[str] = None
    """The state of the connection to the test port location.

    The format should be the configured port location along with any custom
    connection state message.
    """

    name: Optional[str] = None
    """The name of a configured port

    x-constraint:

    - /components/schemas/Port/properties/name
    """

    transmit: Optional[Literal["started", "stopped"]] = None
    """The transmit state of the flow."""


class Rocev2FlowPerQpMetric(BaseModel):
    ack_rx: Optional[int] = None
    """Current number of ACK received."""

    ack_tx: Optional[int] = None
    """Current number of ACK transmitted."""

    avg_latency: Optional[int] = None
    """Current average latency measured in ns."""

    cnp_rx: Optional[int] = None
    """Current number of CNP received."""

    cnp_tx: Optional[int] = None
    """Current number of CNP transmitted."""

    data_frames_retransmitted: Optional[int] = None
    """Current number of data frames re-transmitted."""

    data_frames_rx: Optional[int] = None
    """Current number of data frames received."""

    data_frames_tx: Optional[int] = None
    """Current number of data frames transmitted."""

    data_rx_rate: Optional[int] = None
    """Current rate at which data is received in Gbps."""

    data_tx_rate: Optional[int] = None
    """Current rate at which data is transmitted in Gbps."""

    dest_ipv4: Optional[str] = None
    """Current destination address."""

    dest_qp: Optional[int] = None
    """Current destination QP number."""

    ecn_ce_rx: Optional[int] = None
    """Current number of ECN-CE Recevied."""

    first_timestamp: Optional[str] = None
    """First Timestamp."""

    flow_completion_time: Optional[int] = None
    """Current flow comletion time in ms."""

    flow_name: Optional[str] = None
    """Flow Name."""

    frame_delta: Optional[int] = None
    """Current differnece between tx and rx data frames"""

    frame_sequence_error: Optional[int] = None
    """Current number of frame sequence errors."""

    last_timestamp: Optional[str] = None
    """Last Timestamp."""

    max_latency: Optional[int] = None
    """Current maximum latency measured in ns."""

    message_complete_rx: Optional[int] = None
    """Current number of Message Complete received."""

    message_fail: Optional[int] = None
    """Current number of Message Fail count."""

    message_tx: Optional[int] = None
    """Current number of Message transmitted."""

    min_latency: Optional[int] = None
    """Current minimum latency measured in ns."""

    nak_rx: Optional[int] = None
    """Current number of NAK received."""

    nak_tx: Optional[int] = None
    """Current number of NAK transmitted."""

    port_rx: Optional[str] = None
    """The name of the receive port"""

    port_tx: Optional[str] = None
    """The name of the transmit port"""

    rx_bytes: Optional[int] = None
    """Current number of bytes received."""

    src_ipv4: Optional[str] = None
    """Current source address."""

    src_qp: Optional[int] = None
    """Current source QP number."""

    tx_bytes: Optional[int] = None
    """Current number of bytes transmitted."""


class Rocev2Ipv4PerPeerMetric(BaseModel):
    connect_reply_rx: Optional[int] = None
    """Number of REP Message Received."""

    connect_reply_tx: Optional[int] = None
    """Number of REP Message Transmitted."""

    connect_request_rx: Optional[int] = None
    """Number of REQ Message Received."""

    connect_request_tx: Optional[int] = None
    """Number of REQ Message Transmitted."""

    disconnect_reply_rx: Optional[int] = None
    """Number of DREP Message Received."""

    disconnect_reply_tx: Optional[int] = None
    """Number of DREP Message Transmitted."""

    disconnect_request_rx: Optional[int] = None
    """Number of DREQ Message Received."""

    disconnect_request_tx: Optional[int] = None
    """Number of DREQ Message Transmitted."""

    name: Optional[str] = None
    """The name of a configured RoCEv2 peer."""

    qp_configured: Optional[int] = None
    """Number of QPs configured on this port."""

    qp_down: Optional[int] = None
    """Number of QPs that have not come UP."""

    qp_up: Optional[int] = None
    """Number of QPs that are in UP state."""

    ready_rx: Optional[int] = None
    """Number of RTU Message Received."""

    ready_tx: Optional[int] = None
    """Number of RTU Message Transmitted."""

    reject_tx: Optional[int] = None
    """Number of REJ Message Transmitted."""

    unknown_msg_rx: Optional[int] = None
    """Number of Unknown Message Received."""


class Rocev2Ipv6PerPeerMetric(BaseModel):
    connect_reply_rx: Optional[int] = None
    """Number of REP Message Received."""

    connect_reply_tx: Optional[int] = None
    """Number of REP Message Transmitted."""

    connect_request_rx: Optional[int] = None
    """Number of REQ Message Received."""

    connect_request_tx: Optional[int] = None
    """Number of REQ Message Transmitted."""

    disconnect_reply_rx: Optional[int] = None
    """Number of DREP Message Received."""

    disconnect_reply_tx: Optional[int] = None
    """Number of DREP Message Transmitted."""

    disconnect_request_rx: Optional[int] = None
    """Number of DREQ Message Received."""

    disconnect_request_tx: Optional[int] = None
    """Number of DREQ Message Transmitted."""

    name: Optional[str] = None
    """The name of a configured RoCEv2 peer."""

    qp_configured: Optional[int] = None
    """Number of QPs configured on this port."""

    qp_down: Optional[int] = None
    """Number of QPs that have not come UP."""

    qp_up: Optional[int] = None
    """Number of QPs that are in UP state."""

    ready_rx: Optional[int] = None
    """Number of RTU Message Received."""

    ready_tx: Optional[int] = None
    """Number of RTU Message Transmitted."""

    reject_tx: Optional[int] = None
    """Number of REJ Message Transmitted."""

    unknown_msg_rx: Optional[int] = None
    """Number of Unknown Message Received."""


class RsvpMetric(BaseModel):
    acks_rx: Optional[int] = None
    """The number of Ack messages received by this RSVP router."""

    acks_tx: Optional[int] = None
    """The number of Ack messages sent by this RSVP router."""

    bundle_rx: Optional[int] = None
    """The number of Bundle messages received by this RSVP router."""

    bundle_tx: Optional[int] = None
    """The number of Bundle messages sent by this RSVP router."""

    egress_p2p_lsps_up: Optional[int] = None
    """
    The number of egress point-to-point LSPs for which Path requests were
    successfully processed and is currently up.
    """

    hellos_rx: Optional[int] = None
    """The number of Hello messages received by this RSVP router."""

    hellos_tx: Optional[int] = None
    """The number of Hello messages sent by this RSVP router."""

    ingress_p2p_lsps_configured: Optional[int] = None
    """
    The number of ingress point-to-point LSPs configured or transiting through the
    RSVP router which have been initated from the test port.
    """

    ingress_p2p_lsps_up: Optional[int] = None
    """
    The number of ingress point-to-point LSPs for which Resv has been received and
    is currently up.
    """

    lsp_flap_count: Optional[int] = None
    """
    The number of times an LSP went from up to down state either because it timed
    out while waiting for Refreshes or a PathTear or ResvTear message was received
    which caused the LSP to flap.
    """

    nacks_rx: Optional[int] = None
    """The number of Nack messages received by this RSVP router."""

    nacks_tx: Optional[int] = None
    """The number of Nack messages sent by this RSVP router."""

    name: Optional[str] = None
    """The name of a configured RSVP router."""

    path_errors_rx: Optional[int] = None
    """The number of Path Error messages received by this RSVP router."""

    path_errors_tx: Optional[int] = None
    """The number of Path Error messages sent by this RSVP router."""

    path_reevaluation_request_tx: Optional[int] = None
    """
    The number of Path messages with Path Re-evaluation Request enabled sent by this
    RSVP router.
    """

    path_reoptimizations: Optional[int] = None
    """
    The number of successfully completed Make-Before-Break operations on LSPs on
    this RSVP router.
    """

    path_tears_rx: Optional[int] = None
    """The number of Path Tear messages received by this RSVP router."""

    path_tears_tx: Optional[int] = None
    """The number of Path Tear messages sent by this RSVP router."""

    paths_rx: Optional[int] = None
    """The number of Path messages received by this RSVP router."""

    paths_tx: Optional[int] = None
    """The number of Path messages sent by this RSVP router."""

    resv_conf_rx: Optional[int] = None
    """The number of ResvConf messages received by this RSVP router."""

    resv_conf_tx: Optional[int] = None
    """The number of ResvConf messages sent by this RSVP router."""

    resv_errors_rx: Optional[int] = None
    """The number of Resv Error messages received by this RSVP router."""

    resv_errors_tx: Optional[int] = None
    """The number of Resv Error messages sent by this RSVP router."""

    resv_tears_rx: Optional[int] = None
    """The number of Resv Tear messages received by this RSVP router."""

    resv_tears_tx: Optional[int] = None
    """The number of Resv Tear messages sent by this RSVP router."""

    resvs_rx: Optional[int] = None
    """The number of Resv messages received by this RSVP router."""

    resvs_tx: Optional[int] = None
    """The number of Resv messages sent by this RSVP router."""

    srefresh_rx: Optional[int] = None
    """The number of SRefresh messages received by this RSVP router."""

    srefresh_tx: Optional[int] = None
    """The number of SRefresh messages sent by this RSVP router."""


class MonitorCreateMetricsResponse(BaseModel):
    bgpv4_metrics: Optional[List[Bgpv4Metric]] = None

    bgpv6_metrics: Optional[List[Bgpv6Metric]] = None

    choice: Optional[
        Literal[
            "flow_metrics",
            "port_metrics",
            "bgpv4_metrics",
            "bgpv6_metrics",
            "isis_metrics",
            "lag_metrics",
            "lacp_metrics",
            "lldp_metrics",
            "rsvp_metrics",
            "dhcpv4_client",
            "dhcpv4_server",
            "dhcpv6_client",
            "dhcpv6_server",
            "ospfv2_metrics",
            "convergence_metrics",
            "macsec_metrics",
            "mka_metrics",
            "ospfv3_metrics",
            "rocev2_ipv4_per_peer_metrics",
            "rocev2_ipv6_per_peer_metrics",
            "rocev2_flow_per_qp_metrics",
            "egress_only_tracking_metrics",
        ]
    ] = None

    convergence_metrics: Optional[List[ConvergenceMetric]] = None

    dhcpv4client_metrics: Optional[List[Dhcpv4clientMetric]] = None

    dhcpv4server_metrics: Optional[List[Dhcpv4serverMetric]] = None

    dhcpv6client_metrics: Optional[List[Dhcpv6clientMetric]] = None

    dhcpv6server_metrics: Optional[List[Dhcpv6serverMetric]] = None

    egress_only_tracking_metrics: Optional[List[EgressOnlyTrackingMetric]] = None

    flow_metrics: Optional[List[FlowMetric]] = None

    isis_metrics: Optional[List[IsisMetric]] = None

    lacp_metrics: Optional[List[LacpMetric]] = None

    lag_metrics: Optional[List[LagMetric]] = None

    lldp_metrics: Optional[List[LldpMetric]] = None

    macsec_metrics: Optional[List[MacsecMetric]] = None

    mka_metrics: Optional[List[MkaMetric]] = None

    ospfv2_metrics: Optional[List[Ospfv2Metric]] = None

    ospfv3_metrics: Optional[List[Ospfv3Metric]] = None

    port_metrics: Optional[List[PortMetric]] = None

    rocev2_flow_per_qp_metrics: Optional[List[Rocev2FlowPerQpMetric]] = None

    rocev2_ipv4_per_peer_metrics: Optional[List[Rocev2Ipv4PerPeerMetric]] = None

    rocev2_ipv6_per_peer_metrics: Optional[List[Rocev2Ipv6PerPeerMetric]] = None

    rsvp_metrics: Optional[List[RsvpMetric]] = None
