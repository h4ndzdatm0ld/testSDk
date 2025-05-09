# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpLearnedInformationFilter"]


class BgpLearnedInformationFilter(BaseModel):
    unicast_ipv4_prefix: Optional[bool] = None
    """
    If enabled, will store the information related to Unicast IPv4 Prefixes recieved
    from the peer.
    """

    unicast_ipv6_prefix: Optional[bool] = None
    """
    If enabled, will store the information related to Unicast IPv6 Prefixes recieved
    from the peer.
    """
