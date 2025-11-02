from django.db import models
from django.contrib.auth.models import User


class Notification (models.Model) : 
    sender = models.ForeignKey(User, related_name='notifcation_sender', on_delete=models.CASCADE)
    reciver = models.ForeignKey(User, related_name='notifcation_reciver', on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title