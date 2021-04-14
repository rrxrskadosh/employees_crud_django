from django.urls import path

from permissions.views import PermissionGenericView, PermissionDetailGenericView

app_name = 'permissions'
urlpatterns = [
    path('', PermissionGenericView.as_view()),
    path('<pk>/', PermissionDetailGenericView.as_view())
]