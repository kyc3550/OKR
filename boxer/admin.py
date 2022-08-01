from django.contrib import admin
from .models import BoxerInfo
# Register your models here.

@admin.register(BoxerInfo)
class BoserInfoAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'age',
        'weight',
        'total',
        'win',
        'lose',
        'draw',
        'note',
    ]