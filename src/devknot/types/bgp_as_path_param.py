# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["BgpAsPathParam", "Segment"]


class Segment(TypedDict, total=False):
    as_numbers: Iterable[int]
    """The AS numbers in this AS path segment."""

    type: Literal["as_seq", "as_set", "as_confed_seq", "as_confed_set"]
    """
    AS sequence is the most common type of AS_PATH, it contains the list of ASNs
    starting with the most recent ASN being added read from left to right. The other
    three AS_PATH types are used for Confederations - AS_SET is the type of AS_PATH
    attribute that summarizes routes using using the aggregate-address command,
    allowing AS_PATHs to be summarized in the update as well. - AS_CONFED_SEQ gives
    the list of ASNs in the path starting with the most recent ASN to be added
    reading left to right - AS_CONFED_SET will allow summarization of multiple AS
    PATHs to be sent in BGP Updates.
    """


class BgpAsPathParam(TypedDict, total=False):
    as_set_mode: Literal[
        "do_not_include_local_as",
        "include_as_seq",
        "include_as_set",
        "include_as_confed_seq",
        "include_as_confed_set",
        "prepend_to_first_segment",
    ]
    """Defines how the Local AS should be included in the MP REACH NLRI.

    For iBGP sessions, "Do Not Include Local AS" must be chosen. For eBGP sessions,
    any choice other than "Do Not Include Local AS" can be chosen.
    """

    segments: Iterable[Segment]
    """The additional AS path segments to be added in the NLRI.

    By default, an empty AS path is always included and the local AS is added to it
    as per the value of 'as_set_mode' attribute.
    """
