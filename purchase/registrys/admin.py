from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class RegistrysAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = (['id', 'customer', 'sale_date'])
    list_display_links = ('id', 'customer')
    search_fields = ('customer', 'sale_date')
    # fields = ('name', 'purchase_price', 'sale_price')

class RegistryDatasAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = (['id', 'registry', 'product', 'count', 'price', 'sum'])
    list_display_links = ('id', 'registry', 'product')
    search_fields = ('customer', 'product', 'count', 'price', 'sum')
    # fields = ('name', 'purchase_price', 'sale_price')

admin.site.register(Registry, RegistrysAdmin)
admin.site.register(RegistryData, RegistryDatasAdmin)

registry = models.ForeignKey(Registry, on_delete=models.PROTECT, verbose_name="Строка реестра")
product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Товар")
count = models.IntegerField(verbose_name='Кол-во')
price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена за единицу", blank=True, null=True)
sum = models.DecimalField(max_digits=22, decimal_places=2, verbose_name="Сумма", blank=True, null=True)