# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IsisInterfaceLevelParam"]


class IsisInterfaceLevelParam(TypedDict, total=False):
    dead_interval: int
    """The Dead (Holding Time) interval for Level 1 Hello messages, in seconds."""

    hello_interval: int
    """The Hello interval for Level 1 Hello messages, in seconds."""

    priority: int
    """The Priority setting in Level 1 LAN Hellos for Designated Router election."""
