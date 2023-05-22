import json
import grpc
from grpc_impl import grpc_service_pb2
from grpc_impl import grpc_service_pb2_grpc

config = json.load(open(r"/home/ubuntu/jdvalencit-st0263/ch2-mom-grcp/config.json", 'r'))


def list(stub):
    response = stub.list(grpc_service_pb2.list_req())
    res = {"method": response.method, "list": "".join(response.files)}
    return json.dumps(res)


def search(stub, file):
    response = stub.search(grpc_service_pb2.search_req(file_name=file))
    res = {"method":response.method,"file":file,"status":response.status,"path":response.path}
    return json.dumps(res)


def grpc_service(req):
    with grpc.insecure_channel(f"{config['grpc_client_host']}:{config['grpc_client_port']}") as channel:
        stub = grpc_service_pb2_grpc.fileServicesStub(channel)
        smg = json.loads(req)
        serv = smg["service"]

        if serv == "list":
            return list(stub)

        file = smg["file"]
        return search(stub, file)
