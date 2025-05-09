# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .bgp_nlri_prefix_path_id_param import BgpNlriPrefixPathIDParam

__all__ = ["BgpOneTraditionalNlriPrefixParam"]


class BgpOneTraditionalNlriPrefixParam(TypedDict, total=False):
    address: str
    """The IPv4 address of the network."""

    path_id: BgpNlriPrefixPathIDParam
    """Optional field in the NLRI carrying Path Id of the prefix."""

    prefix: int
    """The IPv4 network prefix length to be applied to the address."""
