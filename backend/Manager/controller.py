from backend import utils, models, geoutils
import json
import datetime


class ManagerHandler:
    def campaign_edit(self, request, id):
        try:
            body = json.loads(request.body)
            campaign_dict = body['campaign']
            print(campaign_dict)
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_manager(uid):
                if 'end_date' in campaign_dict:
                    if len(campaign_dict['end_date']) > 0:
                        d = campaign_dict['end_date']
                        campaign_dict['end_date'] = datetime.date(d[0], d[1], d[2])
                    else:
                        campaign_dict.pop('end_date')
                if 'start_date' in campaign_dict:
                    if len(campaign_dict['start_date']) > 0:
                        d = campaign_dict['start_date']
                        campaign_dict['start_date'] = datetime.date(d[0], d[1], d[2])
                    else:
                        campaign_dict.pop('start_date')
                if campaign_dict['duration'] is None:
                    campaign_dict.pop('duration')
                locations = campaign_dict.pop('locations', [])
                managers = campaign_dict.pop('managers', [])
                canvassers = campaign_dict.pop('canvassers', [])
                if 'talking_points' in campaign_dict:
                    campaign_dict['talking_points'] = json.dumps(campaign_dict['talking_points'])
                if 'questions' in campaign_dict:
                    campaign_dict['questions'] = json.dumps(campaign_dict['questions'])
                campaign = models.Campaign.objects.create(**campaign_dict)
                campaign.managers.set(utils.get_user(managers))
                campaign.canvassers.set(utils.get_user(canvassers))
                campaign.locations.set(utils.add_locations(locations))
                return utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not manager')
        else:
            return utils.generate_error(request, 'Not logged in')

    def campaign_create(self, request):
        try:
            body = json.loads(request.body)
            campaign_dict = body['campaign']
            print(campaign_dict)
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_manager(uid):
                if 'end_date' in campaign_dict:
                    if len(campaign_dict['end_date']) > 0:
                        d = campaign_dict['end_date']
                        campaign_dict['end_date'] = datetime.date(d[0], d[1], d[2])
                    else:
                        campaign_dict.pop('end_date')
                if 'start_date' in campaign_dict:
                    if len(campaign_dict['start_date']) > 0:
                        d = campaign_dict['start_date']
                        campaign_dict['start_date'] = datetime.date(d[0], d[1], d[2])
                    else:
                        campaign_dict.pop('start_date')
                if campaign_dict['duration'] is None:
                    campaign_dict.pop('duration')
                locations = campaign_dict.pop('locations', [])
                managers = campaign_dict.pop('managers', [])
                canvassers = campaign_dict.pop('canvassers', [])
                if 'talking_points' in campaign_dict:
                    campaign_dict['talking_points'] = json.dumps(campaign_dict['talking_points'])
                if 'questions' in campaign_dict:
                    campaign_dict['questions'] = json.dumps(campaign_dict['questions'])
                campaign = models.Campaign.objects.create(**campaign_dict)
                campaign.managers.set(utils.get_user(managers))
                campaign.canvassers.set(utils.get_user(canvassers))
                campaign.locations.set(utils.add_locations(locations))
                return utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not manager')
        else:
            return utils.generate_error(request, 'Not logged in')

    def generate_assignments(self, request, cid):
        geoutils.generate_assignment(cid)
        return utils.generate_response(request, {})

    def campaign_start(self, request, cid):
        models.Campaign.objects.filter(id=cid).update(start=True)
        return utils.generate_response(request, {})

    # def campaigns(self, request):
    #     if 'cookie' in request.COOKIES:
    #         uid = request.COOKIES['cookie']
    #         if utils.check_manager(uid):
    #             result = []
    #             campaigns = models.Campaign.objects.filter(managers__id=uid).all()
    #             for campaign in campaigns:
    #                 result.append(campaign.dict())
    #             return utils.generate_response(request, {'campaigns': result})
    #         else:
    #             return utils.generate_error(request, 'Not manager')
    #     else:
    #         return utils.generate_error(request, 'Not logged in')
    #
    # def availabilities(self, request):
    #     if 'cookie' in request.COOKIES:
    #         uid = request.COOKIES['cookie']
    #         if utils.check_manager(uid):
    #             result = []
    #             for user in models.User.objects.filter(canvasser=True).all():
    #                 dates = []
    #                 for ava in models.Availability.objects.filter(canvasser=user).all():
    #                     if ava.assignment is None:
    #                         dates.append(ava.dict())
    #                 result.append({'uid': user.dict(), 'availability': dates})
    #             return utils.generate_response(request, {'availabilities': result})
    #         else:
    #             return utils.generate_error(request, 'Not manager')
    #     else:
    #         return utils.generate_error(request, 'Not logged in')