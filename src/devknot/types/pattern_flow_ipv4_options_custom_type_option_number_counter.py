# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PatternFlowIpv4OptionsCustomTypeOptionNumberCounter"]


class PatternFlowIpv4OptionsCustomTypeOptionNumberCounter(BaseModel):
    count: Optional[int] = None

    start: Optional[int] = None

    step: Optional[int] = None
