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
            token = str(user.uid)
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

    def canvassers(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_admin(uid) or utils.check_manager(uid):
                result = []
                users = models.User.objects.filter(canvasser=True).all()
                for user in users:
                    result.append({'uid': user.uid,
                                   'email': user.email})
                utils.generate_response(request, {'users': result})
            else:
                return utils.generate_error(request, 'Not admin or manager to view canvasser list')
        else:
            return utils.generate_error(request, 'Not logged in')
