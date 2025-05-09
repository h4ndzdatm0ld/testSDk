# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

__all__ = [
    "MonitorCreateStatesParams",
    "BgpPrefixes",
    "BgpPrefixesIpv4UnicastFilter",
    "BgpPrefixesIpv6UnicastFilter",
    "Dhcpv4Interfaces",
    "Dhcpv4Leases",
    "Dhcpv6Interfaces",
    "Dhcpv6Leases",
    "Ipv4Neighbors",
    "Ipv6Neighbors",
    "IsisLsps",
    "LldpNeighbors",
    "Ospfv2Lsas",
    "Ospfv3Lsas",
    "RsvpLsps",
]


class MonitorCreateStatesParams(TypedDict, total=False):
    bgp_prefixes: BgpPrefixes
    """The request to retrieve BGP peer prefix information."""

    choice: Literal[
        "ipv4_neighbors",
        "ipv6_neighbors",
        "bgp_prefixes",
        "isis_lsps",
        "lldp_neighbors",
        "rsvp_lsps",
        "dhcpv4_interfaces",
        "dhcpv4_leases",
        "dhcpv6_interfaces",
        "dhcpv6_leases",
        "ospfv2_lsas",
        "ospfv3_lsas",
    ]

    dhcpv4_interfaces: Dhcpv4Interfaces
    """
    The request for assigned IPv4 address information associated with DHCP Client
    sessions.
    """

    dhcpv4_leases: Dhcpv4Leases
    """The request to retrieve DHCP Server host allocated status."""

    dhcpv6_interfaces: Dhcpv6Interfaces
    """
    The request for assigned IPv6 address information associated with DHCP Client
    sessions.
    """

    dhcpv6_leases: Dhcpv6Leases
    """The request to retrieve DHCP Server host allocated status."""

    ipv4_neighbors: Ipv4Neighbors
    """
    The request to retrieve IPv4 Neighbor state (ARP cache entries) of a network
    interface(s).
    """

    ipv6_neighbors: Ipv6Neighbors
    """
    The request to retrieve IPv6 Neighbor state (NDISC cache entries) of a network
    interface(s).
    """

    isis_lsps: IsisLsps
    """
    The request to retrieve ISIS Link State PDU (LSP) information learned by the
    router.
    """

    lldp_neighbors: LldpNeighbors
    """The request to retrieve LLDP neighbor information for a given instance."""

    ospfv2_lsas: Ospfv2Lsas
    """
    The request to retrieve OSPFv2 Link State Advertisements (LSA) information
    learned by the routers.
    """

    ospfv3_lsas: Ospfv3Lsas
    """
    The request to retrieve OSPFv3 Link State Advertisements (LSA) information
    learned by the routers.
    """

    rsvp_lsps: RsvpLsps
    """
    The request to retrieve RSVP Label Switched Path (LSP) information learned by
    the router.
    """


class BgpPrefixesIpv4UnicastFilter(TypedDict, total=False):
    addresses: List[str]
    """The addresses to match.

    If the addresses property is missing or empty then all addresses will match.
    """

    origin: Literal["igp", "egp", "incomplete"]
    """The origin to match. If the origin is missing then all origins will match."""

    path_id: int
    """The path id to match. If the path id is missing then all path ids will match."""

    prefix_length: int
    """The prefix length to match.

    If the prefix length is missing then all prefix lengths will match.
    """


class BgpPrefixesIpv6UnicastFilter(TypedDict, total=False):
    addresses: List[str]
    """The addresses to match.

    If the addresses property is missing or empty then all addresses will match.
    """

    origin: Literal["igp", "egp", "incomplete"]
    """The origin to match. If the origin is missing then all origins will match."""

    path_id: int
    """The path id to match. If the path id is missing then all path ids will match."""

    prefix_length: int
    """The prefix length to match.

    If the prefix length is missing then all prefix lengths will match.
    """


class BgpPrefixes(TypedDict, total=False):
    bgp_peer_names: List[str]
    """The names of BGP peers for which prefix information will be retrieved.

    If no names are specified then the results will contain prefix information for
    all configured BGP peers.

    x-constraint:

    - /components/schemas/Bgp.V4Peer/properties/name
    - /components/schemas/Bgp.V6Peer/properties/name
    """

    ipv4_unicast_filters: Iterable[BgpPrefixesIpv4UnicastFilter]
    """
    The IPv4 unicast results can be filtered by specifying additional prefix search
    criteria. If the ipv4_unicast_filters property is missing or empty then all IPv4
    prefixes will be returned.
    """

    ipv6_unicast_filters: Iterable[BgpPrefixesIpv6UnicastFilter]
    """
    The IPv6 unicast results can be filtered by specifying additional prefix search
    criteria. If the ipv6_unicast_filters property is missing or empty then all IPv6
    prefixes will be returned.
    """

    prefix_filters: List[Literal["ipv4_unicast", "ipv6_unicast"]]
    """Specify which prefixes to return.

    If the list is empty or missing then all prefixes will be returned.
    """


class Dhcpv4Interfaces(TypedDict, total=False):
    dhcp_client_names: List[str]
    """The names of DHCPv4 client to return results for.

    An empty list will return results for all DHCPv4 Client address information.

    x-constraint:

    - /components/schemas/Device.Dhcpv4client/properties/name
    """


class Dhcpv4Leases(TypedDict, total=False):
    dhcp_server_names: List[str]
    """The names of DHCPv4 server to return results for.

    An empty list will return results for all DHCPv4 servers.

    x-constraint:

    - /components/schemas/Device.Dhcpv4server/properties/name
    """


class Dhcpv6Interfaces(TypedDict, total=False):
    dhcp_client_names: List[str]
    """The names of DHCPv6 client to return results for.

    An empty list will return results for all DHCPv6 Client address information.

    x-constraint:

    - /components/schemas/Device.Dhcpv6client/properties/name
    """


class Dhcpv6Leases(TypedDict, total=False):
    dhcp_server_names: List[str]
    """The names of DHCPv6 server to return results for.

    An empty list will return results for all DHCPv6 servers.

    x-constraint:

    - /components/schemas/Device.Dhcpv6server/properties/name
    """


class Ipv4Neighbors(TypedDict, total=False):
    ethernet_names: List[str]
    """
    The names of Ethernet interfaces for which Neighbor state (ARP cache entries)
    will be retrieved. If no names are specified then the results will contain
    Neighbor state (ARP cache entries) for all available Ethernet interfaces.

    x-constraint:

    - /components/schemas/Device.Ethernet/properties/name
    """


class Ipv6Neighbors(TypedDict, total=False):
    ethernet_names: List[str]
    """
    The names of Ethernet interfaces for which Neighbor state (NDISC cache entries)
    will be retrieved. If no names are specified then the results will contain
    Neighbor state (NDISC cache entries) for all available Ethernet interfaces.

    x-constraint:

    - /components/schemas/Device.Ethernet/properties/name
    """


class IsisLsps(TypedDict, total=False):
    isis_router_names: List[str]
    """The names of ISIS routers for which learned information is requested.

    An empty list will return results for all ISIS routers.

    x-constraint:

    - /components/schemas/Device.IsisRouter/properties/name
    """


class LldpNeighbors(TypedDict, total=False):
    lldp_names: List[str]
    """The names of LLDP instances for which neighbor information will be retrieved.

    If no names are specified then the results will contain neighbor information for
    all configured LLDP instances.

    x-constraint:

    - /components/schemas/Lldp/properties/name
    """

    neighbor_id_filters: List[str]
    """Specify the neighbors for which information will be returned.

    If empty or missing then information for all neighbors will be returned.
    """


class Ospfv2Lsas(TypedDict, total=False):
    router_names: List[str]
    """The names of OSPFv2 routers for which learned information is requested.

    An empty list will return results for all OSPFv2 routers.

    x-constraint:

    - /components/schemas/Device.Ospfv2Router/properties/name
    """


class Ospfv3Lsas(TypedDict, total=False):
    router_names: List[str]
    """The names of OSPFv3 routers for which learned information is requested.

    An empty list will return results for all OSPFv3 routers.

    x-constraint:

    - /components/schemas/Ospfv3.RouterInstance/properties/name
    """


class RsvpLsps(TypedDict, total=False):
    rsvp_router_names: List[str]
    """The names of RSVP-TE routers for which learned information is requested.

    An empty list will return results for all RSVP=TE routers.

    x-constraint:

    - /components/schemas/Device.Rsvp/properties/name
    """
