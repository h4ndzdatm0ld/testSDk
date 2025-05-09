# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IsisLspPrefixAttributes"]


class IsisLspPrefixAttributes(BaseModel):
    n_flag: Optional[bool] = None
    """
    Node Flag (Bit 2). Set when the prefix identifies the advertising router, i.e.,
    the prefix is a host prefix advertising a globally reachable address typically
    associated with a loopback address.
    """

    r_flag: Optional[bool] = None
    """Readvertisement flag (Bit 1).

    Set when the prefix has been leaked from one level to another (upwards or
    downwards).
    """

    x_flag: Optional[bool] = None
    """External prefix flag (Bit 0).

    Set if the prefix has been redistributed from another protocol. This includes
    the case where multiple virtual routers are supported and the source of the
    redistributed prefix is another IS-IS instance.
    """
