from backend import models
import datetime
import json


def generate_error_data(request, msg):
    return {'msg': msg,
            'url': request.build_absolute_uri()}


def get_roles(uid):
    user = models.User.objects.filter(id=uid).get()
    return [user.admin, user.manager, user.canvasser]


def get_availability(uid):
    dates = []
    for ava in models.Availability.objects.filter(canvasser_id=uid).all():
        dates.append(ava.dict())
    return dates


def get_campaigns(uid):
    result = []
    campaigns = models.Campaign.objects.filter(managers__id=uid).all()
    for campaign in campaigns:
        result.append(campaign.dict())
    return result


def get_campaign(uid, cid):
    campaign = models.Campaign.objects.filter(id=cid, managers__id=uid).get()
    return campaign.dict()


def get_assignments(uid, cid):
    result = []
    assignments = models.Assignment.objects.filter(campaign_id=cid).all()
    for assignment in assignments:
        result.append(assignment.dict())
    return result


def get_result(uid, cid):
    pass


def get_assignment(uid, cid, aid):
    assignment = models.Assignment.objects.filter(id=aid, campaign_id=cid).get()
    return assignment.dict()


def canvasser_get_assignment(uid, aid):
    assignment = models.Assignment.objects.filter(canvasser_id=uid, id=aid).get()
    return assignment.dict()


def canvasser_get_next(uid):
    result = []
    for a in models.Assignment.objects.filter(canvasser_id=uid).all():
        if a.date.date >= datetime.date.today():
            result.append(a)
    return find_closet(result)


def find_closet(result):
    if not result:
        return None, None
    for a in result:
        if is_smallest(a, result):
            print("current assignment found")
            return a, a.campaign.questions


def is_smallest(a, result):
    for b in result:
        if a.date.date > b.date.date:
            return False
    return True


def get_users():
    result = []
    users = models.User.objects.all()
    for user in users:
        result.append(user.dict())
    return result


def get_settings():
    result = []
    parameters = models.Parameter.objects.all()
    for parameter in parameters:
        result.append(parameter.dict())
    return result


def get_canvassers():
    result = []
    canvassers = models.User.objects.filter(canvasser=True).all()
    for canvasser in canvassers:
        result.append(canvasser.dict())
    return result


def get_managers():
    result = []
    managers = models.User.objects.filter(manager=True).all()
    for manager in managers:
        result.append(manager.dict())
    return result


def get_user(uid):
    return models.User.objects.filter(id=uid).get().dict()


def get_geo(locations):
    result = []
    for location in locations:
        result.append([location['latitude'], location['longitude']])
    return result


def get_canvasser_assignments(uid):
    result = []
    for assignment in models.Assignment.objects.filter(canvasser_id=uid).all():
        result.append(assignment.dict())
    return result


def get_questions(aid):
    return json.dumps(models.Assignment.objects.filter(id=aid).get().campaign.questions)


def get_talking_points(aid):
    return json.dumps(models.Assignment.objects.filter(id=aid).get().campaign.talking_points)


def get_result(cid):
    return models.CampaignResult.objects.filter(id=cid).get().result
