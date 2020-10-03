from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import EspecialidadeSerializer, MedicoSerializer, AgendaSerializer, ConsultaSerializer
from .models import Especialidade, Medico, Agenda, Horas,  Consulta


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all ()
    serializer_class = EspecialidadeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    # def get_queryset(self):
    #     user = self.request.user
    #     return Especialidade.objects.filter

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    # este ultimo campo é para usar o postman

# class HorasViewSet(viewsets.ModelViewSet):
    # queryset = Horas.objects.all ()
    # serializer_class = HorasSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]