from rest_framework import permissions, status
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)


from transactionapi.models import Currency, Category, Transaction

from transactionapi.serializers import (
    ReadCurrencySerializer,
    ReadCategorySerializer,
    ReadTransactionSerializer,
    WriteCategorySerializer,
    WriteTransactionSerializer,
)


# Currency resource view


class CurrencyListApiView(ListAPIView):
    pagination_class = PageNumberPagination
    queryset = Currency.objects.all()
    serializer_class = ReadCurrencySerializer
    model = Currency
    permission_classes = (permissions.AllowAny,)
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["id", "currency_code", "currency_name"]
    search_fields = ["id", "currency_code", "currency_name"]
    ordering_fields = ["id", "currency_code", "currency_name"]


# Category resource views
class CategoryListCreateApiView(ListCreateAPIView):
    pagination_class = PageNumberPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["category_name"]
    search_fields = ["category_name"]
    ordering_fields = ["category_name"]

    def get_queryset(self):
        return Category.objects.select_related("user").filter(user=self.request.user)

    def get_serializer_class(self):
        # uses a serializer based on request
        if self.request.method in ("list"):
            return ReadCategorySerializer
        else:
            return WriteCategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryDetailApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    model = Category
    queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.select_related("user").filter(user=self.request.user)

    def get_serializer_class(self):
        # uses a serializer based on request
        if self.request.method in ("retrieve"):
            return ReadCategorySerializer
        else:
            return WriteCategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DeleteAllCategories(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        user = request.user
        categories = Category.objects.filter(user=user)
        for category in categories:
            category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionListCreateApiView(ListCreateAPIView):
    pagination_class = PageNumberPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "transaction_amount",
        "date_added",
        "transaction_purpose",
        "date_modified",
    ]
    search_fields = [
        "transaction_amount",
        "date_added",
        "transaction_purpose",
        "date_modified",
    ]
    ordering_fields = [
        "transaction_amount",
        "date_added",
        "transaction_purpose",
        "date_modified",
    ]

    def get_queryset(self):
        return Transaction.objects.select_related(
            "currency", "category", "user"
        ).filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        # uses a serializer based on request
        if self.request == "GET":
            return ReadTransactionSerializer
        else:
            return WriteTransactionSerializer


class DeleteAllTransactions(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        user = request.user
        transactions = Transaction.objects.filter(user=user)
        for transaction in transactions:
            transaction.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TransactionRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.select_related(
            "currency", "category", "user"
        ).filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        # uses a serializer based on request
        if self.request == "GET":
            return ReadTransactionSerializer
        else:
            return WriteTransactionSerializer
