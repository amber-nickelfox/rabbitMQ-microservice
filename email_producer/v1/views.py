from django.shortcuts import render
from django.core.mail import send_mail
from .services import RabbitMQ
# Create your views here.


def index(request):
    """
    Render HTML page and send email as a producer in Queue using RabbitMQ as a Microservice
    :param request:
    :return:
    """
    RabbitMQ("Hello world").create_connection()
    # send_mail("Hello world", "Hello world", "amberawstest@gmail.com", ["amber@nickelfox.com"], fail_silently=False)
    return render(request, "index.html")
