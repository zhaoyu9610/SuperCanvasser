from backend import utils, models
import json


class AdministratorHandler:
    def users(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_admin(uid):
                result = []
                users = models.User.objects.all()
                for user in users:
                    result.append(user.dict())
                return utils.generate_response(request, {'users': result})
            else:
                return utils.generate_error(request, 'Not admin')
        else:
            return utils.generate_error(request, 'Not logged in')

    def parameters(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_admin(uid):
                result = []
                parameters = models.Parameter.objects.all()
                for parameter in parameters:
                    result.append(parameter.dict())
                return utils.generate_response(request, {'parameters': result})
            else:
                return utils.generate_error(request, 'Not admin')
        else:
            return utils.generate_error(request, 'Not logged in')

    def user_edit(self, request):
        try:
            body = json.loads(request.body)
            users_dict = body['users']
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_admin(uid):
                for user in users_dict:
                    models.User.objects.filter(id=user['id']).update(**user)
                return utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not admin')
        else:
            return utils.generate_error(request, 'Not logged in')

    def parameter_update(self, request):
        try:
            body = json.loads(request.body)
            parameters = body['parameters']
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_admin(uid):
                for parameter in parameters:
                    models.Parameter.objects.filter(name=parameter['name']).update(**parameter)
                return utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not admin')
        else:
            return utils.generate_error(request, 'Not logged in')
