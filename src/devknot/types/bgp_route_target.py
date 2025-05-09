# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BgpRouteTarget"]


class BgpRouteTarget(BaseModel):
    rt_type: Optional[Literal["as_2octet", "ipv4_address", "as_4octet"]] = None
    """Extended Community Type field of 2 Byte.

    - as_2octet: Two-Octet AS Specific Extended Community (RFC 4360).
    - ipv4_address: IPv4 Address Specific Extended Community (RFC 4360).
    - as_4octet: 4-Octet AS Specific Extended Community (RFC 5668).
    """

    rt_value: Optional[str] = None
    """Colon separated Extended Community value of 6 Bytes - AS number: Assigned
    Number.

    Example - for the as_2octet or as_4octet "60005:100", for ipv4_address
    "1.1.1.1:100"
    """
