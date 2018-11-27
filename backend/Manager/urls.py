from django.urls import path
from . import views

urlpatterns = [
    path('campaigns/<int:id>/edit', views.campaign_edit, name='edit campaign with id'),
    path('campaigns/<int:id>/start', views.campaign_start, name='start a campaign'),
    path('campaigns/<int:id>/create_assignment', views.generate_assignment, name='create assignments for a campaign'),
    path('campaigns/create', views.campaign_create, name='create campaign'),
    # path('campaigns', views.campaigns, name='view all campaigns'),
    # path('campaigns/availabilities', views.canvasser_availabilities, name='view canvasser availabilities')
]
