# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FlowRsvpLspTunnelFlag"]


class FlowRsvpLspTunnelFlag(BaseModel):
    choice: Optional[Literal["local_protection_desired", "label_recording_desired", "se_style_desired"]] = None
