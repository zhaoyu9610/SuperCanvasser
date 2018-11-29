from django.db import models
import json
import datetime
from . import geoutils


class CampaignDate(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, verbose_name="Date", unique=True)

    def dict(self):
        return {'id': self.id, 'date': [self.date.year, self.date.month, self.date.day]}

    def __str__(self):
        return self.date.__str__()


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, verbose_name="Email address", unique=True)
    phone = models.CharField(max_length=10, verbose_name='Phone number', default='0000000000')
    gender = models.BooleanField(default=True, verbose_name='gender')
    address = models.TextField(default='', verbose_name='address')
    password = models.CharField(max_length=32, verbose_name="Password")
    # first_name = models.CharField(max_length=50, verbose_name='first name', default='first name')
    # last_name = models.CharField(max_length=50, verbose_name='last name', default='last name')
    admin = models.BooleanField(verbose_name='Administrator', default=False)
    manager = models.BooleanField(verbose_name='Manager', default=False)
    canvasser = models.BooleanField(verbose_name='canvasser', default=False)

    def dict(self):
        return {'id': self.id, 'email': self.email, 'password': self.password, 'admin': self.admin,
                'canvasser': self.canvasser, 'manager': self.manager, 'phone': self.phone, 'gender': self.gender,
                'address': self.address}

    def __str__(self):
        return self.email


class Availability(models
                   .Model):
    id = models.AutoField(primary_key=True)

    date = models.ForeignKey(to='CampaignDate', to_field='id', on_delete=models.PROTECT)
    canvasser = models.ForeignKey(to='User', to_field='id', on_delete=models.CASCADE)
    assignment = models.OneToOneField(to='Assignment', to_field='id', on_delete=models.SET_DEFAULT, default=None, null=True)

    def dict(self):
        if self.assignment:
            assignment = self.assignment.dict()
        else:
            assignment = {}
        return {'id': self.id, 'date': self.date.dict(), 'assignment': assignment}

    def __str__(self):
        return self.canvasser.__str__() + " " + self.date.__str__()


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=200, verbose_name='Number')
    street = models.CharField(max_length=200, verbose_name='Street')
    unit = models.CharField(max_length=200, verbose_name='unit')
    city = models.CharField(max_length=200, verbose_name='City')
    state = models.CharField(max_length=200, verbose_name='State')
    zipcode = models.CharField(max_length=200, verbose_name='Zip code')
    lon = models.FloatField(verbose_name='longitude', default=None, null=True)
    lat = models.FloatField(verbose_name='latitude', default=None, null=True)

    def name(self):
        return ', '.join([self.number, self.street, self.unit, self.city, self.state, self.zipcode])

    def dict(self):
        if not self.lon or not self.lat:
            self.lon, self.lat = geoutils.generate_log_lat({'id': self.id, 'street': self.number + ' ' + self.street, 'state': self.state, 'city': self.city, 'zipcode': self.zipcode,})
            self.save()
        return {'id': self.id, 'number': self.number, 'street': self.street, 'unit': self.unit, 'state': self.state, 'city': self.city, 'zipcode': self.zipcode, 'longitude': self.lon, 'latitude': self.lat}

    def __str__(self):
        return self.street + " " + self.state


class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Campaign name', max_length=100, default='Campaign Name')
    talking_points = models.TextField(verbose_name='Talking points', default='[]')
    start = models.BooleanField(verbose_name='Start', default=False)
    finish = models.BooleanField(verbose_name='Finish', default=False)
    median = models.FloatField(verbose_name='Median', default=None, null=True, blank=True)
    average = models.FloatField(verbose_name='Average', default=None, null=True, blank=True)
    sd = models.FloatField(verbose_name='Standard deviation', default=None, null=True, blank=True)
    questions = models.TextField(verbose_name='questions', default='[]')
    duration = models.FloatField(verbose_name='duration', default=0.5)
    start_date = models.DateField(verbose_name='start date', default=datetime.date.today)
    end_date = models.DateField(verbose_name='end date', default=datetime.datetime(2018, 12, 31))

    managers = models.ManyToManyField(to='User', verbose_name='Managers', related_name='Managers', blank=True)
    canvassers = models.ManyToManyField(to='User', verbose_name='Canvassers', related_name='Canvassers', blank=True)
    locations = models.ManyToManyField(to='Location', verbose_name='Locations', blank=True)

    def dict(self):
        return {'id': self.id, 'name': self.name, 'talking_points': json.loads(self.talking_points), 'start': self.start, 'finish': self.finish, 'median': self.median, 'duration':self.duration,
                'average': self.average, 'sd': self.sd, 'questions': json.loads(self.questions), 'manager': [a.dict() for a in self.managers.all()], 'canvassers': [a.dict() for a in self.canvassers.all()],
                'locations': [a.dict() for a in self.locations.all()], 'start_date':  [self.start_date.year, self.start_date.month, self.start_date.day],
                'end_date': [self.end_date.year, self.end_date.month, self.end_date.day]}

    def __str__(self):
        return str(self.id) + ' ' + self.name


class Parameter(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField(verbose_name='value')
    name = models.CharField(max_length=50, verbose_name='name', unique=True)

    def dict(self):
        return {'id': self.id, 'value': self.value, 'name': self.name}

    def __str__(self):
        return self.name + ': ' + str(self.value)


class Assignment(models.Model):
    id = models.AutoField(primary_key=True)
    duration = models.FloatField(verbose_name='Duration')
    finished = models.BooleanField(verbose_name='Finished', default=False)

    campaign = models.ForeignKey(to='Campaign', to_field='id', on_delete=models.CASCADE, verbose_name='Campaign')
    canvasser = models.ForeignKey(to='User', to_field='id', on_delete=models.PROTECT, verbose_name='Canvasser')
    date = models.ForeignKey(to='CampaignDate', to_field='id', on_delete=models.PROTECT, verbose_name='Visit Date', default=None)
    locations = models.ManyToManyField(to='Location', verbose_name='Locations')

    def dict(self):
        return {'id': self.id, 'duration': self.duration, 'campaign': self.campaign.dict(), 'canvassers': self.canvasser.dict(),
                'date': self.date.dict(), 'locations': [a.dict() for a in self.locations.all()], 'finished': self.finished}

    def __str__(self):
        return self.campaign.__str__() + ' ' + str(self.id)


class LocationResult(models.Model):
    id = models.AutoField(primary_key=True)
    number_of_people = models.IntegerField(verbose_name='The number of people spoke to', default=0)
    rating = models.IntegerField(verbose_name='rating', default=0)
    answers = models.TextField(verbose_name='answers', default='[]')
    notes = models.TextField(verbose_name='brief note', default='')
    result = models.TextField(verbose_name='result', default='[]')

    campaign = models.ForeignKey(to='Campaign', to_field='id', on_delete=models.CASCADE)
    assignment = models.ForeignKey(to='Assignment', to_field='id', on_delete=models.SET_DEFAULT, default=None, verbose_name='Assignment')
    location = models.ForeignKey(to='Location', to_field='id', verbose_name='Location', on_delete=models.SET_DEFAULT, default=None)

    def dict(self):
        return {'id': self.id, 'assignment': self.assignment.dict(), 'location': self.location.dict(), 'answers': json.loads(self.answers),
                'rating': self.rating, 'number_of_people': self.number_of_people, 'notes': self.notes}

    def __str__(self):
        return self.assignment.__str__() + ' result'


class CampaignResult(models.Model):
    id = models.AutoField(primary_key=True)

    campaign = models.ForeignKey(to='Campaign', to_field='id', on_delete=models.CASCADE, verbose_name='Campaign')
    location_result = models.ManyToManyField(to='LocationResult', verbose_name='location result')
    result = models.TextField(verbose_name='result')

    def dict(self):
        return {'id': self.id, 'assignment': self.campaign.dict(), 'location_result': [a.dict() for a in self.location_result.all()],
                'result': self.result}

    def __str__(self):
        return self.campaign.__str__() + ' result'
