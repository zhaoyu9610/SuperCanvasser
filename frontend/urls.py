from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('account', views.account, name='account'),
    path('campaigns', views.campaigns, name='table for campaigns'),
    path('campaigns/<int:cid>', views.campaign, name='view page for campaign with id'),
    path('campaigns/<int:cid>/edit', views.campaign_edit, name='edit page for campaign with id'),
    path('campaigns/<int:cid>/assignments', views.campaign_assignments, name='table for assignments for the campaigns'),
    path('campaigns/<int:cid>/result', views.campaign_result, name='result of a campaign'),
    path('campaigns/<int:cid>/assignments/<int:aid>', views.campaign_assignment, name='view page for an assignment'),
    path('campaigns/create', views.campaign_create, name='create page for campaign'),
    path('assignments', views.canvasser_assignments, name='table for assignments for a canvasser'),
    path('assignments/<int:aid>', views.canvasser_assignment, name='view page for an assignment'),
    path('assignments/current', views.current_assignment, name='view page for current assignment'),
    path('assignments/canvass/<int:aid>', views.canvass, name='canvass the current assignment'),
    path('admin', views.admin, name='home page for admin')]
