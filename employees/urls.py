from django.urls import path

from employees.views import EmployeeGenericView, EmployeeDetailGenericView

app_name = 'employees'
urlpatterns = [
    path('', EmployeeGenericView.as_view()),
    path('<pk>/', EmployeeDetailGenericView.as_view())
]