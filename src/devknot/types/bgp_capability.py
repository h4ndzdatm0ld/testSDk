# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BgpCapability"]


class BgpCapability(BaseModel):
    evpn: Optional[bool] = None
    """Support for the EVPN address family."""

    extended_next_hop_encoding: Optional[bool] = None
    """
    Support for extended Next Hop Encoding for Nexthop field in IPv4 routes
    advertisement. This allows IPv4 routes being advertised by IPv6 peers to include
    an IPv6 Nexthop.
    """

    ipv4_mdt: Optional[bool] = None
    """Supports for IPv4 MDT address family messages."""

    ipv4_mpls_vpn: Optional[bool] = None
    """Support for the IPv4 MPLS L3VPN address family."""

    ipv4_multicast: Optional[bool] = None
    """Support for the IPv4 Multicast address family."""

    ipv4_multicast_mpls_vpn: Optional[bool] = None
    """Support for the IPv4 Multicast VPN address family."""

    ipv4_multicast_vpn: Optional[bool] = None
    """Support for the IPv4 Multicast VPN address family."""

    ipv4_sr_te_policy: Optional[bool] = None
    """Support for IPv4 SRTE policy."""

    ipv4_unicast: Optional[bool] = None
    """Support for the IPv4 Unicast address family."""

    ipv4_unicast_add_path: Optional[bool] = None
    """Support for IPv4 Unicast Add Path Capability."""

    ipv4_unicast_flow_spec: Optional[bool] = None
    """Support for propagation of IPv4 unicast flow specification rules."""

    ipv6_mdt: Optional[bool] = None
    """Support for IPv6 MDT address family messages."""

    ipv6_mpls_vpn: Optional[bool] = None
    """Support for the IPv6 MPLS L3VPN address family."""

    ipv6_multicast: Optional[bool] = None
    """Support for the IPv6 Multicast address family."""

    ipv6_multicast_mpls_vpn: Optional[bool] = None
    """Support for the IPv6 Multicast VPN address family."""

    ipv6_multicast_vpn: Optional[bool] = None
    """Support for the IPv6 Multicast VPN address family."""

    ipv6_sr_te_policy: Optional[bool] = None
    """Support for IPv6 SRTE policy."""

    ipv6_unicast: Optional[bool] = None
    """Support for the IPv4 Unicast address family."""

    ipv6_unicast_add_path: Optional[bool] = None
    """Support for IPv6 Unicast Add Path Capability."""

    ipv6_unicast_flow_spec: Optional[bool] = None
    """Support for propagation of IPv6 unicast flow specification rules."""

    link_state_non_vpn: Optional[bool] = None
    """Support for BGP Link State for ISIS and OSPF."""

    link_state_vpn: Optional[bool] = None
    """Capability advertisement of BGP Link State for VPNs."""

    route_constraint: Optional[bool] = None
    """Supports for the route constraint capabilities.

    Route Constraint allows the advertisement of Route Target Membership
    information. The BGP peers exchange Route Target Reachability Information, which
    is used to build a route distribution graph. This limits the propagation of VPN
    Network Layer Reachability Information (NLRI) between different autonomous
    systems or distinct clusters of the same autonomous system. This is supported
    for Layer 3 Virtual Private Network scenario.
    """

    route_refresh: Optional[bool] = None
    """Support for the route refresh capabilities.

    Route Refresh allows the dynamic exchange of route refresh requests and routing
    information between BGP peers and the subsequent re-advertisement of the
    outbound or inbound routing table.
    """

    vpls: Optional[bool] = None
    """Support for VPLS as below.

    RFC4761 - Virtual Private LAN Service (VPLS) using BGP for Auto-Discovery and
    Signaling. RFC6624 - Layer 2 Virtual Private Networks using BGP for
    Auto-Discovery and Signaling.
    """
