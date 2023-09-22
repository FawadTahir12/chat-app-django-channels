from django.urls import re_path
from chat import consumer
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)', consumer.ChatRoomConsumer.as_asgi()),
]