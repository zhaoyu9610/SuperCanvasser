from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.login, name='Log in'),
    path('logout', views.logout, name='Log out'),
    path('signup', views.signup, name='Sign up'),
    path('manager/', include('backend.Manager.urls')),
    path('canvasser/', include('backend.Canvasser.urls')),
    path('administrator/', include('backend.Administrator.urls')),
]