# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OpenMessageErrorParam"]


class OpenMessageErrorParam(TypedDict, total=False):
    subcode: Literal[
        "unsupported_version_number_code2_subcode1",
        "error_peer_as_code2_subcode2",
        "error_bgp_id_code2_subcode3",
        "unsupported_optional_parameter_code2_subcode4",
        "auth_failed_code2_subcode5",
        "unsupported_hold_time_code2_subcode6",
        "unsupported_capability_code2_subcode7",
    ]
    """
    The Error Subcode indicates the specific type of error encountered during OPEN
    message processing.
    """
