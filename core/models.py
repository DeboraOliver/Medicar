from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, time, datetime, timedelta
import datetime as dt
from smart_selects.db_fields import GroupedForeignKey, ChainedForeignKey, ChainedManyToManyField


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



class Agenda(models.Model):
    medico = models.ForeignKey (Medico, on_delete=models.CASCADE)
    dia = models.DateField()
    #horario = models.TimeField()
    horario = models.ManyToManyField(Horas)

    def __str__(self):
        return '{} - {}'.format (self.medico, self.dia)


    def get_dia(self):
        hoje = date.today()
        if hoje.strftime('%Y-%m-%d') > self.dia:
            raise ValidationError("Não é possível agendar horários em datas passadas.")

    def choquededatas(self, ignore=[]):
        dias_agendados = type (self).objects.filter(dia=self.dia)
        for agendado in ignore:
            try:
                dias_agendados = dias_agendados.exclude(id=agendado.id)
            except:
                pass

        #if dias_agendados.exists():
         #   raise ValidationError("Já existe agenda para este dia.Escolha outro dia.")



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
    #dia = ChainedForeignKey(
     #   Agenda,
      #  chained_field="medico",
       # chained_model_field="medico",
        #show_all=False,
        #auto_choose=True,
        #sort=True)

    horario = ChainedManyToManyField(
        Agenda,
		horizontal = True,
		verbose_name = "horario",
        chained_field="medico",
        chained_model_field="medico")

    data_agendamento = models.DateTimeField(auto_now=True)

	
    #após salva fazer update da agenda

    #class Meta:
     #   ordering = ['dia']