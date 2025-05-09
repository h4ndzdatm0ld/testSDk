# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import monitor_capture_params, monitor_create_states_params, monitor_create_metrics_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.monitor_create_states_response import MonitorCreateStatesResponse
from ..types.monitor_create_metrics_response import MonitorCreateMetricsResponse

__all__ = ["MonitorResource", "AsyncMonitorResource"]


class MonitorResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MonitorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/h4ndzdatm0ld/testSDk#accessing-raw-response-data-eg-headers
        """
        return MonitorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/h4ndzdatm0ld/testSDk#with_streaming_response
        """
        return MonitorResourceWithStreamingResponse(self)

    def capture(
        self,
        *,
        port_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BinaryAPIResponse:
        """
        Args:
          port_name: The name of a port a capture is started on.

              x-constraint:

              - /components/schemas/Port/properties/name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/monitor/capture",
            body=maybe_transform({"port_name": port_name}, monitor_capture_params.MonitorCaptureParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def create_metrics(
        self,
        *,
        bgpv4: monitor_create_metrics_params.Bgpv4 | NotGiven = NOT_GIVEN,
        bgpv6: monitor_create_metrics_params.Bgpv6 | NotGiven = NOT_GIVEN,
        choice: Literal[
            "port",
            "flow",
            "bgpv4",
            "bgpv6",
            "isis",
            "lag",
            "lacp",
            "lldp",
            "rsvp",
            "dhcpv4_client",
            "dhcpv4_server",
            "dhcpv6_client",
            "dhcpv6_server",
            "ospfv2",
            "convergence",
            "macsec",
            "mka",
            "ospfv3",
            "rocev2_ipv4",
            "rocev2_ipv6",
            "rocev2_flow",
            "egress_only_tracking",
        ]
        | NotGiven = NOT_GIVEN,
        convergence: monitor_create_metrics_params.Convergence | NotGiven = NOT_GIVEN,
        dhcpv4_client: monitor_create_metrics_params.Dhcpv4Client | NotGiven = NOT_GIVEN,
        dhcpv4_server: monitor_create_metrics_params.Dhcpv4Server | NotGiven = NOT_GIVEN,
        dhcpv6_client: monitor_create_metrics_params.Dhcpv6Client | NotGiven = NOT_GIVEN,
        dhcpv6_server: monitor_create_metrics_params.Dhcpv6Server | NotGiven = NOT_GIVEN,
        egress_only_tracking: monitor_create_metrics_params.EgressOnlyTracking | NotGiven = NOT_GIVEN,
        flow: monitor_create_metrics_params.Flow | NotGiven = NOT_GIVEN,
        isis: monitor_create_metrics_params.Isis | NotGiven = NOT_GIVEN,
        lacp: monitor_create_metrics_params.Lacp | NotGiven = NOT_GIVEN,
        lag: monitor_create_metrics_params.Lag | NotGiven = NOT_GIVEN,
        lldp: monitor_create_metrics_params.Lldp | NotGiven = NOT_GIVEN,
        macsec: monitor_create_metrics_params.Macsec | NotGiven = NOT_GIVEN,
        mka: monitor_create_metrics_params.Mka | NotGiven = NOT_GIVEN,
        ospfv2: monitor_create_metrics_params.Ospfv2 | NotGiven = NOT_GIVEN,
        ospfv3: monitor_create_metrics_params.Ospfv3 | NotGiven = NOT_GIVEN,
        port: monitor_create_metrics_params.Port | NotGiven = NOT_GIVEN,
        rocev2_flow: monitor_create_metrics_params.Rocev2Flow | NotGiven = NOT_GIVEN,
        rocev2_ipv4: monitor_create_metrics_params.Rocev2Ipv4 | NotGiven = NOT_GIVEN,
        rocev2_ipv6: monitor_create_metrics_params.Rocev2Ipv6 | NotGiven = NOT_GIVEN,
        rsvp: monitor_create_metrics_params.Rsvp | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MonitorCreateMetricsResponse:
        """
        Args:
          bgpv4: The request to retrieve BGPv4 per peer metrics/statistics.

          bgpv6: The request to retrieve BGPv6 per peer metrics/statistics.

          convergence: Under Review: Convergence metrics is currently under review for pending
              exploration on use cases.

              Container for requesting control-plane and data-plane convergence time metrics
              for flows.

          dhcpv4_client: The request to retrieve DHCPv4 per client metrics/statistics.

          dhcpv4_server: The request to retrieve DHCPv4 per Server metrics/statistics.

          dhcpv6_client: The request to retrieve DHCPv6 per client metrics/statistics.

          dhcpv6_server: The request to retrieve DHCPv6 per Server metrics/statistics.

          egress_only_tracking: The container for a egress only tracking metric request.

          flow: The container for a flow metric request.

          isis: The request to retrieve ISIS per Router metrics/statistics.

          lacp: The request to retrieve LACP per LAG member metrics/statistics.

          lag: The request to retrieve per LAG metrics/statistics.

          lldp: The request to retrieve LLDP per instance metrics/statistics.

          macsec: The request to retrieve MACsec per secure entity(secY) metrics/statistics.

          mka: The request to retrieve MKA per peer metrics/statistics.

          ospfv2: The request to retrieve OSPFv2 per Router metrics/statistics.

          ospfv3: The request to retrieve OSPFv3 per router metrics/statistics.

          port: The port result request to the traffic generator

          rocev2_flow: Request to retrieve RoCEv2 FLow statistics.

          rocev2_ipv4: Request to retrieve RoCEv2 over IPv4 per peer metrics/statistics.

          rocev2_ipv6: Request to retrieve RoCEv2 over IPv6 per peer metrics/statistics.

          rsvp: The request to retrieve RSVP-TE per Router metrics/statistics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/monitor/metrics",
            body=maybe_transform(
                {
                    "bgpv4": bgpv4,
                    "bgpv6": bgpv6,
                    "choice": choice,
                    "convergence": convergence,
                    "dhcpv4_client": dhcpv4_client,
                    "dhcpv4_server": dhcpv4_server,
                    "dhcpv6_client": dhcpv6_client,
                    "dhcpv6_server": dhcpv6_server,
                    "egress_only_tracking": egress_only_tracking,
                    "flow": flow,
                    "isis": isis,
                    "lacp": lacp,
                    "lag": lag,
                    "lldp": lldp,
                    "macsec": macsec,
                    "mka": mka,
                    "ospfv2": ospfv2,
                    "ospfv3": ospfv3,
                    "port": port,
                    "rocev2_flow": rocev2_flow,
                    "rocev2_ipv4": rocev2_ipv4,
                    "rocev2_ipv6": rocev2_ipv6,
                    "rsvp": rsvp,
                },
                monitor_create_metrics_params.MonitorCreateMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorCreateMetricsResponse,
        )

    def create_states(
        self,
        *,
        bgp_prefixes: monitor_create_states_params.BgpPrefixes | NotGiven = NOT_GIVEN,
        choice: Literal[
            "ipv4_neighbors",
            "ipv6_neighbors",
            "bgp_prefixes",
            "isis_lsps",
            "lldp_neighbors",
            "rsvp_lsps",
            "dhcpv4_interfaces",
            "dhcpv4_leases",
            "dhcpv6_interfaces",
            "dhcpv6_leases",
            "ospfv2_lsas",
            "ospfv3_lsas",
        ]
        | NotGiven = NOT_GIVEN,
        dhcpv4_interfaces: monitor_create_states_params.Dhcpv4Interfaces | NotGiven = NOT_GIVEN,
        dhcpv4_leases: monitor_create_states_params.Dhcpv4Leases | NotGiven = NOT_GIVEN,
        dhcpv6_interfaces: monitor_create_states_params.Dhcpv6Interfaces | NotGiven = NOT_GIVEN,
        dhcpv6_leases: monitor_create_states_params.Dhcpv6Leases | NotGiven = NOT_GIVEN,
        ipv4_neighbors: monitor_create_states_params.Ipv4Neighbors | NotGiven = NOT_GIVEN,
        ipv6_neighbors: monitor_create_states_params.Ipv6Neighbors | NotGiven = NOT_GIVEN,
        isis_lsps: monitor_create_states_params.IsisLsps | NotGiven = NOT_GIVEN,
        lldp_neighbors: monitor_create_states_params.LldpNeighbors | NotGiven = NOT_GIVEN,
        ospfv2_lsas: monitor_create_states_params.Ospfv2Lsas | NotGiven = NOT_GIVEN,
        ospfv3_lsas: monitor_create_states_params.Ospfv3Lsas | NotGiven = NOT_GIVEN,
        rsvp_lsps: monitor_create_states_params.RsvpLsps | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MonitorCreateStatesResponse:
        """
        Args:
          bgp_prefixes: The request to retrieve BGP peer prefix information.

          dhcpv4_interfaces: The request for assigned IPv4 address information associated with DHCP Client
              sessions.

          dhcpv4_leases: The request to retrieve DHCP Server host allocated status.

          dhcpv6_interfaces: The request for assigned IPv6 address information associated with DHCP Client
              sessions.

          dhcpv6_leases: The request to retrieve DHCP Server host allocated status.

          ipv4_neighbors: The request to retrieve IPv4 Neighbor state (ARP cache entries) of a network
              interface(s).

          ipv6_neighbors: The request to retrieve IPv6 Neighbor state (NDISC cache entries) of a network
              interface(s).

          isis_lsps: The request to retrieve ISIS Link State PDU (LSP) information learned by the
              router.

          lldp_neighbors: The request to retrieve LLDP neighbor information for a given instance.

          ospfv2_lsas: The request to retrieve OSPFv2 Link State Advertisements (LSA) information
              learned by the routers.

          ospfv3_lsas: The request to retrieve OSPFv3 Link State Advertisements (LSA) information
              learned by the routers.

          rsvp_lsps: The request to retrieve RSVP Label Switched Path (LSP) information learned by
              the router.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/monitor/states",
            body=maybe_transform(
                {
                    "bgp_prefixes": bgp_prefixes,
                    "choice": choice,
                    "dhcpv4_interfaces": dhcpv4_interfaces,
                    "dhcpv4_leases": dhcpv4_leases,
                    "dhcpv6_interfaces": dhcpv6_interfaces,
                    "dhcpv6_leases": dhcpv6_leases,
                    "ipv4_neighbors": ipv4_neighbors,
                    "ipv6_neighbors": ipv6_neighbors,
                    "isis_lsps": isis_lsps,
                    "lldp_neighbors": lldp_neighbors,
                    "ospfv2_lsas": ospfv2_lsas,
                    "ospfv3_lsas": ospfv3_lsas,
                    "rsvp_lsps": rsvp_lsps,
                },
                monitor_create_states_params.MonitorCreateStatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorCreateStatesResponse,
        )


class AsyncMonitorResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMonitorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/h4ndzdatm0ld/testSDk#accessing-raw-response-data-eg-headers
        """
        return AsyncMonitorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/h4ndzdatm0ld/testSDk#with_streaming_response
        """
        return AsyncMonitorResourceWithStreamingResponse(self)

    async def capture(
        self,
        *,
        port_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          port_name: The name of a port a capture is started on.

              x-constraint:

              - /components/schemas/Port/properties/name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/monitor/capture",
            body=await async_maybe_transform({"port_name": port_name}, monitor_capture_params.MonitorCaptureParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def create_metrics(
        self,
        *,
        bgpv4: monitor_create_metrics_params.Bgpv4 | NotGiven = NOT_GIVEN,
        bgpv6: monitor_create_metrics_params.Bgpv6 | NotGiven = NOT_GIVEN,
        choice: Literal[
            "port",
            "flow",
            "bgpv4",
            "bgpv6",
            "isis",
            "lag",
            "lacp",
            "lldp",
            "rsvp",
            "dhcpv4_client",
            "dhcpv4_server",
            "dhcpv6_client",
            "dhcpv6_server",
            "ospfv2",
            "convergence",
            "macsec",
            "mka",
            "ospfv3",
            "rocev2_ipv4",
            "rocev2_ipv6",
            "rocev2_flow",
            "egress_only_tracking",
        ]
        | NotGiven = NOT_GIVEN,
        convergence: monitor_create_metrics_params.Convergence | NotGiven = NOT_GIVEN,
        dhcpv4_client: monitor_create_metrics_params.Dhcpv4Client | NotGiven = NOT_GIVEN,
        dhcpv4_server: monitor_create_metrics_params.Dhcpv4Server | NotGiven = NOT_GIVEN,
        dhcpv6_client: monitor_create_metrics_params.Dhcpv6Client | NotGiven = NOT_GIVEN,
        dhcpv6_server: monitor_create_metrics_params.Dhcpv6Server | NotGiven = NOT_GIVEN,
        egress_only_tracking: monitor_create_metrics_params.EgressOnlyTracking | NotGiven = NOT_GIVEN,
        flow: monitor_create_metrics_params.Flow | NotGiven = NOT_GIVEN,
        isis: monitor_create_metrics_params.Isis | NotGiven = NOT_GIVEN,
        lacp: monitor_create_metrics_params.Lacp | NotGiven = NOT_GIVEN,
        lag: monitor_create_metrics_params.Lag | NotGiven = NOT_GIVEN,
        lldp: monitor_create_metrics_params.Lldp | NotGiven = NOT_GIVEN,
        macsec: monitor_create_metrics_params.Macsec | NotGiven = NOT_GIVEN,
        mka: monitor_create_metrics_params.Mka | NotGiven = NOT_GIVEN,
        ospfv2: monitor_create_metrics_params.Ospfv2 | NotGiven = NOT_GIVEN,
        ospfv3: monitor_create_metrics_params.Ospfv3 | NotGiven = NOT_GIVEN,
        port: monitor_create_metrics_params.Port | NotGiven = NOT_GIVEN,
        rocev2_flow: monitor_create_metrics_params.Rocev2Flow | NotGiven = NOT_GIVEN,
        rocev2_ipv4: monitor_create_metrics_params.Rocev2Ipv4 | NotGiven = NOT_GIVEN,
        rocev2_ipv6: monitor_create_metrics_params.Rocev2Ipv6 | NotGiven = NOT_GIVEN,
        rsvp: monitor_create_metrics_params.Rsvp | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MonitorCreateMetricsResponse:
        """
        Args:
          bgpv4: The request to retrieve BGPv4 per peer metrics/statistics.

          bgpv6: The request to retrieve BGPv6 per peer metrics/statistics.

          convergence: Under Review: Convergence metrics is currently under review for pending
              exploration on use cases.

              Container for requesting control-plane and data-plane convergence time metrics
              for flows.

          dhcpv4_client: The request to retrieve DHCPv4 per client metrics/statistics.

          dhcpv4_server: The request to retrieve DHCPv4 per Server metrics/statistics.

          dhcpv6_client: The request to retrieve DHCPv6 per client metrics/statistics.

          dhcpv6_server: The request to retrieve DHCPv6 per Server metrics/statistics.

          egress_only_tracking: The container for a egress only tracking metric request.

          flow: The container for a flow metric request.

          isis: The request to retrieve ISIS per Router metrics/statistics.

          lacp: The request to retrieve LACP per LAG member metrics/statistics.

          lag: The request to retrieve per LAG metrics/statistics.

          lldp: The request to retrieve LLDP per instance metrics/statistics.

          macsec: The request to retrieve MACsec per secure entity(secY) metrics/statistics.

          mka: The request to retrieve MKA per peer metrics/statistics.

          ospfv2: The request to retrieve OSPFv2 per Router metrics/statistics.

          ospfv3: The request to retrieve OSPFv3 per router metrics/statistics.

          port: The port result request to the traffic generator

          rocev2_flow: Request to retrieve RoCEv2 FLow statistics.

          rocev2_ipv4: Request to retrieve RoCEv2 over IPv4 per peer metrics/statistics.

          rocev2_ipv6: Request to retrieve RoCEv2 over IPv6 per peer metrics/statistics.

          rsvp: The request to retrieve RSVP-TE per Router metrics/statistics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/monitor/metrics",
            body=await async_maybe_transform(
                {
                    "bgpv4": bgpv4,
                    "bgpv6": bgpv6,
                    "choice": choice,
                    "convergence": convergence,
                    "dhcpv4_client": dhcpv4_client,
                    "dhcpv4_server": dhcpv4_server,
                    "dhcpv6_client": dhcpv6_client,
                    "dhcpv6_server": dhcpv6_server,
                    "egress_only_tracking": egress_only_tracking,
                    "flow": flow,
                    "isis": isis,
                    "lacp": lacp,
                    "lag": lag,
                    "lldp": lldp,
                    "macsec": macsec,
                    "mka": mka,
                    "ospfv2": ospfv2,
                    "ospfv3": ospfv3,
                    "port": port,
                    "rocev2_flow": rocev2_flow,
                    "rocev2_ipv4": rocev2_ipv4,
                    "rocev2_ipv6": rocev2_ipv6,
                    "rsvp": rsvp,
                },
                monitor_create_metrics_params.MonitorCreateMetricsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorCreateMetricsResponse,
        )

    async def create_states(
        self,
        *,
        bgp_prefixes: monitor_create_states_params.BgpPrefixes | NotGiven = NOT_GIVEN,
        choice: Literal[
            "ipv4_neighbors",
            "ipv6_neighbors",
            "bgp_prefixes",
            "isis_lsps",
            "lldp_neighbors",
            "rsvp_lsps",
            "dhcpv4_interfaces",
            "dhcpv4_leases",
            "dhcpv6_interfaces",
            "dhcpv6_leases",
            "ospfv2_lsas",
            "ospfv3_lsas",
        ]
        | NotGiven = NOT_GIVEN,
        dhcpv4_interfaces: monitor_create_states_params.Dhcpv4Interfaces | NotGiven = NOT_GIVEN,
        dhcpv4_leases: monitor_create_states_params.Dhcpv4Leases | NotGiven = NOT_GIVEN,
        dhcpv6_interfaces: monitor_create_states_params.Dhcpv6Interfaces | NotGiven = NOT_GIVEN,
        dhcpv6_leases: monitor_create_states_params.Dhcpv6Leases | NotGiven = NOT_GIVEN,
        ipv4_neighbors: monitor_create_states_params.Ipv4Neighbors | NotGiven = NOT_GIVEN,
        ipv6_neighbors: monitor_create_states_params.Ipv6Neighbors | NotGiven = NOT_GIVEN,
        isis_lsps: monitor_create_states_params.IsisLsps | NotGiven = NOT_GIVEN,
        lldp_neighbors: monitor_create_states_params.LldpNeighbors | NotGiven = NOT_GIVEN,
        ospfv2_lsas: monitor_create_states_params.Ospfv2Lsas | NotGiven = NOT_GIVEN,
        ospfv3_lsas: monitor_create_states_params.Ospfv3Lsas | NotGiven = NOT_GIVEN,
        rsvp_lsps: monitor_create_states_params.RsvpLsps | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MonitorCreateStatesResponse:
        """
        Args:
          bgp_prefixes: The request to retrieve BGP peer prefix information.

          dhcpv4_interfaces: The request for assigned IPv4 address information associated with DHCP Client
              sessions.

          dhcpv4_leases: The request to retrieve DHCP Server host allocated status.

          dhcpv6_interfaces: The request for assigned IPv6 address information associated with DHCP Client
              sessions.

          dhcpv6_leases: The request to retrieve DHCP Server host allocated status.

          ipv4_neighbors: The request to retrieve IPv4 Neighbor state (ARP cache entries) of a network
              interface(s).

          ipv6_neighbors: The request to retrieve IPv6 Neighbor state (NDISC cache entries) of a network
              interface(s).

          isis_lsps: The request to retrieve ISIS Link State PDU (LSP) information learned by the
              router.

          lldp_neighbors: The request to retrieve LLDP neighbor information for a given instance.

          ospfv2_lsas: The request to retrieve OSPFv2 Link State Advertisements (LSA) information
              learned by the routers.

          ospfv3_lsas: The request to retrieve OSPFv3 Link State Advertisements (LSA) information
              learned by the routers.

          rsvp_lsps: The request to retrieve RSVP Label Switched Path (LSP) information learned by
              the router.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/monitor/states",
            body=await async_maybe_transform(
                {
                    "bgp_prefixes": bgp_prefixes,
                    "choice": choice,
                    "dhcpv4_interfaces": dhcpv4_interfaces,
                    "dhcpv4_leases": dhcpv4_leases,
                    "dhcpv6_interfaces": dhcpv6_interfaces,
                    "dhcpv6_leases": dhcpv6_leases,
                    "ipv4_neighbors": ipv4_neighbors,
                    "ipv6_neighbors": ipv6_neighbors,
                    "isis_lsps": isis_lsps,
                    "lldp_neighbors": lldp_neighbors,
                    "ospfv2_lsas": ospfv2_lsas,
                    "ospfv3_lsas": ospfv3_lsas,
                    "rsvp_lsps": rsvp_lsps,
                },
                monitor_create_states_params.MonitorCreateStatesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitorCreateStatesResponse,
        )


class MonitorResourceWithRawResponse:
    def __init__(self, monitor: MonitorResource) -> None:
        self._monitor = monitor

        self.capture = to_custom_raw_response_wrapper(
            monitor.capture,
            BinaryAPIResponse,
        )
        self.create_metrics = to_raw_response_wrapper(
            monitor.create_metrics,
        )
        self.create_states = to_raw_response_wrapper(
            monitor.create_states,
        )


class AsyncMonitorResourceWithRawResponse:
    def __init__(self, monitor: AsyncMonitorResource) -> None:
        self._monitor = monitor

        self.capture = async_to_custom_raw_response_wrapper(
            monitor.capture,
            AsyncBinaryAPIResponse,
        )
        self.create_metrics = async_to_raw_response_wrapper(
            monitor.create_metrics,
        )
        self.create_states = async_to_raw_response_wrapper(
            monitor.create_states,
        )


class MonitorResourceWithStreamingResponse:
    def __init__(self, monitor: MonitorResource) -> None:
        self._monitor = monitor

        self.capture = to_custom_streamed_response_wrapper(
            monitor.capture,
            StreamedBinaryAPIResponse,
        )
        self.create_metrics = to_streamed_response_wrapper(
            monitor.create_metrics,
        )
        self.create_states = to_streamed_response_wrapper(
            monitor.create_states,
        )


class AsyncMonitorResourceWithStreamingResponse:
    def __init__(self, monitor: AsyncMonitorResource) -> None:
        self._monitor = monitor

        self.capture = async_to_custom_streamed_response_wrapper(
            monitor.capture,
            AsyncStreamedBinaryAPIResponse,
        )
        self.create_metrics = async_to_streamed_response_wrapper(
            monitor.create_metrics,
        )
        self.create_states = async_to_streamed_response_wrapper(
            monitor.create_states,
        )
