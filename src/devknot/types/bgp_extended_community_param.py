# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = [
    "BgpExtendedCommunityParam",
    "Custom",
    "NonTransitive2octetAsType",
    "NonTransitive2octetAsTypeLinkBandwidthSubtype",
    "Transitive2octetAsType",
    "Transitive2octetAsTypeRouteOriginSubtype",
    "Transitive2octetAsTypeRouteTargetSubtype",
    "Transitive4octetAsType",
    "Transitive4octetAsTypeRouteOriginSubtype",
    "Transitive4octetAsTypeRouteTargetSubtype",
    "TransitiveEvpnType",
    "TransitiveEvpnTypeRouterMacSubtype",
    "TransitiveIpv4AddressType",
    "TransitiveIpv4AddressTypeRouteOriginSubtype",
    "TransitiveIpv4AddressTypeRouteTargetSubtype",
    "TransitiveOpaqueType",
    "TransitiveOpaqueTypeColorSubtype",
    "TransitiveOpaqueTypeEncapsulationSubtype",
]


class Custom(TypedDict, total=False):
    community_subtype: str
    """The sub-type to be set in the Extended Community attribute.

    For certain types with no sub-type this byte can also be used as part of an
    extended value field. Accepts hexadecimal input upto ff.
    """

    community_type: str
    """The type to be set in the Extended Community attribute.

    Accepts hexadecimal input upto ff .
    """

    value: str
    """6 byte hex value to be carried in the last 6 bytes of the Extended Community.

    Accepts hexadecimal input upto ffffffffffff.
    """


class NonTransitive2octetAsTypeLinkBandwidthSubtype(TypedDict, total=False):
    bandwidth: float
    """Bandwidth of the link in bytes per second.

    ( 1 Kbps is 1000 bytes per second and 1 Mbps is 1000 Kbps per second )
    """

    global_2byte_as: int
    """
    The value of the Global Administrator subfield should represent the Autonomous
    System of the router that attaches the Link Bandwidth Community. If four octet
    AS numbering scheme is used, AS_TRANS (23456) should be used.
    """


class NonTransitive2octetAsType(TypedDict, total=False):
    choice: Literal["link_bandwidth_subtype"]

    link_bandwidth_subtype: NonTransitive2octetAsTypeLinkBandwidthSubtype
    """
    The Link Bandwidth Extended Community attribute is defined in
    draft-ietf-idr-link-bandwidth. It is sent with sub-type as 0x04.
    """


class Transitive2octetAsTypeRouteOriginSubtype(TypedDict, total=False):
    global_2byte_as: int
    """The two octet IANA assigned AS value assigned to the Autonomous System."""

    local_4byte_admin: int
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class Transitive2octetAsTypeRouteTargetSubtype(TypedDict, total=False):
    global_2byte_as: int
    """The two octet IANA assigned AS value assigned to the Autonomous System."""

    local_4byte_admin: int
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class Transitive2octetAsType(TypedDict, total=False):
    choice: Literal["route_target_subtype", "route_origin_subtype"]

    route_origin_subtype: Transitive2octetAsTypeRouteOriginSubtype
    """
    The Route Origin Community identifies one or more routers that inject a set of
    routes (that carry this Community) into BGP. It is sent with sub-type as 0x03 .
    """

    route_target_subtype: Transitive2octetAsTypeRouteTargetSubtype
    """
    The Route Target Community identifies one or more routers that may receive a set
    of routes (that carry this Community) carried by BGP. It is sent with sub-type
    as 0x02.
    """


class Transitive4octetAsTypeRouteOriginSubtype(TypedDict, total=False):
    global_4byte_as: int
    """The four octet IANA assigned AS value assigned to the Autonomous System."""

    local_2byte_admin: int
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class Transitive4octetAsTypeRouteTargetSubtype(TypedDict, total=False):
    global_4byte_as: int
    """The four octet IANA assigned AS value assigned to the Autonomous System."""

    local_2byte_admin: int
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class Transitive4octetAsType(TypedDict, total=False):
    choice: Literal["route_target_subtype", "route_origin_subtype"]

    route_origin_subtype: Transitive4octetAsTypeRouteOriginSubtype
    """
    The Route Origin Community identifies one or more routers that inject a set of
    routes (that carry this Community) into BGP. It is sent with sub-type as 0x03.
    """

    route_target_subtype: Transitive4octetAsTypeRouteTargetSubtype
    """
    The Route Target Community identifies one or more routers that may receive a set
    of routes (that carry this Community) carried by BGP. It is sent with sub-type
    as 0x02
    """


class TransitiveEvpnTypeRouterMacSubtype(TypedDict, total=False):
    router_mac: str
    """MAC Address of the PE Router."""


class TransitiveEvpnType(TypedDict, total=False):
    choice: Literal["router_mac_subtype"]

    router_mac_subtype: TransitiveEvpnTypeRouterMacSubtype
    """
    The Router MAC EVPN Community is defined in RFC9135 and normally sent only for
    EVPN Type-2 Routes . It is sent with sub-type 0x03.
    """


class TransitiveIpv4AddressTypeRouteOriginSubtype(TypedDict, total=False):
    global_ipv4_admin: str
    """An IPv4 unicast address assigned by one of the Internet registries."""

    local_2byte_admin: int
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the IP address carried in the
    Global Administrator sub-field has been assigned by an appropriate authority.
    """


class TransitiveIpv4AddressTypeRouteTargetSubtype(TypedDict, total=False):
    global_ipv4_admin: str
    """An IPv4 unicast address assigned by one of the Internet registries."""

    local_2byte_admin: int
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the IP address carried in the
    Global Administrator sub-field has been assigned by an appropriate authority.
    """


class TransitiveIpv4AddressType(TypedDict, total=False):
    choice: Literal["route_target_subtype", "route_origin_subtype"]

    route_origin_subtype: TransitiveIpv4AddressTypeRouteOriginSubtype
    """
    The Route Origin Community identifies one or more routers that inject a set of
    routes (that carry this Community) into BGP It is sent with sub-type as 0x03.
    """

    route_target_subtype: TransitiveIpv4AddressTypeRouteTargetSubtype
    """
    The Route Target Community identifies one or more routers that may receive a set
    of routes (that carry this Community) carried by BGP. It is sent with sub-type
    as 0x02.
    """


class TransitiveOpaqueTypeColorSubtype(TypedDict, total=False):
    color: int
    """
    The color value is user defined and configured locally and used to determine
    whether a data packet can be transmitted on a certain tunnel or not in
    conjunction with the Encapsulation attribute. It is defined in RFC9012.
    """

    flags: int
    """Two octet flag values."""


class TransitiveOpaqueTypeEncapsulationSubtype(TypedDict, total=False):
    reserved: int
    """Four bytes of reserved values.

    Normally set to 0 on transmit and ignored on receive.
    """

    tunnel_type: int
    """Identifies the type of tunneling technology being signalled.

    Initially defined in RFC5512 and extended in RFC9012. Some of the important
    tunnel types include 1 L2TPv3 over IP [RFC9012], 2 GRE [RFC9012] 7 IP in IP
    [RFC9012] 8 VXLAN Encapsulation [RFC8365] 9 NVGRE Encapsulation [RFC8365] 10
    MPLS Encapsulation [RFC8365] 15 SR TE Policy Type
    [draft-ietf-idr-segment-routing-te-policy] 19 Geneve Encapsulation [RFC8926]
    """


class TransitiveOpaqueType(TypedDict, total=False):
    choice: Literal["color_subtype", "encapsulation_subtype"]

    color_subtype: TransitiveOpaqueTypeColorSubtype
    """
    The Color Community contains locally administrator defined 'color' value which
    is used in conjunction with Encapsulation attribute to decide whether a data
    packet can be transmitted on a certain tunnel or not. It is defined in RFC9012
    and sent with sub-type as 0x0b.
    """

    encapsulation_subtype: TransitiveOpaqueTypeEncapsulationSubtype
    """This identifies the type of tunneling technology being signalled.

    It is defined in RFC9012 and sent with sub-type as 0x0c.
    """


class BgpExtendedCommunityParam(TypedDict, total=False):
    choice: Literal[
        "transitive_2octet_as_type",
        "transitive_ipv4_address_type",
        "transitive_4octet_as_type",
        "transitive_opaque_type",
        "transitive_evpn_type",
        "non_transitive_2octet_as_type",
        "custom",
    ]

    custom: Custom
    """
    Add a custom Extended Community with a combination of types , sub-types and
    values not explicitly specified above or not defined yet.
    """

    non_transitive_2octet_as_type: NonTransitive2octetAsType
    """
    The Non-Transitive Two-Octet AS-Specific Extended Community is sent as type
    0x40.
    """

    transitive_2octet_as_type: Transitive2octetAsType
    """The Transitive Two-Octet AS-Specific Extended Community is sent as type 0x00 ."""

    transitive_4octet_as_type: Transitive4octetAsType
    """The Transitive Four-Octet AS-Specific Extended Community is sent as type 0x02.

    It is defined in RFC 5668.
    """

    transitive_evpn_type: TransitiveEvpnType
    """The Transitive EVPN Extended Community is sent as type 0x06 ."""

    transitive_ipv4_address_type: TransitiveIpv4AddressType
    """The Transitive IPv4 Address Specific Extended Community is sent as type 0x01."""

    transitive_opaque_type: TransitiveOpaqueType
    """The Transitive Opaque Extended Community is sent as type 0x03."""
