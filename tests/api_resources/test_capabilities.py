# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from devknot import Devknot, AsyncDevknot
from tests.utils import assert_matches_type
from devknot.types import CapabilityRetrieveVersionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCapabilities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_version(self, client: Devknot) -> None:
        capability = client.capabilities.retrieve_version()
        assert_matches_type(CapabilityRetrieveVersionResponse, capability, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_version(self, client: Devknot) -> None:
        response = client.capabilities.with_raw_response.retrieve_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = response.parse()
        assert_matches_type(CapabilityRetrieveVersionResponse, capability, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_version(self, client: Devknot) -> None:
        with client.capabilities.with_streaming_response.retrieve_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = response.parse()
            assert_matches_type(CapabilityRetrieveVersionResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCapabilities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_version(self, async_client: AsyncDevknot) -> None:
        capability = await async_client.capabilities.retrieve_version()
        assert_matches_type(CapabilityRetrieveVersionResponse, capability, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_version(self, async_client: AsyncDevknot) -> None:
        response = await async_client.capabilities.with_raw_response.retrieve_version()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        capability = await response.parse()
        assert_matches_type(CapabilityRetrieveVersionResponse, capability, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_version(self, async_client: AsyncDevknot) -> None:
        async with async_client.capabilities.with_streaming_response.retrieve_version() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            capability = await response.parse()
            assert_matches_type(CapabilityRetrieveVersionResponse, capability, path=["response"])

        assert cast(Any, response.is_closed) is True
