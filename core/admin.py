from django.contrib import admin
from .models import Especialidade, Medico, Agenda, Horas, Consulta


admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Agenda)
admin.site.register(Horas)
admin.site.register(Consulta)
