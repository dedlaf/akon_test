from . import traffic_pb2

test_data = [
    {
        "request": traffic_pb2.TrafficRequest(
            customer_name="John Doe", start_date="2022-01-01 00:00:00"
        ),
        "expected_answer": traffic_pb2.TrafficResponse(
            name="John Doe", total_traffic=410.0
        ),
    },
    {
        "request": traffic_pb2.TrafficRequest(
            customer_name="Jane Smith",
            start_date="2022-01-01 00:00:00",
            ip="192.168.5.110",
        ),
        "expected_answer": traffic_pb2.TrafficResponse(
            name="Jane Smith", total_traffic=560.0
        ),
    },
    {
        "request": traffic_pb2.TrafficRequest(
            customer_name="Alice Johnson", end_date="2023-05-23 14:50:00"
        ),
        "expected_answer": traffic_pb2.TrafficResponse(
            name="Alice Johnson", total_traffic=175.00
        ),
    },
    {
        "request": traffic_pb2.TrafficRequest(
            customer_name="Bob Brown", ip="192.168.10.5"
        ),
        "expected_answer": traffic_pb2.TrafficResponse(
            name="Bob Brown", total_traffic=670.00
        ),
    },
]
