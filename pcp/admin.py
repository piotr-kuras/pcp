from django.contrib import admin
from .models import Product, Shop, Price


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "url"
    ]


class ShopAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


class PriceAdmin(admin.ModelAdmin):
    list_display = [
        "shop",
        "price",
        "date",
        "product_url"
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Price, PriceAdmin)
