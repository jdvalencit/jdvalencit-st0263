import grpc
import os
import json
import grpc_service_pb2
import grpc_service_pb2_grpc
from concurrent import futures

config = json.load(open(r'/home/ubuntu/jdvalencit-st0263/ch2-mom-grcp/config.json', 'r'))


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


def main():
    server = grpc.server(futures.ThreadPoolExecutor(
        max_workers=config['grpc_workers']))
    grpc_service_pb2_grpc.add_fileServicesServicer_to_server(
        fileServices(), server)

    server.add_insecure_port(f"{config['grpc_server_host']}:{config['grpc_server_port']}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    main()
