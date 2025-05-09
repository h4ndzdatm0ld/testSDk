# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.capability_retrieve_version_response import CapabilityRetrieveVersionResponse

__all__ = ["CapabilitiesResource", "AsyncCapabilitiesResource"]


class CapabilitiesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CapabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devknot-python#accessing-raw-response-data-eg-headers
        """
        return CapabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CapabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devknot-python#with_streaming_response
        """
        return CapabilitiesResourceWithStreamingResponse(self)

    def retrieve_version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CapabilityRetrieveVersionResponse:
        return self._get(
            "/capabilities/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CapabilityRetrieveVersionResponse,
        )


class AsyncCapabilitiesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCapabilitiesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/devknot-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCapabilitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCapabilitiesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/devknot-python#with_streaming_response
        """
        return AsyncCapabilitiesResourceWithStreamingResponse(self)

    async def retrieve_version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CapabilityRetrieveVersionResponse:
        return await self._get(
            "/capabilities/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CapabilityRetrieveVersionResponse,
        )


class CapabilitiesResourceWithRawResponse:
    def __init__(self, capabilities: CapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.retrieve_version = to_raw_response_wrapper(
            capabilities.retrieve_version,
        )


class AsyncCapabilitiesResourceWithRawResponse:
    def __init__(self, capabilities: AsyncCapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.retrieve_version = async_to_raw_response_wrapper(
            capabilities.retrieve_version,
        )


class CapabilitiesResourceWithStreamingResponse:
    def __init__(self, capabilities: CapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.retrieve_version = to_streamed_response_wrapper(
            capabilities.retrieve_version,
        )


class AsyncCapabilitiesResourceWithStreamingResponse:
    def __init__(self, capabilities: AsyncCapabilitiesResource) -> None:
        self._capabilities = capabilities

        self.retrieve_version = async_to_streamed_response_wrapper(
            capabilities.retrieve_version,
        )
