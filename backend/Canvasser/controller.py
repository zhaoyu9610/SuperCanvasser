from backend import utils, models
import json


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
                for date in utils.get_dates(dates):
                    campaign_date = {'date': models.CampaignDate.objects.filter(date=date).get(), 'canvasser_id': uid}
                    models.Availability.objects.create(**campaign_date)
                return utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')
