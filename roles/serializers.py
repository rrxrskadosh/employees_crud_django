from rest_framework.serializers import ModelSerializer

from roles.models import Role


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class RoleGenericView(ModelSerializer):
    class Meta:
        model = Role
        fields = ('nombre',)


class RoleDetailGenericView(ModelSerializer):
    class Meta:
        model = Role
        fields = ('descripcion',)


class CreateRoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'