from django.contrib import admin
from .models import Holiday

class HolidayAdmin(admin.ModelAdmin):
    list_display = ['holiday_date', 'description']  # Lista de campos a mostrar en el listado

admin.site.register(Holiday, HolidayAdmin)