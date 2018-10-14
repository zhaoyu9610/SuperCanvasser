"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include
from . import views

urlpatterns = [
    url(r'^login$', views.login, name='Log in'),
    url(r'^logout$', views.logout, name='Log out'),
    url(r'^signup$', views.signup, name='Sign up'),
    url(r'^canvassers$', views.canvassers, name='List of canvassers'),
    url(r'^manager/', include(('SuperCanvasser.Manager.urls', 'Manager'), namespace='Manager')),
    url(r'^canvasser/', include(('SuperCanvasser.Canvasser.urls', 'Canvasser'), namespace='Canvasser')),
    url(r'^administrator/', include(('SuperCanvasser.Administrator.urls', 'Administrator'), namespace='Administrator')),
]
