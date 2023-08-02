from rest_framework import viewsets
from miles.models import Depoimento
from miles.serializer import DepoimentosSerializer

class DepoimentosViewSet(viewsets.ModelViewSet):
    """Depoimentos de jornadas"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentosSerializer
