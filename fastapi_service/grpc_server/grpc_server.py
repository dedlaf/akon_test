from concurrent import futures
from datetime import datetime

import grpc
from db.sqlite import get_db
from grpc_reflection.v1alpha import reflection
from models.models import Customer, Traffic
from sqlalchemy import func

from . import traffic_pb2, traffic_pb2_grpc
from schemas.schemas import TrafficQuery


class TrafficService(traffic_pb2_grpc.TrafficServiceServicer):
    def GetTraffic(self, request, context):
        try:
            data = TrafficQuery(
                customer_name=request.customer_name,
                start_date=datetime.strptime(request.start_date, "%Y-%m-%d %H:%M:%S") if request.start_date else None,
                end_date=datetime.strptime(request.end_date, "%Y-%m-%d %H:%M:%S") if request.end_date else None,
                ip=request.ip if request.ip else None,
            )
        except ValueError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

        filters = [
            Customer.name == data.customer_name if data.customer_name else None,
            Traffic.date >= data.start_date if data.start_date else None,
            Traffic.date <= data.end_date if data.end_date else None,
            Traffic.ip == data.ip if data.ip else None,
        ]

        filters = [f for f in filters if f is not None]

        with get_db() as db:
            query = (
                db.query(
                    Customer.name,
                    func.sum(Traffic.received_traffic).label("total_traffic"),
                )
                .join(Traffic)
                .filter(*filters)
                .group_by(Customer.name)
            )
            results = query.all()

            for result in results:
                yield traffic_pb2.TrafficResponse(
                    name=result[0], total_traffic=result[1]
                )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    traffic_pb2_grpc.add_TrafficServiceServicer_to_server(TrafficService(), server)
    SERVICE_NAMES = (
        traffic_pb2.DESCRIPTOR.services_by_name["TrafficService"].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
