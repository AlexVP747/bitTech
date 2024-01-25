# Generated by Django 5.0 on 2024-01-25 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0001_initial'),
        ('products', '0007_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='Gallery.image', verbose_name='Галерея изображений'),
        ),
    ]