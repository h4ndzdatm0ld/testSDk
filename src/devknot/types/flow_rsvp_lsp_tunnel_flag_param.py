# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FlowRsvpLspTunnelFlagParam"]


class FlowRsvpLspTunnelFlagParam(TypedDict, total=False):
    choice: Literal["local_protection_desired", "label_recording_desired", "se_style_desired"]
