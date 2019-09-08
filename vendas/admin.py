from django.contrib import admin
from .models import *
from .actions import *

class VendaAdmin(admin.ModelAdmin):
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id','pessoa', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name', 'pessoa__doc__cpf')
    autocomplete_fields = ['pessoa']
    readonly_fields = ('valor',)
    #filter_horizontal = ['produtos',]

    actions = [mod_nfe, mod_nfe_no]

    # Venda.get_total.short_description = 'Venda'
    """def total(self, obj):
        return obj.get_total()

    total.short_description = 'total'"""


admin.site.register(ItensDoPedido)
admin.site.register(Venda, VendaAdmin)