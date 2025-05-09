# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Ospfv2V4RrExtdPrefixFlags"]


class Ospfv2V4RrExtdPrefixFlags(BaseModel):
    a_flag: Optional[bool] = None
    """
    0x80 - (Attach Flag): An Area Border Router (ABR) generating an OSPFv2 Extended
    Prefix TLV for an inter-area prefix that is locally connected or attached in
    another connected area SHOULD set this flag.
    """

    n_flag: Optional[bool] = None
    """
    N-Flag (Node Flag): Set when the prefix identifies the advertising router, i.e.,
    the prefix is a host prefix advertising a globally reachable address typically
    associated with a loopback address.
    """
