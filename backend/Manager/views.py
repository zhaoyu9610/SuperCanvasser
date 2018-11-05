from django.views.decorators.csrf import csrf_exempt
from . import controller

handler = controller.ManagerHandler()


@csrf_exempt
def campaigns(request):
    return handler.campaigns(request)


@csrf_exempt
def campaign_edit(request, id=1):
    return handler.campaign_edit(request, id)


@csrf_exempt
def campaign_create(request):
    return handler.campaign_create(request)


@csrf_exempt
def canvasser_availabilities(request):
    return handler.availabilities(request)


def generate_assignment(request, cid):
    return handler.generate_assignemnts(request, cid)