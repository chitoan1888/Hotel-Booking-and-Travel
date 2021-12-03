from django.contrib import admin

from camnang.models import Camnang
from .models import Camnang

# Register your models here.
@admin.register(Camnang)
class Camnang(admin.ModelAdmin):
    list_display = ('camnang_id', 'camnang_name', 'location', 'view',)
    search_fields = ('location', 'camnang_name',)
