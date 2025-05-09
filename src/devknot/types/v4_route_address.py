# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["V4RouteAddress"]


class V4RouteAddress(BaseModel):
    address: str
    """The starting address of the network."""

    count: Optional[int] = None
    """The total number of addresses in the range."""

    prefix: Optional[int] = None
    """The IPv4 network prefix length to be applied to the address."""

    step: Optional[int] = None
    """
    Increments the network address prefixes within a route range where multiple
    routes are present. The value is incremented according to the Prefix Length and
    Step.
    """
