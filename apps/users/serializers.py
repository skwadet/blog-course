
from rest_framework import serializers
from .models import BlogUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUser
        fields = "__all__"
