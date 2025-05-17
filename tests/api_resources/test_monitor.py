# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from devknot import Devknot, AsyncDevknot
from tests.utils import assert_matches_type
from devknot.types import (
    MonitorCreateStatesResponse,
    MonitorCreateMetricsResponse,
)
from devknot._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitor:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_capture(self, client: Devknot, respx_mock: MockRouter) -> None:
        respx_mock.post("/monitor/capture").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        monitor = client.monitor.capture(
            port_name="port_name",
        )
        assert monitor.is_closed
        assert monitor.json() == {"foo": "bar"}
        assert cast(Any, monitor.is_closed) is True
        assert isinstance(monitor, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_capture(self, client: Devknot, respx_mock: MockRouter) -> None:
        respx_mock.post("/monitor/capture").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        monitor = client.monitor.with_raw_response.capture(
            port_name="port_name",
        )

        assert monitor.is_closed is True
        assert monitor.http_request.headers.get("X-Stainless-Lang") == "python"
        assert monitor.json() == {"foo": "bar"}
        assert isinstance(monitor, BinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_capture(self, client: Devknot, respx_mock: MockRouter) -> None:
        respx_mock.post("/monitor/capture").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.monitor.with_streaming_response.capture(
            port_name="port_name",
        ) as monitor:
            assert not monitor.is_closed
            assert monitor.http_request.headers.get("X-Stainless-Lang") == "python"

            assert monitor.json() == {"foo": "bar"}
            assert cast(Any, monitor.is_closed) is True
            assert isinstance(monitor, StreamedBinaryAPIResponse)

        assert cast(Any, monitor.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_metrics(self, client: Devknot) -> None:
        monitor = client.monitor.create_metrics()
        assert_matches_type(MonitorCreateMetricsResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_metrics_with_all_params(self, client: Devknot) -> None:
        monitor = client.monitor.create_metrics(
            bgpv4={
                "column_names": ["session_state"],
                "peer_names": ["string"],
            },
            bgpv6={
                "column_names": ["session_state"],
                "peer_names": ["string"],
            },
            choice="port",
            convergence={"flow_names": ["string"]},
            dhcpv4_client={
                "client_names": ["string"],
                "column_names": ["discovers_sent"],
            },
            dhcpv4_server={
                "column_names": ["discovers_received"],
                "server_names": ["string"],
            },
            dhcpv6_client={
                "client_names": ["string"],
                "column_names": ["solicits_sent"],
            },
            dhcpv6_server={
                "column_names": ["solicits_received"],
                "server_names": ["string"],
            },
            egress_only_tracking={
                "port_names": ["string"],
                "tagged_metrics": {
                    "include_empty_metrics": True,
                    "metric_names": ["frames_rx"],
                },
            },
            flow={
                "flow_names": ["string"],
                "metric_names": ["transmit"],
                "tagged_metrics": {
                    "filters": [
                        {
                            "name": "name",
                            "values": ["string"],
                        }
                    ],
                    "include": True,
                    "include_empty_metrics": True,
                    "metric_names": ["frames_tx"],
                },
            },
            isis={
                "column_names": ["l1_sessions_up"],
                "router_names": ["string"],
            },
            lacp={
                "column_names": ["lacp_packets_rx"],
                "lag_member_port_names": ["string"],
                "lag_names": ["string"],
            },
            lag={
                "column_names": ["oper_status"],
                "lag_names": ["string"],
            },
            lldp={
                "column_names": ["frames_rx"],
                "lldp_names": ["string"],
            },
            macsec={
                "column_names": ["session_state"],
                "secure_entity_names": ["string"],
            },
            mka={
                "column_names": ["session_state"],
                "peer_names": ["string"],
            },
            ospfv2={
                "column_names": ["full_state_count"],
                "router_names": ["string"],
            },
            ospfv3={
                "column_names": ["full_state_count"],
                "router_names": ["string"],
            },
            port={
                "column_names": ["transmit"],
                "port_names": ["string"],
            },
            rocev2_flow={
                "choice": "per_qp",
                "per_qp": {"column_names": ["flow_name"]},
            },
            rocev2_ipv4={
                "choice": "per_peer",
                "per_peer": {
                    "column_names": ["qp_configured"],
                    "peer_names": ["string"],
                },
            },
            rocev2_ipv6={
                "choice": "per_peer",
                "per_peer": {
                    "column_names": ["qp_configured"],
                    "peer_names": ["string"],
                },
            },
            rsvp={
                "column_names": ["ingress_p2p_lsps_configured"],
                "router_names": ["string"],
            },
        )
        assert_matches_type(MonitorCreateMetricsResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_metrics(self, client: Devknot) -> None:
        response = client.monitor.with_raw_response.create_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorCreateMetricsResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_metrics(self, client: Devknot) -> None:
        with client.monitor.with_streaming_response.create_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorCreateMetricsResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_states(self, client: Devknot) -> None:
        monitor = client.monitor.create_states()
        assert_matches_type(MonitorCreateStatesResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_states_with_all_params(self, client: Devknot) -> None:
        monitor = client.monitor.create_states(
            bgp_prefixes={
                "bgp_peer_names": ["string"],
                "ipv4_unicast_filters": [
                    {
                        "addresses": ["192.168.1.1"],
                        "origin": "igp",
                        "path_id": 0,
                        "prefix_length": 128,
                    }
                ],
                "ipv6_unicast_filters": [
                    {
                        "addresses": ["2001:0db8:85a3:0000:0000:8a2e:0370:7334"],
                        "origin": "igp",
                        "path_id": 0,
                        "prefix_length": 128,
                    }
                ],
                "prefix_filters": ["ipv4_unicast"],
            },
            choice="ipv4_neighbors",
            dhcpv4_interfaces={"dhcp_client_names": ["string"]},
            dhcpv4_leases={"dhcp_server_names": ["string"]},
            dhcpv6_interfaces={"dhcp_client_names": ["string"]},
            dhcpv6_leases={"dhcp_server_names": ["string"]},
            ipv4_neighbors={"ethernet_names": ["string"]},
            ipv6_neighbors={"ethernet_names": ["string"]},
            isis_lsps={"isis_router_names": ["string"]},
            lldp_neighbors={
                "lldp_names": ["string"],
                "neighbor_id_filters": ["string"],
            },
            ospfv2_lsas={"router_names": ["string"]},
            ospfv3_lsas={"router_names": ["string"]},
            rsvp_lsps={"rsvp_router_names": ["string"]},
        )
        assert_matches_type(MonitorCreateStatesResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_states(self, client: Devknot) -> None:
        response = client.monitor.with_raw_response.create_states()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(MonitorCreateStatesResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_states(self, client: Devknot) -> None:
        with client.monitor.with_streaming_response.create_states() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(MonitorCreateStatesResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMonitor:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_capture(self, async_client: AsyncDevknot, respx_mock: MockRouter) -> None:
        respx_mock.post("/monitor/capture").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        monitor = await async_client.monitor.capture(
            port_name="port_name",
        )
        assert monitor.is_closed
        assert await monitor.json() == {"foo": "bar"}
        assert cast(Any, monitor.is_closed) is True
        assert isinstance(monitor, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_capture(self, async_client: AsyncDevknot, respx_mock: MockRouter) -> None:
        respx_mock.post("/monitor/capture").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        monitor = await async_client.monitor.with_raw_response.capture(
            port_name="port_name",
        )

        assert monitor.is_closed is True
        assert monitor.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await monitor.json() == {"foo": "bar"}
        assert isinstance(monitor, AsyncBinaryAPIResponse)

    @pytest.mark.skip()
    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_capture(self, async_client: AsyncDevknot, respx_mock: MockRouter) -> None:
        respx_mock.post("/monitor/capture").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.monitor.with_streaming_response.capture(
            port_name="port_name",
        ) as monitor:
            assert not monitor.is_closed
            assert monitor.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await monitor.json() == {"foo": "bar"}
            assert cast(Any, monitor.is_closed) is True
            assert isinstance(monitor, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, monitor.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_metrics(self, async_client: AsyncDevknot) -> None:
        monitor = await async_client.monitor.create_metrics()
        assert_matches_type(MonitorCreateMetricsResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_metrics_with_all_params(self, async_client: AsyncDevknot) -> None:
        monitor = await async_client.monitor.create_metrics(
            bgpv4={
                "column_names": ["session_state"],
                "peer_names": ["string"],
            },
            bgpv6={
                "column_names": ["session_state"],
                "peer_names": ["string"],
            },
            choice="port",
            convergence={"flow_names": ["string"]},
            dhcpv4_client={
                "client_names": ["string"],
                "column_names": ["discovers_sent"],
            },
            dhcpv4_server={
                "column_names": ["discovers_received"],
                "server_names": ["string"],
            },
            dhcpv6_client={
                "client_names": ["string"],
                "column_names": ["solicits_sent"],
            },
            dhcpv6_server={
                "column_names": ["solicits_received"],
                "server_names": ["string"],
            },
            egress_only_tracking={
                "port_names": ["string"],
                "tagged_metrics": {
                    "include_empty_metrics": True,
                    "metric_names": ["frames_rx"],
                },
            },
            flow={
                "flow_names": ["string"],
                "metric_names": ["transmit"],
                "tagged_metrics": {
                    "filters": [
                        {
                            "name": "name",
                            "values": ["string"],
                        }
                    ],
                    "include": True,
                    "include_empty_metrics": True,
                    "metric_names": ["frames_tx"],
                },
            },
            isis={
                "column_names": ["l1_sessions_up"],
                "router_names": ["string"],
            },
            lacp={
                "column_names": ["lacp_packets_rx"],
                "lag_member_port_names": ["string"],
                "lag_names": ["string"],
            },
            lag={
                "column_names": ["oper_status"],
                "lag_names": ["string"],
            },
            lldp={
                "column_names": ["frames_rx"],
                "lldp_names": ["string"],
            },
            macsec={
                "column_names": ["session_state"],
                "secure_entity_names": ["string"],
            },
            mka={
                "column_names": ["session_state"],
                "peer_names": ["string"],
            },
            ospfv2={
                "column_names": ["full_state_count"],
                "router_names": ["string"],
            },
            ospfv3={
                "column_names": ["full_state_count"],
                "router_names": ["string"],
            },
            port={
                "column_names": ["transmit"],
                "port_names": ["string"],
            },
            rocev2_flow={
                "choice": "per_qp",
                "per_qp": {"column_names": ["flow_name"]},
            },
            rocev2_ipv4={
                "choice": "per_peer",
                "per_peer": {
                    "column_names": ["qp_configured"],
                    "peer_names": ["string"],
                },
            },
            rocev2_ipv6={
                "choice": "per_peer",
                "per_peer": {
                    "column_names": ["qp_configured"],
                    "peer_names": ["string"],
                },
            },
            rsvp={
                "column_names": ["ingress_p2p_lsps_configured"],
                "router_names": ["string"],
            },
        )
        assert_matches_type(MonitorCreateMetricsResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_metrics(self, async_client: AsyncDevknot) -> None:
        response = await async_client.monitor.with_raw_response.create_metrics()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorCreateMetricsResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_metrics(self, async_client: AsyncDevknot) -> None:
        async with async_client.monitor.with_streaming_response.create_metrics() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorCreateMetricsResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_states(self, async_client: AsyncDevknot) -> None:
        monitor = await async_client.monitor.create_states()
        assert_matches_type(MonitorCreateStatesResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_states_with_all_params(self, async_client: AsyncDevknot) -> None:
        monitor = await async_client.monitor.create_states(
            bgp_prefixes={
                "bgp_peer_names": ["string"],
                "ipv4_unicast_filters": [
                    {
                        "addresses": ["192.168.1.1"],
                        "origin": "igp",
                        "path_id": 0,
                        "prefix_length": 128,
                    }
                ],
                "ipv6_unicast_filters": [
                    {
                        "addresses": ["2001:0db8:85a3:0000:0000:8a2e:0370:7334"],
                        "origin": "igp",
                        "path_id": 0,
                        "prefix_length": 128,
                    }
                ],
                "prefix_filters": ["ipv4_unicast"],
            },
            choice="ipv4_neighbors",
            dhcpv4_interfaces={"dhcp_client_names": ["string"]},
            dhcpv4_leases={"dhcp_server_names": ["string"]},
            dhcpv6_interfaces={"dhcp_client_names": ["string"]},
            dhcpv6_leases={"dhcp_server_names": ["string"]},
            ipv4_neighbors={"ethernet_names": ["string"]},
            ipv6_neighbors={"ethernet_names": ["string"]},
            isis_lsps={"isis_router_names": ["string"]},
            lldp_neighbors={
                "lldp_names": ["string"],
                "neighbor_id_filters": ["string"],
            },
            ospfv2_lsas={"router_names": ["string"]},
            ospfv3_lsas={"router_names": ["string"]},
            rsvp_lsps={"rsvp_router_names": ["string"]},
        )
        assert_matches_type(MonitorCreateStatesResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_states(self, async_client: AsyncDevknot) -> None:
        response = await async_client.monitor.with_raw_response.create_states()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(MonitorCreateStatesResponse, monitor, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_states(self, async_client: AsyncDevknot) -> None:
        async with async_client.monitor.with_streaming_response.create_states() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(MonitorCreateStatesResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True
