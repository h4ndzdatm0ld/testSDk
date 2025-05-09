# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IsisAuthenticationBaseParam"]


class IsisAuthenticationBaseParam(TypedDict, total=False):
    auth_type: Required[Literal["md5", "password"]]
    """The authentication method."""

    md5: str
    """Authentication as an MD5 key."""

    password: str
    """Authentication as a clear text password."""
