from django.contrib import admin
from Tipo_Contato.models import TipoContato


class TipoContatoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


admin.site.register(TipoContato, TipoContatoAdmin)
