# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FlowIpv4AutoParam"]


class FlowIpv4AutoParam(TypedDict, total=False):
    choice: Required[Literal["dhcp"]]
    """The method to be used to provide the system generated value.

    The dhcp option populates the field based on the dynamic IPv4 address that has
    been assigned to the DHCPv4 client by a DHCPv4 server.
    """
