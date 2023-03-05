import pika
import json
import os

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_server_queue')
def on_request(ch, method, props, body):

    msg = json.loads(body)
    serv = msg["service"]

    response: str
    if serv == "list":
        response = list_service()
    else:
        response = search_service(msg["file"])

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=response)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def list_service() -> str:
    result: str = ["method: MOM "]
    for paths, _, files in os.walk('files'):
        result += ["dir: "+paths,"files: "+str(files)]
    return json.dumps(result)

def search_service(file) -> str:
    for paths, _, files in os.walk('files'):
        if file in files:
            return json.dumps({"method":"MOM","file":file,"status":"found","path":paths})
    return json.dumps({"method":"MOM","file":file,"status":"not found","path":""})

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_server_queue', on_message_callback=on_request)

print(" [x] Awaiting RPC requests")
channel.start_consuming()