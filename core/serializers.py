from .models import Especialidade, Medico
from rest_framework import serializers


class MedicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'especialidade']


class EspecialidadeSerializer(serializers.HyperlinkedModelSerializer):
    medico_set = MedicoSerializer(many=True)

    class Meta:
        model = Especialidade
        fields = ['id', 'nome', 'medico_set']