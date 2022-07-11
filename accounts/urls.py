from django.urls import path
from accounts.views import (
    RegistrationView,
    UserProfileView,
    ObtainAuthTokenView,
    ChangePasswordView,
    user_logout,
  
)

app_name = "accounts"

urlpatterns = [
    path("auth/register/", RegistrationView.as_view(), name="register"),
    path("auth/login/", ObtainAuthTokenView.as_view(), name="login"),
    path("logout/", user_logout, name="logout"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("me/", UserProfileView, name="user-details"),
]
