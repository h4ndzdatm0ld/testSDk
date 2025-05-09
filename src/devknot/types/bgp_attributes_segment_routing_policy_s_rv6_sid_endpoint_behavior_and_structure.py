# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpAttributesSegmentRoutingPolicySRv6SidEndpointBehaviorAndStructure"]


class BgpAttributesSegmentRoutingPolicySRv6SidEndpointBehaviorAndStructure(BaseModel):
    arg_length: Optional[int] = None
    """SRv6 SID Arguments length in bits."""

    endpoint_behaviour: Optional[str] = None
    """
    This is a 2-octet field that is used to specify the SRv6 Endpoint Behavior code
    point for the SRv6 SID as defined in section 9.2 of [RFC8986]. When set with the
    value 0xFFFF (i.e., Opaque), the choice of SRv6 Endpoint Behavior is left to the
    headend. Well known 16-bit values for this field are available at
    https://www.iana.org/assignments/segment-routing/segment-routing.xhtml .
    """

    func_length: Optional[int] = None
    """SRv6 SID Function length in bits."""

    lb_length: Optional[int] = None
    """SRv6 SID Locator Block length in bits."""

    ln_length: Optional[int] = None
    """SRv6 SID Locator Node length in bits."""
