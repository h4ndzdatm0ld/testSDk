# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FlowIpv6AutoParam"]


class FlowIpv6AutoParam(TypedDict, total=False):
    choice: Required[Literal["dhcp"]]
    """
    The method to be used to provide the system generated value. The dhcp option
    populates the field based on the dynamic IPv6 address that has been assigned to
    the DHCPv6 client by a DHCPv6 server.
    """
