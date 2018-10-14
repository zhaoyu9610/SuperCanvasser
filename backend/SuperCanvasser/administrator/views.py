import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import controller

handler = controller.ApplicationHandler()


@csrf_exempt
def users(request):
    data = json.dumps({'status': 'ok',
                       'method': request.method,
                       'url': request.build_absolute_uri()})
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def user_edit(request):
    data = json.dumps({'status': 'ok',
                       'method': request.method,
                       'url': request.build_absolute_uri()})
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def parameters(request):
    data = json.dumps({'status': 'ok',
                       'method': request.method,
                       'url': request.build_absolute_uri()})
    return HttpResponse(data, content_type='application/json')


@csrf_exempt
def parameter_update(request):
    data = json.dumps({'status': 'ok',
                       'method': request.method,
                       'url': request.build_absolute_uri()})
    return HttpResponse(data, content_type='application/json')
