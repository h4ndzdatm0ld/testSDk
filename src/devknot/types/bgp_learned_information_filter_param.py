# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BgpLearnedInformationFilterParam"]


class BgpLearnedInformationFilterParam(TypedDict, total=False):
    unicast_ipv4_prefix: bool
    """
    If enabled, will store the information related to Unicast IPv4 Prefixes recieved
    from the peer.
    """

    unicast_ipv6_prefix: bool
    """
    If enabled, will store the information related to Unicast IPv6 Prefixes recieved
    from the peer.
    """
