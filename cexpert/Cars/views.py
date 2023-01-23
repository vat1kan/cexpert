from django.shortcuts import redirect, render
from .forms import CarForm, FindForm
from .models import Cars
from .topsis import Distances, Topsis
from django.db.models import Q


def index(request):
    submitbutton= request.POST.get("submit")
    data, search_value = "",""
    form = FindForm(request.POST or None)
    if form.is_valid():
        data = Cars.objects.filter(name = form.cleaned_data.get("name"),
        cost__lte = form.cleaned_data.get("cost"),
        serv__lte = form.cleaned_data.get("serv")).values('name__brand',
        'carmod',
        'picture',
        'cost',
        'serv',
        'year',
        'trans__trans',
        'volume',
        'drive__drive',
        'fuel__fuel',
        'type__type')
        print(data)
        search_value = form.cleaned_data.get("country")
        best_car = Topsis(data,search_value)
        context = {'car_brand':best_car[0],'car_model':best_car[1],'car_img':best_car[2],
        'car_cost':best_car[3],'car_serv':best_car[4],'car_year':best_car[5],'car_trans':best_car[6],
        'car_volume':best_car[7],'car_drive':best_car[8],'car_fuel':best_car[9],'car_type':best_car[10],
        'search_value':search_value}
        return result(request,context)
    else:
        form = FindForm(request.POST or None)
        return render(request,'Cars/index.html', {'form':form, 'submitbutton': submitbutton})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            Cars.objects.create(**form.cleaned_data)
            return redirect('add_car')
    else:
        form = CarForm
    return render(request,'Cars/add_car.html',{'form':form})

def result (request,context):
    return render(request,'Cars/result.html',context)