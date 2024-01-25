from django.http import HttpRequest
from django.shortcuts import render

#Подклучаю готовые формы авторизации и регистрации для представлений
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def login_page(request: HttpRequest):
  context = {
    "form": AuthenticationForm
  }
  if request.method == "GET":
    return render(request, "login/login.html", context=context)
