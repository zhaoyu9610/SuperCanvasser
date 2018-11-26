from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path('', include('frontend.urls')),
]
urlpatterns += staticfiles_urlpatterns()