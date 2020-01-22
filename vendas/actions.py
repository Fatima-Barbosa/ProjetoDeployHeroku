from django.http import HttpResponseNotFound

def mod_nfe(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)
    else:
        return HttpResponseNotFound('<h2>Sem permissão</>')

mod_nfe.short_description = 'nfe - emitida'    

def mod_nfe_no(modeladmin, request, queryset):
    queryset.update(nfe_emitida=False)

mod_nfe_no.short_description = 'nfe - não emitida'