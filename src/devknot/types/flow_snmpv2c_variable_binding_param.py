# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

from .pattern_flow_snmpv2c_variable_binding_value_counter_value_counter_param import (
    PatternFlowSnmpv2cVariableBindingValueCounterValueCounterParam,
)
from .pattern_flow_snmpv2c_variable_binding_value_integer_value_counter_param import (
    PatternFlowSnmpv2cVariableBindingValueIntegerValueCounterParam,
)
from .pattern_flow_snmpv2c_variable_binding_value_timeticks_value_counter_param import (
    PatternFlowSnmpv2cVariableBindingValueTimeticksValueCounterParam,
)
from .pattern_flow_snmpv2c_variable_binding_value_ip_address_value_counter_param import (
    PatternFlowSnmpv2cVariableBindingValueIPAddressValueCounterParam,
)
from .pattern_flow_snmpv2c_variable_binding_value_big_counter_value_counter_param import (
    PatternFlowSnmpv2cVariableBindingValueBigCounterValueCounterParam,
)
from .pattern_flow_snmpv2c_variable_binding_value_unsigned_integer_value_counter_param import (
    PatternFlowSnmpv2cVariableBindingValueUnsignedIntegerValueCounterParam,
)

__all__ = [
    "FlowSnmpv2cVariableBindingParam",
    "Value",
    "ValueBigCounterValue",
    "ValueCounterValue",
    "ValueIntegerValue",
    "ValueIPAddressValue",
    "ValueStringValue",
    "ValueTimeticksValue",
    "ValueUnsignedIntegerValue",
]


class ValueBigCounterValue(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cVariableBindingValueBigCounterValueCounterParam
    """integer counter pattern"""

    increment: PatternFlowSnmpv2cVariableBindingValueBigCounterValueCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class ValueCounterValue(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cVariableBindingValueCounterValueCounterParam
    """integer counter pattern"""

    increment: PatternFlowSnmpv2cVariableBindingValueCounterValueCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class ValueIntegerValue(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cVariableBindingValueIntegerValueCounterParam
    """integer counter pattern"""

    increment: PatternFlowSnmpv2cVariableBindingValueIntegerValueCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class ValueIPAddressValue(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cVariableBindingValueIPAddressValueCounterParam
    """ipv4 counter pattern"""

    increment: PatternFlowSnmpv2cVariableBindingValueIPAddressValueCounterParam
    """ipv4 counter pattern"""

    value: str

    values: List[str]


class ValueStringValue(TypedDict, total=False):
    ascii: str
    """It contains the ASCII string to be sent.

    As of now it is restricted to 10000 bytes.
    """

    choice: Literal["ascii", "raw"]

    raw: str
    """It contains the hex string to be sent.

    As of now it is restricted to 10000 bytes.
    """


class ValueTimeticksValue(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cVariableBindingValueTimeticksValueCounterParam
    """integer counter pattern"""

    increment: PatternFlowSnmpv2cVariableBindingValueTimeticksValueCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class ValueUnsignedIntegerValue(TypedDict, total=False):
    choice: Literal["value", "values", "increment", "decrement"]

    decrement: PatternFlowSnmpv2cVariableBindingValueUnsignedIntegerValueCounterParam
    """integer counter pattern"""

    increment: PatternFlowSnmpv2cVariableBindingValueUnsignedIntegerValueCounterParam
    """integer counter pattern"""

    value: int

    values: Iterable[int]


class Value(TypedDict, total=False):
    arbitrary_value: str
    """It contains the hex bytes of the value to be sent.

    As of now it is restricted to 10000 bytes.
    """

    big_counter_value: ValueBigCounterValue
    """Big counter returned for the requested OID."""

    choice: Literal[
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

    counter_value: ValueCounterValue
    """Counter returned for the requested OID."""

    integer_value: ValueIntegerValue
    """Integer value returned for the requested OID."""

    ip_address_value: ValueIPAddressValue
    """IPv4 address returned for the requested OID."""

    object_identifier_value: str
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

    string_value: ValueStringValue
    """It contains the raw/ascii string value to be sent."""

    timeticks_value: ValueTimeticksValue
    """Timeticks returned for the requested OID."""

    unsigned_integer_value: ValueUnsignedIntegerValue
    """Unsigned integer value returned for the requested OID."""


class FlowSnmpv2cVariableBindingParam(TypedDict, total=False):
    object_identifier: str
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

    value: Value
    """The value for the object_identifier as per RFC2578."""
