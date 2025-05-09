# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .bgp_nlri_prefix_path_id_param import BgpNlriPrefixPathIDParam

__all__ = ["BgpOneIpv6NlriPrefixParam"]


class BgpOneIpv6NlriPrefixParam(TypedDict, total=False):
    address: str
    """The IPv6 address of the network."""

    path_id: BgpNlriPrefixPathIDParam
    """Optional field in the NLRI carrying Path Id of the prefix."""

    prefix: int
    """The IPv6 network prefix length to be applied to the address."""
