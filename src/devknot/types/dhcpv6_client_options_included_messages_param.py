# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["Dhcpv6ClientOptionsIncludedMessagesParam", "MsgType"]


class MsgType(TypedDict, total=False):
    choice: Literal["solicit", "request", "inform_request", "release", "renew", "rebind"]
    """The client message name where the option is included, by default it is all."""


class Dhcpv6ClientOptionsIncludedMessagesParam(TypedDict, total=False):
    choice: Literal["all", "msg_types"]
    """The client message name where the option is included, by default it is all."""

    msg_types: Iterable[MsgType]
    """User must specify the Dhcpv6 message type."""
