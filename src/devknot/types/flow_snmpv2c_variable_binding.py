# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .pattern_flow_snmpv2c_variable_binding_value_counter_value_counter import (
    PatternFlowSnmpv2cVariableBindingValueCounterValueCounter,
)
from .pattern_flow_snmpv2c_variable_binding_value_integer_value_counter import (
    PatternFlowSnmpv2cVariableBindingValueIntegerValueCounter,
)
from .pattern_flow_snmpv2c_variable_binding_value_timeticks_value_counter import (
    PatternFlowSnmpv2cVariableBindingValueTimeticksValueCounter,
)
from .pattern_flow_snmpv2c_variable_binding_value_ip_address_value_counter import (
    PatternFlowSnmpv2cVariableBindingValueIPAddressValueCounter,
)
from .pattern_flow_snmpv2c_variable_binding_value_big_counter_value_counter import (
    PatternFlowSnmpv2cVariableBindingValueBigCounterValueCounter,
)
from .pattern_flow_snmpv2c_variable_binding_value_unsigned_integer_value_counter import (
    PatternFlowSnmpv2cVariableBindingValueUnsignedIntegerValueCounter,
)

__all__ = [
    "FlowSnmpv2cVariableBinding",
    "Value",
    "ValueBigCounterValue",
    "ValueCounterValue",
    "ValueIntegerValue",
    "ValueIPAddressValue",
    "ValueStringValue",
    "ValueTimeticksValue",
    "ValueUnsignedIntegerValue",
]


class ValueBigCounterValue(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cVariableBindingValueBigCounterValueCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowSnmpv2cVariableBindingValueBigCounterValueCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class ValueCounterValue(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cVariableBindingValueCounterValueCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowSnmpv2cVariableBindingValueCounterValueCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class ValueIntegerValue(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cVariableBindingValueIntegerValueCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowSnmpv2cVariableBindingValueIntegerValueCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class ValueIPAddressValue(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cVariableBindingValueIPAddressValueCounter] = None
    """ipv4 counter pattern"""

    increment: Optional[PatternFlowSnmpv2cVariableBindingValueIPAddressValueCounter] = None
    """ipv4 counter pattern"""

    value: Optional[str] = None

    values: Optional[List[str]] = None


class ValueStringValue(BaseModel):
    ascii: Optional[str] = None
    """It contains the ASCII string to be sent.

    As of now it is restricted to 10000 bytes.
    """

    choice: Optional[Literal["ascii", "raw"]] = None

    raw: Optional[str] = None
    """It contains the hex string to be sent.

    As of now it is restricted to 10000 bytes.
    """


class ValueTimeticksValue(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cVariableBindingValueTimeticksValueCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowSnmpv2cVariableBindingValueTimeticksValueCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class ValueUnsignedIntegerValue(BaseModel):
    choice: Optional[Literal["value", "values", "increment", "decrement"]] = None

    decrement: Optional[PatternFlowSnmpv2cVariableBindingValueUnsignedIntegerValueCounter] = None
    """integer counter pattern"""

    increment: Optional[PatternFlowSnmpv2cVariableBindingValueUnsignedIntegerValueCounter] = None
    """integer counter pattern"""

    value: Optional[int] = None

    values: Optional[List[int]] = None


class Value(BaseModel):
    arbitrary_value: Optional[str] = None
    """It contains the hex bytes of the value to be sent.

    As of now it is restricted to 10000 bytes.
    """

    big_counter_value: Optional[ValueBigCounterValue] = None
    """Big counter returned for the requested OID."""

    choice: Optional[
        Literal[
            "no_value",
            "integer_value",
            "string_value",
            "object_identifier_value",
            "ip_address_value",
            "counter_value",
            "timeticks_value",
            "arbitrary_value",
            "big_counter_value",
            "unsigned_integer_value",
        ]
    ] = None

    counter_value: Optional[ValueCounterValue] = None
    """Counter returned for the requested OID."""

    integer_value: Optional[ValueIntegerValue] = None
    """Integer value returned for the requested OID."""

    ip_address_value: Optional[ValueIPAddressValue] = None
    """IPv4 address returned for the requested OID."""

    object_identifier_value: Optional[str] = None
    """The Object Identifier points to a particular parameter in the SNMP agent.

    - Encoding of this field follows RFC2578(section 3.5) and ASN.1 X.690(section
      8.1.3.6) specification. Refer: http://www.itu.int/ITU-T/asn1/
    - According to BER, the first two numbers of any OID (x.y) are encoded as one
      value using the formula (40*x)+y. Example, the first two numbers of an SNMP
      OID 1.3... are encoded as 43 or 0x2B, because (40*1)+3 = 43.
    - After the first two numbers are encoded, the subsequent numbers in the OID are
      each encoded as a byte.
    - However, a special rule is required for large numbers because one byte can
      only represent a number from 0-127.
    - The rule for large numbers states that only the lower 7 bits in the byte are
      used for holding the value (0-127).
    - The highest order bit(8th) is used as a flag to indicate that this number
      spans more than one byte. Therefore, any number over 127 must be encoded using
      more than one byte.
      - Example, the number 2680 in the OID '1.3.6.1.4.1.2680.1.2.7.3.2.0' cannot be
        encoded using a single byte. According to this rule, the number 2680 must be
        encoded as 0x94 0x78. Since the most significant bit is set in the first
        byte (0x94), it indicates that number spans to the next byte. Since the most
        significant bit is not set in the next byte (0x78), it indicates that the
        number ends at the second byte. The value is derived by appending 7 bits
        from each of the concatenated bytes i.e (0x14 _128^1) + (0x78 _ 128^0)
        = 2680.
    """

    string_value: Optional[ValueStringValue] = None
    """It contains the raw/ascii string value to be sent."""

    timeticks_value: Optional[ValueTimeticksValue] = None
    """Timeticks returned for the requested OID."""

    unsigned_integer_value: Optional[ValueUnsignedIntegerValue] = None
    """Unsigned integer value returned for the requested OID."""


class FlowSnmpv2cVariableBinding(BaseModel):
    object_identifier: Optional[str] = None
    """The Object Identifier points to a particular parameter in the SNMP agent.

    - Encoding of this field follows RFC2578(section 3.5) and ASN.1 X.690(section
      8.1.3.6) specification. Refer: http://www.itu.int/ITU-T/asn1/
    - According to BER, the first two numbers of any OID (x.y) are encoded as one
      value using the formula (40*x)+y. Example, the first two numbers of an SNMP
      OID 1.3... are encoded as 43 or 0x2B, because (40*1)+3 = 43.
    - After the first two numbers are encoded, the subsequent numbers in the OID are
      each encoded as a byte.
    - However, a special rule is required for large numbers because one byte can
      only represent a number from 0-127.
    - The rule for large numbers states that only the lower 7 bits in the byte are
      used for holding the value (0-127).
    - The highest order bit(8th) is used as a flag to indicate that this number
      spans more than one byte. Therefore, any number over 127 must be encoded using
      more than one byte.
      - Example, the number 2680 in the OID '1.3.6.1.4.1.2680.1.2.7.3.2.0' cannot be
        encoded using a single byte. According to this rule, the number 2680 must be
        encoded as 0x94 0x78. Since the most significant bit is set in the first
        byte (0x94), it indicates that number spans to the next byte. Since the most
        significant bit is not set in the next byte (0x78), it indicates that the
        number ends at the second byte. The value is derived by appending 7 bits
        from each of the concatenated bytes i.e (0x14 _128^1) + (0x78 _ 128^0)
        = 2680.
    """

    value: Optional[Value] = None
    """The value for the object_identifier as per RFC2578."""
