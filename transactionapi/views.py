from rest_framework import permissions, status
from transactionapi.pagination import PaginationHandlerMixin
from transactionapi.models import Currency, Category, Transaction
from transactionapi.serializers import (
    ReadCurrencySerializer,
    ReadCategorySerializer,
    WriteCategorySerializer,
)
from rest_framework.response import Response
from rest_framework.generics import (
    ListCreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.settings import api_settings
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

# Currency resource views


class CurrencyListApiView(ListAPIView):
    pagination_class = PageNumberPagination
    serializer_class = ReadCurrencySerializer
    model = Currency
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["id", "currency_code", "currency_name"]
    search_fields = ["id", "currency_code", "currency_name"]

    def get(self, request, *args, **kwargs):
        currencies = Currency.objects.all()

        page = self.paginate_queryset(currencies)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        data = {
            "data": serializer.data,
            "status": f"{status.HTTP_200_OK} OK",
        }
        return Response(data)


class CategoryApiView(APIView, PaginationHandlerMixin):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReadCategorySerializer
    model = Category
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request, *args, **kwargs):
        user = request.user
        categories = Category.objects.filter(user=user)
        page = self.paginate_queryset(categories)
        if page is not None:
            serializer = self.get_paginated_response(
                self.serializer_class(page, many=True).data
            )
        else:
            serializer = self.serializer_class(categories, many=True)

        data = {
            "data": serializer.data,
            "status": f"{status.HTTP_200_OK} OK",
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = WriteCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        data = {
            "response": "Category created successfully",
            "data": serializer.data,
            "status": status.HTTP_201_CREATED,
        }
        return Response(data)


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


class DeleteAllTransactions(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        user = request.user
        transactions = Transaction.objects.filter(user=user)
        for transaction in transactions:
            transaction.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
