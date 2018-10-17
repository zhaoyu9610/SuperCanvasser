from django.urls import path
from . import views

urlpatterns = [
    path('edit_availability', views.edit_availability, name='edit availability'),
    path('availability', views.availability, name='list of availability'),
]
