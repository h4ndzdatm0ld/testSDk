# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Dhcpv6ServerOptionsIncludedMessages", "MsgType"]


class MsgType(BaseModel):
    choice: Optional[Literal["advertise", "reply", "re_configure"]] = None
    """The server message name where the option is included, by default it is all."""


class Dhcpv6ServerOptionsIncludedMessages(BaseModel):
    choice: Optional[Literal["all", "msg_types"]] = None
    """The server message name where the option is included, by default it is all."""

    msg_types: Optional[List[MsgType]] = None
    """User must specify the Dhcpv6 message type."""
