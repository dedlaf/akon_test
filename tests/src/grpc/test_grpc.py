import pytest

from .config import traffic_pb2_grpc
from .config.test_data import test_data


@pytest.mark.parametrize("test_case", test_data)
def test_get_traffic(grpc_channel, test_case):
    stub = traffic_pb2_grpc.TrafficServiceStub(grpc_channel)
    response = stub.GetTraffic(test_case["request"])
    for res in response:
        assert res.name == test_case["expected_answer"].name
        assert res.total_traffic == test_case["expected_answer"].total_traffic
