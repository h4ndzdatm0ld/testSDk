# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BgpSrteBindingSubTlv"]


class BgpSrteBindingSubTlv(BaseModel):
    binding_sid_type: Optional[Literal["no_binding", "four_octet_sid", "ipv6_sid"]] = None
    """Type of the binding SID.

    Supported types are "No Binding SID" or "Four Octets Sid" or "IPv6 SID".
    """

    four_octet_sid: Optional[int] = None
    """Binding SID is encoded in 4 octets."""

    i_flag: Optional[bool] = None
    """I-Flag encodes the "Drop Upon Invalid" behavior."""

    ipv6_sid: Optional[str] = None
    """IPv6 SID value."""

    s_flag: Optional[bool] = None
    """S-Flag encodes the "Specified-BSID-only" behavior."""
