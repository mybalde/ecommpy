from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name', )} 
    list_display = 'product_name', 'stock', 'price', 'modified_date'
    ordering = 'product_name',

admin.site.register(Product, ProductAdmin)