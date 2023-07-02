from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from channelApp1 import consumer

websocket_urlPattern=[
    path('ws/polData/', consumer.DashConsumer),
]

application=ProtocolTypeRouter({
    # 'http':
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))
})