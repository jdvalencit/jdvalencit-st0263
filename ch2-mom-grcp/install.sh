#!/bin/bash

sudo apt-get update
yes Y | sudo apt-get install rabbitmq-server
sudo apt install nginx
sudo apt install python3-pip
pip install pika
pip install grpcio grpcio-tools
pip install fastapi
pip install uvicorn
