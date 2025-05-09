# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FlowIpv6Auto"]


class FlowIpv6Auto(BaseModel):
    choice: Literal["dhcp"]
    """
    The method to be used to provide the system generated value. The dhcp option
    populates the field based on the dynamic IPv6 address that has been assigned to
    the DHCPv6 client by a DHCPv6 server.
    """
