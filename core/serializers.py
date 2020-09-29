from .models import Especialidade, Medico, Agenda
from rest_framework import serializers


class MedicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'especialidade']
        depth = 2


class EspecialidadeSerializer(serializers.HyperlinkedModelSerializer):
    #medico_set = MedicoSerializer(many=True)

    class Meta:
        model = Especialidade
        fields = ['id', 'nome']

class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'dia', 'horario']
        depth = 2