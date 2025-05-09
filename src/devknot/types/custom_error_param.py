# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomErrorParam"]


class CustomErrorParam(TypedDict, total=False):
    code: int
    """The Error code to be sent in the NOTIFICATION message to peer."""

    subcode: int
    """The Error Subcode to be sent in the NOTIFICATION message to peer."""
