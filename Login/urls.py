from django.urls import path
from Login.views import login_page


urlpatterns = [
    path("login/", login_page) #Использую функцию
   
]