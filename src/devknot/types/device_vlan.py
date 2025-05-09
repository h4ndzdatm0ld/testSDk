# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeviceVlan"]


class DeviceVlan(BaseModel):
    name: str
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    id: Optional[int] = None
    """VLAN identifier"""

    priority: Optional[int] = None
    """Priority code point"""

    tpid: Optional[Literal["x8100", "x88A8", "x9100", "x9200", "x9300"]] = None
    """Tag protocol identifier"""
