from channels.auth import AuthMiddlewareStack # users have to be authorized to enter chatroom
from channels.routing import ProtocolTypeRouter, URLRouter
import chatapp.routing
from django.core.asgi import get_asgi_application


# when ws request rout it to ...
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chatapp.routing.websocket_urlpatterns
        )
    ),
})