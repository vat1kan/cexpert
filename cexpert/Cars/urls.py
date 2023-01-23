from django.urls import path 
from .views import *
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path('',index,name='home'),
    path('result',result,name='result'),
    path('add-car',add_car,name='add_car'),
]