from .models import Especialidade, Medico, Agenda, Consulta
from rest_framework import serializers


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'crm', 'nome', 'especialidade']
        depth = 2


class EspecialidadeSerializer(serializers.HyperlinkedModelSerializer):
    #medico_set = MedicoSerializer(many=True)

    class Meta:
        model = Especialidade
        fields = ['id', 'especialidade']
        depth = 2

class AgendaSerializer(serializers.ModelSerializer):
    horario_str = serializers.ReadOnlyField (source='horario')

    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'horario_str']
        depth = 2

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id','dia', 'horario', 'data_agendamento', 'medico','especialidade',]
        depth = 1 # só funciona para foreignfields