# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Rocev2ImmediateData"]


class Rocev2ImmediateData(BaseModel):
    immediate_data: Optional[str] = None
    """Four bytes of immediate Data for SEND/WRITE with immediate."""
