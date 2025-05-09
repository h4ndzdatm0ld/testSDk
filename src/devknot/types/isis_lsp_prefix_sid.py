# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["IsisLspPrefixSid", "Flags"]


class Flags(BaseModel):
    e_flag: Optional[bool] = None
    """Explicit-Null flag.

    When set, any upstream neighbor of the Prefix-SID originator MUST replace the
    Prefix-SID with a Prefix-SID having an Explicit-NULL value (0 for IPv4 and 2 for
    IPv6) before forwarding the packet.
    """

    l_flag: Optional[bool] = None
    """Local flag.

    When set, the value/index carried by the Prefix-SID has local significance.
    """

    n_flag: Optional[bool] = None
    """Node flag.

    When set, the Prefix-SID refers to the router identified by the prefix.
    Typically, the N-Flag is set on Prefix-SIDs attached to a router loopback
    address.
    """

    p_flag: Optional[bool] = None
    """Penultimate-Hop-Popping flag.

    When set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering
    the packet to the node that advertised the Prefix-SID.
    """

    r_flag: Optional[bool] = None
    """Readvertisment flag.

    When set, the prefix to which this Prefix-SID is attached, has been propagated
    by the router either from another level or from redistribution.
    """

    v_flag: Optional[bool] = None
    """Value flag. When set, the Prefix-SID carries avalue (instead of an index)."""


class IsisLspPrefixSid(BaseModel):
    algorithm: Optional[int] = None
    """
    The Isis may use various algorithms when calculating reachability to other nodes
    or to prefixes attached to these nodes.
    """

    flags: Optional[Flags] = None
    """Flags associated with Prefix Segment-ID."""

    sids: Optional[List[int]] = None
    """
    One or more SIDs/Indices are the SID/Label values associated with the IGP Prefix
    segment attached to the specific IPv4 or IPv6 prefix.
    """
