import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import controller

handler = controller.AdministratorHandler()


@csrf_exempt
def users(request):
    return handler.users(request)


@csrf_exempt
def user_edit(request, id=1):
    return handler.user_edit(request, id)


@csrf_exempt
def parameters(request):
    return handler.parameters(request)


@csrf_exempt
def parameter_update(request):
    return handler.parameter_update(request)
