#!/usr/bin/env python
import os
import pika
import sys
import json


def get_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='test1')

    def callback(ch, method, properties, body):
        print(f" [x] Received: Surname : {json.loads(body)['surname']}")
        return json.loads(body)

    channel.basic_consume(queue='test1', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        get_message()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
