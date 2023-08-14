from django.contrib import admin
from .models import Product, ProductCategory, ProductType

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'type', 'category', 'is_active']
    list_editable = ['is_active']
    list_filter = ['type', 'category', 'is_active']



@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'group']



@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title']

