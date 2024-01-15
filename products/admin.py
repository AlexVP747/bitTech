from django.contrib import admin
from products.models import Product, Maker

# Добавляем нашу таблицу товаров на административную панель
admin.site.register(Product)
admin.site.register(Maker)

#  чтобы зайти на административную панель, нужен суперадмин, которого нужно создать
