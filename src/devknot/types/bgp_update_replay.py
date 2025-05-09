# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .bgp_extended_community import BgpExtendedCommunity
from .bgp_attributes_next_hop import BgpAttributesNextHop
from .bgp_attributes_sid_mpls import BgpAttributesSidMpls
from .bgp_attributes_sid_srv6 import BgpAttributesSidSrv6
from .bgp_one_ipv4_nlri_prefix import BgpOneIpv4NlriPrefix
from .bgp_one_ipv6_nlri_prefix import BgpOneIpv6NlriPrefix
from .bgp_ipv4_sr_policy_nlri_prefix import BgpIpv4SrPolicyNlriPrefix
from .bgp_ipv6_sr_policy_nlri_prefix import BgpIpv6SrPolicyNlriPrefix
from .bgp_one_traditional_nlri_prefix import BgpOneTraditionalNlriPrefix
from .bgp_attributes_four_byte_as_path_segment import BgpAttributesFourByteAsPathSegment
from .bgp_attributes_segment_routing_policy_type_flags import BgpAttributesSegmentRoutingPolicyTypeFlags
from .bgp_attributes_segment_routing_policy_s_rv6_sid_endpoint_behavior_and_structure import (
    BgpAttributesSegmentRoutingPolicySRv6SidEndpointBehaviorAndStructure,
)

__all__ = [
    "BgpUpdateReplay",
    "RawBytes",
    "RawBytesUpdate",
    "StructuredPdus",
    "StructuredPdusUpdate",
    "StructuredPdusUpdatePathAttributes",
    "StructuredPdusUpdatePathAttributesAggregator",
    "StructuredPdusUpdatePathAttributesAsPath",
    "StructuredPdusUpdatePathAttributesAsPathFourByteAsPath",
    "StructuredPdusUpdatePathAttributesAsPathTwoByteAsPath",
    "StructuredPdusUpdatePathAttributesAsPathTwoByteAsPathSegment",
    "StructuredPdusUpdatePathAttributesAs4Aggregator",
    "StructuredPdusUpdatePathAttributesAs4Path",
    "StructuredPdusUpdatePathAttributesCommunity",
    "StructuredPdusUpdatePathAttributesCommunityCustomCommunity",
    "StructuredPdusUpdatePathAttributesLocalPreference",
    "StructuredPdusUpdatePathAttributesMpReach",
    "StructuredPdusUpdatePathAttributesMpUnreach",
    "StructuredPdusUpdatePathAttributesMultiExitDiscriminator",
    "StructuredPdusUpdatePathAttributesOriginatorID",
    "StructuredPdusUpdatePathAttributesOtherAttribute",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulation",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicy",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyBindingSegmentIdentifier",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyBindingSegmentIdentifierMpls",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyBindingSegmentIdentifierSrv6",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyExplicitNullLabelPolicy",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPolicyCandidateName",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPolicyName",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPreference",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPriority",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentList",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegment",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeA",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeB",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeC",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeD",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeE",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeF",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeG",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeH",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeI",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeJ",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeK",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListWeight",
    "StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySrv6BindingSegmentIdentifier",
]


class RawBytesUpdate(BaseModel):
    update_bytes: str
    """Bytes specified in hex format to be sent to peer after the BGP Update Header.

    The Update Header will always have the initial 16 bytes containing Marker bytes,
    2 bytes containing the Length and 1 byte containing the Type.The string MUST
    contain sequence of valid hex bytes. The bytes specified in hex format should be
    appended to the Update message to be sent to the peer after the fixed 19 bytes
    described above. This byte stream can be of any length from 1 to 4077 bytes.The
    value 4077 is derived from the maximum length allowed for a BGP message in
    RFC4271 which is 4096 minus mandatory 19 bytes described above. In the imported
    byte stream, one byte is represented as string of 2 characters, for example 2
    character string (0x)AB represents value of a single byte. So the maximum length
    of this attribute is 8154 (4077 \\** 2 hex characters per byte).
    """

    time_gap: Optional[int] = None
    """
    Minimum time interval in milliseconds from previous Update from the sequence of
    BGP Updates to be replayed.
    """


class RawBytes(BaseModel):
    updates: Optional[List[RawBytesUpdate]] = None
    """
    Array of ordered BGP Updates ( including both Advertise and Withdraws ) to be
    sent in the order given in the input to the peer after the BGP session is
    established.
    """


class StructuredPdusUpdatePathAttributesAggregator(BaseModel):
    choice: Optional[Literal["four_byte_as", "two_byte_as"]] = None

    four_byte_as: Optional[int] = None
    """The value of the 4 byte AS number of the BGP speaker which aggregated the route.

    If the value of the AS number is less than 2 octets ( 65535 or less), the
    AS4_AGGREGATOR object should not be sent.
    """

    ipv4_address: Optional[str] = None
    """The IPv4 address of the BGP speaker which aggregated the route."""

    two_byte_as: Optional[int] = None
    """
    The value of the 2 byte AS number of the BGP speaker which aggregated the route.
    """


class StructuredPdusUpdatePathAttributesAsPathFourByteAsPath(BaseModel):
    segments: Optional[List[BgpAttributesFourByteAsPathSegment]] = None
    """
    The AS path segments containing 4 byte AS numbers to be added in the AS Path
    attribute. By default, an empty AS path should always be included and for EBGP
    at minimum the local AS number should be present in the AS Path.
    """


class StructuredPdusUpdatePathAttributesAsPathTwoByteAsPathSegment(BaseModel):
    as_numbers: Optional[List[int]] = None
    """The 2 byte AS numbers in this AS path segment."""

    type: Optional[Literal["as_seq", "as_set", "as_confed_seq", "as_confed_set"]] = None
    """
    AS sequence is the most common type of AS_PATH, it contains the list of ASNs
    starting with the most recent ASN being added read from left to right. The other
    three AS_PATH types are used for Confederations

    - AS_SET is the type of AS_PATH attribute that summarizes routes using using the
      aggregate-address command, allowing AS_PATHs to be summarized in the update as
      well.
    - AS_CONFED_SEQ gives the list of ASNs in the path starting with the most recent
      ASN to be added reading left to right
    - AS_CONFED_SET will allow summarization of multiple AS PATHs to be sent in BGP
      Updates.
    """


class StructuredPdusUpdatePathAttributesAsPathTwoByteAsPath(BaseModel):
    segments: Optional[List[StructuredPdusUpdatePathAttributesAsPathTwoByteAsPathSegment]] = None
    """
    The AS path segments containing 2 byte AS numbers to be added in the AS Path
    attribute. By default, an empty AS path should always be included and for EBGP
    the sender's AS number should be prepended to the AS Path.
    """


class StructuredPdusUpdatePathAttributesAsPath(BaseModel):
    choice: Optional[Literal["four_byte_as_path", "two_byte_as_path"]] = None

    four_byte_as_path: Optional[StructuredPdusUpdatePathAttributesAsPathFourByteAsPath] = None
    """
    AS Paths with 4 byte AS numbers can be exchanged only if both BGP speakers
    support 4 byte AS number extensions.
    """

    two_byte_as_path: Optional[StructuredPdusUpdatePathAttributesAsPathTwoByteAsPath] = None
    """AS Paths with 2 byte AS numbers is used when any of the two scenarios occur :

    - An old BGP speaker and new BGP speaker are sending BGP Updates to one another.
    - Two old BGP speakers are sending BGP Updates to one another.
    """


class StructuredPdusUpdatePathAttributesAs4Aggregator(BaseModel):
    as_num: Optional[int] = None
    """
    The value of the 4 byte AS number of the BGP speaker which aggregated the route.
    """

    ipv4_address: Optional[str] = None
    """The IPv4 address of the BGP speaker which aggregated the route."""


class StructuredPdusUpdatePathAttributesAs4Path(BaseModel):
    segments: Optional[List[BgpAttributesFourByteAsPathSegment]] = None
    """
    The AS path segments containing 4 byte AS numbers to be added in the AS4_PATH
    attribute.
    """


class StructuredPdusUpdatePathAttributesCommunityCustomCommunity(BaseModel):
    as_number: Optional[int] = None
    """First two octets of the community value containing a 2 byte AS number."""

    custom: Optional[str] = None
    """Last two octets of the community value in hex.

    If user provides less than 4 hex bytes, it should be left-padded with 0s.
    """


class StructuredPdusUpdatePathAttributesCommunity(BaseModel):
    choice: Literal["custom_community", "no_export", "no_advertised", "no_export_subconfed", "llgr_stale", "no_llgr"]
    """The type of community AS number."""

    custom_community: Optional[StructuredPdusUpdatePathAttributesCommunityCustomCommunity] = None
    """
    User defined COMMUNITY attribute containing 2 byte AS and custom 2 byte value
    defined by the administrator of the domain.
    """


class StructuredPdusUpdatePathAttributesLocalPreference(BaseModel):
    value: Optional[int] = None
    """
    Value to be set in the LOCAL_PREFERENCE attribute The multi exit discriminator
    (MED) value used for route selection sent to the peer.
    """


class StructuredPdusUpdatePathAttributesMpReach(BaseModel):
    choice: Literal["ipv4_unicast", "ipv6_unicast", "ipv4_srpolicy", "ipv6_srpolicy"]
    """The AFI and SAFI to be sent in the MPREACH_NLRI in the Update."""

    ipv4_srpolicy: Optional[BgpIpv4SrPolicyNlriPrefix] = None
    """IPv4 endpoint with Segment Routing Policy being sent in the IPv4 MPREACH_NLRI ."""

    ipv4_unicast: Optional[List[BgpOneIpv4NlriPrefix]] = None
    """List of IPv4 prefixes being sent in the IPv4 Unicast MPREACH_NLRI ."""

    ipv6_srpolicy: Optional[BgpIpv6SrPolicyNlriPrefix] = None
    """IPv6 endpoint with Segment Routing Policy being sent in the IPv6 MPREACH_NLRI ."""

    ipv6_unicast: Optional[List[BgpOneIpv6NlriPrefix]] = None
    """List of IPv6 prefixes being sent in the IPv6 Unicast MPREACH_NLRI ."""

    next_hop: Optional[BgpAttributesNextHop] = None
    """
    Next hop to be sent inside MP_REACH NLRI or as the NEXT_HOP attribute if
    advertised as traditional NLRI.
    """


class StructuredPdusUpdatePathAttributesMpUnreach(BaseModel):
    choice: Optional[Literal["ipv4_unicast", "ipv6_unicast", "ipv4_srpolicy", "ipv6_srpolicy"]] = None
    """The AFI and SAFI to be sent in the MPUNREACH_NLRI in the Update."""

    ipv4_srpolicy: Optional[BgpIpv4SrPolicyNlriPrefix] = None
    """
    IPv4 endpoint with Segment Routing Policy being sent in the IPv4 MPUNREACH_NLRI
    .
    """

    ipv4_unicast: Optional[List[BgpOneIpv4NlriPrefix]] = None
    """List of IPv4 prefixes being sent in the IPv4 Unicast MPUNREACH_NLRI ."""

    ipv6_srpolicy: Optional[BgpIpv6SrPolicyNlriPrefix] = None
    """
    IPv6 endpoint with Segment Routing Policy being sent in the IPv4 MPUNREACH_NLRI
    .
    """

    ipv6_unicast: Optional[List[BgpOneIpv6NlriPrefix]] = None
    """List of IPv6 prefixes being sent in the IPv6 Unicast MPUNREACH_NLRI ."""


class StructuredPdusUpdatePathAttributesMultiExitDiscriminator(BaseModel):
    value: Optional[int] = None
    """
    The multi exit discriminator (MED) value used for route selection sent to the
    peer.
    """


class StructuredPdusUpdatePathAttributesOriginatorID(BaseModel):
    value: Optional[str] = None
    """The value of the originator's Router Id."""


class StructuredPdusUpdatePathAttributesOtherAttribute(BaseModel):
    raw_value: str
    """
    Contents of the value field ( the contents after the initial two bytes
    containing the Flags and Type field ) of the attribute in hex bytes. It includes
    the contents of length of the extended length field if included.
    """

    type: int
    """The value of the Type field in the attribute."""

    flag_extended_length: Optional[bool] = None
    """Extended length flag in the BGP attribute."""

    flag_optional: Optional[bool] = None
    """Optional flag in the BGP attribute."""

    flag_partial: Optional[bool] = None
    """Partial flag in the BGP attribute."""

    flag_transitive: Optional[bool] = None
    """Transitive flag in the BGP attribute."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyBindingSegmentIdentifierMpls(BaseModel):
    flag_drop_upon_invalid: Optional[bool] = None
    """I-Flag: This flag encodes the "Drop Upon Invalid" behavior.

    It's usage is described in section 8.2 in [RFC9256].
    """

    flag_specified_bsid_only: Optional[bool] = None
    """S-Flag: This flag encodes the "Specified-BSID-only" behavior.

    It's usage is described in section 6.2.3 in [RFC9256].
    """

    mpls_sid: Optional[BgpAttributesSidMpls] = None
    """
    This carries a 20 bit Multi Protocol Label Switching alongwith 3 bits traffic
    class, 1 bit indicating presence or absence of Bottom-Of-Stack and 8 bits
    carrying the Time to Live value.
    """


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyBindingSegmentIdentifierSrv6(BaseModel):
    flag_drop_upon_invalid: Optional[bool] = None
    """I-Flag: This flag encodes the "Drop Upon Invalid" behavior.

    It's usage is described in section 8.2 in [RFC9256].
    """

    flag_specified_bsid_only: Optional[bool] = None
    """S-Flag: This flag encodes the "Specified-BSID-only" behavior.

    It's usage is described in section 6.2.3 in [RFC9256].
    """

    ipv6_addr: Optional[str] = None
    """IPv6 address denoting the SRv6 SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyBindingSegmentIdentifier(BaseModel):
    choice: Literal["mpls", "srv6"]
    """The type of Segment Identifier."""

    mpls: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyBindingSegmentIdentifierMpls] = None
    """
    When the active candidate path has a specified Binding Segment Identifier, the
    SR Policy uses that BSID defined as a MPLS label.The format of the sub-TLV is
    defined in draft-ietf-idr-sr-policy-safi-02 Section 2.4.2 .
    """

    srv6: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyBindingSegmentIdentifierSrv6] = None
    """
    When the active candidate path has a specified Binding Segment Identifier, the
    SR Policy uses that BSID defined as an IPv6 Address.The format of the sub-TLV is
    defined in draft-ietf-idr-sr-policy-safi-02 Section 2.4.2 .
    """


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyExplicitNullLabelPolicy(BaseModel):
    choice: Optional[Literal["unknown", "push_ipv4", "push_ipv6", "push_ipv4_and_ipv6", "donot_push"]] = None
    """The Explicit NULL Label policy."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPolicyCandidateName(BaseModel):
    value: str
    """
    Value of the symbolic Policy Candidate Path Name carried in the Policy Candidate
    Path Name sub-tlv. It is recommended that the size of the name is limited to 255
    bytes.
    """


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPolicyName(BaseModel):
    value: str
    """
    Value of the symbolic policy name carried in the Policy Name sub-tlv. It is
    recommended that the size of the name is limited to 255 bytes.
    """


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPreference(BaseModel):
    value: Optional[int] = None
    """Value to be carried in the Preference sub-tlv."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPriority(BaseModel):
    value: Optional[int] = None
    """Value to be carried in the Priority sub-tlv."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeA(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    mpls_sid: Optional[BgpAttributesSidMpls] = None
    """
    This carries a 20 bit Multi Protocol Label Switching alongwith 3 bits traffic
    class, 1 bit indicating presence or absence of Bottom-Of-Stack and 8 bits
    carrying the Time to Live value.
    """


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeB(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    srv6_endpoint_behavior: Optional[BgpAttributesSegmentRoutingPolicySRv6SidEndpointBehaviorAndStructure] = None
    """Configuration for optional SRv6 Endpoint Behavior and SID Structure.

    Summation of lengths for Locator Block, Locator Node, Function, and Argument
    MUST be less than or equal to 128. - This is specified in
    draft-ietf-idr-sr-policy-safi-02 Section 2.4.4.2.4
    """

    srv6_sid: Optional[str] = None
    """SRv6 SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeC(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    ipv4_node_address: Optional[str] = None
    """IPv4 address representing a node."""

    sr_algorithm: Optional[int] = None
    """SR Algorithm identifier when A-Flag in on.

    If A-flag is not enabled, it should be set to 0 on transmission and ignored on
    receipt.
    """

    sr_mpls_sid: Optional[BgpAttributesSidMpls] = None
    """Optional SR-MPLS SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeD(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    ipv6_node_address: Optional[str] = None
    """IPv6 address representing a node."""

    sr_algorithm: Optional[int] = None
    """SR Algorithm identifier when A-Flag in on.

    If A-flag is not enabled, it should be set to 0 on transmission and ignored on
    receipt.
    """

    sr_mpls_sid: Optional[BgpAttributesSidMpls] = None
    """Optional SR-MPLS SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeE(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    ipv4_node_address: Optional[str] = None
    """IPv4 address representing a node."""

    local_interface_id: Optional[int] = None
    """The Interface Index as defined in [RFC8664]."""

    sr_mpls_sid: Optional[BgpAttributesSidMpls] = None
    """Optional SR-MPLS SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeF(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    local_ipv4_address: Optional[str] = None
    """Local IPv4 Address."""

    remote_ipv4_address: Optional[str] = None
    """Remote IPv4 Address."""

    sr_mpls_sid: Optional[BgpAttributesSidMpls] = None
    """Optional SR-MPLS SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeG(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    local_interface_id: Optional[int] = None
    """The local Interface Index as defined in [RFC8664]."""

    local_ipv6_node_address: Optional[str] = None
    """The IPv6 address representing the local node."""

    remote_interface_id: Optional[int] = None
    """The remote Interface Index as defined in [RFC8664].

    The value MAY be set to zero when the local node address and interface
    identifiers are sufficient to describe the link.
    """

    remote_ipv6_node_address: Optional[str] = None
    """IPv6 address representing the remote node.

    The value MAY be set to zero when the local node address and interface
    identifiers are sufficient to describe the link.
    """

    sr_mpls_sid: Optional[BgpAttributesSidMpls] = None
    """Optional SR-MPLS SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeH(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    local_ipv6_address: Optional[str] = None
    """Local IPv6 Address."""

    remote_ipv6_address: Optional[str] = None
    """Remote IPv6 Address."""

    sr_mpls_sid: Optional[BgpAttributesSidMpls] = None
    """Optional SR-MPLS SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeI(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    ipv6_node_address: Optional[str] = None
    """IPv6 address representing a node."""

    sr_algorithm: Optional[int] = None
    """SR Algorithm identifier when A-Flag in on.

    If A-flag is not enabled, it should be set to 0 on transmission and ignored on
    receipt.
    """

    srv6_endpoint_behavior: Optional[BgpAttributesSegmentRoutingPolicySRv6SidEndpointBehaviorAndStructure] = None
    """Configuration for optional SRv6 Endpoint Behavior and SID Structure.

    Summation of lengths for Locator Block, Locator Node, Function, and Argument
    MUST be less than or equal to 128. - This is specified in
    draft-ietf-idr-sr-policy-safi-02 Section 2.4.4.2.4
    """

    srv6_sid: Optional[BgpAttributesSidSrv6] = None
    """An IPv6 address denoting a SRv6 SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeJ(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    local_interface_id: Optional[int] = None
    """The local Interface Index as defined in [RFC8664]."""

    local_ipv6_node_address: Optional[str] = None
    """The IPv6 address representing the local node."""

    remote_interface_id: Optional[int] = None
    """The remote Interface Index as defined in [RFC8664].

    The value MAY be set to zero when the local node address and interface
    identifiers are sufficient to describe the link.
    """

    remote_ipv6_node_address: Optional[str] = None
    """IPv6 address representing the remote node.

    The value MAY be set to zero when the local node address and interface
    identifiers are sufficient to describe the link.
    """

    sr_algorithm: Optional[int] = None
    """SR Algorithm identifier when A-Flag in on.

    If A-flag is not enabled, it should be set to 0 on transmission and ignored on
    receipt.
    """

    srv6_endpoint_behavior: Optional[BgpAttributesSegmentRoutingPolicySRv6SidEndpointBehaviorAndStructure] = None
    """Configuration for optional SRv6 Endpoint Behavior and SID Structure.

    Summation of lengths for Locator Block, Locator Node, Function, and Argument
    MUST be less than or equal to 128. - This is specified in
    draft-ietf-idr-sr-policy-safi-02 Section 2.4.4.2.4
    """

    srv6_sid: Optional[BgpAttributesSidSrv6] = None
    """An IPv6 address denoting a SRv6 SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeK(BaseModel):
    flags: Optional[BgpAttributesSegmentRoutingPolicyTypeFlags] = None
    """Flags for each Segment in SEGMENT_LIST sub-tlv.

    - V-flag. Indicates verification is enabled. See section 5, of
      https://datatracker.ietf.org/doc/html/rfc9256
    - A-flag. Indicates presence of SR Algorithm field applicable to Segment Types
      C, D , I , J and K .
    - B-Flag. Indicates presence of SRv6 Endpoint Behavior and SID Structure
      encoding applicable to Segment Types B , I , J and K .
    - S-Flag: This flag, when set, indicates the presence of the SR-MPLS or SRv6 SID
      depending on the segment type. (draft-ietf-idr-bgp-sr-segtypes-ext-03 Section
      2.10). This flag is applicable for Segment Types C, D, E, F, G, H, I, J, and
      K.
    """

    local_ipv6_address: Optional[str] = None
    """Local IPv6 Address."""

    remote_ipv6_address: Optional[str] = None
    """Remote IPv6 Address."""

    sr_algorithm: Optional[int] = None
    """SR Algorithm identifier when A-Flag in on.

    If A-flag is not enabled, it should be set to 0 on transmission and ignored on
    receipt.
    """

    srv6_endpoint_behavior: Optional[BgpAttributesSegmentRoutingPolicySRv6SidEndpointBehaviorAndStructure] = None
    """Configuration for optional SRv6 Endpoint Behavior and SID Structure.

    Summation of lengths for Locator Block, Locator Node, Function, and Argument
    MUST be less than or equal to 128. - This is specified in
    draft-ietf-idr-sr-policy-safi-02 Section 2.4.4.2.4
    """

    srv6_sid: Optional[BgpAttributesSidSrv6] = None
    """An IPv6 address denoting a SRv6 SID."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegment(BaseModel):
    choice: Literal[
        "type_a", "type_b", "type_c", "type_d", "type_e", "type_f", "type_g", "type_h", "type_i", "type_j", "type_k"
    ]
    """
    Specify one of the segment types as defined in
    ietf-idr-segment-routing-te-policy

    - Type A: SID only, in the form of MPLS Label.
    - Type B: SID only, in the form of IPv6 Address.
    - Type C: IPv4 Prefix with optional SR Algorithm.
    - Type D: IPv6 Global Prefix with optional SR Algorithm for SR-MPLS.
    - Type E: IPv4 Prefix with Local Interface ID.
    - Type F: IPv4 Addresses for link endpoints as Local, Remote pair.
    - Type G: IPv6 Prefix and Interface ID for link endpoints as Local, Remote pair
      for SR-MPLS.
    - Type H: IPv6 Addresses for link endpoints as Local, Remote pair for SR-MPLS.
    - Type I: IPv6 Global Prefix with optional SR Algorithm for SRv6.
    - Type J: IPv6 Prefix and Interface ID for link endpoints as Local, Remote pair
      for SRv6.
    - Type K: IPv6 Addresses for link endpoints as Local, Remote pair for SRv6.
    """

    type_a: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeA] = None
    """
    Type A: SID only, in the form of MPLS Label. It is encoded as a Segment of Type
    1 in the SEGMENT_LIST sub-tlv.
    """

    type_b: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeB] = None
    """
    Type B: SID only, in the form of IPv6 address. It is encoded as a Segment of
    Type 13 in the SEGMENT_LIST sub-tlv.
    """

    type_c: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeC] = None
    """
    Type C: IPv4 Node Address with optional SID. It is encoded as a Segment of Type
    3 in the SEGMENT_LIST sub-tlv.
    """

    type_d: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeD] = None
    """
    Type D: IPv6 Node Address with optional SID for SR MPLS. It is encoded as a
    Segment of Type 4 in the SEGMENT_LIST sub-tlv.
    """

    type_e: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeE] = None
    """
    Type E: IPv4 Address and Local Interface ID with optional SID It is encoded as a
    Segment of Type 5 in the SEGMENT_LIST sub-tlv.
    """

    type_f: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeF] = None
    """
    Type F: IPv4 Local and Remote addresses with optional SR-MPLS SID. It is encoded
    as a Segment of Type 6 in the SEGMENT_LIST sub-tlv.
    """

    type_g: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeG] = None
    """
    Type G: IPv6 Address, Interface ID for local and remote pair with optional SID
    for SR MPLS. It is encoded as a Segment of Type 7 in the SEGMENT_LIST sub-tlv.
    """

    type_h: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeH] = None
    """
    Type H: IPv6 Local and Remote addresses with optional SID for SR MPLS. It is
    encoded as a Segment of Type 8 in the SEGMENT_LIST sub-tlv.
    """

    type_i: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeI] = None
    """
    Type I: IPv6 Node Address with optional SR Algorithm and optional SRv6 SID. It
    is encoded as a Segment of Type 14 in the SEGMENT_LIST sub-tlv.
    """

    type_j: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeJ] = None
    """
    Type J: IPv6 Address, Interface ID for local and remote pair for SRv6 with
    optional SID. It is encoded as a Segment of Type 15 in the SEGMENT_LIST sub-tlv.
    """

    type_k: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegmentTypeK] = None
    """
    Type K: IPv6 Local and Remote addresses for SRv6 with optional SID. It is
    encoded as a Segment of Type 16 in the SEGMENT_LIST sub-tlv.
    """


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListWeight(BaseModel):
    value: Optional[int] = None
    """Value of the weight."""


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentList(BaseModel):
    segments: Optional[List[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListSegment]] = None

    weight: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentListWeight] = None
    """
    The optional Weight sub-TLV (Type 9) specifies the weight associated with a
    given segment list. The weight is used for weighted multipath.
    """


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySrv6BindingSegmentIdentifier(BaseModel):
    flag_drop_upon_invalid: Optional[bool] = None
    """I-Flag: This flag encodes the "Drop Upon Invalid" behavior.

    It's usage is described in section 8.2 in [RFC9256].
    """

    flag_specified_bsid_only: Optional[bool] = None
    """S-Flag: This flag encodes the "Specified-BSID-only" behavior.

    It's usage is described in section 6.2.3 in [RFC9256].
    """

    flag_srv6_endpoint_behavior: Optional[bool] = None
    """
    B-Flag: This flag, when set, indicates the presence of the SRv6 Endpoint
    Behavior and SID Structure encoding specified in Section 2.4.4.2.4 of
    draft-ietf-idr-sr-policy-safi-02.
    """

    ipv6_addr: Optional[str] = None
    """IPv6 address denoting the SRv6 SID."""

    srv6_endpoint_behavior: Optional[BgpAttributesSegmentRoutingPolicySRv6SidEndpointBehaviorAndStructure] = None
    """Configuration for optional SRv6 Endpoint Behavior and SID Structure.

    Summation of lengths for Locator Block, Locator Node, Function, and Argument
    MUST be less than or equal to 128. - This is specified in
    draft-ietf-idr-sr-policy-safi-02 Section 2.4.4.2.4
    """


class StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicy(BaseModel):
    binding_segment_identifier: Optional[
        StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyBindingSegmentIdentifier
    ] = None
    """
    The Binding Segment Identifier is an optional sub-tlv of type 13 that can be
    sent with a SR Policy Tunnel Encapsulation attribute. When the active candidate
    path has a specified Binding Segment Identifier, the SR Policy uses that BSID if
    this value (label in MPLS, IPv6 address in SRv6) is available.

    - The format of the sub-TLV is defined in draft-ietf-idr-sr-policy-safi-02
      Section 2.4.2 .
    - It is recommended that if SRv6 Binding SID is desired to be signalled, the
      SRv6 Binding SID sub-TLV that enables the specification of the SRv6 Endpoint
      Behavior should be used.
    """

    explicit_null_label_policy: Optional[
        StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyExplicitNullLabelPolicy
    ] = None
    """
    This is an optional sub-tlv (Type 14) which indicates whether an Explicit NULL
    Label must be pushed on an unlabeled IP packet before other labels for IPv4 or
    IPv6 flows.

    - It is defined in Section 2.4.5 of draft-ietf-idr-sr-policy-safi-02.
    """

    policy_candidate_name: Optional[
        StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPolicyCandidateName
    ] = None
    """
    Optional Policy Candidate Path Name sub-tlv (Type 129) which carries the
    symbolic name for the SR Policy candidate path for debugging.

    - It is defined in Section 2.4.7 of draft-ietf-idr-sr-policy-safi-02 .
    """

    policy_name: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPolicyName] = None
    """
    Optional Policy Name sub-tlv (Type 130) which carries the symbolic name for the
    SR Policy for which the candidate path is being advertised for debugging.

    - It is defined in Section 2.4.8 of draft-ietf-idr-sr-policy-safi-02 .
    """

    preference: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPreference] = None
    """
    Optional Preference sub-tlv (Type 12) is used to select the best candidate path
    for an SR Policy. It is defined in Section 2.4.1 of
    draft-ietf-idr-sr-policy-safi-02 .
    """

    priority: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicyPriority] = None
    """
    Optional Priority sub-tlv (Type 15) used to select the order in which policies
    should be re-computed.

    - It is defined in Section 2.4.6 of draft-ietf-idr-sr-policy-safi-02 .
    """

    segment_list: Optional[List[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySegmentList]] = None

    srv6_binding_segment_identifier: Optional[
        List[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicySrv6BindingSegmentIdentifier]
    ] = None
    """
    The SRv6 Binding SID sub-TLV is an optional sub-TLV of type 20 that is used to
    signal the SRv6 Binding SID related information of an SR Policy candidate path.

    - More than one SRv6 Binding SID sub-TLVs MAY be signaled in the same SR Policy
      encoding to indicate one or more SRv6 SIDs, each with potentially different
      SRv6 Endpoint Behaviors to be instantiated.
    - The format of the sub-TLV is defined in draft-ietf-idr-sr-policy-safi-02
      Section 2.4.3 .
    """


class StructuredPdusUpdatePathAttributesTunnelEncapsulation(BaseModel):
    choice: Optional[Literal["sr_policy"]] = None
    """Identifies a type of tunnel.

    The field contains values from the IANA registry "BGP Tunnel Encapsulation
    Attribute Tunnel Types".
    """

    sr_policy: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulationSrPolicy] = None
    """
    Optional Segment Routing Policy information as defined in
    draft-ietf-idr-sr-policy-safi-02. This information is carried in
    TUNNEL_ENCAPSULATION attribute with type set to SR Policy (15).
    """


class StructuredPdusUpdatePathAttributes(BaseModel):
    aggregator: Optional[StructuredPdusUpdatePathAttributesAggregator] = None
    """
    Optional AGGREGATOR attribute which maybe be added by a BGP speaker which
    performs route aggregation. When AGGREGATOR attribute is being sent to a new BGP
    speaker , the AS number is encoded as a 4 byte value. When AGGREGATOR attribute
    is being exchanged between a new and an old BGP speaker or between two old BGP
    speakers, the AS number is encoded as a 2 byte value. It contain the AS number
    and IP address of the speaker performing the aggregation.
    """

    as_path: Optional[StructuredPdusUpdatePathAttributesAsPath] = None
    """AS_PATH attribute to be included in the Update."""

    as4_aggregator: Optional[StructuredPdusUpdatePathAttributesAs4Aggregator] = None
    """
    Optional AS4_AGGREGATOR attribute which maybe be added by a BGP speaker in one
    of two cases:

    - If it is a new BGP speaker speaking to an old BGP speaker and needs to send a
      4 byte value for the AS number of the BGP route aggregator.
    - If it is a old BGP speaker speaking to a new BGP speaker and has to
      transparently forward a received AS4_AGGREGATOR from some other peer. Its
      usage is described in RFC4893.
    """

    as4_path: Optional[StructuredPdusUpdatePathAttributesAs4Path] = None
    """AS4_PATH attribute to be included in the Update."""

    cluster_ids: Optional[List[str]] = None
    """
    When a Route Reflector reflects a route, it prepends the local CLUSTER_ID to the
    CLUSTER_LIST as defined in RFC4456.
    """

    community: Optional[List[StructuredPdusUpdatePathAttributesCommunity]] = None

    extended_communities: Optional[List[BgpExtendedCommunity]] = None
    """
    Optional EXTENDED_COMMUNITY attribute settings. The EXTENDED_COMMUNITY Attribute
    is a transitive optional BGP attribute, with the Type Code 16. Community and
    Extended Communities attributes are utilized to trigger routing decisions, such
    as acceptance, rejection, preference, or redistribution. An extended community
    is an eight byte value. It is divided into two main parts. The first two bytes
    of the community encode a type and sub-type fields and the last six bytes carry
    a unique set of data in a format defined by the type and sub-type field.
    Extended communities provide a larger range for grouping or categorizing
    communities.
    """

    include_atomic_aggregator: Optional[bool] = None
    """
    If enabled, it indicates that the ATOMIC_AGGREGATOR attribute should be included
    in the Update. Presence of this attribute Indicates that this route might not be
    getting sent on a fully optimized path since some intermediate BGP speaker has
    aggregated the route.
    """

    local_preference: Optional[StructuredPdusUpdatePathAttributesLocalPreference] = None
    """
    Optional LOCAL_PREFERENCE attribute sent to the peer to indicate the degree of
    preference for externally learned routes.This should be included only for
    internal peers.It is used for the selection of the path for the traffic leaving
    the AS.The route with the highest local preference value is preferred.
    """

    mp_reach: Optional[StructuredPdusUpdatePathAttributesMpReach] = None
    """
    The MP_REACH attribute is an optional attribute which can be included in the
    attributes of a BGP Update message as defined in
    https://datatracker.ietf.org/doc/html/rfc4760#section-3. The following AFI /
    SAFI combinations are supported:

    - IPv4 Unicast with AFI as 1 and SAFI as 1
    - IPv6 Unicast with AFI as 2 and SAFI as 1
    - Segment Routing Policy for IPv4 Unicast with AFI as 1 and SAFI as 73 (
      draft-ietf-idr-sr-policy-safi-02 Section 2.1 )
    - Segment Routing Policy for IPv6 Unicast with AFI as 2 and SAFI as 73
    """

    mp_unreach: Optional[StructuredPdusUpdatePathAttributesMpUnreach] = None
    """
    The MP_UNREACH attribute is an optional attribute which can be included in the
    attributes of a BGP Update message as defined in
    https://datatracker.ietf.org/doc/html/rfc4760#section-3. The following AFI /
    SAFI combinations are supported:

    - IPv4 Unicast with AFI as 1 and SAFI as 1
    - IPv6 Unicast with AFI as 2 and SAFI as 1
    - Segment Routing Policy for IPv4 Unicast with AFI as 1 and SAFI as 73
      (draft-ietf-idr-sr-policy-safi-02 Section 2.1)
    - Segment Routing Policy for IPv6 Unicast with AFI as 2 and SAFI as 73
    """

    multi_exit_discriminator: Optional[StructuredPdusUpdatePathAttributesMultiExitDiscriminator] = None
    """
    Optional MULTI_EXIT_DISCRIMINATOR attribute sent to the peer to help in the
    route selection process.
    """

    next_hop: Optional[BgpAttributesNextHop] = None
    """
    Next hop to be sent inside MP_REACH NLRI or as the NEXT_HOP attribute if
    advertised as traditional NLRI.
    """

    origin: Optional[Literal["igp", "egp", "incomplete"]] = None
    """
    The ORIGIN attribute is a mandatory attribute which can take three values: the
    prefix originates from an interior routing protocol 'igp', it originates from
    'egp' or the origin is 'incomplete',if the prefix is learned through other
    means.
    """

    originator_id: Optional[StructuredPdusUpdatePathAttributesOriginatorID] = None
    """
    Optional ORIGINATOR_ID attribute (type code 9) carries the Router Id of the
    route's originator in the local AS.
    """

    other_attributes: Optional[List[StructuredPdusUpdatePathAttributesOtherAttribute]] = None
    """
    Any attributes not present in the list of configurable attributes should be
    added to the list of unknown attributes.
    """

    tunnel_encapsulation: Optional[StructuredPdusUpdatePathAttributesTunnelEncapsulation] = None
    """
    The TUNNEL_ENCAPSULATION attribute is used by a BGP speaker to inform other BGP
    speakers how to encapsulate packets that need to be sent to it. It is defined in
    RFC9012 and is assigned a Type code of 23.
    """


class StructuredPdusUpdate(BaseModel):
    path_attributes: Optional[StructuredPdusUpdatePathAttributes] = None
    """Attributes carried in the Update packet alongwith the reach/unreach prefixes."""

    time_gap: Optional[int] = None
    """
    Minimum time interval in milliseconds from previous Update from the sequence of
    BGP Updates to be replayed.
    """

    traditional_reach_nlris: Optional[List[BgpOneTraditionalNlriPrefix]] = None
    """The IPv4 prefixes to be included in the traditional REACH_NLRI."""

    traditional_unreach_nlris: Optional[List[BgpOneTraditionalNlriPrefix]] = None
    """The IPv4 prefixes to be included in the traditional UNREACH_NLRI."""


class StructuredPdus(BaseModel):
    updates: Optional[List[StructuredPdusUpdate]] = None
    """
    Array of ordered BGP Updates ( including both Advertise and Withdraws ) to be
    sent in the order given in the input to the peer after the BGP session is
    established.
    """


class BgpUpdateReplay(BaseModel):
    choice: Optional[Literal["structured_pdus", "raw_bytes"]] = None

    raw_bytes: Optional[RawBytes] = None
    """
    Ordered BGP Updates ( including both Advertise and Withdraws ) to be sent in the
    order given in the input to the peer after the BGP session is established.
    """

    structured_pdus: Optional[StructuredPdus] = None
    """
    Ordered BGP Updates ( including both Advertise and Withdraws ) to be sent in the
    order given in the input to the peer after the BGP session is established.
    """
