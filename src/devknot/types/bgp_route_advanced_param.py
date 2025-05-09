# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BgpRouteAdvancedParam"]


class BgpRouteAdvancedParam(TypedDict, total=False):
    include_local_preference: bool
    """
    BGP Local Preference attribute sent to the peer to indicate the degree of
    preference for externally learned routes. If set to true, the Local Preference
    attribute will be included in the route advertisement. This should be included
    only for internal peers.
    """

    include_multi_exit_discriminator: bool
    """
    BGP Multi Exit Discriminator attribute sent to the peer to help in the route
    selection process. If set to true, the Multi Exit Discriminator attribute will
    be included in the route advertisement.
    """

    include_origin: bool
    """
    If set to true, the Origin attribute will be included in the route
    advertisement.
    """

    local_preference: int
    """
    Value to be set in Local Preference attribute if include_local_preference is set
    to true. It is used for the selection of the path for the traffic leaving the
    AS. The route with the highest local preference value is preferred.
    """

    multi_exit_discriminator: int
    """
    The multi exit discriminator (MED) value used for route selection sent to the
    peer.
    """

    origin: Literal["igp", "egp", "incomplete"]
    """
    The origin attribute of a prefix can take three values: the prefix originates
    from an interior routing protocol 'igp', it originates from 'egp' or the origin
    is 'incomplete', if the prefix is learned through other means.
    """
