from django.urls import path
from .views import SignupView, UserListView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import UserDeleteView


urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "users/",
        UserListView.as_view(),
        name="users"
    ),
   path(
    "users/<int:pk>/",
    UserDeleteView.as_view(),
    name="user-delete",
),
]