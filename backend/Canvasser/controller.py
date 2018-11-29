from backend import geoutils
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

    def submit(self, request):
        try:
            print(request.body)
            body = json.loads(request.body)
            id = body['id']
            results = body['results']
            print(id)
            print(results)
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_canvasser(uid):
                assignment = models.Assignment.objects.filter(id=id).get()
                assignment.finished = True
                assignment.save()
                for r in results:
                    models.LocationResult.objects.create(
                        **{'number_of_people': len(r['answer']),
                           'rating': r['rating'],
                           'answers': r['answer'],
                           'notes': r['notes'],
                           'result': utils.get_result(r['answer'], r['rating'], int(r['id']), r['notes']),
                           'assignment_id': assignment.id,
                           'location_id': int(r['id']),
                           'campaign_id': assignment.campaign_id})
                    utils.check_assignment(assignment)
                return utils.generate_response(request, {})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')

    def new_order(self, request):
        try:
            body = json.loads(request.body)
            current = body['current']
            others = body['others']
        except Exception as e:
            return utils.generate_error(request, 'Parameter error')
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_canvasser(uid):
                return utils.generate_response(request, {'order': geoutils.alternative_assignment(current, others)})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')
