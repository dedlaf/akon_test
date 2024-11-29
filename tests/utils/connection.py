import asyncio

import grpc
from aiohttp import ClientConnectorError, ClientSession
from grpc_config import traffic_pb2, traffic_pb2_grpc


async def wait_for_server(url, retries=5, delay=2):
    for _ in range(retries):
        try:
            async with ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        print("Server is up and running!")
                        return True
        except ClientConnectorError as e:
            print("Server is not up yet, retrying...", e)
            await asyncio.sleep(delay)
    print("Server did not become available after retries")
    return False


async def wait_for_grpc_server(target, retries=5, delay=2):
    for _ in range(retries):
        try:
            async with grpc.aio.insecure_channel(target) as channel:
                stub = traffic_pb2_grpc.TrafficServiceStub(channel)
                request = traffic_pb2.TrafficRequest(
                    customer_name="Test", start_date="2022-01-01 00:00:00"
                )
                stub.GetTraffic(request)
                print("gRPC Server is up and running!")
                return True
        except grpc.aio._call.AioRpcError as e:
            print("gRPC server is not up yet, retrying...", e)
            await asyncio.sleep(delay)
    print("gRPC server did not become available after retries")
    return False


asyncio.run(wait_for_server("http://fastapi:8080/traffic/"))
asyncio.run(wait_for_grpc_server("fastapi:50051"))
