import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import controller

handler = controller.ManagerHandler()


@csrf_exempt
def campaigns(request):
    data = json.dumps({'status': 'ok',
                       'method': request.method,
                       'url': request.build_absolute_uri()})
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def campaign_edit(request):
    data = json.dumps({'status': 'ok',
                       'method': request.method,
                       'url': request.build_absolute_uri()})
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def campaign_create(request):
    data = json.dumps({'status': 'ok',
                       'method': request.method,
                       'url': request.build_absolute_uri()})
    return HttpResponse(data, content_type='application/json')
