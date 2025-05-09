# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpSrteColorSubTlv"]


class BgpSrteColorSubTlv(BaseModel):
    color: Optional[str] = None
    """Six octet values. Example: 000000000064 for color value 100."""
