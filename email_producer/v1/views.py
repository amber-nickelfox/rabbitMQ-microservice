from django.shortcuts import render
from .services import SendEmailRabbitMQ
# Create your views here.


def index(request):
    """
    Render HTML page and send email as a producer in Queue using RabbitMQ as a Microservice
    :param request:
    :return:
    """
    email_context = {
        "receiver": "test@nickelfox.com",
        "message": "Hello world"
    }
    # Send email context
    SendEmailRabbitMQ(email_context).create_connection()
    # send_mail("Hello world", "Hello world", "amberawstest@gmail.com", ["amber@nickelfox.com"], fail_silently=False)
    return render(request, "index.html")
