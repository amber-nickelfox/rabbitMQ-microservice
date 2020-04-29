import pika
import smtplib
import json


class SendEmail:
    """
    send email as a background process
    """
    def __init__(self, sender, receiver, message):
        """
        send email
        :param sender: sender email
        :param receiver: receiver email
        :param message: message plain text for now
        """
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.host = "smtp.gmail.com"
        self.sender_password = "random_password"

    def send_email(self):
        """
        send email functionality
        :return:
        """
        s = smtplib.SMTP(self.host, 587)
        # start TLS for security
        s.starttls()
        # Authentication using credentials
        s.login(self.sender, self.sender_password)
        # message to be sent
        message = self.message
        # sending the mail
        s.sendmail(self.sender, self.receiver, message)
        # terminating the session
        s.quit()


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
        data = json.loads(body)
        SendEmail(data['sender'], data['receiver'], data['message']).send_email()
        print("Email sent")

    def create_connection(self):
        """
        create connection and channel
        :return:
        """
        # Create  RabbitMQ connection instance, this connection uses TCP as protocol
        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        # Create a channel, all the client operations happens on a channel
        channel = connection.channel()
        # Create an Exchange, The responsibility of the Exchange is to route the messages to the queue or queues.
        channel.exchange_declare(exchange=self.exchange, exchange_type=self.exchange_type)
        # We create a queue with queue — the queue name and durable as parameter.
        channel.queue_declare(queue=self.queue, durable=True)
        channel.queue_bind(exchange=self.exchange, queue=self.queue, routing_key=self.routing_key)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=self.queue, on_message_callback=RabbitMQ.call_back, auto_ack=True)
        channel.start_consuming()


if __name__ == "__main__":
    config = RabbitMQ()
    config.create_connection()
