
from rest_framework import serializers
from .models import BlogUser, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
