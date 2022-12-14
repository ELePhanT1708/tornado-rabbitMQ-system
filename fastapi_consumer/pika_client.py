import pika
from fastapi.logger import logger
from aio_pika import connect_robust
import json
import os
import crud



class PikaClient:

    def __init__(self):
        self.publish_queue_name = "test1"  # env('PUBLISH_QUEUE', 'foo_publish_queue')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="my-rabbitmq")  # env('RABBIT_HOST', '127.0.0.1')
        )
        self.channel = self.connection.channel()
        self.publish_queue = self.channel.queue_declare(queue=self.publish_queue_name)
        self.callback_queue = self.publish_queue.method.queue
        self.response = None
        logger.info('Pika connection initialized')

    async def consume(self, loop):
        """Setup message listener with the current running loop"""
        connection = await connect_robust(host=os.getenv("HOST_FROM"),
                                          port=os.getenv("PORT_FROM"),
                                          loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue(os.getenv("QUEUE_NAME"))
        await queue.consume(self.process_incoming_message, no_ack=False)
        print('Established pika async listener')
        return connection

    async def process_incoming_message(self, message):
        """Processing incoming message from RabbitMQ"""
        # message.ack()
        body = message.body
        print('Received message')
        if body:
            crud.create_request(json.loads(body))
        else:
            print("Body is empty ! ")
