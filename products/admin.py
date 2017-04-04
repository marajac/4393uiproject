from django.contrib import admin
from .models import Product, CatalogCategory, Catalog


class ProductsAdmin(admin.ModelAdmin):
    class Meta:
        model = Product


class CatalogAdmin(admin.ModelAdmin):
    class Meta:
        model = Catalog


class CatalogCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = CatalogCategory

admin.site.register(Product, ProductsAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(CatalogCategory, CatalogCategoryAdmin)
