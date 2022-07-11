from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse


class Currency(models.Model):
    currency_code = models.CharField(max_length=3, unique=True, blank=False, null=False)
    currency_name = models.CharField(
        max_length=32, unique=True, blank=False, null=False
    )
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        value = f"Currency name - {self.currency_name} | Currency code {self.currency_code} "
        return value

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class Category(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories"
    )
    category_name = models.CharField(max_length=32)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Category name - {self.category_name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("date_created",)


class Transaction(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_transactions",
    )
    currency = models.ForeignKey(
        Currency, on_delete=models.PROTECT, related_name="currency_transactions"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="category_transactions",
    )
    transaction_amount = models.DecimalField(max_digits=15, decimal_places=2)

    date_added = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True)
    transaction_purpose = models.TextField(blank=True)

    def __str__(self):
        return f"Transaction made by {self.user}"
