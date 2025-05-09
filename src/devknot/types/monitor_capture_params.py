# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MonitorCaptureParams"]


class MonitorCaptureParams(TypedDict, total=False):
    port_name: Required[str]
    """The name of a port a capture is started on.

    x-constraint:

    - /components/schemas/Port/properties/name
    """
