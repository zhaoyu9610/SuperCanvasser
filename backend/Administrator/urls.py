from django.urls import path
from . import views

urlpatterns = [
    path('update_users', views.user_edit, name='edit user'),
    path('update_parameters', views.parameter_update, name='edit parameters')
    # path('users', views.users, name='view all users'),
    # path('parameters', views.parameters, name='view all parameters'),
]
