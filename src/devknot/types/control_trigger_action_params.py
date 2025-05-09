# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .cease_error_param import CeaseErrorParam
from .custom_error_param import CustomErrorParam
from .open_message_error_param import OpenMessageErrorParam
from .message_header_error_param import MessageHeaderErrorParam
from .update_message_error_param import UpdateMessageErrorParam

__all__ = [
    "ControlTriggerActionParams",
    "Protocol",
    "ProtocolBgp",
    "ProtocolBgpInitiateGracefulRestart",
    "ProtocolBgpInitiateGracefulRestartNotification",
    "ProtocolBgpNotification",
    "ProtocolIpv4",
    "ProtocolIpv4Ping",
    "ProtocolIpv4PingRequest",
    "ProtocolIpv6",
    "ProtocolIpv6Ping",
    "ProtocolIpv6PingRequest",
]


class ControlTriggerActionParams(TypedDict, total=False):
    choice: Required[Literal["protocol"]]

    protocol: Protocol
    """Actions associated with protocols on configured resources."""


class ProtocolBgpInitiateGracefulRestartNotification(TypedDict, total=False):
    cease: CeaseErrorParam
    """
    In the absence of any fatal errors, a BGP peer can close its BGP connection by
    sending the NOTIFICATION message with the Error Code Cease. The
    'hard_reset_code6_subcode9' subcode for Cease Notification can be used to signal
    a hard reset that will indicate that Graceful Restart cannot be performed, even
    when Notification extensions to Graceful Restart procedure is supported.
    """

    choice: Literal[
        "cease",
        "message_header_error",
        "open_message_error",
        "update_message_error",
        "hold_timer_expired",
        "finite_state_machine_error",
        "custom",
    ]
    """
    Each BGP NOTIFICATION message includes an Error Code field indicating what type
    of problem occurred. For certain Error Codes, an Error Subcode field provides
    additional details about the specific nature of the problem. The choice value
    will provide the Error Code used in NOTIFICATION message. The Subcode can be set
    for each of the corresponding errors except for Hold Timer Expired error and BGP
    Finite State Machine error. In both of these cases Subcode 0 will be sent. If a
    user wants to use non zero Sub Code then custom choice can be used.
    """

    custom: CustomErrorParam
    """
    A BGP peer can send NOTIFICATION message with user defined Error Code and Error
    Subcode.
    """

    finite_state_machine_error: object
    """
    Any error detected by the BGP Finite State Machine (e.g., receipt of an
    unexpected event) is indicated by sending the NOTIFICATION message with the
    Error Code-Finite State Machine Error(Error Code 5). The Sub Code used is 0. If
    a user wants to use non zero Sub Code then CustomError can be used.
    """

    hold_timer_expired: object
    """
    If a system does not receive successive KEEPALIVE, UPDATE, and/or NOTIFICATION
    messages within the period specified in the Hold Time field of the OPEN message,
    then the NOTIFICATION message with the Hold Timer Expired Error Code(Error
    Code 4) is sent and the BGP connection is closed. The Sub Code used is 0. If a
    user wants to use non zero Sub Code then CustomError can be used.
    """

    message_header_error: MessageHeaderErrorParam
    """
    All errors detected while processing the Message Header are indicated by sending
    the NOTIFICATION message with the Error Code-Message Header Error. The Error
    Subcode elaborates on the specific nature of the error.
    """

    open_message_error: OpenMessageErrorParam
    """
    All errors detected while processing the OPEN message are indicated by sending
    the NOTIFICATION message with the Error Code-Open Message Error. The Error
    Subcode elaborates on the specific nature of the error.
    """

    update_message_error: UpdateMessageErrorParam
    """
    All errors detected while processing the UPDATE message are indicated by sending
    the NOTIFICATION message with the Error Code-Update Message Error. The Error
    Subcode elaborates on the specific nature of the error.
    """


class ProtocolBgpInitiateGracefulRestart(TypedDict, total=False):
    notification: ProtocolBgpInitiateGracefulRestartNotification
    """
    Send a Notification to the peer as per configured parameters when initially
    bringing down a session as per configured parameters.
    """

    peer_names: List[str]
    """The names of device BGP peers objects to control.

    x-constraint:

    - /components/schemas/Bgp.V4Peer/properties/name
    - /components/schemas/Bgp.V6Peer/properties/name
    """

    restart_delay: int
    """
    Duration (in seconds) after which selected BGP peers will initiate Graceful
    restart by sending the Open Message with Restart State bit set in the Graceful
    Restart capability.
    """


class ProtocolBgpNotification(TypedDict, total=False):
    cease: CeaseErrorParam
    """
    In the absence of any fatal errors, a BGP peer can close its BGP connection by
    sending the NOTIFICATION message with the Error Code Cease. The
    'hard_reset_code6_subcode9' subcode for Cease Notification can be used to signal
    a hard reset that will indicate that Graceful Restart cannot be performed, even
    when Notification extensions to Graceful Restart procedure is supported.
    """

    choice: Literal[
        "cease",
        "message_header_error",
        "open_message_error",
        "update_message_error",
        "hold_timer_expired",
        "finite_state_machine_error",
        "custom",
    ]
    """
    Each BGP NOTIFICATION message includes an Error Code field indicating what type
    of problem occurred. For certain Error Codes, an Error Subcode field provides
    additional details about the specific nature of the problem. The choice value
    will provide the Error Code used in NOTIFICATION message. The Subcode can be set
    for each of the corresponding errors except for Hold Timer Expired error and BGP
    Finite State Machine error. In both of these cases Subcode 0 will be sent. If a
    user wants to use non zero Sub Code then custom choice can be used.
    """

    custom: CustomErrorParam
    """
    A BGP peer can send NOTIFICATION message with user defined Error Code and Error
    Subcode.
    """

    finite_state_machine_error: object
    """
    Any error detected by the BGP Finite State Machine (e.g., receipt of an
    unexpected event) is indicated by sending the NOTIFICATION message with the
    Error Code-Finite State Machine Error(Error Code 5). The Sub Code used is 0. If
    a user wants to use non zero Sub Code then CustomError can be used.
    """

    hold_timer_expired: object
    """
    If a system does not receive successive KEEPALIVE, UPDATE, and/or NOTIFICATION
    messages within the period specified in the Hold Time field of the OPEN message,
    then the NOTIFICATION message with the Hold Timer Expired Error Code(Error
    Code 4) is sent and the BGP connection is closed. The Sub Code used is 0. If a
    user wants to use non zero Sub Code then CustomError can be used.
    """

    message_header_error: MessageHeaderErrorParam
    """
    All errors detected while processing the Message Header are indicated by sending
    the NOTIFICATION message with the Error Code-Message Header Error. The Error
    Subcode elaborates on the specific nature of the error.
    """

    names: List[str]
    """The names of BGP Peers to send NOTIFICATION to.

    If no name is specified then NOTIFICATION will be sent to all configured BGP
    peers.

    x-constraint:

    - /components/schemas/Bgp.V4Peer/properties/name
    - /components/schemas/Bgp.V6Peer/properties/name
    """

    open_message_error: OpenMessageErrorParam
    """
    All errors detected while processing the OPEN message are indicated by sending
    the NOTIFICATION message with the Error Code-Open Message Error. The Error
    Subcode elaborates on the specific nature of the error.
    """

    update_message_error: UpdateMessageErrorParam
    """
    All errors detected while processing the UPDATE message are indicated by sending
    the NOTIFICATION message with the Error Code-Update Message Error. The Error
    Subcode elaborates on the specific nature of the error.
    """


class ProtocolBgp(TypedDict, total=False):
    choice: Required[Literal["notification", "initiate_graceful_restart"]]

    initiate_graceful_restart: ProtocolBgpInitiateGracefulRestart
    """Initiates BGP Graceful Restart process for the selected BGP peers.

    If no name is specified then Graceful Restart will be sent to all configured BGP
    peers. To emulate scenarios where a peer sends a Notification and stops the
    session, an optional Notification object is included. If the remote peer and the
    local peer are both configured to perform Graceful Restart for Notification
    triggered session , this will result in Graceful Restart scenario to be
    triggered as per RFC8538.
    """

    notification: ProtocolBgpNotification
    """
    A NOTIFICATION message is sent when an error is detected with the BGP session,
    such as hold timer expiring, misconfigured AS number or a BGP session reset is
    requested. This causes the BGP connection to close. Send explicit NOTIFICATIONs
    for list of specified BGP peers. If a user wants to send custom Error Code and
    Error Subcode the custom object should be configured. A user can send IANA
    defined BGP NOTIFICATIONs according to
    https://www.iana.org/assignments/bgp-parameters/bgp-parameters.xhtml.
    """


class ProtocolIpv4PingRequest(TypedDict, total=False):
    dst_ip: str
    """Destination IPv4 address to ping."""

    src_name: str
    """Name of source IPv4 interface to be used.

    x-constraint:

    - /components/schemas/Device.Ipv4/properties/name
    """


class ProtocolIpv4Ping(TypedDict, total=False):
    requests: Iterable[ProtocolIpv4PingRequest]
    """List of IPv4 ping requests."""


class ProtocolIpv4(TypedDict, total=False):
    choice: Required[Literal["ping"]]

    ping: ProtocolIpv4Ping
    """Request for initiating ping between multiple source and destination pairs."""


class ProtocolIpv6PingRequest(TypedDict, total=False):
    dst_ip: str
    """Destination IPv6 address to ping."""

    src_name: str
    """Name of source IPv6 interface to be used.

    x-constraint:

    - /components/schemas/Device.Ipv6/properties/name
    """


class ProtocolIpv6Ping(TypedDict, total=False):
    requests: Iterable[ProtocolIpv6PingRequest]
    """List of IPv6 ping requests."""


class ProtocolIpv6(TypedDict, total=False):
    choice: Required[Literal["ping"]]

    ping: ProtocolIpv6Ping
    """Request for initiating ping between multiple source and destination pairs."""


class Protocol(TypedDict, total=False):
    choice: Required[Literal["ipv4", "ipv6", "bgp"]]

    bgp: ProtocolBgp
    """Actions associated with BGP on configured resources."""

    ipv4: ProtocolIpv4
    """Actions associated with IPv4 on configured resources."""

    ipv6: ProtocolIpv6
    """Actions associated with IPv6 on configured resources."""
