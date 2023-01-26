from django.conf.urls import url 
from django.urls import path, re_path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:roomname',consumers.Chatconsumer.as_asgi())
]