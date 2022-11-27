import pika
from fastapi.logger import logger
from aio_pika import connect_robust
import json
from api_fast import create_request


class PikaClient:

    def __init__(self):
        self.publish_queue_name = "test1"  # env('PUBLISH_QUEUE', 'foo_publish_queue')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")  # env('RABBIT_HOST', '127.0.0.1')
        )
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(queue=self.publish_queue_name)
        self.callback_queue = self.publish_queue.method.queue
        self.response = None
        self.process_callable = create_request
        logger.info('Pika connection initialized')

    async def consume(self, loop):
        """Setup message listener with the current running loop"""
        connection = await connect_robust(host="localhost",
                                          port=5672,
                                          loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue("test1")
        await queue.consume(self.process_incoming_message, no_ack=False)
        print('Established pika async listener')
        return connection

    async def process_incoming_message(self, message):
        """Processing incoming message from RabbitMQ"""
        # message.ack()
        body = message.body
        print('Received message')
        if body:
            self.process_callable(json.loads(body))
