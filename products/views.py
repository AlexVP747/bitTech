from django.shortcuts import render
from products.models import Product
from products.models import Maker
from django.views.generic import ListView # Подключаем класс-представление

# Классы представления, в отличии от функций, заранее уже настроены
# В них надо писать меньше кода и они берут большинство задач на себя "за кулисами"

class ListProducts(ListView):
    template_name = "products/index.html" # Имя шаблона, который использовать
    model = Product # Модель, в которой он будет делать запрос на получение всех записей
    context_object_name = "listProducts" # Имя переменной, которая будет показваться в HTML-шаблоне

def main_page(request):
    # Получаю все товары из таблицы
    listProducts = Product.objects.all() # Получить все записи в таблице товаров

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