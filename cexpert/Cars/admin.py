from django.contrib import admin
from .models import Cars, Name, Transmission, Drive, Fuel, Country, Types

class CarsAdmin(admin.ModelAdmin):
    list_display = ("name","cost","carmod","type","fuel")

# class CostAdmin(admin.ModelAdmin):
#     list_display: (Cars.cost)

class NameAdmin(admin.ModelAdmin):
    list_display: (Name.brand)

class TransmissionAdmin(admin.ModelAdmin):
    list_display: (Transmission.trans)

class DriveAdmin(admin.ModelAdmin):
    list_display: (Drive.drive)

class FuelAdmin(admin.ModelAdmin):
    list_display: (Fuel.fuel)

class CountryAdmin(admin.ModelAdmin):
    list_display: (Country.country)

class TypesAdmin(admin.ModelAdmin):
    list_display: (Types.type)



admin.site.register(Cars, CarsAdmin)
admin.site.register(Name, NameAdmin)
admin.site.register(Transmission, TransmissionAdmin)
admin.site.register(Drive, DriveAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Types, TypesAdmin)