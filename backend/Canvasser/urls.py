from django.urls import path
from . import views

urlpatterns = [
    path('edit_availability', views.edit_availability, name='edit availability'),
    path('submit', views.submit, name='submit result for a location'),
    path('new_order', views.new_order, name='generate new order'),
]
