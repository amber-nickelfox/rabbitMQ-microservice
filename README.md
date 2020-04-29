# RABBIT MQ Micro service  for sending email

#### There are two sections
* Email producer: Django application, which publish the email in queue
* Email consumer: A microservice which consume the email data (receiver and message) and execute in background

#### Run application

1 . Create and activate Virtualenv:

```
virtualenv venv
source venv/bin/activate
```

2 . Install requirements:

```
pip install -r requirements.txt
```

3 . Open terminal and run consumer service
Before running this setup the email credentials in consumer.py

Note: The credentials will move to env file.

```
cd email-consumer
python consumer.py
```
It starts consuming

4 . Open another terminal and run django application

```
cd email_producer
python manage.py migrate
python manage.py runserver
```

In web browser go to [http://localhost:8000](http://localhost:8000)

When you hit enter it will immediate show the page but in background email
sending task is performed
Check in consumer teminal for response.


