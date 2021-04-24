from django.db import models


class AcumuladoDiario(models.Model):
    data = models.DateField(blank=False, null=False)
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
        return f'Casos acumulados até o dia {self.data}'

    class Meta:
        ordering = ['-data']
        verbose_name = "acumulado diário"
        verbose_name_plural = "acumulados diários"
        indexes = [
            models.Index(fields=['data'])
        ]
