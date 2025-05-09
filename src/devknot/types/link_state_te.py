# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["LinkStateTe", "PriorityBandwidths"]


class PriorityBandwidths(BaseModel):
    pb0: Optional[int] = None
    """Specifies the amount of bandwidth that can be reserved for the Priority 0."""

    pb1: Optional[int] = None
    """Specifies the amount of bandwidth that can be reserved for the Priority 1."""

    pb2: Optional[int] = None
    """Specify the amount of bandwidth that can be reserved for the Priority 2."""

    pb3: Optional[int] = None
    """Specifies the amount of bandwidth that can be reserved for the Priority 3."""

    pb4: Optional[int] = None
    """Specifies the amount of bandwidth that can be reserved for the Priority 4."""

    pb5: Optional[int] = None
    """Specifies the amount of bandwidth that can be reserved for the Priority 5."""

    pb6: Optional[int] = None
    """Specifies the amount of bandwidth that can be reserved for the Priority 6."""

    pb7: Optional[int] = None
    """Specifies the amount of bandwidth that can be reserved for the Priority 7."""


class LinkStateTe(BaseModel):
    administrative_group: Optional[str] = None
    """The Administrative group sub-TLV (sub-TLV 3).

    It is a 4-octet user-defined bit mask used to assign administrative group
    numbers to the interface, for use in assigning colors and resource classes. Each
    set bit corresponds to a single administrative group for this interface. The
    settings translate into Group numbers, which range from 0 to 31 (integers).
    """

    max_bandwith: Optional[int] = None
    """
    The maximum link bandwidth (sub-TLV 9) in bytes/sec allowed for this link for a
    direction.
    """

    max_reservable_bandwidth: Optional[int] = None
    """
    The maximum link bandwidth (sub-TLV 10) in bytes/sec allowed for this link in a
    direction.
    """

    metric_level: Optional[int] = None
    """The user-assigned link metric for Traffic Engineering."""

    priority_bandwidths: Optional[PriorityBandwidths] = None
    """Configuration of bandwidths of priority 0 through priority 7."""
