import json
from . import models
from . import utils


class ApplicationHandler:
    def login(self, request):
        try:
            body = json.loads(request.body)
            email = body['email']
            password = body['password']
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        user_model = models.User.objects.filter(email__exact=email, password__exact=password)
        if user_model.count() == 1:
            user = user_model.get()
            token = str(user.id)
            roles = [user.canvasser, user.manager, user.admin]
            response = utils.generate_response(request, {'role': roles})
            response.set_cookie('cookie', token)
            return response
        else:
            return utils.generate_error(request, 'No such user')

    def signup(self, request):
        try:
            body = json.loads(request.body)
            email = body['email']
            password = body['password']
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        user = {'email': email, 'password': password}
        user_obj = models.User.objects.create(**user)
        try:
            user_obj.save()
        except Exception as e:
            return utils.generate_error(request, 'Email already used')
        return utils.generate_response(request, {})

    def update_account(self, request):
        try:
            body = json.loads(request.body)
            user_dict = body['user']
            user_dict.pop('id', None)
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            models.User.objects.filter(id=id).update(**user_dict)
            return utils.generate_response(request, {})
        else:
            return utils.generate_error(request, 'Not logged in')