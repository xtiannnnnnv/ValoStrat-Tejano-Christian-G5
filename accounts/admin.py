from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Admin configuration for the custom user model."""

    model = CustomUser
    list_display = [
        'username', 'email', 'first_name', 'last_name',
        'role', 'is_staff', 'is_active',
    ]
    list_filter = ['role', 'is_staff', 'is_active']
    search_fields = ['username', 'email', 'first_name', 'last_name']

    fieldsets = UserAdmin.fieldsets + (
        ('ValoStrat Info', {
            'fields': ('role', 'contact_number', 'favorite_agent', 'rank', 'profile_photo'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('ValoStrat Info', {
            'fields': ('role', 'email', 'first_name', 'last_name'),
        }),
    )
