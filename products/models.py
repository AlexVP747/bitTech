from django.db import models
from django.contrib.auth.models import User
from Gallery.models import Image

class Maker (models.Model):
 
    country = models.CharField(verbose_name="Страна производитель", max_length=30)

    firm = models.CharField(verbose_name="Фирма", max_length=50)
        
    class Meta:
       
        verbose_name="Страна производитель"
            
        verbose_name_plural="Страны производители"

    def __str__(self):
            return self.country 
    
# Создаю модель (таблицу) товаров
#  Она должна наследоваться от models.Model, чтобы джанго понял что это модель
class Product (models.Model):
    # поле id создается по умолчанию, нам писать его не надо
    #  Создаем поле модели с названием title
    # verbose_name - "человеческое имя", которое будет отоюражаться на админ. панели
    #  max_length - максю длинна строки, только для Charfield
    title = models.CharField(verbose_name="Название товара", max_length=150)

    price = models.FloatField(verbose_name="цена")

    category = models.CharField(verbose_name="Категория", max_length=120, null=True)

    image = models.ImageField(
        verbose_name="Изображение товара",
        upload_to="products_images/",
        null=True
    )
    gallery = models.ForeignKey(
        Image,
        verbose_name="Галерея изображений",
        on_delete=models.CASCADE,
        related_name="product",
        null=True
    )

    desc = models.TextField(verbose_name="Описание")

    maker = models.ForeignKey(
        Maker, 
        verbose_name="Производитель",
        on_delete=models.CASCADE,
        related_name="products",
        null=True
        )

# Служебный класс
    class Meta:
        # название таблицы в единственном числе
        verbose_name="Товар"
        # название таблицы в множественном числе
        verbose_name_plural="Товары"

# Чтобы в списке на административной панели товары отображались под своими названиями
    def __str__(self):
        return self.title 

#  Создание консоли
#  - создание миграции для создании таблицы
#  - загрузка созданной таблици в свою базу данных
    
class Profile (models.Model):
 
    name = models.CharField(verbose_name="Имя", max_length=50,)

    middle_name = models.CharField(verbose_name="Отчество", max_length=50,)

    surname = models.CharField(verbose_name="Фамилия", max_length=50,)

    date_of_birth = models.DateField(verbose_name="Дата рождения",)
    
    delivery_address = models.CharField(verbose_name="Адрес доставки", max_length=100,)
    
    bonus_and_discount = models.IntegerField(verbose_name="Бонусы и скидка", null=True)
    
    purchased_products = models.ManyToManyField(
        Product, 
        verbose_name="Купленные товары",
        related_name="Profiles",
    )

    user = models.OneToOneField(
        User,
        verbose_name="Системный пользователь",
        on_delete=models.CASCADE,
        related_name="profile",
        null=True
    )



    class Meta:
       
        verbose_name="Профиль"
            
        verbose_name_plural="Профили"

    def __str__(self):
        return self.name + " " + self.middle_name + " " + self.surname 


