# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["Dhcpv6ClientOptionsLinkLayerAddressParam"]


class Dhcpv6ClientOptionsLinkLayerAddressParam(TypedDict, total=False):
    value: Required[str]
    """The MAC address that becomes part of DUID llt or DUID ll."""
