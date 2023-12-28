from django.urls import path
from products.views import main_page

urlpatterns = [
    path("", main_page)
]
