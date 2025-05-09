# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["Ospfv2V4RrExtdPrefixFlagsParam"]


class Ospfv2V4RrExtdPrefixFlagsParam(TypedDict, total=False):
    a_flag: bool
    """
    0x80 - (Attach Flag): An Area Border Router (ABR) generating an OSPFv2 Extended
    Prefix TLV for an inter-area prefix that is locally connected or attached in
    another connected area SHOULD set this flag.
    """

    n_flag: bool
    """
    N-Flag (Node Flag): Set when the prefix identifies the advertising router, i.e.,
    the prefix is a host prefix advertising a globally reachable address typically
    associated with a loopback address.
    """
