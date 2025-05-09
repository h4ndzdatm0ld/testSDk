# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FlowIpv4Auto"]


class FlowIpv4Auto(BaseModel):
    choice: Literal["dhcp"]
    """The method to be used to provide the system generated value.

    The dhcp option populates the field based on the dynamic IPv4 address that has
    been assigned to the DHCPv4 client by a DHCPv4 server.
    """
