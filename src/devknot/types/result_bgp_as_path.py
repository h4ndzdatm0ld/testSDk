# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ResultBgpAsPath", "Segment"]


class Segment(BaseModel):
    as_numbers: Optional[List[int]] = None
    """The AS numbers in this AS path segment."""

    type: Optional[Literal["as_seq", "as_set", "as_confed_seq", "as_confed_set"]] = None
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


class ResultBgpAsPath(BaseModel):
    segments: Optional[List[Segment]] = None
    """AS Path segments present in the received AS Path attribute."""
