from django.contrib import admin
from . models import TipoContatoPessoa


class TipoContatoPessoaAdmin(admin.ModelAdmin):
    list_display = ('tipo_contato', 'pessoa', 'contato')
    search_fields = ('tipo_contato', 'pessoa', 'contato')


admin.site.register(TipoContatoPessoa, TipoContatoPessoaAdmin)
