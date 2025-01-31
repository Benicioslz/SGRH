from django.contrib import admin
from .models import Estado


class EstadoAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nome')
    search_fields = ('sigla', 'nome')


admin.site.register(Estado, EstadoAdmin)
