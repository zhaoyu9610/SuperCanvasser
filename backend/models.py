from django.db import models
import json


class CampaignDate(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, verbose_name="Date", unique=True)

    def dict(self):
        return {'id': self.id, 'date': [self.date.year, self.date.month, self.date.day]}


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, verbose_name="Email address", unique=True)
    password = models.CharField(max_length=32, verbose_name="Password")
    admin = models.BooleanField(verbose_name='Administrator', default=False)
    manager = models.BooleanField(verbose_name='Manager', default=False)
    canvasser = models.BooleanField(verbose_name='canvasser', default=False)

    def dict(self):
        return {'id': self.id, 'email': self.email, 'password': self.password, 'admin': self.admin,
                'canvasser': self.canvasser, 'manager': self.manager}


class Availability(models.Model):
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


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    street = models.CharField(max_length=50, verbose_name='Street')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.CharField(max_length=2, verbose_name='State')
    zipcode = models.CharField(max_length=10, verbose_name='Zip code')
    lon = models.FloatField(verbose_name='longitude', default=None)
    lat = models.FloatField(verbose_name='latitude', default=None)

    def dict(self):
        return {'id': self.id, 'street': self.street, 'city': self.city, 'zipcode': self.zipcode, 'longitude': self.lon, 'latitude': self.lat}


class Campaign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Campaign name', max_length=100, default='Campaign Name')
    talking_points = models.TextField(verbose_name='Talking points', default='[]')
    start = models.BooleanField(verbose_name='Start', default=False)
    finish = models.BooleanField(verbose_name='Finish', default=False)
    median = models.FloatField(verbose_name='Median', default=None, null=True)
    average = models.FloatField(verbose_name='Average', default=None, null=True)
    sd = models.FloatField(verbose_name='Standard deviation', default=None, null=True)
    questions = models.TextField(verbose_name='questions', default='[]')
    duration = models.FloatField(verbose_name='duration', default=0.5)

    manager = models.ForeignKey(to='User', to_field='id', on_delete=models.SET_DEFAULT, default=None, verbose_name='Manager', related_name='Manager')
    canvassers = models.ManyToManyField(to='User', verbose_name='Canvassers', related_name='Canvassers')
    locations = models.ManyToManyField(to='Location', verbose_name='Locations')
    dates = models.ManyToManyField(to='CampaignDate', verbose_name='Dates')

    def dict(self):
        if self.talking_points is not '':
            talking_points = json.loads(self.talking_points)
        else:
            talking_points = ''
        if self.questions is not '':
            questions = json.loads(self.questions)
        else:
            questions = ''
        return {'id': self.id, 'talking_points': talking_points, 'start': self.start, 'finish': self.finish, 'median': self.median, 'duration':self.duration,
                'average': self.average, 'sd': self.sd, 'questions': questions, 'manager': self.manager.dict(), 'canvasers': [a.dict() for a in self.canvassers.all()],
                'locations': [a.dict() for a in self.locations.all()], 'dates': [a.dict() for a in self.dates.all()]}


class Parameter(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField(verbose_name='value')
    name = models.CharField(max_length=50, verbose_name='name', unique=True)

    def dict(self):
        return {'id': self.id, 'value': self.value, 'name': self.name}


class Assignment(models.Model):
    id = models.AutoField(primary_key=True)
    duration = models.FloatField(verbose_name='Duration')

    campaign = models.ForeignKey(to='Campaign', to_field='id', on_delete=models.CASCADE, verbose_name='Campaign')
    canvasser = models.ForeignKey(to='User', to_field='id', on_delete=models.PROTECT, verbose_name='Canvasser')
    date = models.ForeignKey(to='CampaignDate', to_field='id', on_delete=models.PROTECT, verbose_name='Visit Date')
    locations = models.ManyToManyField(to='Location', verbose_name='Locations')

    def dict(self):
        return {'id': self.id, 'duration': self.duration, 'campaign': self.campaign.dict(), 'canvassers': self.canvasser.dict(),
                'date': self.date.dict(), 'locations': [a.dict() for a in self.locations.all()]}


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    number_of_people = models.IntegerField(verbose_name='The number of people spoke to', default=0)
    rating = models.IntegerField(verbose_name='rating', default=0)
    answers = models.TextField(verbose_name='answers', default='{}')
    notes = models.TextField(verbose_name='brief note', default='')

    assignment = models.ForeignKey(to='Assignment', to_field='id', on_delete=models.SET_DEFAULT, default=None, verbose_name='Assignment')
    location = models.ForeignKey(to='Location', to_field='id', verbose_name='Location', on_delete=models.SET_DEFAULT, default=None)

    def dict(self):
        return {'id': self.id, 'assignment': self.assignment.dict(), 'location': self.location.dict(), 'answers': json.loads(self.answers),
                'rating': self.rating, 'number_of_people': self.number_of_people, 'notes': self.notes}


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    answers = models.TextField(verbose_name='answers')

    def dict(self):
        if self.answers is not '':
            answers = json.loads(self.answers)
        else:
            answers = ''
        return {'id': self.id, 'answers': answers}


