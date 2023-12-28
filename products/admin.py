from django.contrib import admin
from products.models import Product

# Добавляем нашу таблицу товаров на административную панель
admin.site.register(Product)

#  чтобы зайти на административную панель, нужен суперадмин, которого нужно создать
