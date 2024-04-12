from django.contrib import admin
from product.models import Product, Order
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id' ,'user', 'total_sum']
