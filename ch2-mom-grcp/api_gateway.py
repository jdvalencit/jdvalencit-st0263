import json
from fastapi import FastAPI
from threading import Lock
from mom_rmq.rpc_client import mom_service
from grpc_impl.grpc_client import grpc_service

app = FastAPI()
mutex = Lock()
is_mom = True


@app.get("/")
def index():
    return "Services provided:   /list/ -> Lists all files   /search/{file} -> Searches for specified file"


@app.get("/list")
def list():
    return balance({"service": "list"})


@app.get("/search/{file}")
def search(file):
    return balance({"service": "search", "file": file})


def balance(req):
    global is_mom
    mutex.acquire()

    if is_mom == True:
        is_mom = False
        mutex.release()
        return json.loads(mom_service(json.dumps(req)))

    is_mom = True
    mutex.release()
    return json.loads(grpc_service(json.dumps(req)))
