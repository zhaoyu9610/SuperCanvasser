from django.urls import path
from . import views

urlpatterns = [
    path('campaigns', views.campaigns, name='view all campaigns'),
    path('campaigns/<int:id>/edit', views.campaign_edit, name='edit campaign with id'),
    path('campaigns/create', views.campaign_create, name='create campaign'),
    path('campaigns/availabilities', views.canvasser_availabilities, name='view canvasser availabilities')
]
