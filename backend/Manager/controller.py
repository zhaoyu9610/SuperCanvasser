from backend import utils, models
import json
import datetime


class ManagerHandler:
    def campaigns(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_manager(uid):
                result = []
                campaigns = models.Campaign.objects.filter(manager_id=uid).all()
                for campaign in campaigns:
                    result.append(campaign.dict())
                return utils.generate_response(request, {'campaigns': result})
            else:
                return utils.generate_error(request, 'Not manager')
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
            if utils.check_manager(uid):
                if 'end_date' in campaign_dict:
                    d = campaign_dict['end_date']
                    campaign_dict['end_date'] = datetime.date(d[0], d[1], d[2])
                if 'start_date' in campaign_dict:
                    d = campaign_dict['start_date']
                    campaign_dict['start_date'] = datetime.date(d[0], d[1], d[2])
                models.Campaign.objects.filter(id=id, manager_id=uid).update(**campaign_dict)
                if 'managers' in campaign_dict:
                    models.Campaign.objects.filter(id=id, manager_id=uid).managers.set(campaign_dict['managers'])
                if 'canvassers' in campaign_dict:
                    models.Campaign.objects.filter(id=id, manager_id=uid).canvassers.set(campaign_dict['canvassers'])
                if 'locations' in campaign_dict:
                    models.Campaign.objects.filter(id=id, manager_id=uid).locations.set(campaign_dict['locations'])
                return utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not manager')
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
            if utils.check_manager(uid):
                if 'end_date' in campaign_dict:
                    d = campaign_dict['end_date']
                    campaign_dict['end_date'] = datetime.date(d[0], d[1], d[2])
                if 'start_date' in campaign_dict:
                    d = campaign_dict['start_date']
                    campaign_dict['start_date'] = datetime.date(d[0], d[1], d[2])
                campaign_dict['manager_id'] = uid
                campaign, _ = models.Campaign.objects.update_or_create(**campaign_dict)
                if 'managers' in campaign_dict:
                    campaign.managers.set(campaign_dict['managers'])
                if 'canvassers' in campaign_dict:
                    campaign.canvassers.set(campaign_dict['canvassers'])
                if 'locations' in campaign_dict:
                    campaign.locations.set(campaign_dict['locations'])
                return utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not manager')
        else:
            return utils.generate_error(request, 'Not logged in')

    def availabilities(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_manager(uid):
                result = []
                for user in models.User.objects.filter(canvasser=True).all():
                    dates = []
                    for ava in models.Availability.objects.filter(canvasser=user).all():
                        if ava.assignment is None:
                            dates.append(ava.dict())
                    result.append({'uid': user.dict(), 'availability': dates})
                return utils.generate_response(request, {'availabilities': result})
            else:
                return utils.generate_error(request, 'Not manager')
        else:
            return utils.generate_error(request, 'Not logged in')
