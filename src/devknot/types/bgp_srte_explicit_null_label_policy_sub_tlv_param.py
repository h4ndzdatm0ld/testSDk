# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BgpSrteExplicitNullLabelPolicySubTlvParam"]


class BgpSrteExplicitNullLabelPolicySubTlvParam(TypedDict, total=False):
    explicit_null_label_policy: Literal[
        "reserved_enlp", "push_ipv4_enlp", "push_ipv6_enlp", "push_ipv4_ipv6_enlp", "do_not_push_enlp"
    ]
    """The value of the explicit null label policy"""
