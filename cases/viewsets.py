from .models import AcumuladoDiario
from .serializers import AcumuladoDiarioSerializer
from rest_framework import viewsets


# ViewSets define the view behavior
class AcumuladoDiarioViewSet(viewsets.ModelViewSet):
    queryset = AcumuladoDiario.objects.all()
    serializer_class = AcumuladoDiarioSerializer
