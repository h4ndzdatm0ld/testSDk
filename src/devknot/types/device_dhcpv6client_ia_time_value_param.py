# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DeviceDhcpv6clientIaTimeValueParam"]


class DeviceDhcpv6clientIaTimeValueParam(TypedDict, total=False):
    t1: int
    """
    The suggested time at which the client contacts the server from which the
    addresses were obtained to extend the lifetimes of the addresses assigned. T1 is
    a time duration relative to the current time expressed in units of seconds. If
    set to 0 server will ignore it. If the maximum value is specified it means
    infinite time.
    """

    t2: int
    """
    The suggested time at which the client contacts any available server to extend
    the lifetimes of the addresses assigned. T2 is a time duration relative to the
    current time expressed in units of seconds. If set to 0 server will ignore it.
    If the maximum value is specified it means infinite time
    """
