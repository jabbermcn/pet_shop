from django.contrib import admin

from shop.models import Category, Product


class ProductTabularInline(admin.TabularInline):
    model = Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (ProductTabularInline,)
