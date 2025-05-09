# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IsisAuthenticationBase"]


class IsisAuthenticationBase(BaseModel):
    auth_type: Literal["md5", "password"]
    """The authentication method."""

    md5: Optional[str] = None
    """Authentication as an MD5 key."""

    password: Optional[str] = None
    """Authentication as a clear text password."""
