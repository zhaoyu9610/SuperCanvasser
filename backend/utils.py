import json
from django.http import HttpResponse
from . import models
import logging
import datetime

logger = logging.getLogger('django')


def generate_error(request, error):
    result = {'status': 'error',
              'error': error,
              'method': request.method,
              'url': request.build_absolute_uri()}
    if request.method is 'POST':
        result['body'] = json.loads(request.body)
    result = json.dumps(result)
    logger.debug(result)
    return HttpResponse(result, content_type='application/json')


def generate_response(request, dict):
    dict['status'] = 'ok'
    dict['method'] = request.method
    dict['url'] = request.build_absolute_uri()
    if request.method == 'POST':
        dict['body'] = json.loads(request.body)
    result = json.dumps(dict)
    logger.debug(result)
    return HttpResponse(result, content_type='application/json')


def check_admin(uid):
    user = models.User.objects.get(id=uid)
    return user.admin


def check_manager(uid):
    user = models.User.objects.get(id=uid)
    return user.manager


def check_canvasser(uid):
    user = models.User.objects.get(id=uid)
    return user.canvasser


def get_user(users):
    result = []
    for u in users:
        result.append(models.User.objects.filter(email=u).get().id)
    return result


def add_locations(locations):
    result = []
    for l in locations:
        number, street, city, state, zipcode = l.split(',')
        location, _ = models.Location.objects.update_or_create(
            street=number.strip() + ' ' + street.strip(),
            city=city.strip(),
            state=state.strip(),
            zipcode=zipcode.strip()
        )
        result.append(location.id)
    return result


def get_dates(dates):
    result = []
    for start, end in dates:
        d1 = datetime.date(start[0], start[1], start[2])
        d2 = datetime.date(end[0], end[1], end[2])
        delta = d2 - d1
        for i in range(delta.days + 1):
            result.append(d1 + datetime.timedelta(i))
    return result