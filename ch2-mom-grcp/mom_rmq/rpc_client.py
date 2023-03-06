import pika
import uuid
import json

config = json.load(open(r'/home/ubuntu/jdvalencit-st0263/ch2-mom-grcp/config.json', 'r'))

class rpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=config['mom_client_host'],port=config['mom_client_port']))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(
            queue='rpc_client_queue', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, req):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_server_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=req)
        self.connection.process_data_events(time_limit=None)
        return self.response


rpc_client = rpcClient()


def mom_service(req):
    return rpc_client.call(req)
