# Generated by Django 5.0 on 2024-01-18 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products_images/', verbose_name='Изображение товара'),
        ),
    ]