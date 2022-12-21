from django.urls import path
from airvinyl.utils.general import LIST_CREATE_MODEL_VIEW_SET, DETAIL_MODEL_VIEW_SET
from users.views import NormalUserAPIView, PremiumPlanAPIView, SuperAdminAPIView


urlpatterns = [
    path("super-admins/", SuperAdminAPIView.as_view(LIST_CREATE_MODEL_VIEW_SET), name="super-admin"),
    path("super-admins/<int:pk>/", SuperAdminAPIView.as_view(DETAIL_MODEL_VIEW_SET), name="super-admin-detail"),
    path("normal-users/", NormalUserAPIView.as_view(LIST_CREATE_MODEL_VIEW_SET), name="normal-user"),
    path("normal-users/<int:pk>/", NormalUserAPIView.as_view(DETAIL_MODEL_VIEW_SET), name="normal-user-detail"),
    path("premium-plans/", PremiumPlanAPIView.as_view(LIST_CREATE_MODEL_VIEW_SET), name="premium-plan"),
    path("premium-plans/<int:pk>/", PremiumPlanAPIView.as_view(DETAIL_MODEL_VIEW_SET), name="premium-plan-detail")
]
