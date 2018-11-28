from django.views.decorators.csrf import csrf_exempt
from . import controller

handler = controller.CanvasserHandler()


@csrf_exempt
def edit_availability(request):
    return handler.edit_availability(request)


@csrf_exempt
def submit(request):
    return handler.submit(request)



@csrf_exempt
def new_order(request):
    return handler.new_order(request)


