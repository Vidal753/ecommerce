from django.contrib import admin
from .models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'digital')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'productos', 'total', 'date_ordered')


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity')


class ShoppingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order', 'city', 'date_added')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShoppingAddress, ShoppingAddressAdmin)
