from django.contrib import admin

from transactionapi.models import Category, Currency, Transaction

admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Transaction)
