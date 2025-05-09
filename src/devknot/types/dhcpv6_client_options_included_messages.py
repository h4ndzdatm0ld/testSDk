# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Dhcpv6ClientOptionsIncludedMessages", "MsgType"]


class MsgType(BaseModel):
    choice: Optional[Literal["solicit", "request", "inform_request", "release", "renew", "rebind"]] = None
    """The client message name where the option is included, by default it is all."""


class Dhcpv6ClientOptionsIncludedMessages(BaseModel):
    choice: Optional[Literal["all", "msg_types"]] = None
    """The client message name where the option is included, by default it is all."""

    msg_types: Optional[List[MsgType]] = None
    """User must specify the Dhcpv6 message type."""
