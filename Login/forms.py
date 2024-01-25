# Подключаю готовые формы для пользователей
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Подключаю модуль для создания своих форм
from django import forms



# Создаю форму вручную, создавая каждое поле
class RegistrationForm (forms.Form):
  username = forms.CharField(max_length=120, label="Имя пользователя")

# создаю форму на основе модели (для примера)
# class ProductForm (forms.ModelForm):
#   model = Product


