# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Dhcpv6ServerPoolInfo"]


class Dhcpv6ServerPoolInfo(BaseModel):
    prefix_len: Optional[int] = None
    """
    The prefix_len ( in conjunction with the step) can be used to increment the IPv6
    lease addresses to be assigned to the requested clients when multiple addresses
    are configured by using the size field in the pool. The address is incremented
    using the prefix_len and step.
    """

    size: Optional[int] = None
    """The total number of addresses in the pool."""

    start_address: Optional[str] = None
    """The first IP address of the lease pool."""

    step: Optional[int] = None
    """
    The increment value for the lease address within the lease pool where multiple
    addresses are present. The value of the advertised IPv6 prefixes are incremented
    according to the prefix_len and step.
    """
