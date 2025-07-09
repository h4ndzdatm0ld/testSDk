# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .flow_delay_param import FlowDelayParam
from .flow_header_param import FlowHeaderParam

__all__ = [
    "FlowParam",
    "TxRx",
    "TxRxDevice",
    "TxRxPort",
    "Duration",
    "DurationBurst",
    "DurationBurstInterBurstGap",
    "DurationContinuous",
    "DurationFixedPackets",
    "DurationFixedSeconds",
    "Metrics",
    "MetricsLatency",
    "MetricsPredefinedMetricTags",
    "MetricsRxTxRatio",
    "Rate",
    "Size",
    "SizeIncrement",
    "SizeRandom",
    "SizeWeightPairs",
    "SizeWeightPairsCustom",
]


class TxRxDevice(TypedDict, total=False):
    rx_names: Required[List[str]]
    """TBD

    x-constraint:

    - /components/schemas/Device.Ethernet/properties/name
    - /components/schemas/Device.Ipv4/properties/name
    - /components/schemas/Device.Ipv6/properties/name
    - /components/schemas/Bgp.V4RouteRange/properties/name
    - /components/schemas/Bgp.V6RouteRange/properties/name
    - /components/schemas/Bgp.CMacIpRange/properties/name
    - /components/schemas/Rsvp.LspIpv4Interface.P2PEgressIpv4Lsp/properties/name
    - /components/schemas/Isis.V4RouteRange/properties/name
    - /components/schemas/Isis.V6RouteRange/properties/name
    - /components/schemas/Device.Dhcpv4client/properties/name
    - /components/schemas/Ospfv2.V4RouteRange/properties/name
    - /components/schemas/Ospfv3.V6RouteRange/properties/name
    - /components/schemas/Device.Dhcpv6client/properties/name
    """

    tx_names: Required[List[str]]
    """TBD

    x-constraint:

    - /components/schemas/Device.Ethernet/properties/name
    - /components/schemas/Device.Ipv4/properties/name
    - /components/schemas/Device.Ipv6/properties/name
    - /components/schemas/Bgp.V4RouteRange/properties/name
    - /components/schemas/Bgp.V6RouteRange/properties/name
    - /components/schemas/Bgp.CMacIpRange/properties/name
    - /components/schemas/Rsvp.LspIpv4Interface.P2PIngressIpv4Lsp/properties/name
    - /components/schemas/Isis.V4RouteRange/properties/name
    - /components/schemas/Isis.V6RouteRange/properties/name
    - /components/schemas/Ospfv2.V4RouteRange/properties/name
    - /components/schemas/Ospfv3.V6RouteRange/properties/name
    - /components/schemas/Device.Dhcpv4client/properties/name
    - /components/schemas/Device.Dhcpv6client/properties/name
    """

    mode: Literal["mesh", "one_to_one"]
    """
    Determines the intent of creating traffic sub-flow(s) between the device
    endpoints, from the entities of <b>tx_names</b> to the entities of
    <b>rx_names</b> to derive how <b>auto</b> packet fields can be populated with
    the actual value(s) by the implementation.

    The <b>one_to_one</b> mode creates traffic sub-flow(s) between each device
    endpoint pair in tx_names to rx_names by index. The length of tx_names and
    rx_names MUST be the same. The same device name can be repeated multiple times
    in tx_names or rx_names, in any order to create desired meshing between
    device(s). For 2 values in tx_names and 2 values in rx_names, 2 device endpoint
    pairs would be generated (each pair representing a traffic sub-flow).

    The <b>mesh</b> mode creates traffic sub-flow(s) between each value in tx_names
    to every value in rx_names, forming the device endpoint pair(s). For 2 values in
    tx_names and 3 values in rx_names, generated device endpoint pairs would be
    2x3=6.

    A generated device endpoint pair with same device endpoint name for both
    transmit & receive device endpoint MUST raise an error.

    Packet fields of type <b>auto</b> would be populated with one value for each
    device endpoint pair (representing the traffic sub-flow). The value would be
    determined considering transmit & receive device of the sub-flow. And the
    sequence of the populated value(s) would be in the order of generated device
    endpoint pair(s). If 2 device endpoint pairs are generated (based on mode,
    tx_names and rx_names), say (d1 to d3) and (d2 to d3), and ethernet.dst is set
    as <b>auto</b>, then the auto field would be <b>replaced</b> by the
    implementation with a sequence of 2 values, [v1,v2] where v1 is determined using
    context (d1,d3) and v2 using context (d2,d3). The final outcome is that packets
    generated on the wire will contain the values v1,v2,v1,... for ethernet.dst
    field. Any non-auto packet fields should be configured accordingly. For example,
    non-auto packet field ethernet.src can be configured with values [u1, u2], where
    u1 & u2 are source MAC of the connected interface of device d1 and d2
    respectively. Then packets on the wire will contain correct value pairs
    (u1,v1),(u2,v2),(u1,v1),... for (ethernet.src,ethernet.dst) fields.
    """


class TxRxPort(TypedDict, total=False):
    tx_name: Required[str]
    """The unique name of a port that is the transmit port.

    x-constraint:

    - /components/schemas/Port/properties/name
    - /components/schemas/Lag/properties/name
    """

    rx_name: str
    """Deprecated: This property is deprecated in favor of property rx_names

    The unique name of a port that is the intended receive port.

    x-constraint:

    - /components/schemas/Port/properties/name
    - /components/schemas/Lag/properties/name
    """

    rx_names: List[str]
    """Unique name of ports or lags that are intended receive endpoints.

    x-constraint:

    - /components/schemas/Port/properties/name
    - /components/schemas/Lag/properties/name
    """


class TxRx(TypedDict, total=False):
    choice: Literal["port", "device"]
    """The type of transmit and receive container used by the flow."""

    device: TxRxDevice
    """A container for declaring a map of 1..n transmit devices to 1..n receive
    devices.

    This allows for a single flow to have different tx to rx device flows such as a
    single one to one map or a many to many map.
    """

    port: TxRxPort
    """
    A container for a transmit port and 0..n intended receive ports. When assigning
    this container to a flow the flows's packet headers will not be populated with
    any address resolution information such as source and/or destination addresses.
    For example Flow.Ethernet dst mac address values will be defaulted to 0. For
    full control over the Flow.properties.packet header contents use this container.
    """


class DurationBurstInterBurstGap(TypedDict, total=False):
    bytes: float
    """
    The amount of time between bursts expressed in bytes. A value of 0 indicates no
    gap between bursts.
    """

    choice: Literal["bytes", "nanoseconds", "microseconds"]
    """The type of inter burst gap units."""

    microseconds: float
    """
    The amount of time between bursts expressed in microseconds. A value of 0
    indicates no gap between bursts.
    """

    nanoseconds: float
    """
    The amount of time between bursts expressed in nanoseconds. A value of 0
    indicates no gap between bursts.
    """


class DurationBurst(TypedDict, total=False):
    bursts: int
    """
    The number of packet bursts transmitted per flow. A value of 0 implies
    continuous burst of packets.
    """

    gap: int
    """The minimum gap between packets expressed as bytes."""

    inter_burst_gap: DurationBurstInterBurstGap
    """The optional container for specifying a gap between bursts."""

    packets: int
    """The number of packets transmitted per burst."""


class DurationContinuous(TypedDict, total=False):
    delay: FlowDelayParam
    """
    The optional container to specify the delay before starting transmission of
    packets.
    """

    gap: int
    """The minimum gap between packets expressed as bytes."""


class DurationFixedPackets(TypedDict, total=False):
    delay: FlowDelayParam
    """
    The optional container to specify the delay before starting transmission of
    packets.
    """

    gap: int
    """The minimum gap between packets expressed as bytes."""

    packets: int
    """Stop transmit of the flow after this number of packets."""


class DurationFixedSeconds(TypedDict, total=False):
    delay: FlowDelayParam
    """
    The optional container to specify the delay before starting transmission of
    packets.
    """

    gap: int
    """The minimum gap between packets expressed as bytes."""

    seconds: float
    """Stop transmit of the flow after this number of seconds."""


class Duration(TypedDict, total=False):
    burst: DurationBurst
    """Transmits continuous or fixed burst of packets.

    For continuous burst of packets, it will not automatically stop. For fixed burst
    of packets, it will stop after transmitting fixed number of bursts.
    """

    choice: Literal["fixed_packets", "fixed_seconds", "burst", "continuous"]
    """A choice used to determine the type of duration."""

    continuous: DurationContinuous
    """Transmit will be continuous and will not stop automatically."""

    fixed_packets: DurationFixedPackets
    """Transmit a fixed number of packets after which the flow will stop."""

    fixed_seconds: DurationFixedSeconds
    """Transmit for a fixed number of seconds after which the flow will stop."""


class MetricsLatency(TypedDict, total=False):
    enable: bool
    """True to enable latency metrics using timestamps.

    Enabling this option may affect the resultant packet payload due to additional
    instrumentation data.
    """

    mode: Literal["store_forward", "cut_through"]
    """Select the type of latency measurement.

    The different types of latency measurements are:

    store_forward: The time interval starting when the last bit of the frame leaves
    the sending port and ending when the first bit of the frame is seen on the
    receiving port (LIFO). This is based on the RFC 1242 standard.

    cut_through: The time interval starting when the first bit of the frame leaves
    the sending port and ending when the first bit of the frame is seen on the
    receiving port (FIFO). This is based on the RFC 1242 standard.
    """


class MetricsPredefinedMetricTags(TypedDict, total=False):
    rx_name: bool
    """
    Enables Rx port or lag level disaggregation with predefined metrics tag name set
    as "rx_name". The Rx port / lag names can be found under tagged_metrics tag
    names in flow metrics response.
    """


class MetricsRxTxRatio(TypedDict, total=False):
    choice: Literal["rx_count", "value"]

    rx_count: object
    """
    This is for cases where one copy of Tx packet is received on all Rx ports and so
    the sum total of Rx packets received across all Rx ports is a multiple of Rx
    port count and Tx packets.
    """

    value: float
    """Should be a positive, non-zero value.

    The default value of 1, is when the Rx packet count across all ports is expected
    to match the Tx packet count. A custom integer value (>1) can be specified for
    loss calculation for cases when there are multiple destination addresses
    configured within one flow, but DUT is configured to replicate only to a subset
    of Rx ports. For cases when Tx side generates two packets from each source in
    1:1 protection mode but only one of the two packets are received by the Rx port,
    we may need to specify a fractional value instead.
    """


class Metrics(TypedDict, total=False):
    enable: bool
    """
    Enables flow metrics. Enabling this option may affect the resultant packet
    payload due to additional instrumentation data.
    """

    latency: MetricsLatency
    """Latency metrics."""

    loss: bool
    """Enables additional flow metric loss calculation."""

    predefined_metric_tags: MetricsPredefinedMetricTags
    """Predefined metric tags"""

    rx_tx_ratio: MetricsRxTxRatio
    """Rx Tx ratio."""

    timestamps: bool
    """Enables additional flow metric first and last timestamps."""


class Rate(TypedDict, total=False):
    bps: int
    """Bits per second."""

    choice: Literal["pps", "bps", "kbps", "mbps", "gbps", "percentage"]
    """The available types of flow rate."""

    gbps: int
    """Gigabits per second."""

    kbps: int
    """Kilobits per second."""

    mbps: int
    """Megabits per second."""

    percentage: float
    """The percentage of a port location's available bandwidth."""

    pps: int
    """Packets per second."""


class SizeIncrement(TypedDict, total=False):
    end: int
    """Ending frame size in bytes"""

    start: int
    """Starting frame size in bytes"""

    step: int
    """Step frame size in bytes"""


class SizeRandom(TypedDict, total=False):
    max: int

    min: int


class SizeWeightPairsCustom(TypedDict, total=False):
    size: int
    """The size of the frame (in bytes) for this weight pair."""

    weight: float
    """Weight assigned to the corresponding frame size in this weight pair.

    Higher weight means more packets.
    """


class SizeWeightPairs(TypedDict, total=False):
    choice: Literal["predefined", "custom"]

    custom: Iterable[SizeWeightPairsCustom]

    predefined: Literal["imix", "ipsec_imix", "ipv6_imix", "standard_imix", "tcp_imix"]
    """
    Specify predefined frame size distribution <size, weight> pairs (including IMIX
    distribution).
    The available predefined distribution pairs are:

    - IMIX (64:7, 570:4, and 1518:1)
    - IPSec IMIX (90:58.67, 92:2, 594:23.66 and 1418:15.67)
    - IPv6 IMIX (60:58.67, 496:2, 594:23.66 and 1518:15.67)
    - Standard IMIX (58:58.67, 62:2, 594:23.66 and 1518:15.67)
    - TCP IMIX (90:58.67, 92:2, 594:23.66 and 1518:15.67)
    """


class Size(TypedDict, total=False):
    choice: Literal["fixed", "increment", "random", "weight_pairs"]

    fixed: int

    increment: SizeIncrement
    """
    Frame size that increments from a starting size to an ending size incrementing
    by a step size.
    """

    random: SizeRandom
    """Random frame size from a min value to a max value."""

    weight_pairs: SizeWeightPairs
    """
    Frame size distribution, defined as <size, weight> pairs (including IMIX
    distribution). Frames are randomly generated such that the proportion of each
    frame size out of the total number of frames are matching with the weight value
    of the <size, weight> pair. However, as with any other probability distribution,
    the sample distribution is close to theoretical value only if the size of the
    sample is reasonably large. When the number of frames is very low the
    transmitted frames may not come close to the ratio described in the weight.
    """


class FlowParam(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    tx_rx: Required[TxRx]
    """The transmit and receive endpoints."""

    duration: Duration
    """The transmit duration of the packets."""

    egress_packet: Iterable[FlowHeaderParam]
    """
    Under Review: The packet header schema for egress tracking currently exposes
    unwanted fields. The query structure for tagged metrics inside flows metrics
    requires documenting expected response format.

    The list of protocol headers defining the shape of all intended packets in
    corresponding flow as it is received by traffic-generator port.

    For all protocol headers, only the `metric_tags` property is configurable.
    """

    metrics: Metrics
    """Flow metrics."""

    packet: Iterable[FlowHeaderParam]
    """
    The list of protocol headers defining the shape of all intended packets in
    corresponding flow as it is transmitted by traffic-generator port.

    The order of protocol headers assigned to the list is the order they will appear
    on the wire.

    In the case of an empty list the keyword/value of minItems: 1 indicates that an
    implementation MUST provide at least one Flow.Header object.

    The default value for the Flow.Header choice property is ethernet which will
    result in an implementation by default providing at least one ethernet packet
    header.
    """

    rate: Rate
    """The transmit rate of the packets."""

    size: Size
    """The size of the packets."""
