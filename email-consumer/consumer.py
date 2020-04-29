import pika


class RabbitMQ:
    """
    """
    def __init__(self):
        """
        """
        self.routing_key = "direct_message_key"
        self.host = "localhost"
        self.exchange = "direct_exchange"
        self.queue = "test_queue"
        self.exchange_type = "direct"

    @staticmethod
    def call_back(ch, method, properties, body):
        """
        Call back method
        :param ch:
        :param method:
        :param properties:
        :param body:
        :return:
        """
        print("Receive message", body)

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
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=self.queue, on_message_callback=RabbitMQ.call_back, auto_ack=True)
        channel.start_consuming()


if __name__ == "__main__":
    config = RabbitMQ()
    config.create_connection()
