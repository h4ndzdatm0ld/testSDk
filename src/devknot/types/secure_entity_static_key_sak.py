# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SecureEntityStaticKeySak"]


class SecureEntityStaticKeySak(BaseModel):
    sak: Optional[str] = None
    """Secure association key(SAK) bits as hex string.

    Either 128 bits or 256 bits depending on the chosen cipher suite.
    """

    salt: Optional[str] = None
    """12 bytes salt used in case of XPN cipher suites."""

    ssci: Optional[str] = None
    """4 bytes short SCI(SSCI) used in case of XPN cipher suites."""
