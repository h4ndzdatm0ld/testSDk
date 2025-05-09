# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IsisInterfaceLevel"]


class IsisInterfaceLevel(BaseModel):
    dead_interval: Optional[int] = None
    """The Dead (Holding Time) interval for Level 1 Hello messages, in seconds."""

    hello_interval: Optional[int] = None
    """The Hello interval for Level 1 Hello messages, in seconds."""

    priority: Optional[int] = None
    """The Priority setting in Level 1 LAN Hellos for Designated Router election."""
