# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IsisSrPrefixSid"]


class IsisSrPrefixSid(BaseModel):
    algorithm: Optional[int] = None
    """
    The Isis may use various algorithms when calculating reachability to other nodes
    or to prefixes attached to these nodes. Refernce:
    https://datatracker.ietf.org/doc/html/rfc8667#SRALGOSUBTLV
    """

    choice: Optional[Literal["sid_values", "sid_indices"]] = None
    """
    Choice of whether Prefix-SID carries and absolute value or a relative index to
    the SRGB/SRLB Ranges. Please refer to
    device.isis.segment_routing.router_capability.sr_capability.srgb_ranges for the
    Segment Routing Global Block (SRGB) Descriptor and
    device.isis.segment_routing.router_capability.srlb_ranges for the SR Local Block
    (SRLB). A user needs to configure at least one entry of SID value or SID index.
    If no entry is configured, then an implementation may advertise appropriate
    default SID Value/Index based on the choice. e.g. the first value from the SRGB
    or SRLB range.

    - sid_values: Prefix-SID carries one or more values and then v_flag is set by
      the implementation.
    - sid_indices: Prefix-SID carries one or more indices and then v_flag is unset
      by the implementation.
    """

    e_flag: Optional[bool] = None
    """
    E-Flag: Explicit-Null Flag. If set, any upstream neighbor of the Prefix-SID
    originator MUST replace the Prefix-SID with a Prefix-SID that has an Explicit
    NULL value (0 for IPv4 and 2 for IPv6) before forwarding the packet.
    """

    l_flag: Optional[bool] = None
    """The local flag.

    If set, then the value/index carried by the Prefix-SID has local significance
    and the Prefix SID is from Please refer to
    device.isis.segment_routing.router_capability.srlb_ranges.
    """

    n_flag: Optional[bool] = None
    """N-Flag: Node-SID flag.

    If set, then the Prefix-SID refers to the router identified by the prefix.
    Typically, the N-Flag is set on Prefix-SIDs that are attached to a router
    loopback address. The N-Flag is set when the Prefix-SID is a Node-SID as
    described in [RFC8402].
    """

    p_flag: Optional[bool] = None
    """
    P-Flag: No-PHP (No Penultimate Hop-Popping) Flag. If set, then the penultimate
    hop MUST NOT pop the Prefix-SID before delivering the packet to the node that
    advertised the Prefix-SID.
    """

    r_flag: Optional[bool] = None
    """R-Flag: Re-advertisement Flag.

    If set, then the prefix to which this Prefix-SID is attached has been propagated
    by the router from either another level (i.e., from Level-1 to Level-2 or the
    opposite) or redistribution (e.g., from another protocol).
    """

    sid_indices: Optional[List[int]] = None
    """
    One or more SID/Label Indices that are associated with the IGP Prefix segment
    attached to the specific IPv4 or IPv6 prefix.
    """

    sid_values: Optional[List[int]] = None
    """
    SID/Label as one or more absolute values that are associated with the IGP Prefix
    segment attached to the specific IPv4 or IPv6 prefix.
    """
