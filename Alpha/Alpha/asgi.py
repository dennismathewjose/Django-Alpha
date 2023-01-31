"""
ASGI config for Alpha project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from chat.consumers import chatConsumer
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE','Alpha.settings')

application = ProtocolTypeRouter({
    'websocket' : AllowedHostsOriginValidator(
        URLRouter([
            path('ws/', chatConsumer.as_asgi())
        ])
    )
})

