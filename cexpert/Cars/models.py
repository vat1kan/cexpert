from django.db import models

class Cars(models.Model):
    name = models.ForeignKey('Name', on_delete = models.PROTECT, null=True, verbose_name='Марка')
    carmod = models.CharField(max_length = 150,verbose_name='Модель автомобиля')
    picture = models.CharField(max_length=300,verbose_name='Изображение')
    cost = models.IntegerField(verbose_name='Стоимость')
    serv = models.IntegerField(verbose_name='Стоимость обслуживания в год')
    year = models.IntegerField(verbose_name='Год выпуска')
    trans = models.ForeignKey('Transmission',on_delete = models.PROTECT, null=True,verbose_name='Трансмиссия')
    volume = models.DecimalField(max_digits=2, decimal_places=1,verbose_name='Объем двигателя')
    drive = models.ForeignKey('Drive', on_delete = models.PROTECT, null=True,verbose_name='Привод')
    fuel = models.ForeignKey('Fuel', on_delete = models.PROTECT, null=True, verbose_name='Вид топлива')
    type = models.ForeignKey('Types',on_delete = models.PROTECT, null=True,verbose_name='Кузов')
    
    

    class Meta: 
        verbose_name = 'Авто'
        verbose_name_plural = 'Автомобили' 

    def __str__(self):
        return str(self.name)

    

class Name(models.Model):
    brand = models.CharField(max_length=150, db_index=True, verbose_name='Марка')

    class Meta: 
        verbose_name = 'Марка'
        verbose_name_plural = 'Марка автомобиля'


    def __str__(self):
        return  str(self.brand)


class Transmission(models.Model):
    trans = models.CharField(max_length=150, db_index=True, verbose_name = 'Трансмиссия')
    
    def __str__(self):
        return self.trans

    class Meta: 
        verbose_name = 'Трансмиссия'
        verbose_name_plural = 'Коробка передач'

class Drive(models.Model):
    drive = models.CharField(max_length=150, db_index=True, verbose_name = 'Привод')
    
    def __str__(self):
        return self.drive

    class Meta: 
        verbose_name = 'Привод'
        verbose_name_plural = 'Привод автомобиля'


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
        verbose_name_plural = 'Местность наичастейшего использования автомобиля'

class Types(models.Model):
    type = models.CharField(max_length=150, db_index=True, verbose_name = 'Кузов')

    def __str__(self):
        return self.type

    class Meta: 
        verbose_name = 'Кузов'
        verbose_name_plural = 'Кузов автомобиля'
