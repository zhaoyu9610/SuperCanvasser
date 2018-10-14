from django.contrib import admin
from SuperCanvasser.models import *

admin.site.register([User, Availability. Campaign, CampaignDate, Assignment, Result,
                     Answer, Location, Parameter])

