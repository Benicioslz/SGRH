from django.contrib import admin
from . models import HistoricoSalarial


class HistoricoSalarialAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'carga_horaria', 'salario', 'data_cadastro')
    search_fields = ('pessoa', 'carga_horaria', 'salario', 'data_cadastro')


admin.site.register(HistoricoSalarial, HistoricoSalarialAdmin)
