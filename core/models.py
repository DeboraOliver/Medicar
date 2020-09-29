from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date, time, datetime, timedelta


class Especialidade(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField ("Nome", max_length=200, blank=False, null=False)
    crm = models.CharField ("CRM", max_length=11, null=False)
    email = models.EmailField ()
    telefone = models.CharField ("Telefone", max_length=11)
    especialidade = models.ForeignKey (Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Agenda(models.Model):
    medico = models.ForeignKey (Medico, on_delete=models.CASCADE)
    dia = models.DateField()
    horario = models.TimeField()

    #def __str__(self):
     #   return self.medico

    def __unicode__(self):
        return '%s' % (self.medico)

    def verificaCoerencia(self, errors):
        if date.today () > self.dia:
            errors['dia'] = 'Não é possível viajar no tempo para datas passadas.'

    def get_dia(self):
        return self.dia.strftime('%d/%m/%Y')

    def get_dia(self):
        return self.horario.strftime ('%H:%M')


# class Consultas(models.Model):
#     titulo = models.CharField(max_length = 100)
#     descricao = models.TextField(blank=True, null=True)
#     data_agendamento = models.DateTimeField(verbose_name= 'Data do Agendamento')
#     data_criacao = models.DateTimeField(auto_now=True) #sera automatico
#     usuario = models.ForeignKey(User, on_delete = models.CASCADE)
#     medico = models.ForeignKey (Medico, on_delete=models.CASCADE)
#
#
#     class Meta:
#         db_table = 'consultas' #o nome da nossa tabela será evento, Caso a tabela já esteja criada é só deletar
#
#     def __str__(self):
#         return self.titulo
#
#     def get_data_agendamento(self):
#         return self.data_agendamento.strftime('%d/%m/%Y %H:%M Hrs')
#
#     def get_data_input_agendamento(self):
#         return self.data_agendamento.strftime('%Y-%m-%dT%H:%M')#precisamos da id e ele só reconhece se for nesse formato
#
#     def get_evento_atrasado(self):
#         if self.data_evento < datetime.now():
#             return True
#         else:
#             return False