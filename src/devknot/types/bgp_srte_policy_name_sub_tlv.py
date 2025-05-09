# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpSrtePolicyNameSubTlv"]


class BgpSrtePolicyNameSubTlv(BaseModel):
    policy_name: Optional[str] = None
    """
    Symbolic name for the policy that should be a string of printable ASCII
    characters, without a NULL terminator.
    """
