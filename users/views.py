from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from spotifyapp.utils.views import ReadWriteViewMixin
from users.models import NormalUser
from users.permissions import IsNormalUser, IsSuperAdmin
from users.serializers import NormalUserReadSerializer, NormalUserWriteSerializer


class NormalUserAPIView(viewsets.ModelViewSet, ReadWriteViewMixin):
    read_serializer = NormalUserReadSerializer
    write_serializer = NormalUserWriteSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsSuperAdmin]
        elif self.action in self.read_actions:
            self.permission_classes = [IsSuperAdmin | IsNormalUser] 
        return super().get_permissions()

    def get_queryset(self):
        return NormalUser.objects.filter()

    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))




