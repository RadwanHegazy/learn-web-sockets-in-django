from .consumers import NotificationConsumer
from django.urls import path

ws_urls = [
    path('ws/notifications', NotificationConsumer.as_asgi())
]