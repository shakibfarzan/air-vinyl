from rest_framework.permissions import IsAuthenticated
from users.models import AuthUser

class IsArtist(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(super().has_permission(request, view) and request.user.role == AuthUser.ARTIST)