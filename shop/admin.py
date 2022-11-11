from django.contrib import admin

from shop.models import Category, Product, Professional, Client


class ProductTabularInline(admin.TabularInline):
    model = Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (ProductTabularInline,)


@admin.register(Professional)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
