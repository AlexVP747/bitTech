from django.urls import path

#Два способа
from products.views import main_page # Подключаю функцию
from products.views import ListProducts # Подключаю класс

urlpatterns = [
    path("", main_page) #Использую функцию
   # path("", ListProducts.as_view()) # Использую класс

]
