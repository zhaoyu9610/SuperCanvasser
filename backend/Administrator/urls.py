from django.urls import path
from . import views

urlpatterns = [
    path('users', views.users, name='view all users'),
    path('users/<int:id>/edit', views.user_edit, name='edit user'),
    path('parameters', views.parameters, name='view all parameters'),
    path('parameters/update', views.parameter_update, name='edit parameters')
]
