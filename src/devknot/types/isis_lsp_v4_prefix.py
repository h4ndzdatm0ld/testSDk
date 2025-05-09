# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["IsisLspV4Prefix"]


class IsisLspV4Prefix(BaseModel):
    default_metric: Optional[int] = None
    """ISIS default metric value."""

    ipv4_address: Optional[str] = None
    """An IPv4 unicast prefix reachable via the originator of this LSP."""

    origin_type: Optional[Literal["internal", "external"]] = None
    """The origin of the advertised route-internal or external to the ISIS area.

    Options include the following: Internal-for intra-area routes, through Level 1
    LSPs. External-for inter-area routes redistributed within L1, through Level 1
    LSPs.
    """

    prefix_length: Optional[int] = None
    """The length of the IPv4 prefix."""

    redistribution_type: Optional[Literal["up", "down"]] = None
    """
    Up (0)-used when a prefix is initially advertised within the ISIS L3 hierarchy,
    and for all other prefixes in L1 and L2 LSPs. (default) Down (1)-used when an
    L1/L2 router advertises L2 prefixes in L1 LSPs. The prefixes are being
    advertised from a higher level (L2) down to a lower level (L1).
    """
