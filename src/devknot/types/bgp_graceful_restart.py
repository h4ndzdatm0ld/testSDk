# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpGracefulRestart"]


class BgpGracefulRestart(BaseModel):
    enable_gr: Optional[bool] = None
    """If enabled, Graceful Restart capability is advertised in BGP OPEN messages."""

    enable_llgr: Optional[bool] = None
    """
    If enabled, the "Long-lived Graceful Restart Capability", or "LLGR Capability"
    will be advertised. This capability MUST be advertised in conjunction with the
    Graceful Restart capability.
    """

    enable_notification: Optional[bool] = None
    """
    If enabled, the N flag will be set in the Graceful Restart capability in the
    Open message. If both peers in a BGP connection has this enabled, Graceful
    Restart procedures are performed even if the peer goes down due to sending of a
    Notification Message as per RFC8538.
    """

    restart_time: Optional[int] = None
    """
    This is the estimated duration (in seconds) it will take for the BGP session to
    be re-established after a restart. This can be used to speed up routing
    convergence by its peer in case the BGP speaker does not come back after a
    restart.
    """

    stale_time: Optional[int] = None
    """
    Duration (in seconds) specifying how long stale information (for the AFI/SAFI)
    may be retained. This is a three byte field and is applicable only if
    'enable_llgr' is set to 'true'.
    """
