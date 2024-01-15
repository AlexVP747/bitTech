from django.db import models

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
    
class Maker (models.Model):
 
    country = models.CharField(verbose_name="Страна производитель", max_length=30)

    firm = models.CharField(verbose_name="Фирма", max_length=50)

        
    class Meta:
       
        verbose_name="Страна производитель"
            
        verbose_name_plural="Страны производители"

    def __str__(self):
            return self.title 

