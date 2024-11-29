import asyncio

import aiohttp
import grpc
import pytest_asyncio


@pytest_asyncio.fixture(scope="module")
def grpc_channel():
    channel = grpc.insecure_channel("fastapi:50051")
    yield channel
    channel.close()


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(name="http_session", scope="session")
async def http_session():
    http_session = aiohttp.ClientSession(base_url="http://fastapi:8080")
    yield http_session
    await http_session.close()


@pytest_asyncio.fixture(name="http_session_get")
def http_session_get(http_session: aiohttp.ClientSession) -> callable:
    async def inner(url: str, query_data: dict = None) -> list:
        params = {
            key: value
            for key, value in query_data["query"].items()
            if value is not None
        }
        async with http_session.get("/traffic" + url, params=params) as response:
            return [await response.json(), response.headers, response.status]

    return inner
