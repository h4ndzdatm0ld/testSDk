# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "BgpExtendedCommunity",
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


class Custom(BaseModel):
    community_subtype: Optional[str] = None
    """The sub-type to be set in the Extended Community attribute.

    For certain types with no sub-type this byte can also be used as part of an
    extended value field. Accepts hexadecimal input upto ff.
    """

    community_type: Optional[str] = None
    """The type to be set in the Extended Community attribute.

    Accepts hexadecimal input upto ff .
    """

    value: Optional[str] = None
    """6 byte hex value to be carried in the last 6 bytes of the Extended Community.

    Accepts hexadecimal input upto ffffffffffff.
    """


class NonTransitive2octetAsTypeLinkBandwidthSubtype(BaseModel):
    bandwidth: Optional[float] = None
    """Bandwidth of the link in bytes per second.

    ( 1 Kbps is 1000 bytes per second and 1 Mbps is 1000 Kbps per second )
    """

    global_2byte_as: Optional[int] = None
    """
    The value of the Global Administrator subfield should represent the Autonomous
    System of the router that attaches the Link Bandwidth Community. If four octet
    AS numbering scheme is used, AS_TRANS (23456) should be used.
    """


class NonTransitive2octetAsType(BaseModel):
    choice: Optional[Literal["link_bandwidth_subtype"]] = None

    link_bandwidth_subtype: Optional[NonTransitive2octetAsTypeLinkBandwidthSubtype] = None
    """
    The Link Bandwidth Extended Community attribute is defined in
    draft-ietf-idr-link-bandwidth. It is sent with sub-type as 0x04.
    """


class Transitive2octetAsTypeRouteOriginSubtype(BaseModel):
    global_2byte_as: Optional[int] = None
    """The two octet IANA assigned AS value assigned to the Autonomous System."""

    local_4byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class Transitive2octetAsTypeRouteTargetSubtype(BaseModel):
    global_2byte_as: Optional[int] = None
    """The two octet IANA assigned AS value assigned to the Autonomous System."""

    local_4byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class Transitive2octetAsType(BaseModel):
    choice: Optional[Literal["route_target_subtype", "route_origin_subtype"]] = None

    route_origin_subtype: Optional[Transitive2octetAsTypeRouteOriginSubtype] = None
    """
    The Route Origin Community identifies one or more routers that inject a set of
    routes (that carry this Community) into BGP. It is sent with sub-type as 0x03 .
    """

    route_target_subtype: Optional[Transitive2octetAsTypeRouteTargetSubtype] = None
    """
    The Route Target Community identifies one or more routers that may receive a set
    of routes (that carry this Community) carried by BGP. It is sent with sub-type
    as 0x02.
    """


class Transitive4octetAsTypeRouteOriginSubtype(BaseModel):
    global_4byte_as: Optional[int] = None
    """The four octet IANA assigned AS value assigned to the Autonomous System."""

    local_2byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class Transitive4octetAsTypeRouteTargetSubtype(BaseModel):
    global_4byte_as: Optional[int] = None
    """The four octet IANA assigned AS value assigned to the Autonomous System."""

    local_2byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class Transitive4octetAsType(BaseModel):
    choice: Optional[Literal["route_target_subtype", "route_origin_subtype"]] = None

    route_origin_subtype: Optional[Transitive4octetAsTypeRouteOriginSubtype] = None
    """
    The Route Origin Community identifies one or more routers that inject a set of
    routes (that carry this Community) into BGP. It is sent with sub-type as 0x03.
    """

    route_target_subtype: Optional[Transitive4octetAsTypeRouteTargetSubtype] = None
    """
    The Route Target Community identifies one or more routers that may receive a set
    of routes (that carry this Community) carried by BGP. It is sent with sub-type
    as 0x02
    """


class TransitiveEvpnTypeRouterMacSubtype(BaseModel):
    router_mac: Optional[str] = None
    """MAC Address of the PE Router."""


class TransitiveEvpnType(BaseModel):
    choice: Optional[Literal["router_mac_subtype"]] = None

    router_mac_subtype: Optional[TransitiveEvpnTypeRouterMacSubtype] = None
    """
    The Router MAC EVPN Community is defined in RFC9135 and normally sent only for
    EVPN Type-2 Routes . It is sent with sub-type 0x03.
    """


class TransitiveIpv4AddressTypeRouteOriginSubtype(BaseModel):
    global_ipv4_admin: Optional[str] = None
    """An IPv4 unicast address assigned by one of the Internet registries."""

    local_2byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the IP address carried in the
    Global Administrator sub-field has been assigned by an appropriate authority.
    """


class TransitiveIpv4AddressTypeRouteTargetSubtype(BaseModel):
    global_ipv4_admin: Optional[str] = None
    """An IPv4 unicast address assigned by one of the Internet registries."""

    local_2byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the IP address carried in the
    Global Administrator sub-field has been assigned by an appropriate authority.
    """


class TransitiveIpv4AddressType(BaseModel):
    choice: Optional[Literal["route_target_subtype", "route_origin_subtype"]] = None

    route_origin_subtype: Optional[TransitiveIpv4AddressTypeRouteOriginSubtype] = None
    """
    The Route Origin Community identifies one or more routers that inject a set of
    routes (that carry this Community) into BGP It is sent with sub-type as 0x03.
    """

    route_target_subtype: Optional[TransitiveIpv4AddressTypeRouteTargetSubtype] = None
    """
    The Route Target Community identifies one or more routers that may receive a set
    of routes (that carry this Community) carried by BGP. It is sent with sub-type
    as 0x02.
    """


class TransitiveOpaqueTypeColorSubtype(BaseModel):
    color: Optional[int] = None
    """
    The color value is user defined and configured locally and used to determine
    whether a data packet can be transmitted on a certain tunnel or not in
    conjunction with the Encapsulation attribute. It is defined in RFC9012.
    """

    flags: Optional[int] = None
    """Two octet flag values."""


class TransitiveOpaqueTypeEncapsulationSubtype(BaseModel):
    reserved: Optional[int] = None
    """Four bytes of reserved values.

    Normally set to 0 on transmit and ignored on receive.
    """

    tunnel_type: Optional[int] = None
    """Identifies the type of tunneling technology being signalled.

    Initially defined in RFC5512 and extended in RFC9012. Some of the important
    tunnel types include 1 L2TPv3 over IP [RFC9012], 2 GRE [RFC9012] 7 IP in IP
    [RFC9012] 8 VXLAN Encapsulation [RFC8365] 9 NVGRE Encapsulation [RFC8365] 10
    MPLS Encapsulation [RFC8365] 15 SR TE Policy Type
    [draft-ietf-idr-segment-routing-te-policy] 19 Geneve Encapsulation [RFC8926]
    """


class TransitiveOpaqueType(BaseModel):
    choice: Optional[Literal["color_subtype", "encapsulation_subtype"]] = None

    color_subtype: Optional[TransitiveOpaqueTypeColorSubtype] = None
    """
    The Color Community contains locally administrator defined 'color' value which
    is used in conjunction with Encapsulation attribute to decide whether a data
    packet can be transmitted on a certain tunnel or not. It is defined in RFC9012
    and sent with sub-type as 0x0b.
    """

    encapsulation_subtype: Optional[TransitiveOpaqueTypeEncapsulationSubtype] = None
    """This identifies the type of tunneling technology being signalled.

    It is defined in RFC9012 and sent with sub-type as 0x0c.
    """


class BgpExtendedCommunity(BaseModel):
    choice: Optional[
        Literal[
            "transitive_2octet_as_type",
            "transitive_ipv4_address_type",
            "transitive_4octet_as_type",
            "transitive_opaque_type",
            "transitive_evpn_type",
            "non_transitive_2octet_as_type",
            "custom",
        ]
    ] = None

    custom: Optional[Custom] = None
    """
    Add a custom Extended Community with a combination of types , sub-types and
    values not explicitly specified above or not defined yet.
    """

    non_transitive_2octet_as_type: Optional[NonTransitive2octetAsType] = None
    """
    The Non-Transitive Two-Octet AS-Specific Extended Community is sent as type
    0x40.
    """

    transitive_2octet_as_type: Optional[Transitive2octetAsType] = None
    """The Transitive Two-Octet AS-Specific Extended Community is sent as type 0x00 ."""

    transitive_4octet_as_type: Optional[Transitive4octetAsType] = None
    """The Transitive Four-Octet AS-Specific Extended Community is sent as type 0x02.

    It is defined in RFC 5668.
    """

    transitive_evpn_type: Optional[TransitiveEvpnType] = None
    """The Transitive EVPN Extended Community is sent as type 0x06 ."""

    transitive_ipv4_address_type: Optional[TransitiveIpv4AddressType] = None
    """The Transitive IPv4 Address Specific Extended Community is sent as type 0x01."""

    transitive_opaque_type: Optional[TransitiveOpaqueType] = None
    """The Transitive Opaque Extended Community is sent as type 0x03."""
