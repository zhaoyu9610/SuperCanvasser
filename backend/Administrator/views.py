from django.views.decorators.csrf import csrf_exempt
from . import controller

handler = controller.AdministratorHandler()


@csrf_exempt
def user_edit(request):
    return handler.user_edit(request)


@csrf_exempt
def parameter_update(request):
    return handler.parameter_update(request)


# @csrf_exempt
# def users(request):
#     return handler.users(request)


# @csrf_exempt
# def parameters(request):
#     return handler.parameters(request)
