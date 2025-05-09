# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ResultExtendedCommunity",
    "Structured",
    "StructuredNonTransitive2octetAsType",
    "StructuredNonTransitive2octetAsTypeLinkBandwidthSubtype",
    "StructuredTransitive2octetAsType",
    "StructuredTransitive2octetAsTypeRouteOriginSubtype",
    "StructuredTransitive2octetAsTypeRouteTargetSubtype",
    "StructuredTransitive4octetAsType",
    "StructuredTransitive4octetAsTypeRouteOriginSubtype",
    "StructuredTransitive4octetAsTypeRouteTargetSubtype",
    "StructuredTransitiveIpv4AddressType",
    "StructuredTransitiveIpv4AddressTypeRouteOriginSubtype",
    "StructuredTransitiveIpv4AddressTypeRouteTargetSubtype",
    "StructuredTransitiveOpaqueType",
    "StructuredTransitiveOpaqueTypeColorSubtype",
    "StructuredTransitiveOpaqueTypeEncapsulationSubtype",
]


class StructuredNonTransitive2octetAsTypeLinkBandwidthSubtype(BaseModel):
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


class StructuredNonTransitive2octetAsType(BaseModel):
    choice: Optional[Literal["link_bandwidth_subtype"]] = None

    link_bandwidth_subtype: Optional[StructuredNonTransitive2octetAsTypeLinkBandwidthSubtype] = None
    """
    The Link Bandwidth Extended Community attribute is defined in
    draft-ietf-idr-link-bandwidth. It is sent with sub-type as 0x04.
    """


class StructuredTransitive2octetAsTypeRouteOriginSubtype(BaseModel):
    global_2byte_as: Optional[int] = None
    """The two octet IANA assigned AS value assigned to the Autonomous System."""

    local_4byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class StructuredTransitive2octetAsTypeRouteTargetSubtype(BaseModel):
    global_2byte_as: Optional[int] = None
    """The two octet IANA assigned AS value assigned to the Autonomous System."""

    local_4byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class StructuredTransitive2octetAsType(BaseModel):
    choice: Optional[Literal["route_target_subtype", "route_origin_subtype"]] = None

    route_origin_subtype: Optional[StructuredTransitive2octetAsTypeRouteOriginSubtype] = None
    """
    The Route Origin Community identifies one or more routers that inject a set of
    routes (that carry this Community) into BGP. It is sent with sub-type as 0x03 .
    """

    route_target_subtype: Optional[StructuredTransitive2octetAsTypeRouteTargetSubtype] = None
    """
    The Route Target Community identifies one or more routers that may receive a set
    of routes (that carry this Community) carried by BGP Update message. It is sent
    with sub-type as 0x02.
    """


class StructuredTransitive4octetAsTypeRouteOriginSubtype(BaseModel):
    global_4byte_as: Optional[int] = None
    """The four octet IANA assigned AS value assigned to the Autonomous System."""

    local_2byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class StructuredTransitive4octetAsTypeRouteTargetSubtype(BaseModel):
    global_4byte_as: Optional[int] = None
    """The four octet IANA assigned AS value assigned to the Autonomous System."""

    local_2byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the Autonomous System number
    carried in the Global Administrator sub-field has been assigned by an
    appropriate authority.
    """


class StructuredTransitive4octetAsType(BaseModel):
    choice: Optional[Literal["route_target_subtype", "route_origin_subtype"]] = None

    route_origin_subtype: Optional[StructuredTransitive4octetAsTypeRouteOriginSubtype] = None
    """
    The Route Origin Community identifies one or more routers that inject a set of
    routes (that carry this Community) into BGP. It is sent with sub-type as 0x03.
    """

    route_target_subtype: Optional[StructuredTransitive4octetAsTypeRouteTargetSubtype] = None
    """
    The Route Target Community identifies one or more routers that may receive a set
    of routes (that carry this Community) carried by BGP. It is sent with sub-type
    as 0x02
    """


class StructuredTransitiveIpv4AddressTypeRouteOriginSubtype(BaseModel):
    global_ipv4_admin: Optional[str] = None
    """An IPv4 unicast address assigned by one of the Internet registries."""

    local_2byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the IP address carried in the
    Global Administrator sub-field has been assigned by an appropriate authority.
    """


class StructuredTransitiveIpv4AddressTypeRouteTargetSubtype(BaseModel):
    global_ipv4_admin: Optional[str] = None
    """An IPv4 unicast address assigned by one of the Internet registries."""

    local_2byte_admin: Optional[int] = None
    """
    The Local Administrator sub-field contains a number from a numbering space that
    is administered by the organization to which the IP address carried in the
    Global Administrator sub-field has been assigned by an appropriate authority.
    """


class StructuredTransitiveIpv4AddressType(BaseModel):
    choice: Optional[Literal["route_target_subtype", "route_origin_subtype"]] = None

    route_origin_subtype: Optional[StructuredTransitiveIpv4AddressTypeRouteOriginSubtype] = None
    """
    The Route Origin Community identifies one or more routers that inject a set of
    routes (that carry this Community) into BGP It is sent with sub-type as 0x03.
    """

    route_target_subtype: Optional[StructuredTransitiveIpv4AddressTypeRouteTargetSubtype] = None
    """
    The Route Target Community identifies one or more routers that may receive a set
    of routes (that carry this Community) carried by BGP. It is sent with sub-type
    as 0x02.
    """


class StructuredTransitiveOpaqueTypeColorSubtype(BaseModel):
    color: Optional[int] = None
    """
    The color value is user defined and configured locally and used to determine
    whether a data packet can be transmitted on a certain tunnel or not in
    conjunction with the Encapsulation attribute. It is defined in RFC9012.
    """

    flags: Optional[int] = None
    """Two octet flag values."""


class StructuredTransitiveOpaqueTypeEncapsulationSubtype(BaseModel):
    reserved: Optional[int] = None
    """Four bytes of reserved values.

    Normally set to 0 on transmit and ignored on receive.
    """

    tunnel_type: Optional[int] = None
    """Identifies the type of tunneling technology being signalled.

    Initially defined in RFC5512 and extended in RFC9012. Some of the important
    tunnel types include

    - 1 L2TPv3 over IP [RFC9012],
    - 2 GRE [RFC9012],
    - 7 IP in IP [RFC9012],
    - 8 VXLAN Encapsulation [RFC8365],
    - 9 NVGRE Encapsulation [RFC8365],
    - 10 MPLS Encapsulation [RFC8365],
    - 15 SR TE Policy Type [draft-ietf-idr-segment-routing-te-policy],
    - 19 Geneve Encapsulation [RFC8926]
    """


class StructuredTransitiveOpaqueType(BaseModel):
    choice: Optional[Literal["color_subtype", "encapsulation_subtype"]] = None

    color_subtype: Optional[StructuredTransitiveOpaqueTypeColorSubtype] = None
    """
    The Color Community contains locally administrator defined 'color' value which
    is used in conjunction with Encapsulation attribute to decide whether a data
    packet can be transmitted on a certain tunnel or not. It is defined in RFC9012
    and sent with sub-type as 0x0b.
    """

    encapsulation_subtype: Optional[StructuredTransitiveOpaqueTypeEncapsulationSubtype] = None
    """This identifies the type of tunneling technology being signalled.

    It is defined in RFC9012 and sent with sub-type as 0x0c.
    """


class Structured(BaseModel):
    choice: Optional[
        Literal[
            "transitive_2octet_as_type",
            "transitive_ipv4_address_type",
            "transitive_4octet_as_type",
            "transitive_opaque_type",
            "non_transitive_2octet_as_type",
        ]
    ] = None

    non_transitive_2octet_as_type: Optional[StructuredNonTransitive2octetAsType] = None
    """
    The Non-Transitive Two-Octet AS-Specific Extended Community is sent as type
    0x40.
    """

    transitive_2octet_as_type: Optional[StructuredTransitive2octetAsType] = None
    """The Transitive Two-Octet AS-Specific Extended Community is sent as type 0x00 ."""

    transitive_4octet_as_type: Optional[StructuredTransitive4octetAsType] = None
    """The Transitive Four-Octet AS-Specific Extended Community is sent as type 0x02.

    It is defined in RFC 5668.
    """

    transitive_ipv4_address_type: Optional[StructuredTransitiveIpv4AddressType] = None
    """The Transitive IPv4 Address Specific Extended Community is sent as type 0x01."""

    transitive_opaque_type: Optional[StructuredTransitiveOpaqueType] = None
    """The Transitive Opaque Extended Community is sent as type 0x03."""


class ResultExtendedCommunity(BaseModel):
    raw: Optional[str] = None
    """
    The raw byte contents of the 8 bytes received in the Extended Community as 16
    hex characters.
    """

    structured: Optional[Structured] = None
    """
    The Extended Communities Attribute is a optional BGP attribute,defined in
    RFC4360 with the Type Code 16. Community and Extended Communities attributes are
    utilized to trigger routing decisions, such as acceptance, rejection,
    preference, or redistribution. An extended community is an 8-bytes value. It is
    divided into two main parts. The first 2 bytes of the community encode a type
    and optonal sub-type field. The last 6 bytes (or 7 bytes for types without a
    sub-type) carry a unique set of data in a format defined by the type and
    optional sub-type field. Extended communities provide a larger range for
    grouping or categorizing communities.
    """
