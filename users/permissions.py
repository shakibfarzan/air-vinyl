from rest_framework.permissions import IsAuthenticated
from users.models import AuthUser


class IsSuperAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) and request.user.role == AuthUser.SUPER_ADMIN)

class IsNormalUser(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) and request.user.role == AuthUser.NORMAL_USER)