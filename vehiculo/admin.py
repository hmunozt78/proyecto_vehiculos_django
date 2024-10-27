from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Vehiculo
# Register your models here.

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'codename', 'content_type')
    search_fields = ('name', 'codename')

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ('marca','modelo','categoria','precio')
    list_display = ('marca','modelo','categoria','precio')
    ordering = ('marca','modelo','categoria','precio')