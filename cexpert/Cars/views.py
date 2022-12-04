from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from .forms import CarForm, FindForm
from .models import Cars
from .topsis import dataFrame
from django.db.models import Q

# def index(request):
#     if request.method == 'POST':
#         data = ""
#         form = FindForm(request.POST or None)
#         if form.is_valid():
#             data = form.cleaned_data['srch_name']
#             #data = Cars.objects.filter(name='Ford').values()
#     else:
#         form = FindForm
#     return render(request,'Cars/index.html',{'form':form,'data':data })

def index(request):
    submitbutton= request.POST.get("submit")
    srch = ""
    form = FindForm(request.POST or None)
    if form.is_valid():
        srch = Cars.objects.filter(Q(name=form.cleaned_data.get("name")) | 
        Q(cost = form.cleaned_data.get("cost"))).values()
        #context = {'form':form,'srch':srch,'submitbutton': submitbutton}
        li = dataFrame(srch)
        print(li)
        context = {'srch':srch}
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