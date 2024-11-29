from http import HTTPStatus

import pytest

from .test_data import test_data

pytestmark = pytest.mark.asyncio


@pytest.mark.parametrize("query_data", test_data)
async def test_get(
    http_session_get: pytest.fixture, query_data: list[dict[str, any]]
) -> None:
    body, headers, status = await http_session_get("/", query_data)
    assert status == HTTPStatus.OK
    assert body[0]["name"] == query_data["expected_answer"]["name"]
    assert body[0]["total_traffic"] == query_data["expected_answer"]["total_traffic"]
