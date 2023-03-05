import grpc
import os
import json
from concurrent import futures
import grpc_service_pb2
import grpc_service_pb2_grpc

class fileServices(grpc_service_pb2_grpc.fileServicesServicer):
    def list(self, request, context):
        result: str = []
        for paths, _, files in os.walk('files'):
            result += ["dir: "+paths," files: "+str(files)]
        return grpc_service_pb2.list_res(
            method = "gRPC",
            files = result
            )

    def search(self, request, context):
        for path, _, files in os.walk('files'):
            if request.file_name in files:
                return grpc_service_pb2.search_res(
                    method="gRPC",
                    file_to_find=request.file_name,
                    status="found",
                    path=path
                )
        return grpc_service_pb2.search_res(
            method="gRPC",
            file_to_find = request.file_name,
            status="not found",
            path=""
        )

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
grpc_service_pb2_grpc.add_fileServicesServicer_to_server(fileServices(), server)

server.add_insecure_port('localhost:50051')
server.start()
server.wait_for_termination()

