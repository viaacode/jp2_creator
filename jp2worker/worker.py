import pika
from pika.credentials import PlainCredentials
from .rabbit_publisher import send_message
from json import loads, dumps
from .convertor import convert
from os.path import join


class Consumer:
    def __init__(self, arguments):
        self.host = arguments.broker_ip
        self.port = arguments.broker_port
        self.username = arguments.username
        self.password = arguments.password
        self.queue = arguments.incoming_queue
        self.result_exchange = arguments.result_exchange
        self.result_routing = arguments.result_routing
        self.result_queue = arguments.result_queue
        self.topic_type = arguments.topic_type

    def consume(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=self.host,
            port=self.port,
            credentials=PlainCredentials(self.username, self.password)
        ))

        channel = connection.channel()
        channel.queue_declare(queue=self.queue, durable=True)
        channel.basic_consume(self.callback, self.queue)
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        status = 'OK'
        details = 'file successfully converted'
        convert_params = loads(body.decode("utf-8"))
        try:
            source_file_path = join(convert_params['source_path'], convert_params['source_file'])
            dest_file_path = join(convert_params['destination_path'], convert_params['destination_file'])
            convert(source_file_path, dest_file_path)
        except Exception as e:
            status = 'NOK'
            if type(e).__name__ == 'CalledProcessError':
                details = str(e.output.decode("utf-8"))
            else:
                details = str(type(e)) + ":" + str(e)

        message = {
            "correlation_id": convert_params["correlation_id"],
            "status": status,
            "details": details,
            "destination_server": convert_params["destination_server"],
            "destination_path": convert_params["destination_path"],
            "destination_file": convert_params["destination_file"]
        }

        print(dumps(message))

        send_message(
            self.host,
            self.port,
            self.username,
            self.password,
            self.result_exchange,
            self.result_routing,
            self.result_queue,
            self.topic_type,
            dumps(message)
        )

        ch.basic_ack(delivery_tag=method.delivery_tag)
