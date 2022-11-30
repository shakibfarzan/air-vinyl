from rest_framework.permissions import BasePermission
from users.models import AuthUser


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == AuthUser.SUPER_ADMIN

class IsNormalUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == AuthUser.NORMAL_USER