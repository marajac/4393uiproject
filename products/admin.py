from django.contrib import admin
from .models import Product


class ProductsAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

admin.site.register(Product, ProductsAdmin)