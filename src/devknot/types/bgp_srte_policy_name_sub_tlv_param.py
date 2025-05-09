# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpSrtePolicyNameSubTlvParam"]


class BgpSrtePolicyNameSubTlvParam(TypedDict, total=False):
    policy_name: str
    """
    Symbolic name for the policy that should be a string of printable ASCII
    characters, without a NULL terminator.
    """
