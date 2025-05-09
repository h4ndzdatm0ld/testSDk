# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CaptureFieldParam"]


class CaptureFieldParam(TypedDict, total=False):
    mask: str

    negate: bool

    value: str
