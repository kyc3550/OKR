from django.contrib import admin
from .models import TimeInfo, PriceInfo
# Register your models here.

@admin.register(TimeInfo)
class TimeInfoAdmin(admin.ModelAdmin):
    list_display = [
        'day',
        'start_time',
        'end_time',
        'note',
    ]
@admin.register(PriceInfo)
class PriceInfoAdmin(admin.ModelAdmin):
    list_display = [
        'registration_period',
        'price',
        'note',
    ]