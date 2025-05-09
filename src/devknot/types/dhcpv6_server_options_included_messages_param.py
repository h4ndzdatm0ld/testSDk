# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["Dhcpv6ServerOptionsIncludedMessagesParam", "MsgType"]


class MsgType(TypedDict, total=False):
    choice: Literal["advertise", "reply", "re_configure"]
    """The server message name where the option is included, by default it is all."""


class Dhcpv6ServerOptionsIncludedMessagesParam(TypedDict, total=False):
    choice: Literal["all", "msg_types"]
    """The server message name where the option is included, by default it is all."""

    msg_types: Iterable[MsgType]
    """User must specify the Dhcpv6 message type."""
