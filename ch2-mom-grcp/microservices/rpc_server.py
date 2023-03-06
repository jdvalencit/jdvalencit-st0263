import pika
import json
import os
import sys

path_to_files = ""

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
    for paths, _, files in os.walk(path_to_files):
        result += ["dir: "+paths,"files: "+str(files)]
    return json.dumps(result)

def search_service(file) -> str:
    for paths, _, files in os.walk(path_to_files):
        if file in files:
            return json.dumps({"method":"MOM","file":file,"status":"found","path":paths})
    return json.dumps({"method":"MOM","file":file,"status":"not found","path":""})

def main(argv):
    if len(argv) == 2:
        config_path = argv[1]
        config = json.load(open(config_path, 'r'))
        global path_to_files 
        path_to_files = config['dir_path']

        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=config['mom_host']))
        channel = connection.channel()
        channel.queue_declare(queue='rpc_server_queue')

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='rpc_server_queue', on_message_callback=on_request)
        channel.start_consuming()

if __name__ == '__main__':
    main(sys.argv)