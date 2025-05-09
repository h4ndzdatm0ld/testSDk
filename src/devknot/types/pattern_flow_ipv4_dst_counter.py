# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PatternFlowIpv4DstCounter"]


class PatternFlowIpv4DstCounter(BaseModel):
    count: Optional[int] = None

    start: Optional[str] = None

    step: Optional[str] = None
