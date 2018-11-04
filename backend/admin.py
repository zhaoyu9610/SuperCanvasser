from django.contrib import admin
from backend.models import *

admin.site.register([User, Availability, Campaign, CampaignDate, Assignment, Result,
                     Location, Parameter])

