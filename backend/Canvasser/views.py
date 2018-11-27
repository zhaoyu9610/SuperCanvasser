from django.views.decorators.csrf import csrf_exempt
from . import controller

handler = controller.CanvasserHandler()


@csrf_exempt
def edit_availability(request):
    return handler.edit_availability(request)
