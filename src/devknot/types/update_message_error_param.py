# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["UpdateMessageErrorParam"]


class UpdateMessageErrorParam(TypedDict, total=False):
    subcode: Literal[
        "malformed_attrib_list_code3_subcode1",
        "unrecognized_wellknown_attrib_code3_subcode2",
        "wellknown_attrib_missing_code3_subcode3",
        "attrib_flags_error_code3_subcode4",
        "attrib_length_error_code3_subcode5",
        "invalid_origin_attrib_code3_subcode6",
        "as_routing_loop_code3_subcode7",
        "invalid_nhop_attrib_code3_subcode8",
        "error_optional_attrib_code3_subcode9",
        "invalid_network_field_code3_subcode10",
        "abnormal_aspath_code3_subcode11",
    ]
    """
    The Error Subcode, the specific type of error encountered during UPDATE
    processing.
    """
