# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpAttributesSegmentRoutingPolicyTypeFlags"]


class BgpAttributesSegmentRoutingPolicyTypeFlags(BaseModel):
    a_flag: Optional[bool] = None
    """
    Indicates presence of SR Algorithm field applicable to Segment Types 3, 4,
    and 9.
    """

    b_flag: Optional[bool] = None
    """
    Indicates presence of SRv6 Endpoint Behavior and SID Structure encoding
    specified in Section 2.4.4.2.4 of draft-ietf-idr-sr-policy-safi-02.
    """

    s_flag: Optional[bool] = None
    """
    This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID depending
    on the segment type.
    """

    v_flag: Optional[bool] = None
    """Indicates verification of segment data in is enabled."""
