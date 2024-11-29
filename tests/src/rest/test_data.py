test_data = [
    {
        "query": {
            "customer_name": "John Doe",
            "start_date": "2022-01-01 00:00:00",
            "end_date": "2023-01-01 00:00:00",
            "ip": None,
        },
        "expected_answer": {"name": "John Doe", "total_traffic": 150.0},
    },
    {
        "query": {
            "customer_name": "Jane Smith",
            "start_date": "2022-01-01 00:00:00",
            "end_date": None,
            "ip": "192.168.5.110",
        },
        "expected_answer": {"name": "Jane Smith", "total_traffic": 560.0},
    },
    {
        "query": {
            "customer_name": "Alice Johnson",
            "start_date": None,
            "end_date": "2023-05-23 14:50:00",
            "ip": None,
        },
        "expected_answer": {"name": "Alice Johnson", "total_traffic": 175.00},
    },
    {
        "query": {
            "customer_name": "Bob Brown",
            "start_date": None,
            "end_date": None,
            "ip": "192.168.10.5",
        },
        "expected_answer": {"name": "Bob Brown", "total_traffic": 670.0},
    },
]
