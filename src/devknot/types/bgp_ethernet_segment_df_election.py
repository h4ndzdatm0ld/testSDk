# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpEthernetSegmentDfElection"]


class BgpEthernetSegmentDfElection(BaseModel):
    election_timer: Optional[int] = None
    """The DF election timer in seconds."""
