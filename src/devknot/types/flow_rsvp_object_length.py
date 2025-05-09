# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FlowRsvpObjectLength"]


class FlowRsvpObjectLength(BaseModel):
    auto: Optional[int] = None
    """The OTG implementation will provide a system generated value for this property.

    If the OTG implementation is unable to generate a value the default value must
    be used.
    """

    choice: Optional[Literal["auto", "value"]] = None
    """auto or configured value."""

    value: Optional[int] = None
