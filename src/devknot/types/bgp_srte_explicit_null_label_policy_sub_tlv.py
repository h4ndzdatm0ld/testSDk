# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BgpSrteExplicitNullLabelPolicySubTlv"]


class BgpSrteExplicitNullLabelPolicySubTlv(BaseModel):
    explicit_null_label_policy: Optional[
        Literal["reserved_enlp", "push_ipv4_enlp", "push_ipv6_enlp", "push_ipv4_ipv6_enlp", "do_not_push_enlp"]
    ] = None
    """The value of the explicit null label policy"""
