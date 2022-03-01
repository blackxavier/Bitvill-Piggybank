from django.urls import path
from rest_framework import routers
from transactionapi import views


urlpatterns = [
    path("currencies/", views.CurrencyListApiView.as_view(), name="list-currency"),
    path(
        "transactions/",
        views.TransactionListCreateApiView.as_view(),
        name="list-create-transactions",
    ),
    path(
        "categories/",
        views.CategoryListCreateApiView.as_view(),
        name="ist-create-category",
    ),
    path(
        "categories/<int:pk>/",
        views.CategoryDetailApiView.as_view(),
        name="category-update-delete-retrieve",
    ),
    path(
        "me/categories/delete/",
        views.DeleteAllCategories.as_view(),
        name="categories-delete-all",
    ),
    path(
        "me/transactions/delete/",
        views.DeleteAllTransactions.as_view(),
        name="transaction-delete-all",
    ),
    path(
        "reports/",
        views.TransactionReportAPIView.as_view(),
        name="reports",
    ),
]
