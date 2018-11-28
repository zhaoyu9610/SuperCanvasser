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

    def sibmit(self, request):
        try:
            body = json.loads(request.body)
            data = body['data']
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_canvasser(uid):
                assignment = models.Assignment.objects.filter(id=data['id']).get()
                for key, value in data['result'].items():
                    models.LocationResult.objects.create(
                        **{'number_of_people': len(value['answer']),
                           'rating': value['rating'],
                           'answers': value['answer'],
                           'notes': value['notes'],
                           'result': utils.get_result(value['answer'], value['rating'], key),
                           'assignment_id': assignment.id,
                           'location_id': key})
                    utils.check_assignment(assignment)
                return utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')
