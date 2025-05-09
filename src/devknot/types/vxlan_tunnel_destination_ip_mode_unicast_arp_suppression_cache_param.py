# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VxlanTunnelDestinationIPModeUnicastArpSuppressionCacheParam"]


class VxlanTunnelDestinationIPModeUnicastArpSuppressionCacheParam(TypedDict, total=False):
    remote_vm_ipv4: str
    """Remote VM IPv4 address"""

    remote_vm_mac: str
    """Remote VM MAC address bound to Remote VM IPv4 address"""
