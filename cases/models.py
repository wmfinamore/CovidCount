from django.db import models
from datetime import date


class AcumuladoDiario(models.Model):
    data = models.DateField(blank=False, null=False, unique=True)
    casosConfirmados = models.PositiveIntegerField(blank=False, null=False,
                                                   help_text="Casos confirmados")
    casosDescartados = models.PositiveIntegerField(blank=False, null=False,
                                                   help_text="Casos descartados")
    casosAguardandoResultado = models.PositiveIntegerField(blank=False, null=False,
                                                           help_text="Casos aguardando resultados")
    casosSuspeitosInternados = models.PositiveIntegerField(blank=False, null=False,
                                                           help_text="Casos suspeitos internados")
    obitosConfirmados = models.PositiveIntegerField(blank=False, null=False,
                                                    help_text="Óbitos confirmados")
    obitosSuspeitos = models.PositiveIntegerField(blank=False, null=False,
                                                  help_text="Óbtidos suspeitos de COVID-19")

    def __str__(self):
        d = date.fromisoformat(str(self.data))
        return f'Casos acumulados até o dia {d.strftime("%d/%m/%Y")}'

    class Meta:
        ordering = ['-data']
        verbose_name = "acumulado diário"
        verbose_name_plural = "acumulados diários"
        indexes = [
            models.Index(fields=['data'])
        ]
