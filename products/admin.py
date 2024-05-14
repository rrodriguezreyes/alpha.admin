from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'operational_hour']  # Lista de campos a mostrar en el listado

admin.site.register(Product, ProductAdmin)
