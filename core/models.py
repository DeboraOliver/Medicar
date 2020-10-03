from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, time, datetime, timedelta
import datetime as dt
from smart_selects.db_fields import GroupedForeignKey, ChainedForeignKey, ChainedManyToManyField
from multiselectfield import MultiSelectField


class Especialidade(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=50, default='Demartologia')

    def __str__(self):
        return self.especialidade

    class Meta:
        ordering = ['especialidade']

class Medico(models.Model):
    nome = models.CharField ("Nome", max_length=200, blank=False, null=False)
    crm = models.CharField ("CRM", max_length=11, null=False)
    email = models.EmailField ()
    telefone = models.CharField ("Telefone", max_length=11)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

    

hours = [(i, dt.time(i).strftime('%H:%M')) for i in range(24)]

class Horas(models.Model):
    hours = models.IntegerField(choices=hours)

    def __str__(self):
        return '{}'.format (str(self.hours))

def data_passada(value):
    hoje = date.today()
    if value < hoje:
        raise ValidationError("Não é possível agendar horários em datas passadas.")

class Agenda(models.Model):
    medico = models.ForeignKey (Medico, on_delete=models.CASCADE)
    dia = models.DateField (validators=[data_passada])
    horario = MultiSelectField(choices=hours,
                                 max_choices=5,
                                 max_length=200)
    #horario = JSONField(models.ManyToManyField (Horas))

    class Meta:
        unique_together = ('medico','dia')

    # def save(self, *args, **kwargs):
    #     result= []
    #     data= self.dia
    #     doutor= self.medico
    #     concatenar="{}-{}".format(data, doutor)
    #     if concatenar in result:
    #         raise ValidationError("Já existe agenda para o dia {} com dr(a) {}. Escolha outro dia, ou outro médico.".format(data, doutor))
    #     else:
    #         result.append(concatenar)
    #     super ().save (*args, **kwargs)

    def __str__(self):
        return '{} - {}'.format (self.medico, self.dia)

    class Meta:
        ordering = ['dia']


class Consulta(models.Model):

    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    medico = ChainedForeignKey(
        Medico,
        chained_field="especialidade",
        chained_model_field="especialidade",
        show_all=False,
        auto_choose=True,
        sort=True)
    #usuario = models.ForeignKey (User, on_delete=models.CASCADE)
    dia = ChainedForeignKey(
        Agenda,
        chained_field="medico",
        chained_model_field="medico",
        show_all=False,
        auto_choose=True,
        sort=True)

    #horario = ChainedForeignKey (
     #   Agenda,
        #chained_field="dia",
        #chained_model_field="horario",
        #show_all=False,
        #auto_choose=True,
        #sort=True)

    # horario = ChainedManyToManyField(
    #     Agenda,
		# horizontal = True,
		# verbose_name = "horario",
    #     chained_field="dia",
    #     chained_model_field="dia")

    data_agendamento = models.DateTimeField(auto_now=True)

	
    #após salva fazer update da agenda

    class Meta:
       ordering = ['dia']