from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title="Bitvill Transaction API")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("accounts.urls", namespace="accounts")),
    path("", include("transactionapi.urls")),
    path(
        "api/password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path("swagger1/", schema_view),
]
