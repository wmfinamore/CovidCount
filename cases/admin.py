from django.contrib import admin
from .models import AcumuladoDiario


@admin.register(AcumuladoDiario)
class AcumuladoDiarioAdmin(admin.ModelAdmin):
    list_filter = ['data']
    fields = ('data',
              ('casosConfirmados', 'casosDescartados',),
              ( 'casosAguardandoResultado', 'casosSuspeitosInternados',),
              ('obitosConfirmados', 'obitosSuspeitos'),
              )
