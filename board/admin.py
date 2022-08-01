from django.contrib import admin

# Register your models here.
from .models import Board
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'writer', 'write_dttm', 'hits']
    raw_id_fields = ['writer']
    list_filter = ['write_dttm','update_dttm']