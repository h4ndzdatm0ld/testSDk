# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MessageHeaderErrorParam"]


class MessageHeaderErrorParam(TypedDict, total=False):
    subcode: Literal[
        "connection_not_synchronized_code1_subcode1",
        "bad_message_length_code1_subcode2",
        "bad_message_type_code1_subcode3",
    ]
    """
    The Error Subcode indicates the specific type of error encountered during
    Message Header processing.
    """
