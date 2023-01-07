from asyncio.windows_events import NULL
from django import forms
from .models import Name, Transmission, Drive, Fuel, Country, Types

class CarForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Name.objects.all(), label = 'Марка автомобиля',empty_label="Выберите марку",widget=forms.Select(
        attrs={
            "class":"form-control"
            }))
    carmod = forms.CharField(max_length=50, label = 'Модель',widget=forms.TextInput(
        attrs={
                "class":"form-control",
                "autocomplete":"off"
            }))

    picture = forms.CharField(max_length=3000, label = 'Изображение',widget=forms.TextInput(
        attrs={
                "class":"form-control",
                "autocomplete":"off"
            }))

    cost = forms.IntegerField(label = 'Стоимость',widget=forms.NumberInput(
        attrs={ 
                "class":"form-control",
                "autocomplete":"off",
                "min":"5000",
                "step":"1000"
            }))

    serv = forms.IntegerField(label = 'Стоимость обслуживания',widget=forms.NumberInput(
        attrs={
                "class":"form-control",
                "autocomplete":"off",
                "min":"0",
                "step":"250"
            }))

    year = forms.IntegerField(label = 'Год выпуска',widget=forms.NumberInput(
        attrs={
                "class":"form-control",
                "autocomplete":"off",
                "min":"1980",
                "max":"2022"
            }))

    trans = forms.ModelChoiceField(queryset=Transmission.objects.all(), label = 'Трансмиссия',empty_label="Выберите коробку передач",widget=forms.Select(
        attrs={
            "class":"form-control"
        }))

    volume = forms.DecimalField(label = 'Объем двигателя',widget=forms.NumberInput(
        attrs={ 
                "class":"form-control",
                "autocomplete":"off",
                "max_digits":"2",
                "decimal_places":"1",
                "step":"0.1"
            }))

    drive = forms.ModelChoiceField(queryset=Drive.objects.all(), label = 'Привод',empty_label="Выберите привод",widget=forms.Select(
        attrs={
            "class":"form-control"
        }))    

    fuel = forms.ModelChoiceField(queryset=Fuel.objects.all(), label = 'Тип топлива',empty_label="Выберите топливо",widget=forms.Select(
        attrs={
            "class":"form-control"
            }))


    type = forms.ModelChoiceField(queryset=Types.objects.all(), label = 'Кузов',empty_label="Выберите кузов",widget=forms.Select(
        attrs={
            "class":"form-control"
        }))


class FindForm(forms.Form):

    name = forms.ModelChoiceField(queryset=Name.objects.all(), label = 'Марка',empty_label="Выберите марку автомобиля",widget=forms.Select(
        attrs={
            "class":"form-control"
            }), required=False)

    cost = forms.IntegerField(label = 'Стоимость',widget=forms.NumberInput(
        attrs={ 
                "type":"range",
                "oninput":"this.nextElementSibling.value = this.value",
                "color":"black",
                "min":"5000",
                "max":"100000",
                "step":"1000",
            }))
    serv = forms.IntegerField(label = 'Стоимость обслуживания',widget=forms.NumberInput(
        attrs={
                "class":"form-control",
                "autocomplete":"off",
                "min":"0",
                "step":"250"
            }))

    trans = forms.ModelChoiceField(queryset=Transmission.objects.all(), label = 'Трансмиссия',empty_label="Выберите коробку передачь",widget=forms.Select(
        attrs={
            "class":"form-control"
            }), required=False)

    drive = forms.ModelChoiceField(queryset=Drive.objects.all(), label = 'Марка',empty_label="Выберите марку автомобиля",widget=forms.Select(
        attrs={
            "class":"form-control"
            }), required=False)

    fuel = forms.ModelChoiceField(queryset=Fuel.objects.all(), label = 'Тип топлива',empty_label="Выберите топливо",widget=forms.Select(
        attrs={
            "class":"form-control"
            }),required=False)

    country = forms.ModelChoiceField(queryset=Country.objects.all(), label = 'Местность',empty_label="Выберите местность",widget=forms.Select(
        attrs={
            "class":"form-control"
        }))

    type = forms.ModelChoiceField(queryset=Types.objects.all(), label = 'Кузов',empty_label="Выберите кузов",widget=forms.Select(
        attrs={
            "class":"form-control"
        }),required=False)

    