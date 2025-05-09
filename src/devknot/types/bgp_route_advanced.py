# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BgpRouteAdvanced"]


class BgpRouteAdvanced(BaseModel):
    include_local_preference: Optional[bool] = None
    """
    BGP Local Preference attribute sent to the peer to indicate the degree of
    preference for externally learned routes. If set to true, the Local Preference
    attribute will be included in the route advertisement. This should be included
    only for internal peers.
    """

    include_multi_exit_discriminator: Optional[bool] = None
    """
    BGP Multi Exit Discriminator attribute sent to the peer to help in the route
    selection process. If set to true, the Multi Exit Discriminator attribute will
    be included in the route advertisement.
    """

    include_origin: Optional[bool] = None
    """
    If set to true, the Origin attribute will be included in the route
    advertisement.
    """

    local_preference: Optional[int] = None
    """
    Value to be set in Local Preference attribute if include_local_preference is set
    to true. It is used for the selection of the path for the traffic leaving the
    AS. The route with the highest local preference value is preferred.
    """

    multi_exit_discriminator: Optional[int] = None
    """
    The multi exit discriminator (MED) value used for route selection sent to the
    peer.
    """

    origin: Optional[Literal["igp", "egp", "incomplete"]] = None
    """
    The origin attribute of a prefix can take three values: the prefix originates
    from an interior routing protocol 'igp', it originates from 'egp' or the origin
    is 'incomplete', if the prefix is learned through other means.
    """
