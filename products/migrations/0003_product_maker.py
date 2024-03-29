# Generated by Django 5.0 on 2024-01-15 18:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_maker_product_desc_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='maker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.maker', verbose_name='Производитель'),
        ),
    ]
