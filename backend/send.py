import pika
import json
import os


def send_message_to_rabbit(body: dict):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=os.getenv("HOST_TO")))
        channel = connection.channel()

        channel.queue_declare(queue=os.getenv("QUEUE_NAME"))
        body_bytes = json.dumps(body, indent=2).encode('utf-8')
        channel.basic_publish(exchange='', routing_key=os.getenv("QUEUE_NAME"), body=body_bytes)
        print(f" [x] Sent '{body}'")
        connection.close()
        return 'Success'
    except:
        return 'Failed'
