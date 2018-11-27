import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SuperCanvasser.settings")

django.setup()

from backend import models

for month in [11, 12]:
    for day in range(31):
        try:
            dt = date(year=2018, month=month, day=day+1)
            models.CampaignDate.objects.update_or_create(date=dt)
        except ValueError as e:
            pass

admin, _ = models.User.objects.update_or_create(
    email='admin@admin.com',
    password='admin',
    admin=True,
    manager=False,
    canvasser=False,
)
manager, _ = models.User.objects.update_or_create(
    email='manager@manager.com',
    password='manager',
    admin=False,
    manager=True,
    canvasser=False,
)

for i in range(12):
    canvasser, _ = models.User.objects.update_or_create(
        email='canvasser{}@canvasser.com'.format(i),
        password='canvasser',
        admin=False,
        manager=False,
        canvasser=True,
    )

models.Parameter.objects.update_or_create(name='hours', value=8)
models.Parameter.objects.update_or_create(name='speed', value=60)
