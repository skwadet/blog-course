
from rest_framework import serializers
from .models import BlogUser, Post, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
