from django.urls import path

from roles.views import RoleGenericView, RoleDetailGenericView

app_name = 'roles'
urlpatterns = [
    path('', RoleGenericView.as_view()),
    path('<pk>/', RoleDetailGenericView.as_view())
]