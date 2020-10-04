from rest_framework import viewsets
from django.utils import timezone
from rest_framework import permissions, authentication
from .serializers import EspecialidadeSerializer, MedicoSerializer, AgendaSerializer, ConsultaSerializer
from .models import Especialidade, Medico, Agenda, Consulta


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all ()
    serializer_class = EspecialidadeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    # este ultimo campo é para usar o postman

class AgendaViewSet(viewsets.ModelViewSet):
    now = timezone.now()
    queryset = Agenda.objects.filter(dia__gte=now).order_by('dia')
    serializer_class = AgendaSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

# class AgendaViewSet(viewsets.ListView):
#     def get_queryset(self):
#         now = timezone.now()
#         futuro = Agenda.objects.fiter(dia__gte=now)
#         serializer_class = AgendaSerializer
#         permission_classes = [permissions.IsAuthenticated]
#         authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
#         return list(futuro)

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    # def get_queryset(self):
    #     owner = self.request.user
    #     return Consulta.objects.filter