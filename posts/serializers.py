from rest_framework import serializers
from .models import Comment, Post


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

        return post

    def to_representation(self, instance):
        return {
            'message' : 'like added successfully !'
        }