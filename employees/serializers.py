from rest_framework.serializers import ModelSerializer

from employees.models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeGenericView(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('nombre',)


class EmployeeDetailGenericView(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('descripcion',)


class CreateEmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'