from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProductAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = (['id', 'name', 'purchase_price', 'sale_price'])
    list_display_links = ('id', 'name')
    search_fields = ('name', 'purchase_price', 'sale_price')
    fields = ('name', 'purchase_price', 'sale_price')

admin.site.register(Product, ProductAdmin)