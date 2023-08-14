from django.contrib import admin
from django.http import HttpRequest
from .models import Blog, BlogCategory

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title' ,'user', 'date_created']
    list_filter = ['title' ,'user', 'date_created']

    def save_model(self, request: HttpRequest, obj: Blog, form, change):
        if not change:
            obj.user = request.user
        return super().save_model(request, obj, form, change)
    


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']