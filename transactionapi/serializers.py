from transactionapi.models import Currency, Category, Transaction
from rest_framework import serializers
from accounts.serializers import ReadUserProfileSerializer
from transactionapi.reports import ReportParams


class ReadCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = [
            "currency_code",
            "currency_name",
            "date_created",
            "date_modified",
        ]
        read_only_fields = fields


class ReadCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "category_name", "date_created", "date_modified"]
        read_only_fields = fields


class WriteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "category_name",
        ]


class WriteTransactionSerializer(serializers.ModelSerializer):
    """Handles writing operations (POST,PUT,PATCH) on the transaction model"""

    category = serializers.SlugRelatedField(
        slug_field="category_name", queryset=Category.objects.all()
    )
    currency = serializers.SlugRelatedField(
        slug_field="currency_name", queryset=Currency.objects.all()
    )

    class Meta:
        model = Transaction
        fields = [
            "transaction_amount",
            "transaction_purpose",
            "category",
            "currency",
            "date_added",
            "date_modified",
        ]

    def __init__(self, *args, **kwargs):
        """Class constructor. Check if the user sending the request created the category inputed"""
        super().__init__(*args, **kwargs)
        user = self.context["request"].user
        self.fields["category"].queryset = Category.objects.filter(user=user)


class ReadTransactionSerializer(serializers.ModelSerializer):
    """Handles reading operations (GET) on the transaction model"""

    category = ReadCategorySerializer()
    currency = ReadCurrencySerializer()
    user = ReadUserProfileSerializer()

    class Meta:
        model = Transaction
        fields = [
            "id",
            "user",
            "category",
            "currency",
            "transaction_amount",
            "date_added",
            "transaction_purpose",
            "date_modified",
        ]
        read_only = True


class ReportEntrySerializer(serializers.Serializer):
    category = ReadCategorySerializer()
    total = serializers.DecimalField(max_digits=15, decimal_places=2)
    count = serializers.IntegerField()
    avg = serializers.DecimalField(max_digits=15, decimal_places=2)


class ReportParamsSerializer(serializers.Serializer):
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        return ReportParams(**validated_data)
