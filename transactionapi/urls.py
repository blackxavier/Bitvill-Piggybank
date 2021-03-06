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
        name="list-create-category",
    ),
    path(
        "categories/<int:pk>/",
        views.CategoryDetailApiView.as_view(),
        name="category-update-delete-retrieve",
    ),
    path(
        "categories/delete/",
        views.DeleteAllCategories.as_view(),
        name="categories-delete-all",
    ),
    path(
        "transactions/delete/",
        views.DeleteAllTransactions.as_view(),
        name="transaction-delete-all",
    ),
    path(
        "transactions/<int:pk>/",
        views.TransactionRetrieveUpdateDeleteView.as_view(),
        name="transaction-retrieve-update-delete",
    ),
]
