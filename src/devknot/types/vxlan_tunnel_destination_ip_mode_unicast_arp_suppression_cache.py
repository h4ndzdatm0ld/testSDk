# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VxlanTunnelDestinationIPModeUnicastArpSuppressionCache"]


class VxlanTunnelDestinationIPModeUnicastArpSuppressionCache(BaseModel):
    remote_vm_ipv4: Optional[str] = None
    """Remote VM IPv4 address"""

    remote_vm_mac: Optional[str] = None
    """Remote VM MAC address bound to Remote VM IPv4 address"""
