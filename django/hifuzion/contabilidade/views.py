from rest_framework import viewsets
from hifuzion.contabilidade.serializers import ClienteSerializer, PlanoContaSerializer
from hifuzion.contabilidade.models import Cliente, PlanoConta


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PlanoContaViewSet(viewsets.ModelViewSet):
    queryset = PlanoConta.objects.all()
    serializer_class = PlanoContaSerializer

    def create(self, request, *args, **kwargs):
        return super().create(*args, **kwargs)
