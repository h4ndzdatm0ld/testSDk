# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devknot import Devknot, AsyncDevknot
from tests.utils import assert_matches_type
from devknot.types import (
    ControlSetStateResponse,
    ControlTriggerActionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestControl:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_set_state(self, client: Devknot) -> None:
        control = client.control.set_state(
            choice="port",
        )
        assert_matches_type(ControlSetStateResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_set_state_with_all_params(self, client: Devknot) -> None:
        control = client.control.set_state(
            choice="port",
            port={
                "choice": "link",
                "capture": {
                    "state": "start",
                    "port_names": ["string"],
                },
                "link": {
                    "state": "up",
                    "port_names": ["string"],
                },
            },
            protocol={
                "choice": "all",
                "all": {"state": "start"},
                "bgp": {
                    "choice": "peers",
                    "peers": {
                        "state": "up",
                        "peer_names": ["string"],
                    },
                },
                "isis": {
                    "choice": "routers",
                    "routers": {
                        "state": "up",
                        "router_names": ["string"],
                    },
                },
                "lacp": {
                    "choice": "admin",
                    "admin": {
                        "state": "up",
                        "lag_member_names": ["string"],
                    },
                    "member_ports": {
                        "state": "up",
                        "lag_member_names": ["string"],
                    },
                },
                "ospfv2": {
                    "choice": "routers",
                    "routers": {
                        "state": "up",
                        "router_names": ["string"],
                    },
                },
                "ospfv3": {
                    "choice": "routers",
                    "routers": {
                        "state": "up",
                        "router_names": ["string"],
                    },
                },
                "rocev2": {
                    "choice": "peers",
                    "peers": {
                        "state": "up",
                        "peer_names": ["string"],
                    },
                },
                "route": {
                    "state": "withdraw",
                    "names": ["string"],
                },
            },
            traffic={
                "choice": "flow_transmit",
                "flow_transmit": {
                    "state": "start",
                    "flow_names": ["string"],
                },
            },
        )
        assert_matches_type(ControlSetStateResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set_state(self, client: Devknot) -> None:
        response = client.control.with_raw_response.set_state(
            choice="port",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        control = response.parse()
        assert_matches_type(ControlSetStateResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set_state(self, client: Devknot) -> None:
        with client.control.with_streaming_response.set_state(
            choice="port",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            control = response.parse()
            assert_matches_type(ControlSetStateResponse, control, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_trigger_action(self, client: Devknot) -> None:
        control = client.control.trigger_action(
            choice="protocol",
        )
        assert_matches_type(ControlTriggerActionResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_trigger_action_with_all_params(self, client: Devknot) -> None:
        control = client.control.trigger_action(
            choice="protocol",
            protocol={
                "choice": "ipv4",
                "bgp": {
                    "choice": "notification",
                    "initiate_graceful_restart": {
                        "notification": {
                            "cease": {"subcode": "max_number_prefix_reached_code6_subcode1"},
                            "choice": "cease",
                            "custom": {
                                "code": 0,
                                "subcode": 0,
                            },
                            "finite_state_machine_error": {},
                            "hold_timer_expired": {},
                            "message_header_error": {"subcode": "connection_not_synchronized_code1_subcode1"},
                            "open_message_error": {"subcode": "unsupported_version_number_code2_subcode1"},
                            "update_message_error": {"subcode": "malformed_attrib_list_code3_subcode1"},
                        },
                        "peer_names": ["string"],
                        "restart_delay": 3600,
                    },
                    "notification": {
                        "cease": {"subcode": "max_number_prefix_reached_code6_subcode1"},
                        "choice": "cease",
                        "custom": {
                            "code": 0,
                            "subcode": 0,
                        },
                        "finite_state_machine_error": {},
                        "hold_timer_expired": {},
                        "message_header_error": {"subcode": "connection_not_synchronized_code1_subcode1"},
                        "names": ["string"],
                        "open_message_error": {"subcode": "unsupported_version_number_code2_subcode1"},
                        "update_message_error": {"subcode": "malformed_attrib_list_code3_subcode1"},
                    },
                },
                "ipv4": {
                    "choice": "ping",
                    "ping": {
                        "requests": [
                            {
                                "dst_ip": "dst_ip",
                                "src_name": "src_name",
                            }
                        ]
                    },
                },
                "ipv6": {
                    "choice": "ping",
                    "ping": {
                        "requests": [
                            {
                                "dst_ip": "dst_ip",
                                "src_name": "src_name",
                            }
                        ]
                    },
                },
            },
        )
        assert_matches_type(ControlTriggerActionResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_trigger_action(self, client: Devknot) -> None:
        response = client.control.with_raw_response.trigger_action(
            choice="protocol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        control = response.parse()
        assert_matches_type(ControlTriggerActionResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_trigger_action(self, client: Devknot) -> None:
        with client.control.with_streaming_response.trigger_action(
            choice="protocol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            control = response.parse()
            assert_matches_type(ControlTriggerActionResponse, control, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncControl:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_state(self, async_client: AsyncDevknot) -> None:
        control = await async_client.control.set_state(
            choice="port",
        )
        assert_matches_type(ControlSetStateResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_state_with_all_params(self, async_client: AsyncDevknot) -> None:
        control = await async_client.control.set_state(
            choice="port",
            port={
                "choice": "link",
                "capture": {
                    "state": "start",
                    "port_names": ["string"],
                },
                "link": {
                    "state": "up",
                    "port_names": ["string"],
                },
            },
            protocol={
                "choice": "all",
                "all": {"state": "start"},
                "bgp": {
                    "choice": "peers",
                    "peers": {
                        "state": "up",
                        "peer_names": ["string"],
                    },
                },
                "isis": {
                    "choice": "routers",
                    "routers": {
                        "state": "up",
                        "router_names": ["string"],
                    },
                },
                "lacp": {
                    "choice": "admin",
                    "admin": {
                        "state": "up",
                        "lag_member_names": ["string"],
                    },
                    "member_ports": {
                        "state": "up",
                        "lag_member_names": ["string"],
                    },
                },
                "ospfv2": {
                    "choice": "routers",
                    "routers": {
                        "state": "up",
                        "router_names": ["string"],
                    },
                },
                "ospfv3": {
                    "choice": "routers",
                    "routers": {
                        "state": "up",
                        "router_names": ["string"],
                    },
                },
                "rocev2": {
                    "choice": "peers",
                    "peers": {
                        "state": "up",
                        "peer_names": ["string"],
                    },
                },
                "route": {
                    "state": "withdraw",
                    "names": ["string"],
                },
            },
            traffic={
                "choice": "flow_transmit",
                "flow_transmit": {
                    "state": "start",
                    "flow_names": ["string"],
                },
            },
        )
        assert_matches_type(ControlSetStateResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set_state(self, async_client: AsyncDevknot) -> None:
        response = await async_client.control.with_raw_response.set_state(
            choice="port",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        control = await response.parse()
        assert_matches_type(ControlSetStateResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set_state(self, async_client: AsyncDevknot) -> None:
        async with async_client.control.with_streaming_response.set_state(
            choice="port",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            control = await response.parse()
            assert_matches_type(ControlSetStateResponse, control, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_trigger_action(self, async_client: AsyncDevknot) -> None:
        control = await async_client.control.trigger_action(
            choice="protocol",
        )
        assert_matches_type(ControlTriggerActionResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_trigger_action_with_all_params(self, async_client: AsyncDevknot) -> None:
        control = await async_client.control.trigger_action(
            choice="protocol",
            protocol={
                "choice": "ipv4",
                "bgp": {
                    "choice": "notification",
                    "initiate_graceful_restart": {
                        "notification": {
                            "cease": {"subcode": "max_number_prefix_reached_code6_subcode1"},
                            "choice": "cease",
                            "custom": {
                                "code": 0,
                                "subcode": 0,
                            },
                            "finite_state_machine_error": {},
                            "hold_timer_expired": {},
                            "message_header_error": {"subcode": "connection_not_synchronized_code1_subcode1"},
                            "open_message_error": {"subcode": "unsupported_version_number_code2_subcode1"},
                            "update_message_error": {"subcode": "malformed_attrib_list_code3_subcode1"},
                        },
                        "peer_names": ["string"],
                        "restart_delay": 3600,
                    },
                    "notification": {
                        "cease": {"subcode": "max_number_prefix_reached_code6_subcode1"},
                        "choice": "cease",
                        "custom": {
                            "code": 0,
                            "subcode": 0,
                        },
                        "finite_state_machine_error": {},
                        "hold_timer_expired": {},
                        "message_header_error": {"subcode": "connection_not_synchronized_code1_subcode1"},
                        "names": ["string"],
                        "open_message_error": {"subcode": "unsupported_version_number_code2_subcode1"},
                        "update_message_error": {"subcode": "malformed_attrib_list_code3_subcode1"},
                    },
                },
                "ipv4": {
                    "choice": "ping",
                    "ping": {
                        "requests": [
                            {
                                "dst_ip": "dst_ip",
                                "src_name": "src_name",
                            }
                        ]
                    },
                },
                "ipv6": {
                    "choice": "ping",
                    "ping": {
                        "requests": [
                            {
                                "dst_ip": "dst_ip",
                                "src_name": "src_name",
                            }
                        ]
                    },
                },
            },
        )
        assert_matches_type(ControlTriggerActionResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_trigger_action(self, async_client: AsyncDevknot) -> None:
        response = await async_client.control.with_raw_response.trigger_action(
            choice="protocol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        control = await response.parse()
        assert_matches_type(ControlTriggerActionResponse, control, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_trigger_action(self, async_client: AsyncDevknot) -> None:
        async with async_client.control.with_streaming_response.trigger_action(
            choice="protocol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            control = await response.parse()
            assert_matches_type(ControlTriggerActionResponse, control, path=["response"])

        assert cast(Any, response.is_closed) is True
