from django.contrib import admin
from .models import Cars, Types, Fuel, Country

class CarsAdmin(admin.ModelAdmin):
    list_display = ("name","cost","carmod","type","fuel")

class CostAdmin(admin.ModelAdmin):
    list_display: (Cars.cost)

class TypesAdmin(admin.ModelAdmin):
    list_display: (Types.type)

class FuelAdmin(admin.ModelAdmin):
    list_display: (Fuel.fuel)

class CountryAdmin(admin.ModelAdmin):
    list_display: (Country.country)

class CountryAdmin(admin.ModelAdmin):
    list_display: (Country.country)


admin.site.register(Cars, CarsAdmin)
admin.site.register(Types, TypesAdmin)
admin.site.register(Fuel, FuelAdmin)
admin.site.register(Country, CountryAdmin)