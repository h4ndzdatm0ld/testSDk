# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V6RouteAddressParam"]


class V6RouteAddressParam(TypedDict, total=False):
    address: Required[str]
    """The starting address of the network."""

    count: int
    """The total number of addresses in the range."""

    prefix: int
    """The IPv6 network prefix length to be applied to the address."""

    step: int
    """
    Increments the network address prefixes within a route range where multiple
    routes are present. The value is incremented according to the Prefix Length and
    Step.
    """
