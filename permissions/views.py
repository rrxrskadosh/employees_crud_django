from rest_framework import generics
from permissions.models import Permission
from rest_framework.permissions import AllowAny, IsAuthenticated
from permissions.serializers import PermissionSerializer, PermissionGenericSerializer, PermissionDetailGenericSerializer

#CreatePermissionSerializer


class PermissionGenericView(generics.ListCreateAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAuthenticated,)


class PermissionDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PermissionDetailGenericSerializer
        return PermissionSerializer