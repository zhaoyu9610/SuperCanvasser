import json
from django.http import HttpResponse
from . import models
import logging
import datetime
import numpy as np

logger = logging.getLogger('django')


def generate_error(request, error):
    result = {'status': 'error',
              'error': error,
              'method': request.method,
              'url': request.build_absolute_uri()}
    if request.method is 'POST':
        result['body'] = json.loads(request.body)
    result = json.dumps(result)
    logger.debug(result)
    return HttpResponse(result, content_type='application/json')


def generate_response(request, dict):
    dict['status'] = 'ok'
    dict['method'] = request.method
    dict['url'] = request.build_absolute_uri()
    if request.method == 'POST':
        dict['body'] = json.loads(request.body)
    result = json.dumps(dict)
    logger.debug(result)
    return HttpResponse(result, content_type='application/json')


def check_admin(uid):
    user = models.User.objects.get(id=uid)
    return user.admin


def check_manager(uid):
    user = models.User.objects.get(id=uid)
    return user.manager


def check_canvasser(uid):
    user = models.User.objects.get(id=uid)
    return user.canvasser


def get_user(users):
    result = []
    for u in users:
        result.append(models.User.objects.filter(email=u).get().id)
    return result


def add_locations(locations):
    result = []
    for l in locations:
        number, street, unit, city, state, zipcode = l.split(',')
        location, _ = models.Location.objects.update_or_create(
            number=number.strip(),
            street=street.strip(),
            unit=unit.strip(),
            city=city.strip(),
            state=state.strip(),
            zipcode=zipcode.strip()
        )
        result.append(location.id)
    return result


def get_dates(dates):
    result = []
    for start, end in dates:
        d1 = datetime.date(start[0], start[1], start[2])
        d2 = datetime.date(end[0], end[1], end[2])
        delta = d2 - d1
        for i in range(delta.days + 1):
            result.append(d1 + datetime.timedelta(i))
    return result

flatten = lambda l: [item for sublist in l for item in sublist]

same = lambda a, v:  int(a is v)

def get_result(answer, rating, location, note):
    result = [[[same(c, True) for c in a], [same(c, False) for c in a], [same(c, None) for c in a]] for a in answer]
    n = np.array(result)
    question_total = n.sum(axis=0).tolist()
    number = len(answer)
    rt = json.dumps({'total': number,
                       'question_sum': question_total,
                       'rating': rating,
                       'location': location,
                     'note': note})
    print(rt)
    return rt


def check_assignment(assignment):
    if len(models.LocationResult.objects.filter(campaign_id=assignment.campaign_id).all()) == len(models.Campaign.objects.filter(id=assignment.campaign_id).get().locations.all()):
        results = []
        location_result_id = []
        for location_result in models.LocationResult.objects.filter(campaign_id=assignment.campaign_id).all():
            results.append(json.loads(location_result.result))
            location_result_id.append(location_result.id)
        result = generate_campaign_result(assignment.campaign, results)
        r, _ = models.CampaignResult.objects.update_or_create(
            **{'campaign_id': assignment.campaign_id,
               'result': json.dumps(result)})
        r.location_result.set(location_result_id)


def generate_campaign_result(campaign, results):
    locations = [a['location'] for a in results]
    locations = [models.Location.objects.filter(id=a).get().name() for a in locations]
    notes = [a['note'] for a in results]
    number_of_people = [a['total'] for a in results]
    total_people = sum(number_of_people)
    location_question_sum = [a['question_sum'] for a in results]
    total_question_sum = np.array(location_question_sum).sum(axis=0).tolist()
    location_rating = [int(a['rating']) for a in results]
    location_result = list(zip(locations, number_of_people, location_rating, notes, [list(zip(*a)) for a in location_question_sum]))
    np_rating = np.array(location_rating)
    result = {'rating_avg': np_rating.mean(),
                'rating_sd': np_rating.std(),
                'rating_median': np.median(np_rating),
                'locations': location_result,
                'total_number_of_people': total_people,
              'total_question_sum': list(zip(*total_question_sum))}
    campaign.average = result['rating_avg']
    campaign.sd = result['rating_sd']
    campaign.median = result['rating_median']
    campaign.finish = True
    campaign.save()
    return result
