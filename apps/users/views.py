
from .models import BlogUser, Post
from rest_framework import viewsets
from serializers import UserSerializer, PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = BlogUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects
    serializer_class = PostSerializer
