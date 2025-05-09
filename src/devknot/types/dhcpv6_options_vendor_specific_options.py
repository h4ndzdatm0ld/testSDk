# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Dhcpv6OptionsVendorSpecificOptions"]


class Dhcpv6OptionsVendorSpecificOptions(BaseModel):
    code: int
    """The code for the encapsulated option."""

    data: str
    """The data for the encapsulated option."""
