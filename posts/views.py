from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    CreateCommentSerializer,
    CreateLikePostSerializer
)


class CreateCommentAPI (CreateAPIView) : 
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCommentSerializer

class CreatePostLikeAPI (CreateAPIView) : 
    permission_classes = [IsAuthenticated]
    serializer_class = CreateLikePostSerializer