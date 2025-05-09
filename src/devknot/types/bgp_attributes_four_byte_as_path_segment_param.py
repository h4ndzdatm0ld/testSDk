# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["BgpAttributesFourByteAsPathSegmentParam"]


class BgpAttributesFourByteAsPathSegmentParam(TypedDict, total=False):
    as_numbers: Iterable[int]
    """The 4 byte AS numbers in this AS path segment."""

    type: Literal["as_seq", "as_set", "as_confed_seq", "as_confed_set"]
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
