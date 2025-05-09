# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpAdvanced"]


class BgpAdvanced(BaseModel):
    hold_time_interval: Optional[int] = None
    """Number of seconds the sender proposes for the value of the Hold Timer."""

    keep_alive_interval: Optional[int] = None
    """Number of seconds between transmissions of Keepalive messages by this peer."""

    listen_port: Optional[int] = None
    """The TCP port number on which to accept BGP connections from the remote peer."""

    md5_key: Optional[str] = None
    """The value to be used as a secret MD5 key for authentication.

    If not configured, MD5 authentication will not be enabled.
    """

    neighbor_port: Optional[int] = None
    """
    Destination TCP port number of the BGP peer when initiating a session from the
    local BGP peer.
    """

    passive_mode: Optional[bool] = None
    """
    If set to true, the local BGP peer will wait for the remote peer to initiate the
    BGP session by establishing the TCP connection, rather than initiating sessions
    from the local peer.
    """

    time_to_live: Optional[int] = None
    """
    The limited number of iterations that a unit of data can experience before the
    data is discarded. This is placed in the TTL field in the IP header of the
    transmitted packets.
    """

    update_interval: Optional[int] = None
    """
    The time interval at which Update messages are sent to the DUT, expressed as the
    number of milliseconds between Update messages. The update interval 0 implies to
    send all the updates as fast as possible.
    """
