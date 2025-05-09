# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Dhcpv6ServerIapdPoolInfoParam"]


class Dhcpv6ServerIapdPoolInfoParam(TypedDict, total=False):
    advertised_prefix_len: int
    """
    The prefix length of the IPv6 prefix that the Dhcpv6 server offers to the Dhcpv6
    client.
    """

    configured_prefix_len: int
    """
    The configured_prefix_len ( in conjunction with the prefix_step) can be used to
    increment the IPv6 lease addresses to be assigned to the requested clients when
    multiple addresses are configured by using the size field in the pool. e.g. This
    can be used to assign multiple IPv6 host addresses within the same IPv6 subnet (
    defined by advertised_prefix_len ) to multiple requesting clients.
    """

    prefix_size: int
    """The total number of addresses in the pool."""

    prefix_step: int
    """
    The increment value for the lease address within the lease pool where multiple
    addresses are present. The value of the advertised IPv6 prefixes are incremented
    according to the configured_prefix_len and prefix_step.
    """

    start_prefix_address: str
    """The first IP address of the prefix pool."""
