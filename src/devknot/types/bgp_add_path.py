# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpAddPath"]


class BgpAddPath(BaseModel):
    path_id: Optional[int] = None
    """The id of the additional path."""
