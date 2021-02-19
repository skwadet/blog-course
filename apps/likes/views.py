from rest_framework import viewsets
from .models import Like
from serializers import LikeSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects
    serializer_class = LikeSerializer
