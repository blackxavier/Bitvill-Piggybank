from transactionapi.models import Currency, Category
from rest_framework import serializers


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


# class WriteCurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Currency
#         fields = [
#             "currency_code",
#             "currency_name",
#         ]

#     def validate_currency_code(self, value):
#         qs = Currency.objects.filter(currency_code=value).exclude(self.pk)
#         if qs.exists():
#             return serializers.ValidationError(
#                 {"response": "Currency code has been registered already"}
#             )
#         else:
#             return value

#     def validate_currency_name(self, value):
#         qs = Currency.objects.filter(currency_name=value).exclude(self.pk)
#         if qs.exists():
#             return serializers.ValidationError(
#                 {"response": "Currency name has been registered already"}
#             )
#         else:
#             return value
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

    # def validate(self, data):
    #     if data is :
    #         return serializers.ValidationError(
    #             {"response": "Please input a category name"}
    #         )
