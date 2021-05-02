from .models import AcumuladoDiario
from rest_framework import serializers


# Serializer define API representation.
class AcumuladoDiarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AcumuladoDiario
        fields = ['data','casosConfirmados','casosDescartados'
            ,'casosAguardandoResultado','casosSuspeitosInternados'
            ,'obitosConfirmados','obitosSuspeitos']