import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

django.setup()

from SuperCanvasser import models


models.Parameter.objects.all().delete()
models.Campaign.objects.all().delete()
models.Location.objects.all().delete()
models.Availability.objects.all().delete()
models.User.objects.all().delete()
