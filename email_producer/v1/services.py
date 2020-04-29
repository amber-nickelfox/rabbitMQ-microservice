import pika
import json


class SendEmailRabbitMQ:
    """
    """
    def __init__(self, message):
        """

        :param message:
        """
        self.routing_key = "direct_message_key"
        self.host = "localhost"
        self.exchange = "direct_exchange"
        self.queue = "test_queue"
        self.exchange_type = "direct"
        self.message = message

    def create_connection(self):
        """
        create connection and channel
        :return:
        """
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        channel = connection.channel()
        channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type)
        channel.queue_declare(queue=self.queue, durable=True)
        channel.queue_bind(exchange=self.exchange, queue=self.queue, routing_key=self.routing_key)
        channel.confirm_delivery()
        try:
            print("Here to publish message")
            channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=json.dumps(self.message),
                                  properties=pika.BasicProperties(delivery_mode=2))
            print("Message sent")
        except Exception as ex:
            print("Failed to send message", ex)
        connection.close()
