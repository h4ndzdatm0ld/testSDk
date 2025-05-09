# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "ControlSetStateParams",
    "Port",
    "PortCapture",
    "PortLink",
    "Protocol",
    "ProtocolAll",
    "ProtocolBgp",
    "ProtocolBgpPeers",
    "ProtocolIsis",
    "ProtocolIsisRouters",
    "ProtocolLacp",
    "ProtocolLacpAdmin",
    "ProtocolLacpMemberPorts",
    "ProtocolOspfv2",
    "ProtocolOspfv2Routers",
    "ProtocolOspfv3",
    "ProtocolOspfv3Routers",
    "ProtocolRocev2",
    "ProtocolRocev2Peers",
    "ProtocolRoute",
    "Traffic",
    "TrafficFlowTransmit",
]


class ControlSetStateParams(TypedDict, total=False):
    choice: Required[Literal["port", "protocol", "traffic"]]

    port: Port
    """States associated with configured ports."""

    protocol: Protocol
    """States associated with protocols on configured resources."""

    traffic: Traffic
    """States associated with configured flows"""


class PortCapture(TypedDict, total=False):
    state: Required[Literal["start", "stop"]]
    """The capture state."""

    port_names: List[str]
    """The names of ports to which the capture state will be applied to.

    If the list of port_names is empty or null the state will be applied to all
    configured ports. If the list is not empty any port that is not included in the
    list of port_names MUST be ignored and not included in the state change.

    x-constraint:

    - /components/schemas/Port/properties/name
    """


class PortLink(TypedDict, total=False):
    state: Required[Literal["up", "down"]]
    """The link state."""

    port_names: List[str]
    """The names of target ports. An empty or null list will target all ports.

    x-constraint:

    - /components/schemas/Port/properties/name
    """


class Port(TypedDict, total=False):
    choice: Required[Literal["link", "capture"]]

    capture: PortCapture
    """Sets the capture state of configured ports"""

    link: PortLink
    """Sets the link of configured ports."""


class ProtocolAll(TypedDict, total=False):
    state: Required[Literal["start", "stop"]]
    """Protocol states"""


class ProtocolBgpPeers(TypedDict, total=False):
    state: Required[Literal["up", "down"]]
    """The desired state of BGP peer.

    If the desired state is 'up', underlying IP interface(s) would be brought up
    automatically (if not already up), would attempt to bring up the BGP session(s)
    and advertise route(s), if configured. If the desired state is 'down', BGP
    session(s) would be brought down.
    """

    peer_names: List[str]
    """The names of BGP peers for which the state has to be applied.

    An empty or null list will control all BGP peers.

    x-constraint:

    - /components/schemas/Bgp.V4Peer/properties/name
    - /components/schemas/Bgp.V6Peer/properties/name
    """


class ProtocolBgp(TypedDict, total=False):
    choice: Required[Literal["peers"]]

    peers: ProtocolBgpPeers
    """Sets state of configured BGP peers."""


class ProtocolIsisRouters(TypedDict, total=False):
    state: Required[Literal["up", "down"]]
    """The desired state of ISIS router.

    If the desired state is 'up', would attempt to bring up the ISIS session(s) with
    respective peer(s) and advertise route(s), if configured. If the desired state
    is 'down', would bring down ISIS session(s) with respective peer(s).
    """

    router_names: List[str]
    """The names of ISIS routers for which the state has to be applied.

    An empty or null list will control all ISIS routers.

    x-constraint:

    - /components/schemas/Device.IsisRouter/properties/name
    """


class ProtocolIsis(TypedDict, total=False):
    choice: Required[Literal["routers"]]

    routers: ProtocolIsisRouters
    """Sets state of configured ISIS routers."""


class ProtocolLacpAdmin(TypedDict, total=False):
    state: Required[Literal["up", "down"]]
    """The LACP Member admin state.

    'up' will send LACPDUs with 'sync' flag set on selected member ports. 'down'
    will send LACPDUs with 'sync' flag unset on selected member ports.
    """

    lag_member_names: List[str]
    """The names of LAG members (ports) for which the state has to be applied.

    An empty or null list will control all LAG members.

    x-constraint:

    - /components/schemas/Port/properties/name
    """


class ProtocolLacpMemberPorts(TypedDict, total=False):
    state: Required[Literal["up", "down"]]
    """The desired LACP member port state."""

    lag_member_names: List[str]
    """The names of LAG members (ports) for which the state has to be applied.

    An empty or null list will control all LAG members.

    x-constraint:

    - /components/schemas/Port/properties/name
    """


class ProtocolLacp(TypedDict, total=False):
    choice: Required[Literal["admin", "member_ports"]]

    admin: ProtocolLacpAdmin
    """Sets admin state of LACP configured on LAG members"""

    member_ports: ProtocolLacpMemberPorts
    """Sets state of LACP member ports configured on LAG."""


class ProtocolOspfv2Routers(TypedDict, total=False):
    state: Required[Literal["up", "down"]]
    """The desired state of OSPFv2 router.

    If the desired state is 'up', would attempt to bring up the OSPFv2 session(s)
    with respective peer(s) and advertise route(s), if configured. If the desired
    state is 'down', would bring down OSPFv2 session(s) with respective peer(s).
    """

    router_names: List[str]
    """The names of OSPFv2 routers for which the state has to be applied.

    An empty or null list will control all OSPFv2 routers.

    x-constraint:

    - /components/schemas/Device.Ospfv2/properties/name
    """


class ProtocolOspfv2(TypedDict, total=False):
    choice: Required[Literal["routers"]]

    routers: ProtocolOspfv2Routers
    """Sets state of configured OSPFv2 routers."""


class ProtocolOspfv3Routers(TypedDict, total=False):
    state: Required[Literal["up", "down"]]
    """The desired state of OSPFv3 router.

    If the desired state is 'up', would attempt to bring up the OSPFv3 session(s)
    with respective peer(s) and advertise route(s), if configured. If the desired
    state is 'down', would bring down OSPFv3 session(s) with respective peer(s).
    """

    router_names: List[str]
    """The names of OSPFv3 routers for which the state has to be applied.

    An empty or null list will control all OSPFv3 routers.

    x-constraint:

    - /components/schemas/Ospfv3.RouterInstance/properties/name
    """


class ProtocolOspfv3(TypedDict, total=False):
    choice: Required[Literal["routers"]]

    routers: ProtocolOspfv3Routers
    """Sets state of configured OSPFv3 routers."""


class ProtocolRocev2Peers(TypedDict, total=False):
    state: Required[Literal["up", "down"]]
    """The desired state of RoCEv2 peer.

    If the desired state is 'up', underlying IP interface(s) would be brought up
    automatically (if not already up), would attempt to bring up the RoCEv2
    session(s). If the desired state is 'down', RoCEv2 session(s) would be brought
    down.
    """

    peer_names: List[str]
    """The names of RoCEv2 peers for which the state has to be applied.

    An empty or null list will control all RoCEv2 peers.

    x-constraint:

    - /components/schemas/Rocev2.V4Peer/properties/name
    - /components/schemas/Rocev2.V6Peer/properties/name
    """


class ProtocolRocev2(TypedDict, total=False):
    choice: Required[Literal["peers"]]

    peers: ProtocolRocev2Peers
    """Sets state of configured RoCEv2 peers."""


class ProtocolRoute(TypedDict, total=False):
    state: Required[Literal["withdraw", "advertise"]]
    """Route states"""

    names: List[str]
    """The names of device route objects to control.

    If no names are specified then all route objects that match the x-constraint
    will be affected.

    x-constraint:

    - /components/schemas/Bgp.V4RouteRange/properties/name
    - /components/schemas/Bgp.V6RouteRange/properties/name
    - /components/schemas/Isis.V4RouteRange/properties/name
    - /components/schemas/Isis.V6RouteRange/properties/name
    - /components/schemas/Ospfv2.V4RouteRange/properties/name
    - /components/schemas/Ospfv3.V6RouteRange/properties/name
    """


class Protocol(TypedDict, total=False):
    choice: Required[Literal["all", "route", "lacp", "bgp", "isis", "ospfv2", "ospfv3"]]

    all: ProtocolAll
    """
    Sets all configured protocols to `start` or `stop` state. Setting protocol state
    to `start` shall be a no-op if preceding `set_config` API call was made with
    `config.options.protocol_options.auto_start_all` set to `true` or if all the
    configured protocols are already started.
    """

    bgp: ProtocolBgp
    """Sets state of configured BGP peers."""

    isis: ProtocolIsis
    """Sets state of configured ISIS routers."""

    lacp: ProtocolLacp
    """Sets state of configured LACP"""

    ospfv2: ProtocolOspfv2
    """Sets state of configured OSPFv2 routers."""

    ospfv3: ProtocolOspfv3
    """Sets state of configured OSPFv3 routers."""

    rocev2: ProtocolRocev2
    """Sets state of configured RoCEv2 peers."""

    route: ProtocolRoute
    """Sets the state of configured routes"""


class TrafficFlowTransmit(TypedDict, total=False):
    state: Required[Literal["start", "stop", "pause", "resume"]]
    """
    The transmit state. If the value of the state property is 'start' then all flows
    defined by the 'flow_names' property will be started and the metric counters
    MUST be cleared prior to starting the flow(s). If the value of the state
    property is 'stop' then all flows defined by the 'flow_names' property will be
    stopped and the metric counters MUST NOT be cleared. If the value of the state
    property is 'pause' then all flows defined by the 'flow_names' property will be
    paused and the metric counters MUST NOT be cleared. If the value of the state
    property is 'resume' then any paused flows defined by the 'flow_names' property
    will start transmit at the point at which they were paused. Any flow that is
    stopped will start transmit at the beginning of the flow. The flow(s) MUST NOT
    have their metric counters cleared.
    """

    flow_names: List[str]
    """The names of flows to which the transmit state will be applied to.

    If the list of flow_names is empty or null the state will be applied to all
    configured flows. If the list is not empty any flow that is not included in the
    list of flow_names MUST be ignored and not included in the state change.

    x-constraint:

    - /components/schemas/Flow/properties/name
    """


class Traffic(TypedDict, total=False):
    choice: Required[Literal["flow_transmit"]]

    flow_transmit: TrafficFlowTransmit
    """Provides state control of flow transmission."""
