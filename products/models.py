from django.db import models

class Maker (models.Model):
 
    country = models.CharField(verbose_name="Страна производитель", max_length=30)

    firm = models.CharField(verbose_name="Фирма", max_length=50)
        
    class Meta:
       
        verbose_name="Страна производитель"
            
        verbose_name_plural="Страны производители"

    def __str__(self):
            return self.title 
    
# Создаю модель (таблицу) товаров
#  Она должна наследоваться от models.Model, чтобы джанго понял что это модель
class Product (models.Model):
    # поле id создается по умолчанию, нам писать его не надо
    #  Создаем поле модели с названием title
    # verbose_name - "человеческое имя", которое будет отоюражаться на админ. панели
    #  max_length - максю длинна строки, только для Charfield
    title = models.CharField(verbose_name="Название товара", max_length=150)

    price = models.FloatField(verbose_name="цена")

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
        
    class Meta:
       
        verbose_name="Имя"
            
        verbose_name_plural="Имена"

    def __str__(self):
            return self.title 


