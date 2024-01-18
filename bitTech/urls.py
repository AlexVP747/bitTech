from django.contrib import admin
from django.urls import path, include
from products.urls import urlpatterns as urls_products

from django.conf import settings # Получаю настройки своего сайта
from django.conf.urls.static import static # Функция, которая будет обрабатывать все запросы на получения файлов


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("products.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
