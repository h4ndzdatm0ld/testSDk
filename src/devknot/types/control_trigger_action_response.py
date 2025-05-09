# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ControlTriggerActionResponse",
    "Response",
    "ResponseProtocol",
    "ResponseProtocolIpv4",
    "ResponseProtocolIpv4Ping",
    "ResponseProtocolIpv4PingResponse",
    "ResponseProtocolIpv6",
    "ResponseProtocolIpv6Ping",
    "ResponseProtocolIpv6PingResponse",
]


class ResponseProtocolIpv4PingResponse(BaseModel):
    dst_ip: str
    """Destination IPv4 address used for ping."""

    result: Literal["succeeded", "failed"]
    """Result of the ping request."""

    src_name: str
    """Name of source IPv4 interface used for ping.

    x-constraint:

    - /components/schemas/Device.Ipv4/properties/name
    """


class ResponseProtocolIpv4Ping(BaseModel):
    responses: Optional[List[ResponseProtocolIpv4PingResponse]] = None
    """List of responses for IPv4 ping responses."""


class ResponseProtocolIpv4(BaseModel):
    choice: Literal["ping"]

    ping: Optional[ResponseProtocolIpv4Ping] = None
    """Response for ping initiated between multiple source and destination pairs."""


class ResponseProtocolIpv6PingResponse(BaseModel):
    dst_ip: str
    """Destination IPv6 address used for ping."""

    result: Literal["succeeded", "failed"]
    """Result of the ping request."""

    src_name: str
    """Name of source IPv6 interface used for ping.

    x-constraint:

    - /components/schemas/Device.Ipv6/properties/name
    """


class ResponseProtocolIpv6Ping(BaseModel):
    responses: Optional[List[ResponseProtocolIpv6PingResponse]] = None
    """List of responses for IPv6 ping responses."""


class ResponseProtocolIpv6(BaseModel):
    choice: Literal["ping"]

    ping: Optional[ResponseProtocolIpv6Ping] = None
    """Response for ping initiated between multiple source and destination pairs."""


class ResponseProtocol(BaseModel):
    choice: Literal["ipv4", "ipv6"]

    ipv4: Optional[ResponseProtocolIpv4] = None
    """Response for actions associated with IPv4 on configured resources."""

    ipv6: Optional[ResponseProtocolIpv6] = None
    """Response for actions associated with IPv6 on configured resources."""


class Response(BaseModel):
    choice: Literal["protocol"]

    protocol: Optional[ResponseProtocol] = None
    """Response for actions associated with protocols on configured resources."""


class ControlTriggerActionResponse(BaseModel):
    response: Optional[Response] = None
    """Response for action triggered against configured resources."""

    warnings: Optional[List[str]] = None
    """List of warnings generated while triggering specified action"""
