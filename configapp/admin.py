from django.contrib import admin
from .models import Category, Product, Shop, Contact
from django.contrib.auth.admin import UserAdmin


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'created_at']
    list_filter = ['name', 'price']
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'photo', 'category')
        }),
        ('Price and Stock', {
            'fields': ('price', 'stock')
        })
    )


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    list_filter = ['name']


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_filter = ['created_at']


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(Contact, ContactAdmin)
