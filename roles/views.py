from rest_framework import generics
from roles.models import Role

from roles.serializers import RoleSerializer, CreateRoleSerializer


class RoleGenericView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateRoleSerializer
        return RoleSerializer


class RoleDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
