from rest_framework.serializers import ModelSerializer

from permissions.models import Permission


class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class PermissionGenericSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ('nombre',)


class PermissionDetailGenericSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class CreatePermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'