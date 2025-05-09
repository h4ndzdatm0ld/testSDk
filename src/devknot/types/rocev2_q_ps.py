# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Rocev2QPs", "ConnectionType", "ConnectionTypeReliableConnection"]


class ConnectionTypeReliableConnection(BaseModel):
    dscp: Optional[int] = None
    """DSCP value for the RDMA data packets."""

    ecn: Optional[Literal["non_ect", "ect_1", "ect_0", "ce"]] = None
    """
    This field allows to configure bits of the Traffic Class field in the IPv4 or
    IPv6 header to encode four different code points. Those are non_ect, ect_1,
    ect_0 and ce. non_ect quivalent is 00, ect_1 represent 01, ect_0 represent 10
    and ce means 11.
    """

    initial_psn: Optional[int] = None
    """
    Initial packet sequence number of the data transfer packet generated for this
    QP.
    """

    remote_key: Optional[str] = None
    """Remote Key linked to the QP's virtual address."""

    source_qp_number: Optional[int] = None
    """Configure Source QP number which initiates the RDMA operation."""

    udp_source_port: Optional[int] = None
    """UDP source port number for this QP."""

    virtual_address: Optional[str] = None
    """Virtual Address where the data transfer from the remote QP will write to."""


class ConnectionType(BaseModel):
    choice: Optional[Literal["reliable_connection"]] = None

    reliable_connection: Optional[ConnectionTypeReliableConnection] = None
    """Defines the parameters for configuring a RoCEv2 QP."""


class Rocev2QPs(BaseModel):
    qp_name: str
    """Name of each QP. Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    connection_type: Optional[ConnectionType] = None
    """
    Specifies the connection type for the QP, determining what and how the QP
    transfers data.
    """
