from django.urls import path 
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('result',result,name='result'),
    path('add-car',add_car,name='add_car'),
]