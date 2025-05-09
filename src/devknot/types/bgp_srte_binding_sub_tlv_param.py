# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["BgpSrteBindingSubTlvParam"]


class BgpSrteBindingSubTlvParam(TypedDict, total=False):
    binding_sid_type: Literal["no_binding", "four_octet_sid", "ipv6_sid"]
    """Type of the binding SID.

    Supported types are "No Binding SID" or "Four Octets Sid" or "IPv6 SID".
    """

    four_octet_sid: int
    """Binding SID is encoded in 4 octets."""

    i_flag: bool
    """I-Flag encodes the "Drop Upon Invalid" behavior."""

    ipv6_sid: str
    """IPv6 SID value."""

    s_flag: bool
    """S-Flag encodes the "Specified-BSID-only" behavior."""
