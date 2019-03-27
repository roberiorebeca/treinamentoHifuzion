from rest_framework import serializers
from hifuzion.contabilidade.models import Cliente, PlanoConta

class PlanoContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanoConta
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    conta = PlanoContaSerializer()
    class Meta:
        model = Cliente
        fields = '__all__'