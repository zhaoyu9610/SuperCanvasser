import os
import django
from SuperCanvasser import models
import json
from datetime import date, datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ASBTBackendProject.settings")

django.setup()

# create all the date in 2018 month 10, 11, 12
for month in [10, 11, 12]:
    for day in range(31):
        date = date(year=2018, month=month, day=day+1)
        models.CampaignDate.objects.update_or_create(date=date)

models.CampaignDate.objects.filter(date=date(year=2018, month=11, day=31)).delete()

# create three user with three single role
admin, _ = models.User.objects.update_or_create(
    email='admin@admin.com',
    password='admin',
    admin=True,
    manager=False,
    canvasser=False,
)
manager, _ = models.User.objects.update_or_create(
    email='manager@manager.com',
    password='',
    admin=False,
    manager=True,
    canvasser=False,
)
canvasser, _ = models.User.objects.update_or_create(
    email='canvasser@canvasser.com',
    password='canvasser',
    admin=False,
    manager=False,
    canvasser=True,
)

# add some random availabilities for canvasser
for uid in [1, 3, 5, 7, 10, 13, 15, 17, 20]:
    models.Availability.objects.update_or_create(date_uid=uid, canvasser=canvasser)


