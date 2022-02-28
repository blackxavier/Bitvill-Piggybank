# Generated by Django 4.0.2 on 2022-02-28 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=32)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_code', models.CharField(max_length=3, unique=True)),
                ('currency_name', models.CharField(max_length=32, unique=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('transaction_purpose', models.TextField(blank=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_transactions', to='transactionapi.category')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='currency_transactions', to='transactionapi.currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
