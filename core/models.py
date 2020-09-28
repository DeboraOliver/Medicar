from django.db import models
from django.contrib.auth.models import User

class Especialidade(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    nome = models.CharField ("Nome", max_length=200, blank=False, null=False)
    crm = models.IntegerField ("CRM", max_length=11, null=False)
    email = models.EmailField ()
    telefone = models.IntegerField ("Telefone")
    especialidade = models.ForeignKey (Especialidade, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome