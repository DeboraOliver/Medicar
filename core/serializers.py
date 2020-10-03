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

class AgendaSerializer(serializers.ModelSerializer):
    #horario = serializers.PrimaryKeyRelatedField(queryset=Horas.objects.all(),many = True)
    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'horario']
        depth = 2

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'especialidade','medico','dia', 'data_agendamento']
        depth = 1