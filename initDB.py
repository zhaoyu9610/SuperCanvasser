import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SuperCanvasser.settings")

django.setup()

from backend import models

# create all the date in 2018 month 10, 11, 12
for month in [11, 12]:
    for day in range(31):
        try:
            dt = date(year=2018, month=month, day=day+1)
            models.CampaignDate.objects.update_or_create(date=dt)
        except ValueError as e:
            pass

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
    password='manager',
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
    models.Availability.objects.update_or_create(date_id=uid, canvasser=canvasser)


for street, city, state in [('5 Saywood Lane', 'Stony Brook', 'NY'),
                            ('Avalon Pines Drive', 'Coram', 'NY'),
                            ('5 Seabrook Court', 'Stony Brook', 'NY'),
                            ('398 Pond Path', 'Setauket-East Seauket', 'NY'),
                            ('1417 Stony Brook Road', 'Stony Brook', 'NY')]:
    models.Location.objects.update_or_create(street=street, city=city, state=state, zipcode='')

campaign, _ = models.Campaign.objects.update_or_create()
campaign.managers.add(manager)
campaign.locations.add(1, 2, 3)
campaign.canvassers.add(canvasser)


models.Parameter.objects.update_or_create(name='hours', value=8)
models.Parameter.objects.update_or_create(name='speed', value=60)
