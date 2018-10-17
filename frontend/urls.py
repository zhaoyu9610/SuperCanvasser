from django.urls import path
from . import views

urlpatterns = [
    path('campaigns', views.index, name='index'),
]
