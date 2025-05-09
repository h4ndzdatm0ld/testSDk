# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .bgp_srte_sr_mpls_sid_param import BgpSrteSrMplsSidParam
from .bgp_srte_s_rv6_sid_endpoint_behavior_and_structure_param import BgpSrteSRv6SidEndpointBehaviorAndStructureParam

__all__ = [
    "BgpSrteSegmentListParam",
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


class SegmentTypeA(TypedDict, total=False):
    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    label: int
    """Label value in [0, 2^20 -1]."""

    s_bit: bool
    """Bottom-of-Stack bit."""

    tc: int
    """Traffic class in bits."""

    ttl: int
    """Time To Live."""


class SegmentTypeB(TypedDict, total=False):
    srv6_sid: Required[str]
    """SRv6 SID."""

    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    srv6_sid_endpoint_behavior: BgpSrteSRv6SidEndpointBehaviorAndStructureParam
    """Optional SRv6 Endpoint Behavior and SID Structure."""


class SegmentTypeC(TypedDict, total=False):
    ipv4_node_address: Required[str]
    """IPv4 address representing a node."""

    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    sr_algorithm: int
    """SR Algorithm identifier when A-Flag in on."""

    sr_mpls_sid: BgpSrteSrMplsSidParam
    """Optional SR-MPLS SID."""


class SegmentTypeD(TypedDict, total=False):
    ipv6_node_address: Required[str]
    """IPv6 address representing a node."""

    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    sr_algorithm: int
    """specifying SR Algorithm when when A-Flag as defined in above flags."""

    sr_mpls_sid: BgpSrteSrMplsSidParam
    """Optional SR-MPLS SID."""


class SegmentTypeE(TypedDict, total=False):
    ipv4_node_address: Required[str]
    """IPv4 address representing a node."""

    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    local_interface_id: int
    """Local Interface ID: The Interface Index as defined in [RFC8664]."""

    sr_mpls_sid: BgpSrteSrMplsSidParam
    """Optional SR-MPLS SID."""


class SegmentTypeF(TypedDict, total=False):
    local_ipv4_address: Required[str]
    """Local IPv4 Address."""

    remote_ipv4_address: Required[str]
    """Remote IPv4 Address."""

    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    sr_mpls_sid: BgpSrteSrMplsSidParam
    """Optional SR-MPLS SID."""


class SegmentTypeG(TypedDict, total=False):
    local_ipv6_node_address: Required[str]
    """IPv6 address representing a node."""

    remote_ipv6_node_address: Required[str]
    """IPv6 address representing a node."""

    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    local_interface_id: int
    """Local Interface ID: The Interface Index as defined in [RFC8664]."""

    remote_interface_id: int
    """Local Interface ID: The Interface Index as defined in [RFC8664]."""

    sr_mpls_sid: BgpSrteSrMplsSidParam
    """Optional SR-MPLS SID."""


class SegmentTypeH(TypedDict, total=False):
    local_ipv6_address: Required[str]
    """Local IPv6 Address."""

    remote_ipv6_address: Required[str]
    """Remote IPv6 Address."""

    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    sr_mpls_sid: BgpSrteSrMplsSidParam
    """Optional SR-MPLS SID."""


class SegmentTypeI(TypedDict, total=False):
    ipv6_node_address: Required[str]
    """IPv6 address representing a node."""

    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    srv6_sid: str
    """Optional SRv6 SID."""

    srv6_sid_endpoint_behavior: BgpSrteSRv6SidEndpointBehaviorAndStructureParam
    """Optional SRv6 Endpoint Behavior and SID Structure."""


class SegmentTypeJ(TypedDict, total=False):
    local_ipv6_node_address: Required[str]
    """IPv6 address representing a node."""

    remote_ipv6_node_address: Required[str]
    """IPv6 address representing a node."""

    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    local_interface_id: int
    """Local Interface ID: The Interface Index as defined in [RFC8664]."""

    remote_interface_id: int
    """Local Interface ID: The Interface Index as defined in [RFC8664]."""

    sr_algorithm: int
    """SR Algorithm identifier when A-Flag in on."""

    srv6_sid: str
    """Optional SRv6 SID."""

    srv6_sid_endpoint_behavior: BgpSrteSRv6SidEndpointBehaviorAndStructureParam
    """Optional SRv6 Endpoint Behavior and SID Structure."""


class SegmentTypeK(TypedDict, total=False):
    local_ipv6_address: Required[str]
    """IPv6 address representing a node."""

    remote_ipv6_address: Required[str]
    """IPv6 address representing a node."""

    flags: str
    """One octet bitmap for flags including V-Flag, A-Flag, S-Flag, B-Flag etc.

    as defined in
    https://datatracker.ietf.org/doc/html/draft-ietf-idr-segment-routing-te-policy-13#section-2.4.4.2.12
    """

    sr_algorithm: int
    """SR Algorithm identifier when A-Flag in on."""

    srv6_sid: str
    """Optional SRv6 SID."""

    srv6_sid_endpoint_behavior: BgpSrteSRv6SidEndpointBehaviorAndStructureParam
    """Optional SRv6 Endpoint Behavior and SID Structure."""


class Segment(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    segment_type: Required[
        Literal[
            "type_a", "type_b", "type_c", "type_d", "type_e", "type_f", "type_g", "type_h", "type_i", "type_j", "type_k"
        ]
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

    active: bool
    """
    If enabled means that this part of the configuration including any active
    'children' nodes will be advertised to peer. If disabled, this means that though
    config is present, it is not taking any part of the test but can be activated at
    run-time to advertise just this part of the configuration to the peer.
    """

    type_a: SegmentTypeA
    """Type A: SID only, in the form of MPLS Label."""

    type_b: SegmentTypeB
    """Type B: SID only, in the form of IPv6 address."""

    type_c: SegmentTypeC
    """Type C: IPv4 Node Address with optional SID."""

    type_d: SegmentTypeD
    """Type D: IPv6 Node Address with optional SID for SR MPLS."""

    type_e: SegmentTypeE
    """Type E: IPv4 Address and Local Interface ID with optional SID"""

    type_f: SegmentTypeF
    """Type F: IPv4 Local and Remote addresses with optional SID."""

    type_g: SegmentTypeG
    """
    Type G: IPv6 Address, Interface ID for local and remote pair with optional SID
    for SR MPLS.
    """

    type_h: SegmentTypeH
    """Type H: IPv6 Local and Remote addresses with optional SID for SR MPLS."""

    type_i: SegmentTypeI
    """Type I: IPv6 Node Address with optional SRv6 SID."""

    type_j: SegmentTypeJ
    """
    Type J: IPv6 Address, Interface ID for local and remote pair for SRv6 with
    optional SID.
    """

    type_k: SegmentTypeK
    """Type K: IPv6 Local and Remote addresses for SRv6 with optional SID."""


class BgpSrteSegmentListParam(TypedDict, total=False):
    name: Required[str]
    """Globally unique name of an object.

    It also serves as the primary key for arrays of objects.
    """

    active: bool
    """
    If enabled means that this part of the configuration including any active
    'children' nodes will be advertised to peer. If disabled, this means that though
    config is present, it is not taking any part of the test but can be activated at
    run-time to advertise just this part of the configuration to the peer.
    """

    segments: Iterable[Segment]

    weight: int
    """The Weight associated with a given path and the sub-TLV is optional."""
