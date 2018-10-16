import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import controller

handler = controller.CanvasserHandler()


@csrf_exempt
def edit_availability(request):
    return handler.edit_availability(request)

@csrf_exempt
def availabilities(request):
    return handler.availabilities(request)

@csrf_exempt
def availability(request):
    return handler.availability(request)
