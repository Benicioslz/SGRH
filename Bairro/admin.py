from django.contrib import admin
from . models import Bairro


class BairroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    search_fields = ('nome', 'cidade')


admin.site.register(Bairro, BairroAdmin)
