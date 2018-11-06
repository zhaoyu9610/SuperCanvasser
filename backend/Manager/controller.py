from backend import utils, models, geoutils
import json
import datetime


class ManagerHandler:
    def campaigns(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_manager(uid):
                result = []
                campaigns = models.Campaign.objects.filter(managers__id=uid).all()
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
                campaign = models.Campaign.objects.filter(id=id, managers__id=uid)
                if 'managers' in campaign_dict:
                    managers = campaign_dict.pop('managers', [])
                    managers.apped(uid)
                    campaign.managers.set(managers)
                if 'canvassers' in campaign_dict:
                    canvassers = campaign_dict.pop('canvassers', [])
                    campaign.canvassers.set(canvassers)
                if 'locations' in campaign_dict:
                    locations = campaign_dict.pop('locations', [])
                    location_id = []
                    for l in locations:
                        loc = models.Location.objects.create(**l)
                        location_id.append(loc.id)
                    campaign.locations.set(location_id)
                if 'end_date' in campaign_dict:
                    d = campaign_dict['end_date']
                    campaign_dict['end_date'] = datetime.date(d[0], d[1], d[2])
                if 'start_date' in campaign_dict:
                    d = campaign_dict['start_date']
                    campaign_dict['start_date'] = datetime.date(d[0], d[1], d[2])
                campaign.update(**campaign_dict)
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
                locations = campaign_dict.pop('locations', [])
                managers = campaign_dict.pop('managers', [])
                canvassers = campaign_dict.pop('canvassers', [])
                campaign = models.Campaign.objects.create(**campaign_dict)
                managers.append(uid)
                campaign.managers.set(managers)
                campaign.canvassers.set(canvassers)
                location_id = []
                for l in locations:
                    loc = models.Location.objects.create(**l)
                    location_id.append(loc.id)
                campaign.locations.set(location_id)
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

    def generate_assignments(self, request, cid):
        try:
            geoutils.generate_assignment(cid)
            return utils.generate_response(request, {})
        except Exception as e:
            return utils.generate_error(request, '')

    def campaign_start(self, request, cid):
        models.Campaign.objects.filter(id=cid).update(start=True)
        return utils.generate_response(request, {})
