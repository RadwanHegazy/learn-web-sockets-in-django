from rest_framework import serializers
from .models import Comment, Post
from notifications.utlities import send_real_time_message

class CreateCommentSerializer (serializers.ModelSerializer) : 
    owner = serializers.HiddenField(
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'body',
            'post'
        ]

    def save(self, **kwargs):
        comment : Comment = super().save(**kwargs)
        send_real_time_message(
            comment.owner,
            comment.post.owner,
            f"{comment.owner} add comment to your post, the comment is : '{comment.body}' "
        )
        return comment

class CreateLikePostSerializer (serializers.Serializer) : 
    post = serializers.PrimaryKeyRelatedField(
        queryset = Post.objects.all()
    )


    def create(self, validated_data):
        post : Post = validated_data.get('post')
        
        request = self.context.get('request')
        user = request.user
        
        if user not in post.likes_by.all() : 
            post.likes_by.add(user)
            post.save()

            # Sending real-time msg
            send_real_time_message(
                sender = user,
                reciver = post.owner,
                msg = f"{user.username} likes your post !"
            )

        return post

    def to_representation(self, instance):
        return {
            'message' : 'like added successfully !'
        }