# Generated by Django 5.1.1 on 2025-04-01 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='products/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('tags', models.CharField(blank=True, max_length=200)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('is_available', models.BooleanField(default=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category')),
            ],
        ),
    ]
