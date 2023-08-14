from django.contrib import admin
from .models import Order, OrderDetail, OrderCheckOut

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_paid', 'transportation', 'final_price', 'date_of_payment']
    list_filter = ['is_paid', 'transportation', 'user']



@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    pass



@admin.register(OrderCheckOut)
class OrderCheckOutAdmin(admin.ModelAdmin):
    list_display = ['user', 'order', 'company', 'country', 'state', 'city', 'is_post']
    list_editable = ['is_post']
    list_filter = ['company', 'country', 'state', 'city', 'is_post']
    

