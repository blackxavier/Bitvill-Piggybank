from django.urls import path, include
from accounts.views import (
    registration_view,
    UserProfileView,
    ObtainAuthTokenView,
    ChangePasswordView,
    user_logout,
    user_logout,
)

app_name = "accounts"

urlpatterns = [
    path("auth/register/", registration_view, name="register"),
    path("auth/login/", ObtainAuthTokenView.as_view(), name="login"),
    path("logout/", user_logout, name="logout"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("me/", UserProfileView, name="user-details"),
]
