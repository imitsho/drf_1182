from django.contrib import admin

# Register your models here.
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'is_superuser']