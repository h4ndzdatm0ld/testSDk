# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Dhcpv6ServerPoolInfoParam"]


class Dhcpv6ServerPoolInfoParam(TypedDict, total=False):
    prefix_len: int
    """
    The prefix_len ( in conjunction with the step) can be used to increment the IPv6
    lease addresses to be assigned to the requested clients when multiple addresses
    are configured by using the size field in the pool. The address is incremented
    using the prefix_len and step.
    """

    size: int
    """The total number of addresses in the pool."""

    start_address: str
    """The first IP address of the lease pool."""

    step: int
    """
    The increment value for the lease address within the lease pool where multiple
    addresses are present. The value of the advertised IPv6 prefixes are incremented
    according to the prefix_len and step.
    """
