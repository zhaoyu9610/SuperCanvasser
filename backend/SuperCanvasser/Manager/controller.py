from SuperCanvasser import utils, models
import json


class ManagerHandler:
    def campaigns(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_admin(uid):
                result = []
                campaigns = models.Campaign.objects.all()
                for campaign in campaigns:
                    result.append(campaign.__dict__)
                utils.generate_response(request, {'campaigns': result})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')

    def campaign_edit(self, request, id):
        try:
            body = json.loads(request.body)
            campaign_dict = body['campaign']
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_admin(uid):
                models.Campaign.objects.filter(uid=id).update(**campaign_dict)
                utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')

    def campaign_create(self, request):
        try:
            body = json.loads(request.body)
            campaign_dict = body['campaign']
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_admin(uid):
                models.Campaign.objects.create(**campaign_dict)
                utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')

    def availabilities(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_admin(uid):
                result = []
                for user in models.User.objects.filter(canvasser=True).all():
                    dates = []
                    for campaign_date in models.Availability.objects.filter(canvasser=user).all():
                        dates.append(campaign_date.date)
                    result.append({'uid': user.uid, 'email': user.email, 'availability': dates})
                utils.generate_response(request, {'availabilities': result})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')
