import pika
import json


def send_message_to_rabbit(body: dict):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='my-rabbitmq'))
        channel = connection.channel()

        channel.queue_declare(queue='test1')
        body_bytes = json.dumps(body, indent=2).encode('utf-8')
        channel.basic_publish(exchange='', routing_key='test1', body=body_bytes)
        print(f" [x] Sent '{body}'")
        connection.close()
        return 'Success'
    except:
        return 'Failed'
