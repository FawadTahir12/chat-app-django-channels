"""
ASGI config for Djangochannel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

import django
from django.core.asgi import get_asgi_application
from channels.routing import  get_default_application,ProtocolTypeRouter, URLRouter
from django.urls import path
from home.consumer import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Djangochannel.settings')
# django.setup()
#
# application = get_asgi_application()
#
# ws_patterns = [
#     path('ws/test/', TestConsumer.as_asgi())
# ]
#
# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': URLRouter(ws_patterns)
# })