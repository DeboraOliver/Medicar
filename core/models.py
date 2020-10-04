from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, time, datetime, timedelta
import datetime as dt
from smart_selects.db_fields import GroupedForeignKey, ChainedForeignKey, ChainedManyToManyField
from multiselectfield import MultiSelectField


class Especialidade(models.Model):
    especialidade = models.CharField(max_length=50, default='Demartologia')

    def __str__(self):
        return self.especialidade

    class Meta:
        ordering = ['especialidade']

class Medico(models.Model):
    nome = models.CharField ("Nome", max_length=200, null = False, blank = False)
    crm = models.CharField ("CRM", max_length=11,  null = False, blank = False)
    email = models.EmailField ()
    telefone = models.CharField ("Telefone", max_length=11)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

   
hours = [(i, dt.time(i).strftime('%H:%M')) for i in range(7,21)]

#validator
def data_passada(value):
    hoje = date.today()
    if value < hoje:
        raise ValidationError("Não é possível agendar horários em datas passadas.")

class Agenda(models.Model):
    medico = models.ForeignKey (Medico, on_delete=models.CASCADE)
    dia = models.DateField (validators=[data_passada],  null = False, blank = False)
    horario = MultiSelectField(choices=hours,
                                 max_choices=5,
                                 max_length=200)

    def clean(self):
        if self.dia and Agenda.objects.filter (medico=self.medico).exists ():
            raise ValidationError ("Já existe agenda para o dia {} com dr(a) {}. Escolha outro dia, ou outro médico.".format(self.dia, self.medico))

    #class Meta:
     #   unique_together = ('medico','dia') Só funciona se não houver foreigkey

    def __str__(self):
        return '{} - {}'.format (self.medico, self.dia)

    class Meta:
        ordering = ['dia']

class Consulta(models.Model):

    usuario = models.ForeignKey (User, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    
    medico = ChainedForeignKey(
        Medico,
        chained_field="especialidade",
        chained_model_field="especialidade",
        show_all=False,
        auto_choose=True,
        sort=True)

    dia = ChainedForeignKey(
        Agenda,
        chained_field="medico",
        chained_model_field="medico",
        show_all=False,
        auto_choose=True,
        sort=True)

    horario = models.TimeField()

    data_agendamento = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {} - {}'.format (self.medico, self.dia, self.horario)

    #Ordenar consulta por dia e horário
    class Meta:
        ordering = ['dia','horario']

        #checar se já existe esta consulta
    def hora_marcada(self):
        if self.dia and Consulta.objects.filter (horario=self.horario).exists():
            raise ValidationError ("Você já possui uma consulta marcada para {} - {}.".format(self.dia, self.horario))
			
	
	
