import json
from django.http import HttpResponse
from . import models


def generate_error(request, error):
    result = {'status': 'error',
              'error': error,
              'method': request.method,
              'url': request.build_absolute_uri()}
    if request.method is 'POST':
        result['body'] = json.loads(request.body)
    return HttpResponse(json.dumps(result), content_type='application/json')


def generate_response(request, dict):
    dict['status'] = 'ok'
    dict['method'] = request.method
    dict['url'] = request.build_absolute_uri()
    if request.method == 'POST':
        dict['body'] = json.loads(request.body)
    return HttpResponse(json.dumps(dict), content_type='application/json')


def check_admin(uid):
    user = models.User.objects.get(id=uid)
    return user.admin


def check_manager(uid):
    user = models.User.objects.get(id=uid)
    return user.manager


def check_canvasser(uid):
    user = models.User.objects.get(id=uid)
    return user.canvasser
