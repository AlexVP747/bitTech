from django.shortcuts import render
from products.models import Product
from products.models import Maker

def main_page(request):
    # Получаю все товары из таблицы
    listProducts = Product.objects.all()

    # Создаю контекст, который буду присоединять к шаблону
    # В нем будут указаны все переменные, которые будут доступны в шаблоне
    context = {
        "listProducts": listProducts
    }

    # Не забываю привязать контекст к функции render
    return render(request, "products/index.html", context=context)

# def main_page(request):
   
#     listMakers = Maker.objects.all()

#     context = {
#         "listMakers": listMakers
#     }

#     return render(request, "products/index.html", context=context)