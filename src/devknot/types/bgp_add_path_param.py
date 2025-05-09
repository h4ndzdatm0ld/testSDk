# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpAddPathParam"]


class BgpAddPathParam(TypedDict, total=False):
    path_id: int
    """The id of the additional path."""
