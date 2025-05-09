# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Dhcpv6ClientOptionsLinkLayerAddress"]


class Dhcpv6ClientOptionsLinkLayerAddress(BaseModel):
    value: str
    """The MAC address that becomes part of DUID llt or DUID ll."""
