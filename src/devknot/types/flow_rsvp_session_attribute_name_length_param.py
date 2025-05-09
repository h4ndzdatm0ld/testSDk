# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FlowRsvpSessionAttributeNameLengthParam"]


class FlowRsvpSessionAttributeNameLengthParam(TypedDict, total=False):
    auto: int
    """The OTG implementation will provide a system generated value for this property.

    If the OTG implementation is unable to generate a value the default value must
    be used.
    """

    choice: Literal["auto", "value"]
    """auto or configured value."""

    value: int
