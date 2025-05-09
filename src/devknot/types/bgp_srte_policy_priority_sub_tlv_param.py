# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpSrtePolicyPrioritySubTlvParam"]


class BgpSrtePolicyPrioritySubTlvParam(TypedDict, total=False):
    policy_priority: int
    """One-octet Priority value."""
