from django.db import models

ROLE_CHOICES = [(0, 'Admin'), (1, 'Manager'), (2, 'Canvasser')]
STATE_CHOICES = []


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, verbose_name="Email address", unique=True)
    password = models.CharField(max_length=32, verbose_name="Password")
    admin = models.BooleanField(verbose_name='Administrator', default=False)
    manager = models.BooleanField(verbose_name='Manager', default=False)
    canvasser = models.BooleanField(verbose_name='canvasser', default=False)


class Availability(models.Model):
    uid = models.AutoField(primary_key=True)

    date = models.ForeignKey(to='CampaignDate', to_field='uid', on_delete=models.PROTECT)
    canvasser = models.OneToOneField(to='User', to_field='uid', on_delete=models.CASCADE)
    assignment = models.ForeignKey(to='Assignment', to_field='uid', on_delete=models.SET_DEFAULT, default=None)


class Campaign(models.Model):
    uid = models.AutoField(primary_key=True)
    talking_points = models.TextField(verbose_name='Talking points')
    start = models.BooleanField(verbose_name='Start')
    finish = models.BooleanField(verbose_name='Finish', default=False)
    median = models.FloatField(verbose_name='Median', default=False)
    average = models.FloatField(verbose_name='Average', default=None)
    sd = models.FloatField(verbose_name='Standard deviation', default=None)
    questions = models.TextField(verbose_name='questions')

    manager = models.ForeignKey(to='User', to_field='uid', on_delete=models.SET_DEFAULT, default=None, verbose_name='Manager', related_name='Manager')
    canvassers = models.ManyToManyField(to='User', verbose_name='Canvassers', related_name='Canvassers')
    locations = models.ManyToManyField(to='Location', verbose_name='Locations')
    dates = models.ManyToManyField(to='CampaignDate', verbose_name='Dates')


class CampaignDate(models.Model):
    uid = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, verbose_name="Date", unique=True)


class Assignment(models.Model):
    uid = models.AutoField(primary_key=True)
    duration = models.FloatField(verbose_name='Duration')

    campaign = models.ForeignKey(to='Campaign', to_field='uid', on_delete=models.CASCADE, verbose_name='Campaign')
    canvasser = models.ForeignKey(to='User', to_field='uid', on_delete=models.PROTECT, verbose_name='Canvasser')
    date = models.ForeignKey(to='CampaignDate', to_field='uid', on_delete=models.PROTECT, verbose_name='Visit Date')
    locations = models.ManyToManyField(to='Location', verbose_name='Locations')


class Result(models.Model):
    uid = models.AutoField(primary_key=True)

    assignment = models.ForeignKey(to='Assignment', to_field='uid', on_delete=models.SET_DEFAULT, default=None, verbose_name='Assignment')
    location = models.ForeignKey(to='Location', to_field='uid', verbose_name='Location', on_delete=models.SET_DEFAULT, default=None)


class Answer(models.Model):
    uid = models.AutoField(primary_key=True)
    answers = models.TextField(verbose_name='answers')


class Location(models.Model):
    uid = models.AutoField(primary_key=True)
    street = models.CharField(max_length=50, verbose_name='Street')
    city = models.CharField(max_length=50, verbose_name='City')
    state = models.IntegerField(choices=STATE_CHOICES, verbose_name='State')
    zipcode = models.CharField(max_length=10, verbose_name='Zip code')


class Parameter(models.Model):
    uid = models.AutoField(primary_key=True)
    value = models.FloatField(verbose_name='value')
    name = models.CharField(max_length=50, verbose_name='name', unique=True)
