import grpc
import sys
import os
import json
from concurrent import futures
import grpc_service_pb2
import grpc_service_pb2_grpc

config = {}

class fileServices(grpc_service_pb2_grpc.fileServicesServicer):
    def list(self, request, context):
        result: str = []
        for paths, _, files in os.walk(config['dir_path']):
            result += ["dir: "+paths, " files: "+str(files)]
        return grpc_service_pb2.list_res(
            method="gRPC",
            files=result
        )

    def search(self, request, context):
        for path, _, files in os.walk(config['dir_path']):
            if request.file_name in files:
                return grpc_service_pb2.search_res(
                    method="gRPC",
                    file_to_find=request.file_name,
                    status="found",
                    path=path
                )
        return grpc_service_pb2.search_res(
            method="gRPC",
            file_to_find=request.file_name,
            status="not found",
            path=""
        )


def main(argv):
    global config
    if len(argv) == 2:
        config_path = argv[1]
        config = json.load(open(config_path, 'r'))

        server = grpc.server(futures.ThreadPoolExecutor(
            max_workers=config['grpc_workers']))
        grpc_service_pb2_grpc.add_fileServicesServicer_to_server(
            fileServices(), server)

        server.add_insecure_port(f"[::]:{config['grpc_port']}")
        server.start()
        server.wait_for_termination()


if __name__ == '__main__':
    main(sys.argv)
