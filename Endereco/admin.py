from django.contrib import admin
from .models import Endereco


class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'cep', 'numero', 'complemento', 'pessoa', 'bairro')
    search_fields = ('logradouro', 'cep', 'numero', 'complemento', 'pessoa', 'bairro')


admin.site.register(Endereco, EnderecoAdmin)
