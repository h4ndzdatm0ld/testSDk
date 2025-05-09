# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import control_set_state_params, control_trigger_action_params
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
from ..types.control_set_state_response import ControlSetStateResponse
from ..types.control_trigger_action_response import ControlTriggerActionResponse

__all__ = ["ControlResource", "AsyncControlResource"]


class ControlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ControlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/h4ndzdatm0ld/testSDk#accessing-raw-response-data-eg-headers
        """
        return ControlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ControlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/h4ndzdatm0ld/testSDk#with_streaming_response
        """
        return ControlResourceWithStreamingResponse(self)

    def set_state(
        self,
        *,
        choice: Literal["port", "protocol", "traffic"],
        port: control_set_state_params.Port | NotGiven = NOT_GIVEN,
        protocol: control_set_state_params.Protocol | NotGiven = NOT_GIVEN,
        traffic: control_set_state_params.Traffic | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ControlSetStateResponse:
        """
        Sets the operational state of configured resources.

        Args:
          port: States associated with configured ports.

          protocol: States associated with protocols on configured resources.

          traffic: States associated with configured flows

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/control/state",
            body=maybe_transform(
                {
                    "choice": choice,
                    "port": port,
                    "protocol": protocol,
                    "traffic": traffic,
                },
                control_set_state_params.ControlSetStateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ControlSetStateResponse,
        )

    def trigger_action(
        self,
        *,
        choice: Literal["protocol"],
        protocol: control_trigger_action_params.Protocol | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ControlTriggerActionResponse:
        """
        Triggers actions against configured resources.

        Args:
          protocol: Actions associated with protocols on configured resources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/control/action",
            body=maybe_transform(
                {
                    "choice": choice,
                    "protocol": protocol,
                },
                control_trigger_action_params.ControlTriggerActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ControlTriggerActionResponse,
        )


class AsyncControlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncControlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/h4ndzdatm0ld/testSDk#accessing-raw-response-data-eg-headers
        """
        return AsyncControlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncControlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/h4ndzdatm0ld/testSDk#with_streaming_response
        """
        return AsyncControlResourceWithStreamingResponse(self)

    async def set_state(
        self,
        *,
        choice: Literal["port", "protocol", "traffic"],
        port: control_set_state_params.Port | NotGiven = NOT_GIVEN,
        protocol: control_set_state_params.Protocol | NotGiven = NOT_GIVEN,
        traffic: control_set_state_params.Traffic | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ControlSetStateResponse:
        """
        Sets the operational state of configured resources.

        Args:
          port: States associated with configured ports.

          protocol: States associated with protocols on configured resources.

          traffic: States associated with configured flows

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/control/state",
            body=await async_maybe_transform(
                {
                    "choice": choice,
                    "port": port,
                    "protocol": protocol,
                    "traffic": traffic,
                },
                control_set_state_params.ControlSetStateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ControlSetStateResponse,
        )

    async def trigger_action(
        self,
        *,
        choice: Literal["protocol"],
        protocol: control_trigger_action_params.Protocol | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ControlTriggerActionResponse:
        """
        Triggers actions against configured resources.

        Args:
          protocol: Actions associated with protocols on configured resources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/control/action",
            body=await async_maybe_transform(
                {
                    "choice": choice,
                    "protocol": protocol,
                },
                control_trigger_action_params.ControlTriggerActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ControlTriggerActionResponse,
        )


class ControlResourceWithRawResponse:
    def __init__(self, control: ControlResource) -> None:
        self._control = control

        self.set_state = to_raw_response_wrapper(
            control.set_state,
        )
        self.trigger_action = to_raw_response_wrapper(
            control.trigger_action,
        )


class AsyncControlResourceWithRawResponse:
    def __init__(self, control: AsyncControlResource) -> None:
        self._control = control

        self.set_state = async_to_raw_response_wrapper(
            control.set_state,
        )
        self.trigger_action = async_to_raw_response_wrapper(
            control.trigger_action,
        )


class ControlResourceWithStreamingResponse:
    def __init__(self, control: ControlResource) -> None:
        self._control = control

        self.set_state = to_streamed_response_wrapper(
            control.set_state,
        )
        self.trigger_action = to_streamed_response_wrapper(
            control.trigger_action,
        )


class AsyncControlResourceWithStreamingResponse:
    def __init__(self, control: AsyncControlResource) -> None:
        self._control = control

        self.set_state = async_to_streamed_response_wrapper(
            control.set_state,
        )
        self.trigger_action = async_to_streamed_response_wrapper(
            control.trigger_action,
        )
