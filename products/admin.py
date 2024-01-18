from django.contrib import admin
from products.models import Product, Maker, Profile

# Добавляем нашу таблицу товаров на административную панель
admin.site.register(Product)
admin.site.register(Maker)
admin.site.register(Profile)

#  чтобы зайти на административную панель, нужен суперадмин, которого нужно создать
