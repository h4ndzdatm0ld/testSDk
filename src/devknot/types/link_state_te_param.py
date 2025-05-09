# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LinkStateTeParam", "PriorityBandwidths"]


class PriorityBandwidths(TypedDict, total=False):
    pb0: int
    """Specifies the amount of bandwidth that can be reserved for the Priority 0."""

    pb1: int
    """Specifies the amount of bandwidth that can be reserved for the Priority 1."""

    pb2: int
    """Specify the amount of bandwidth that can be reserved for the Priority 2."""

    pb3: int
    """Specifies the amount of bandwidth that can be reserved for the Priority 3."""

    pb4: int
    """Specifies the amount of bandwidth that can be reserved for the Priority 4."""

    pb5: int
    """Specifies the amount of bandwidth that can be reserved for the Priority 5."""

    pb6: int
    """Specifies the amount of bandwidth that can be reserved for the Priority 6."""

    pb7: int
    """Specifies the amount of bandwidth that can be reserved for the Priority 7."""


class LinkStateTeParam(TypedDict, total=False):
    administrative_group: str
    """The Administrative group sub-TLV (sub-TLV 3).

    It is a 4-octet user-defined bit mask used to assign administrative group
    numbers to the interface, for use in assigning colors and resource classes. Each
    set bit corresponds to a single administrative group for this interface. The
    settings translate into Group numbers, which range from 0 to 31 (integers).
    """

    max_bandwith: int
    """
    The maximum link bandwidth (sub-TLV 9) in bytes/sec allowed for this link for a
    direction.
    """

    max_reservable_bandwidth: int
    """
    The maximum link bandwidth (sub-TLV 10) in bytes/sec allowed for this link in a
    direction.
    """

    metric_level: int
    """The user-assigned link metric for Traffic Engineering."""

    priority_bandwidths: PriorityBandwidths
    """Configuration of bandwidths of priority 0 through priority 7."""
