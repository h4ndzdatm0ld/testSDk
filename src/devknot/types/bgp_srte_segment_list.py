# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .bgp_srte_sr_mpls_sid import BgpSrteSrMplsSid
from .bgp_srte_s_rv6_sid_endpoint_behavior_and_structure import BgpSrteSRv6SidEndpointBehaviorAndStructure

__all__ = [
    "BgpSrteSegmentList",
    "Segment",
    "SegmentTypeA",
    "SegmentTypeB",
    "SegmentTypeC",
    "SegmentTypeD",
    "SegmentTypeE",
    "SegmentTypeF",
    "SegmentTypeG",
    "SegmentTypeH",
    "SegmentTypeI",
    "SegmentTypeJ",
    "SegmentTypeK",
]


class SegmentTypeA(BaseModel):
    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    label: Optional[int] = None
    """Label value in [0, 2^20 -1]."""

    s_bit: Optional[bool] = None
    """Bottom-of-Stack bit."""

    tc: Optional[int] = None
    """Traffic class in bits."""

    ttl: Optional[int] = None
    """Time To Live."""


class SegmentTypeB(BaseModel):
    srv6_sid: str
    """SRv6 SID."""

    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    srv6_sid_endpoint_behavior: Optional[BgpSrteSRv6SidEndpointBehaviorAndStructure] = None
    """Optional SRv6 Endpoint Behavior and SID Structure."""


class SegmentTypeC(BaseModel):
    ipv4_node_address: str
    """IPv4 address representing a node."""

    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    sr_algorithm: Optional[int] = None
    """SR Algorithm identifier when A-Flag in on."""

    sr_mpls_sid: Optional[BgpSrteSrMplsSid] = None
    """Optional SR-MPLS SID."""


class SegmentTypeD(BaseModel):
    ipv6_node_address: str
    """IPv6 address representing a node."""

    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    sr_algorithm: Optional[int] = None
    """specifying SR Algorithm when when A-Flag as defined in above flags."""

    sr_mpls_sid: Optional[BgpSrteSrMplsSid] = None
    """Optional SR-MPLS SID."""


class SegmentTypeE(BaseModel):
    ipv4_node_address: str
    """IPv4 address representing a node."""

    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    local_interface_id: Optional[int] = None
    """Local Interface ID: The Interface Index as defined in [RFC8664]."""

    sr_mpls_sid: Optional[BgpSrteSrMplsSid] = None
    """Optional SR-MPLS SID."""


class SegmentTypeF(BaseModel):
    local_ipv4_address: str
    """Local IPv4 Address."""

    remote_ipv4_address: str
    """Remote IPv4 Address."""

    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    sr_mpls_sid: Optional[BgpSrteSrMplsSid] = None
    """Optional SR-MPLS SID."""


class SegmentTypeG(BaseModel):
    local_ipv6_node_address: str
    """IPv6 address representing a node."""

    remote_ipv6_node_address: str
    """IPv6 address representing a node."""

    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    local_interface_id: Optional[int] = None
    """Local Interface ID: The Interface Index as defined in [RFC8664]."""

    remote_interface_id: Optional[int] = None
    """Local Interface ID: The Interface Index as defined in [RFC8664]."""

    sr_mpls_sid: Optional[BgpSrteSrMplsSid] = None
    """Optional SR-MPLS SID."""


class SegmentTypeH(BaseModel):
    local_ipv6_address: str
    """Local IPv6 Address."""

    remote_ipv6_address: str
    """Remote IPv6 Address."""

    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    sr_mpls_sid: Optional[BgpSrteSrMplsSid] = None
    """Optional SR-MPLS SID."""


class SegmentTypeI(BaseModel):
    ipv6_node_address: str
    """IPv6 address representing a node."""

    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    srv6_sid: Optional[str] = None
    """Optional SRv6 SID."""

    srv6_sid_endpoint_behavior: Optional[BgpSrteSRv6SidEndpointBehaviorAndStructure] = None
    """Optional SRv6 Endpoint Behavior and SID Structure."""


class SegmentTypeJ(BaseModel):
    local_ipv6_node_address: str
    """IPv6 address representing a node."""

    remote_ipv6_node_address: str
    """IPv6 address representing a node."""

    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    local_interface_id: Optional[int] = None
    """Local Interface ID: The Interface Index as defined in [RFC8664]."""

    remote_interface_id: Optional[int] = None
    """Local Interface ID: The Interface Index as defined in [RFC8664]."""

    sr_algorithm: Optional[int] = None
    """SR Algorithm identifier when A-Flag in on."""

    srv6_sid: Optional[str] = None
    """Optional SRv6 SID."""

    srv6_sid_endpoint_behavior: Optional[BgpSrteSRv6SidEndpointBehaviorAndStructure] = None
    """Optional SRv6 Endpoint Behavior and SID Structure."""


class SegmentTypeK(BaseModel):
    local_ipv6_address: str
    """IPv6 address representing a node."""

    remote_ipv6_address: str
    """IPv6 address representing a node."""

    flags: Optional[str] = None
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    sr_algorithm: Optional[int] = None
    """SR Algorithm identifier when A-Flag in on."""

    srv6_sid: Optional[str] = None
    """Optional SRv6 SID."""

    srv6_sid_endpoint_behavior: Optional[BgpSrteSRv6SidEndpointBehaviorAndStructure] = None
    """Optional SRv6 Endpoint Behavior and SID Structure."""


class Segment(BaseModel):
    name: str
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    segment_type: Literal[
        "type_a", "type_b", "type_c", "type_d", "type_e", "type_f", "type_g", "type_h", "type_i", "type_j", "type_k"
    ]
    """
    Specify one of the segment type.
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13
    Type A: SID only, in the form of MPLS Label. Type B: SID only, in the form of
    IPv6 Address. Type C: IPv4 Node Address with optional SID. Type D: IPv6 Node
    Address with optional SID for SR MPLS. Type E: IPv4 Address and index with
    optional SID. Type F: IPv4 Local and Remote addresses with optional SID. Type G:
    IPv6 Address and index for local and remote pair with optional SID for SR MPLS.
    Type H: IPv6 Local and Remote addresses with optional SID for SR MPLS. Type I:
    IPv6 Node Address with optional SID for SRv6. Type J: IPv6 Address and index for
    local and remote pair with optional SID for SRv6. Type K: IPv6 Local and Remote
    addresses for SRv6.
    """

    active: Optional[bool] = None
    """
    If enabled means that this part of the configuration including any active
    'children' nodes will be advertised to peer. If disabled, this means that though
    config is present, it is not taking any part of the test but can be activated at
    run-time to advertise just this part of the configuration to the peer.
    """

    type_a: Optional[SegmentTypeA] = None
    """Type A: SID only, in the form of MPLS Label."""

    type_b: Optional[SegmentTypeB] = None
    """Type B: SID only, in the form of IPv6 address."""

    type_c: Optional[SegmentTypeC] = None
    """Type C: IPv4 Node Address with optional SID."""

    type_d: Optional[SegmentTypeD] = None
    """Type D: IPv6 Node Address with optional SID for SR MPLS."""

    type_e: Optional[SegmentTypeE] = None
    """Type E: IPv4 Address and Local Interface ID with optional SID"""

    type_f: Optional[SegmentTypeF] = None
    """Type F: IPv4 Local and Remote addresses with optional SID."""

    type_g: Optional[SegmentTypeG] = None
    """
    Type G: IPv6 Address, Interface ID for local and remote pair with optional SID
    for SR MPLS.
    """

    type_h: Optional[SegmentTypeH] = None
    """Type H: IPv6 Local and Remote addresses with optional SID for SR MPLS."""

    type_i: Optional[SegmentTypeI] = None
    """Type I: IPv6 Node Address with optional SRv6 SID."""

    type_j: Optional[SegmentTypeJ] = None
    """
    Type J: IPv6 Address, Interface ID for local and remote pair for SRv6 with
    optional SID.
    """

    type_k: Optional[SegmentTypeK] = None
    """Type K: IPv6 Local and Remote addresses for SRv6 with optional SID."""


class BgpSrteSegmentList(BaseModel):
    name: str
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    active: Optional[bool] = None
    """
    If enabled means that this part of the configuration including any active
    'children' nodes will be advertised to peer. If disabled, this means that though
    config is present, it is not taking any part of the test but can be activated at
    run-time to advertise just this part of the configuration to the peer.
    """

    segments: Optional[List[Segment]] = None

    weight: Optional[int] = None
    """The Weight associated with a given path and the sub-TLV is optional."""
