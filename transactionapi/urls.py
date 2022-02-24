from django.urls import path
from rest_framework import routers
from transactionapi import views


urlpatterns = [
    path("currencies/", views.CurrencyListApiView.as_view(), name="list-currency"),
    path("categories/", views.CategoryApiView.as_view(), name="category-create-read"),
    path(
        "categories/<int:pk>/",
        views.CategoryDetailApiView.as_view(),
        name="category-update-delete-retrieve",
    ),
]
