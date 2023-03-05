import json
import grpc
from grpc_impl import grpc_service_pb2
from grpc_impl import grpc_service_pb2_grpc

def list(stub):
    response = stub.list(grpc_service_pb2.list_req())
    res = {"method":response.method,"list":"".join(response.files)}
    return json.dumps(res)

def search(stub, file):
    response = stub.search(grpc_service_pb2.search_req(file_name=file))
    res = {"method":response.method,"file":file,"status":response.status,"path":response.path}
    return json.dumps(res)
    

def grpc_service(req):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_service_pb2_grpc.fileServicesStub(channel)
        smg = json.loads(req)
        serv = smg["service"]

        if serv == "list":
            return list(stub)

        file = smg["file"]
        return search(stub, file)