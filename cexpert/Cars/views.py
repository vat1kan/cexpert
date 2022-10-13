from django.shortcuts import render
from .forms import CarForm
from .models import Cars

def index(request):
    return render(request,'Cars/index.html')

def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            Cars.objects.create(**form.cleaned_data)
    else:
        form = CarForm
    return render(request,'Cars/add_car.html',{'form':form})