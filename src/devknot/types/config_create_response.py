# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ConfigCreateResponse"]


class ConfigCreateResponse(BaseModel):
    warnings: Optional[List[str]] = None
    """
    A list of any system specific warnings that have occurred while executing the
    request.
    """
