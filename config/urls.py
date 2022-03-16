from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

# from rest_framework.schemas import get_schema_view
# from rest_framework.documentation import include_docs_urls


# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


# schema_view = get_schema_view(
#     openapi.Info(
#         title="Bitvill Transacction API",
#         default_version="v1",
#         description="Create and manage your transactions",
#         terms_of_service="https://www.bitvill.com/policies/terms/",
#         contact=openapi.Contact(email="ogbuchi@snippets.local"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
#     authentication_classes=[]
# )

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


#   path(
#         "swagger/",
#         schema_view.with_ui("swagger", cache_timeout=0),
#         name="schema-swagger-ui",
#     ),
#     path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
# ]
