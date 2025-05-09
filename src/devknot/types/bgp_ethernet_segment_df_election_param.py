# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpEthernetSegmentDfElectionParam"]


class BgpEthernetSegmentDfElectionParam(TypedDict, total=False):
    election_timer: int
    """The DF election timer in seconds."""
