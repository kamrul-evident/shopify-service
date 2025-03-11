import pika
import json
import sys

# RabbitMQ configuration (matched to your existing code)
RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5674  # Your custom port
RABBITMQ_VHOST = "/"
RABBITMQ_USERNAME = "kamrul"
RABBITMQ_PASSWORD = "kamrul"
RABBITMQ_QUEUE = "order_queue"


def get_rabbitmq_connection():
    try:
        credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBITMQ_HOST,
                port=RABBITMQ_PORT,
                virtual_host=RABBITMQ_VHOST,
                credentials=credentials,
            )
        )
        channel = connection.channel()
        channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
        return connection, channel
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Failed to connect to RabbitMQ: {e}", file=sys.stderr)
        raise


def publish_to_rabbitmq(payload: dict):
    try:
        connection, channel = get_rabbitmq_connection()
        channel.basic_publish(
            exchange="",
            routing_key=RABBITMQ_QUEUE,
            body=json.dumps(payload).encode(),
            properties=pika.BasicProperties(delivery_mode=2),  # Persistent messages
        )
        connection.close()
    except Exception as e:
        print(f"Error publishing to RabbitMQ: {e}", file=sys.stderr)
        raise
