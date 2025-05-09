# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["Dhcpv6OptionsVendorSpecificOptionsParam"]


class Dhcpv6OptionsVendorSpecificOptionsParam(TypedDict, total=False):
    code: Required[int]
    """The code for the encapsulated option."""

    data: Required[str]
    """The data for the encapsulated option."""
