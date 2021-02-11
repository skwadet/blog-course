
from .models import BlogUser
from rest_framework import viewsets

from serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = BlogUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

