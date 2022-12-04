from asyncio.windows_events import NULL
from django import forms
from .models import Types, Fuel, Country

class CarForm(forms.Form):
    name = forms.CharField(max_length=50, label='Бренд автомобиля',widget=forms.TextInput(
        attrs={
                "class":"form-control",
            }))
    carmod = forms.CharField(max_length=50, label = 'Модель',widget=forms.TextInput(
        attrs={
                "class":"form-control",
                "autocomplete":"off"
            }))
    cost = forms.IntegerField(label = 'Стоимость',widget=forms.NumberInput(
        attrs={ 
                "class":"form-control",
                "autocomplete":"off",
                "step":"2000"
            }))
    serv = forms.IntegerField(label = 'Стоимость обслуживания',widget=forms.NumberInput(
        attrs={
                "class":"form-control",
                "autocomplete":"off",
                "step":"250"
            }))
    #picture = forms.ImageField(upload_to ='pictures/%Y/%M/%D/',blank = True)
    type = forms.ModelChoiceField(queryset=Types.objects.all(), label = 'Кузов',empty_label="Выберите кузов",widget=forms.Select(
        attrs={
            "class":"form-control"
        }))
    fuel = forms.ModelChoiceField(queryset=Fuel.objects.all(), label = 'Тип топлива',empty_label="Выберите топливо",widget=forms.Select(
        attrs={
            "class":"form-control"
            }))
    country = forms.ModelChoiceField(queryset=Country.objects.all(), label = 'Местность',empty_label="Выберите местность",widget=forms.Select(
        attrs={
            "class":"form-control"
            }))


class FindForm(forms.Form):
    name = forms.CharField(max_length=50, label='Бренд автомобиля',widget=forms.TextInput(
        attrs={
                "class":"form-control",
                "name":"srch_name"
            }), required=False)
    cost = forms.IntegerField(label = 'Стоимость',widget=forms.NumberInput(
        attrs={ 
                "type":"range",
                "oninput":"this.nextElementSibling.value = this.value",
                "min":"5000",
                "max":"100000",
                "step":"5000",
            }))
    serv = forms.IntegerField(label = 'Стоимость обслуживания',widget=forms.NumberInput(
        attrs={
                "class":"form-control",
                "autocomplete":"off",
                "step":"250"
            }))
    type = forms.ModelChoiceField(queryset=Types.objects.all(), label = 'Кузов',empty_label="Выберите кузов",widget=forms.Select(
        attrs={
            "class":"form-control"
        }))
    fuel = forms.ModelChoiceField(queryset=Fuel.objects.all(), label = 'Тип топлива',empty_label="Выберите топливо",widget=forms.Select(
        attrs={
            "class":"form-control"
            }))
    country = forms.ModelChoiceField(queryset=Country.objects.all(), label = 'Местность',empty_label="Выберите местность",widget=forms.Select(
        attrs={
            "class":"form-control"
            }))

    