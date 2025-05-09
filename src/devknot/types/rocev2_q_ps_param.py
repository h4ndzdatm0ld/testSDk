# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["Rocev2QPsParam", "ConnectionType", "ConnectionTypeReliableConnection"]


class ConnectionTypeReliableConnection(TypedDict, total=False):
    dscp: int
    """DSCP value for the RDMA data packets."""

    ecn: Literal["non_ect", "ect_1", "ect_0", "ce"]
    """
    This field allows to configure bits of the Traffic Class field in the IPv4 or
    IPv6 header to encode four different code points. Those are non_ect, ect_1,
    ect_0 and ce. non_ect quivalent is 00, ect_1 represent 01, ect_0 represent 10
    and ce means 11.
    """

    initial_psn: int
    """
    Initial packet sequence number of the data transfer packet generated for this
    QP.
    """

    remote_key: str
    """Remote Key linked to the QP's virtual address."""

    source_qp_number: int
    """Configure Source QP number which initiates the RDMA operation."""

    udp_source_port: int
    """UDP source port number for this QP."""

    virtual_address: str
    """Virtual Address where the data transfer from the remote QP will write to."""


class ConnectionType(TypedDict, total=False):
    choice: Literal["reliable_connection"]

    reliable_connection: ConnectionTypeReliableConnection
    """Defines the parameters for configuring a RoCEv2 QP."""


class Rocev2QPsParam(TypedDict, total=False):
    qp_name: Required[str]
    """Name of each QP. Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    connection_type: ConnectionType
    """
    Specifies the connection type for the QP, determining what and how the QP
    transfers data.
    """
