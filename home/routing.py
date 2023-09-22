from django.urls import re_path
from chat import consumer
from django.urls import path
from home.consumer import *
ws_patterns = [
    path('ws/test/', TestConsumer.as_asgi())
]