# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpIpv4SrPolicyNlriPrefix"]


class BgpIpv4SrPolicyNlriPrefix(BaseModel):
    color: Optional[int] = None
    """4-octet value identifying (with the endpoint) the policy.

    The color is used to match the color of the destination prefixes to steer
    traffic into the SR Policy as specified in section 8 of RFC9256.
    """

    distinguisher: Optional[int] = None
    """
    The 4-octet value uniquely identifying the policy in the context of <color,
    endpoint> tuple. The distinguisher has no semantic value and is solely used by
    the SR Policy originator to make unique (from an NLRI perspective) both for
    multiple candidate paths of the same SR Policy as well as candidate paths of
    different SR Policies (i.e. with different segment lists) with the same Color
    and Endpoint but meant for different headends.
    """

    endpoint: Optional[str] = None
    """Identifies the endpoint of a policy.

    The Endpoint is an IPv4 address and can be either a unicast or an unspecified
    address (0.0.0.0) as specified in section 2.1 of RFC9256.
    """
