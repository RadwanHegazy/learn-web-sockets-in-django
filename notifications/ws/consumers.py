from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class NotificationConsumer (WebsocketConsumer) : 

    def connect(self):
        self.user = self.scope['user']

        if self.user.is_anonymous:
            self.close()

        self.accept()
        self.GROUP_NAME = f"notification_{self.user.id}"

        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME,
            self.channel_name
        )        

    def disconnect(self, code):
        if self.user.is_authenticated:
            async_to_sync(self.channel_layer.group_discard)(
                self.GROUP_NAME,
                self.channel_name
            )        
    
    def receive(self, text_data = None, bytes_data = None):
        async_to_sync(self.channel_layer.group_send)(
            self.GROUP_NAME,
            {
                'type' : 'notify',
                'message' : text_data
            }
        )

    def notify(self, message) : 
        json_data = json.dumps({
            'message' : message['message']
        })
        self.send(json_data)