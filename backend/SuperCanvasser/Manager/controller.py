from SuperCanvasser import utils, models
import json


class ManagerHandler:
    def campaigns(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_admin(uid):
                result = []
                campaigns = models.Campaign.objects.filter(manager_id=uid).all()
                for campaign in campaigns:
                    result.append(campaign.dict())
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
                models.Campaign.objects.filter(id=id, manager_id=uid).update(**campaign_dict)
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
                campaign_dict['manager_id'] = uid
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
                    for ava in models.Availability.objects.filter(canvasser=user).all():
                        if ava.assignment is None:
                            dates.append(ava.dict())
                    result.append({'uid': user.dict(), 'availability': dates})
                utils.generate_response(request, {'availabilities': result})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')
