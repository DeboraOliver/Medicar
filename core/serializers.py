from .models import Especialidade, Medico, Agenda, Horas, Consulta
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

class HorasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horas
        fields = ['id','hours']


class AgendaSerializer(serializers.ModelSerializer):
    #horario = serializers.PrimaryKeyRelatedField(queryset=Horas.objects.all(),many = True)
    class Meta:
        model = Agenda
        fields = ['id', 'medico', 'horario', 'data_agendamento']
        depth = 2

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'especialidade','medico','dia','data_agendamento']
        depth = 1