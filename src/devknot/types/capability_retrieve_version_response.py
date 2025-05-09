# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CapabilityRetrieveVersionResponse"]


class CapabilityRetrieveVersionResponse(BaseModel):
    api_spec_version: Optional[str] = None
    """Version of API specification"""

    app_version: Optional[str] = None
    """Version of application consuming or serving the API"""

    sdk_version: Optional[str] = None
    """Version of SDK generated from API specification"""
