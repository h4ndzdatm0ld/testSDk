# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DeviceVlanParam"]


class DeviceVlanParam(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    id: int
    """VLAN identifier"""

    priority: int
    """Priority code point"""

    tpid: Literal["x8100", "x88A8", "x9100", "x9200", "x9300"]
    """Tag protocol identifier"""
