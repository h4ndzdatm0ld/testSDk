# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

from .flow_snmpv2c_variable_binding_param import FlowSnmpv2cVariableBindingParam
from .pattern_flow_snmpv2c_pdu_request_id_counter_param import PatternFlowSnmpv2cPduRequestIDCounterParam
from .pattern_flow_snmpv2c_pdu_error_index_counter_param import PatternFlowSnmpv2cPduErrorIndexCounterParam

__all__ = ["FlowSnmpv2cPduParam", "ErrorIndex", "RequestID"]


class ErrorIndex(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cPduErrorIndexCounterParam
    """integer counter pattern"""

    increment: PatternFlowSnmpv2cPduErrorIndexCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class RequestID(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cPduRequestIDCounterParam
    """integer counter pattern"""

    increment: PatternFlowSnmpv2cPduRequestIDCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class FlowSnmpv2cPduParam(TypedDict, total=False):
    error_index: ErrorIndex
    """
    When Error Status is non-zero, this field contains a pointer that specifies
    which object generated the error. Always zero in a request.
    """

    error_status: Literal[
        "no_error",
        "too_big",
        "no_such_name",
        "bad_value",
        "read_only",
        "gen_err",
        "no_access",
        "wrong_type",
        "wrong_length",
        "wrong_encoding",
        "wrong_value",
        "no_creation",
        "inconsistent_value",
        "resource_unavailable",
        "commit_failed",
        "undo_failed",
        "authorization_error",
        "not_writable",
        "inconsistent_name",
    ]
    """
    The SNMP agent places an error code in this field in the response message if an
    error occurred processing the request.
    """

    request_id: RequestID
    """Identifies a particular SNMP request.

    This index is echoed back in the response from the SNMP agent, allowing the SNMP
    manager to match an incoming response to the appropriate request.

    - Encoding of this field follows ASN.1 X.690(section 8.3) specification. Refer:
      http://www.itu.int/ITU-T/asn1/
    """

    variable_bindings: Iterable[FlowSnmpv2cVariableBindingParam]
    """A Sequence of variable_bindings."""
