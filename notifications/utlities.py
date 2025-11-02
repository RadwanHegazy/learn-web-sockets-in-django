from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import Notification

def send_real_time_message(sender, reciver, msg) :
    Notification.objects.create(
        sender = sender,
        reciver = reciver,
        title = msg
    )

    GROUP_NAME = f"notification_{reciver.id}"
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        GROUP_NAME,
        {
            'type' : 'notify',
            'message' : msg
        }
    )
