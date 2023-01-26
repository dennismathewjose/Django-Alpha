from channels.routing import ProtocolTypeRouter, URLRouter
from channel.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({
     'websockets' : AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
     ),
})