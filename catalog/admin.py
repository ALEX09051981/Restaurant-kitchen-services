from django.contrib import admin
from .models import Specialist, Department, Client, Material, Appointment

@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'department')
    search_fields = ('username', 'phone')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'specialist', 'department')
    search_fields = ('full_name', 'phone', 'email')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'quantity', 'threshold')
    list_filter = ('department',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'specialist', 'department', 'scheduled_time')
    list_filter = ('department', 'scheduled_time')
    search_fields = ('client__full_name', 'specialist__username')
