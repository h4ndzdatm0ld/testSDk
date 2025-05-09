# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .flow_snmpv2c_variable_binding import FlowSnmpv2cVariableBinding
from .pattern_flow_snmpv2c_pdu_request_id_counter import PatternFlowSnmpv2cPduRequestIDCounter
from .pattern_flow_snmpv2c_pdu_error_index_counter import PatternFlowSnmpv2cPduErrorIndexCounter

__all__ = ["FlowSnmpv2cPdu", "ErrorIndex", "RequestID"]


class ErrorIndex(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cPduErrorIndexCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowSnmpv2cPduErrorIndexCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class RequestID(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cPduRequestIDCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowSnmpv2cPduRequestIDCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class FlowSnmpv2cPdu(BaseModel):
    error_index: Optional[ErrorIndex] = None
    """
    When Error Status is non-zero, this field contains a pointer that specifies
    which object generated the error. Always zero in a request.
    """

    error_status: Optional[
        Literal[
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
    ] = None
    """
    The SNMP agent places an error code in this field in the response message if an
    error occurred processing the request.
    """

    request_id: Optional[RequestID] = None
    """Identifies a particular SNMP request.

    This index is echoed back in the response from the SNMP agent, allowing the SNMP
    manager to match an incoming response to the appropriate request.

    - Encoding of this field follows ASN.1 X.690(section 8.3) specification. Refer:
      http://www.itu.int/ITU-T/asn1/
    """

    variable_bindings: Optional[List[FlowSnmpv2cVariableBinding]] = None
    """A Sequence of variable_bindings."""
