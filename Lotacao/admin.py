from django.contrib import admin
from . models import Lotacao


class LotacaoAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'setor', 'cargo', 'matricula', 'data_admissao', 'data_demissional')
    search_fields = ('pessoa', 'setor', 'id_cargo', 'matricula', 'data_admissao', 'data_demissional')


admin.site.register(Lotacao, LotacaoAdmin)
