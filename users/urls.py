from django.urls import path
from users.views import NormalUserAPIView


urlpatterns = [
    path("normal-users/", NormalUserAPIView.as_view({ "get": "list", "post": "create"}), name="normal-user"),
    path("normal-users/<int:pk>/", NormalUserAPIView.as_view({"get": "retrieve", "patch": "partial_update", "delete": "destroy"}), name="normal-user-detail")
]
