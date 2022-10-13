from django import forms
from .models import Types, Fuel, Country

class CarForm(forms.Form):
    name = forms.CharField(max_length=50, label='Бренд автомобиля',widget=forms.TextInput(
        attrs={"class":"form-control"}))
    carmod = forms.CharField(max_length=50, label = 'Модель')
    cost = forms.IntegerField(label = 'Стоимость')
    serv = forms.IntegerField(label = 'Стоимость обслуживания')
    #picture = forms.ImageField(upload_to ='pictures/%Y/%M/%D/',blank = True)
    type = forms.ModelChoiceField(queryset=Types.objects.all(), label = 'Кузов')
    fuel = forms.ModelChoiceField(queryset=Fuel.objects.all(), label = 'Тип топлива')
    country = forms.ModelChoiceField(queryset=Country.objects.all(), label = 'Местность')
