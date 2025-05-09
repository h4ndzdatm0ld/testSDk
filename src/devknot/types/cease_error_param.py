# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CeaseErrorParam"]


class CeaseErrorParam(TypedDict, total=False):
    subcode: Literal[
        "max_number_prefix_reached_code6_subcode1",
        "admin_shutdown_code6_subcode2",
        "peer_deleted_code6_subcode3",
        "admin_reset_code6_subcode4",
        "connection_reject_code6_subcode5",
        "other_config_changes_code6_subcode6",
        "connection_collision_resolution_code6_subcode7",
        "out_of_resources_code6_subcode8",
        "bfd_session_down_code6_subcode10",
        "hard_reset_code6_subcode9",
    ]
    """The Error Subcode to be sent to the peer in the Cease NOTIFICATION."""
