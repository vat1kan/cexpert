from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=150,verbose_name='Марка')
    carmod = models.CharField(max_length = 150,verbose_name='Модель автомобиля')
    cost = models.IntegerField(verbose_name='Стоимость')
    serv = models.IntegerField(verbose_name='Стоимость обслуживания в год')
    picture = models.ImageField(upload_to ='pictures/%Y/%M/%D/',blank = True,verbose_name='Изображение')
    type = models.ForeignKey('Types',on_delete = models.PROTECT, null=True,verbose_name='Кузов')
    fuel = models.ForeignKey('Fuel',on_delete = models.PROTECT, null=True, verbose_name='Вид топлива')
    country = models.ForeignKey('Country',on_delete = models.PROTECT, null=True,verbose_name='Тип местности')

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = 'Авто'
        verbose_name_plural = 'Автомобили'

class Types(models.Model):
    type = models.CharField(max_length=150, db_index=True, verbose_name = 'Кузов')

    def __str__(self):
        return self.type

    class Meta: 
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузов автомобиля'

class Fuel(models.Model):
    fuel = models.CharField(max_length=150, db_index=True, verbose_name = 'Топливо')
    
    def __str__(self):
        return self.fuel

    class Meta: 
        verbose_name = 'Топливо'
        verbose_name_plural = 'Вид топлива'


class Country(models.Model):
    country = models.CharField(max_length=150, db_index=True, verbose_name = 'Местность')
    
    def __str__(self):
        return self.country

    class Meta: 
        verbose_name = 'Местность'
        verbose_name_plural = 'Вид местности'


