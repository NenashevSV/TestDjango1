from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CustomerAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id', 'FIO', 'birthDate', 'registerDate', 'gender', 'PDConsent', 'photo', 'photoimage')
    list_display_links = ('id', 'FIO')
    search_fields = ('FIO', 'birthDate')
    list_filter =('gender', 'PDConsent')
    readonly_fields = ('registerDate', 'photoimage')
    fields = ('FIO', 'birthDate', 'registerDate', 'gender', 'PDConsent', 'photo', 'photoimage')


    def photoimage(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50px">')
        else:
            return '-'

    photoimage.short_description = 'Фото'

admin.site.register(Customer, CustomerAdmin)