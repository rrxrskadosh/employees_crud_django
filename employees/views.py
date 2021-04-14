from rest_framework import generics
from employees.models import Employee

from employees.serializers import EmployeeSerializer, CreateEmployeeSerializer


class EmployeeGenericView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateEmployeeSerializer
        return EmployeeSerializer


class EmployeeDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
