from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('account', views.account, name='account'),
    path('manager', views.manager, name='manager home page'),
    path('manager/campaigns/<int:id>', views.campaign, name='campaign page'),
    path('canvasser', views.canvasser, name='canvasser home page'),
    path('canvasser/assignments/<int:id>', views.assignment, name='assignments page'),
    path('canvasser/assignments/current', views.current, name='current assignment')
]
