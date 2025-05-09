# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Dhcpv6ServerIapdPoolInfo"]


class Dhcpv6ServerIapdPoolInfo(BaseModel):
    advertised_prefix_len: Optional[int] = None
    """
    The prefix length of the IPv6 prefix that the Dhcpv6 server offers to the Dhcpv6
    client.
    """

    configured_prefix_len: Optional[int] = None
    """
    The configured_prefix_len ( in conjunction with the prefix_step) can be used to
    increment the IPv6 lease addresses to be assigned to the requested clients when
    multiple addresses are configured by using the size field in the pool. e.g. This
    can be used to assign multiple IPv6 host addresses within the same IPv6 subnet (
    defined by advertised_prefix_len ) to multiple requesting clients.
    """

    prefix_size: Optional[int] = None
    """The total number of addresses in the pool."""

    prefix_step: Optional[int] = None
    """
    The increment value for the lease address within the lease pool where multiple
    addresses are present. The value of the advertised IPv6 prefixes are incremented
    according to the configured_prefix_len and prefix_step.
    """

    start_prefix_address: Optional[str] = None
    """The first IP address of the prefix pool."""
