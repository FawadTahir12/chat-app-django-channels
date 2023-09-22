from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import URLRouter, ProtocolTypeRouter
import chat.routing
import home.routing

# ws_patterns = [
#     path('ws/test/', TestConsumer.as_asgi())
# ]
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
       URLRouter(
           chat.routing.websocket_urlpatterns +
           home.routing.ws_patterns
       )
    ),
})