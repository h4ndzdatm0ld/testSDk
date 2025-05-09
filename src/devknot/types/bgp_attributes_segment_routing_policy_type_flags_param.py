# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpAttributesSegmentRoutingPolicyTypeFlagsParam"]


class BgpAttributesSegmentRoutingPolicyTypeFlagsParam(TypedDict, total=False):
    a_flag: bool
    """
    Indicates presence of SR Algorithm field applicable to Segment Types 3, 4,
    and 9.
    """

    b_flag: bool
    """
    Indicates presence of SRv6 Endpoint Behavior and SID Structure encoding
    specified in Section 2.4.4.2.4 of draft-ietf-idr-sr-policy-safi-02.
    """

    s_flag: bool
    """
    This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID depending
    on the segment type.
    """

    v_flag: bool
    """Indicates verification of segment data in is enabled."""
