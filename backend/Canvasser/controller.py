from backend import utils, models
import json
from datetime import date


class CanvasserHandler:
    def edit_availability(self, request):
        try:
            body = json.loads(request.body)
            dates = body['dates']
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_canvasser(uid):
                models.Availability.objects.filter(canvasser_id=uid).delete()
                for year, month, day in dates:
                    campaign_date = {'date': models.CampaignDate.objects.filter(date=date(year, month, day)).get(), 'canvasser_id': uid}
                    models.Availability.objects.create(**campaign_date)
                return utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')

    def availability(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_canvasser(uid) or utils.check_admin(uid):
                dates = []
                for ava in models.Availability.objects.filter(canvasser_id=uid).all():
                    dates.append(ava.dict())
                return utils.generate_response(request, {'availability': dates})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')
