import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from . import controller
from . import utils

handler = controller.ApplicationHandler()


@csrf_exempt
def login(request):
    return handler.login(request)


@csrf_exempt
def logout(request):
    if 'cookie' in request.COOKIES:
        data = json.dumps({'status': 'ok',
                           'method': request.method,
                           'url': request.build_absolute_uri()})
        response = HttpResponse(data, content_type='application/json')
        response.set_cookie('cookie', None, expires=datetime.now())
        return response
    return utils.generate_error(request, 'Not logged in')


@csrf_exempt
def signup(request):
    return handler.signup(request)
