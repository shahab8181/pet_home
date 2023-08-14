from django.contrib import admin
from account_module.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user_group', 'email', 'phone_number', 'is_staff', 'is_superuser']
    list_editable = ['is_staff', 'is_superuser']
    list_filter = ['user_group', 'is_staff', 'is_superuser']
    
