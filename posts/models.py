from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model) :

    owner = models.ForeignKey(
        User,
        related_name='post_owner',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=225)
    body = models.TextField()

    likes_by = models.ManyToManyField(
        User,
        related_name='post_likes_by',
        blank=True
    )

    @property
    def total_likes_by (self) : 
        return self.likes_by.count()
    
    def __str__(self):
        return self.title
    

class Comment (models.Model) : 
    owner = models.ForeignKey(
        User,
        related_name='comment_owner',
        on_delete=models.CASCADE
    )

    post = models.ForeignKey(
        Post,
        related_name='comment',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    body = models.TextField()

    def __str__(self):
        return self.owner.username