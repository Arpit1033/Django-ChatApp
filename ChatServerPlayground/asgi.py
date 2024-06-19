import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import personal.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatServerPlayground.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(
        personal.routing.websocket_urlpatterns
    )
})
