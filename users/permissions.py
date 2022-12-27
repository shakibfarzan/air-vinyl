from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from users.models import AuthUser


class IsSuperAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) and request.user.role == AuthUser.SUPER_ADMIN)

class IsNormalUser(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) and request.user.role == AuthUser.NORMAL_USER)

class IsSuperAdminOrReadOnly(IsSuperAdmin):
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method in SAFE_METHODS
