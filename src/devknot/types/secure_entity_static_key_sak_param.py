# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SecureEntityStaticKeySakParam"]


class SecureEntityStaticKeySakParam(TypedDict, total=False):
    sak: str
    """Secure association key(SAK) bits as hex string.

    Either 128 bits or 256 bits depending on the chosen cipher suite.
    """

    salt: str
    """12 bytes salt used in case of XPN cipher suites."""

    ssci: str
    """4 bytes short SCI(SSCI) used in case of XPN cipher suites."""
