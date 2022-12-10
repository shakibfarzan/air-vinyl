from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from spotifyapp.utils.general import StandardPagination
from spotifyapp.utils.views import ReadWriteViewMixin
from users.models import AuthUser, NormalUser
from users.permissions import IsNormalUser, IsSuperAdmin
from users.serializers import NormalUserReadSerializer, NormalUserWriteSerializer
from users.filters import NormalUserFilterSet


class NormalUserAPIView(viewsets.ModelViewSet, ReadWriteViewMixin):
    read_serializer = NormalUserReadSerializer
    write_serializer = NormalUserWriteSerializer
    pagination_class = StandardPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['email', 'created_at', 'first_name', 'last_name']
    filterset_class = NormalUserFilterSet

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsSuperAdmin]
        elif self.action in ['retrieve', 'partial_update', 'destroy']:
            self.permission_classes = [IsSuperAdmin | IsNormalUser] 
        return super().get_permissions()

    def get_queryset(self):
        if self.request.user.role == AuthUser.NORMAL_USER:
            return NormalUser.objects.filter(auth_user__id=self.request.user.id)
        return NormalUser.objects.filter()

    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get("pk"))




