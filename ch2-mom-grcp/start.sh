#!/bin/bash

sudo systemctl start rabbitmq-server

sudo service nginx restart

python3 /home/ubuntu/jdvalencit-st0263/ch2-mom-grcp/microservices/rpc_server.py 

python3 /home/ubuntu/jdvalencit-st0263/ch2-mom-grcp/microservices/grpc_server.py

cd /home/ubuntu/jdvalencit-st0263/ch2-mom-grcp/

uvicorn api_gateway:app --reload
