# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Ospfv2LsaHeader"]


class Ospfv2LsaHeader(BaseModel):
    advertising_router_id: Optional[str] = None
    """The router ID (in the IPv4 format) of the router that originated the LSA."""

    age: Optional[int] = None
    """The time since the LSA's generation in seconds."""

    lsa_id: Optional[str] = None
    """LSA ID in the IPv4 format. The Link State ID for the specified LSA type."""

    option_bits: Optional[int] = None
    """The optional bits."""

    sequence_number: Optional[int] = None
    """Sequence number to detect old and duplicate LSAs.

    The greater the sequence number the more recent the LSA.
    """
