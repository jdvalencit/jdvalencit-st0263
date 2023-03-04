from fastapi import FastAPI
from threading import Lock
from mom_rmq.rpc_client import mom_list, mom_search
import json

app = FastAPI()
mutex = Lock()
is_mom = True

@app.get("/")
def index():
    return balance(json.dumps({}))

@app.get("/list")
def list():
    return balance({"service": "list"})

@app.get("/search/{file}")
def search(file):
    return balance({"service": "search", "file": file})

def grcp(req):
    return "grcp comming soon"

def balance(req):
    global is_mom
    mutex.acquire()

    if is_mom == True:
        is_mom = False
        mutex.release()

        if req["service"] == "list":
            return mom_list(json.dumps(req))

        return mom_search(json.dumps(req))

    is_mom = True
    mutex.release()
    # if req["service"] == "list":
    #    return grcp_list(json.dumps(req))
    # return grcp_search(json.dumps(req))
    
    return grcp(json.dumps(req))