from django.contrib import admin
from .models import Cidade


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado_id')
    search_fields = ('nome', 'estado_id')


admin.site.register(Cidade, CidadeAdmin)
