from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import EspecialidadeSerializer, MedicoSerializer
from .models import Especialidade, Medico


class EspecialidadeViewSet(viewsets.ModelViewSet):
    serializer_class = EspecialidadeSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Especialidade.objects.filter

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    # este ultimo campo é para usar o postman