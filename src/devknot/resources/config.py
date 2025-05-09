# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import config_create_params, config_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.config import Config
from ..types.flow_param import FlowParam
from ..types.config_create_response import ConfigCreateResponse
from ..types.config_update_response import ConfigUpdateResponse

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devknot-python#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devknot-python#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        captures: Iterable[config_create_params.Capture] | NotGiven = NOT_GIVEN,
        devices: Iterable[config_create_params.Device] | NotGiven = NOT_GIVEN,
        egress_only_tracking: Iterable[config_create_params.EgressOnlyTracking] | NotGiven = NOT_GIVEN,
        events: config_create_params.Events | NotGiven = NOT_GIVEN,
        flows: Iterable[FlowParam] | NotGiven = NOT_GIVEN,
        lags: Iterable[config_create_params.Lag] | NotGiven = NOT_GIVEN,
        layer1: Iterable[config_create_params.Layer1] | NotGiven = NOT_GIVEN,
        lldp: Iterable[config_create_params.Lldp] | NotGiven = NOT_GIVEN,
        options: config_create_params.Options | NotGiven = NOT_GIVEN,
        ports: Iterable[config_create_params.Port] | NotGiven = NOT_GIVEN,
        stateful_flows: config_create_params.StatefulFlows | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigCreateResponse:
        """
        Sets configuration resources on the traffic generator.

        Args:
          captures: The capture settings that will be configured on the traffic generator.

          devices: The emulated devices that will be configured on the traffic generator. Each
              device contains configurations for network interfaces and protocols running on
              top of those interfaces.

          egress_only_tracking: Container for specification of desired tracking, based on certain offset and
              length of bits for received packets on specified receive ports. It enables the
              user to retrieve information based on number of unique packets received for each
              unique value in the bits being tracked from the beginning of the test.

          events: Under Review: Event configuration is currently under review for pending
              exploration on use cases.

              The optional container for event configuration. Both cp_events.enable and
              dp_events.enable must be explicitly set to true to get
              control_plane_data_plane_convergence_us metric values for convergence metrics.

          flows: The flows that will be configured on the traffic generator.

          lags: The LAGs that will be configured on the traffic generator.

          layer1: The layer1 settings that will be configured on the traffic generator. Since
              layer1 settings usually vary across variety of test ports, these most likely
              won't be portable.

          lldp: LLDP protocol that will be configured on traffic generator.

          options: Global configuration options.

          ports: The ports that will be configured on the traffic generator.

          stateful_flows: Conversational traffic where the responding side can be responded back with
              control messages, eg incase of rocev2 responding side can send ack, nak.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/config",
            body=maybe_transform(
                {
                    "captures": captures,
                    "devices": devices,
                    "egress_only_tracking": egress_only_tracking,
                    "events": events,
                    "flows": flows,
                    "lags": lags,
                    "layer1": layer1,
                    "lldp": lldp,
                    "options": options,
                    "ports": ports,
                    "stateful_flows": stateful_flows,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigCreateResponse,
        )

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Config:
        return self._get(
            "/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Config,
        )

    def update(
        self,
        *,
        choice: Literal["flows"] | NotGiven = NOT_GIVEN,
        flows: config_update_params.Flows | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigUpdateResponse:
        """
        Updates specific attributes of resources configured on the traffic generator.
        The fetched configuration shall reflect the updates applied successfully. The
        Response.Warnings in the Success response is available for implementers to
        disclose additional information about a state change including any implicit
        changes that are outside the scope of the state change.

        Args:
          flows: A container of flows with associated properties to be updated without affecting
              the flows current transmit state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/config",
            body=maybe_transform(
                {
                    "choice": choice,
                    "flows": flows,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateResponse,
        )


class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devknot-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devknot-python#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        captures: Iterable[config_create_params.Capture] | NotGiven = NOT_GIVEN,
        devices: Iterable[config_create_params.Device] | NotGiven = NOT_GIVEN,
        egress_only_tracking: Iterable[config_create_params.EgressOnlyTracking] | NotGiven = NOT_GIVEN,
        events: config_create_params.Events | NotGiven = NOT_GIVEN,
        flows: Iterable[FlowParam] | NotGiven = NOT_GIVEN,
        lags: Iterable[config_create_params.Lag] | NotGiven = NOT_GIVEN,
        layer1: Iterable[config_create_params.Layer1] | NotGiven = NOT_GIVEN,
        lldp: Iterable[config_create_params.Lldp] | NotGiven = NOT_GIVEN,
        options: config_create_params.Options | NotGiven = NOT_GIVEN,
        ports: Iterable[config_create_params.Port] | NotGiven = NOT_GIVEN,
        stateful_flows: config_create_params.StatefulFlows | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigCreateResponse:
        """
        Sets configuration resources on the traffic generator.

        Args:
          captures: The capture settings that will be configured on the traffic generator.

          devices: The emulated devices that will be configured on the traffic generator. Each
              device contains configurations for network interfaces and protocols running on
              top of those interfaces.

          egress_only_tracking: Container for specification of desired tracking, based on certain offset and
              length of bits for received packets on specified receive ports. It enables the
              user to retrieve information based on number of unique packets received for each
              unique value in the bits being tracked from the beginning of the test.

          events: Under Review: Event configuration is currently under review for pending
              exploration on use cases.

              The optional container for event configuration. Both cp_events.enable and
              dp_events.enable must be explicitly set to true to get
              control_plane_data_plane_convergence_us metric values for convergence metrics.

          flows: The flows that will be configured on the traffic generator.

          lags: The LAGs that will be configured on the traffic generator.

          layer1: The layer1 settings that will be configured on the traffic generator. Since
              layer1 settings usually vary across variety of test ports, these most likely
              won't be portable.

          lldp: LLDP protocol that will be configured on traffic generator.

          options: Global configuration options.

          ports: The ports that will be configured on the traffic generator.

          stateful_flows: Conversational traffic where the responding side can be responded back with
              control messages, eg incase of rocev2 responding side can send ack, nak.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/config",
            body=await async_maybe_transform(
                {
                    "captures": captures,
                    "devices": devices,
                    "egress_only_tracking": egress_only_tracking,
                    "events": events,
                    "flows": flows,
                    "lags": lags,
                    "layer1": layer1,
                    "lldp": lldp,
                    "options": options,
                    "ports": ports,
                    "stateful_flows": stateful_flows,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigCreateResponse,
        )

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Config:
        return await self._get(
            "/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Config,
        )

    async def update(
        self,
        *,
        choice: Literal["flows"] | NotGiven = NOT_GIVEN,
        flows: config_update_params.Flows | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigUpdateResponse:
        """
        Updates specific attributes of resources configured on the traffic generator.
        The fetched configuration shall reflect the updates applied successfully. The
        Response.Warnings in the Success response is available for implementers to
        disclose additional information about a state change including any implicit
        changes that are outside the scope of the state change.

        Args:
          flows: A container of flows with associated properties to be updated without affecting
              the flows current transmit state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/config",
            body=await async_maybe_transform(
                {
                    "choice": choice,
                    "flows": flows,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigUpdateResponse,
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.create = to_raw_response_wrapper(
            config.create,
        )
        self.retrieve = to_raw_response_wrapper(
            config.retrieve,
        )
        self.update = to_raw_response_wrapper(
            config.update,
        )


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.create = async_to_raw_response_wrapper(
            config.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            config.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            config.update,
        )


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.create = to_streamed_response_wrapper(
            config.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            config.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            config.update,
        )


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.create = async_to_streamed_response_wrapper(
            config.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            config.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            config.update,
        )
