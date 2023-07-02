from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import Product

# Register your models here.
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'title', 'price', 'created_at')
    fields = ['name', 'title', 'price', 'created_at']
    readonly_fields = ('created_at',)

admin.site.register(Product, ProductAdmin)