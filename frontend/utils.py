from backend import models


def generate_error_data(request, msg):
    return {}


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
    campaigns = models.Campaign.objects.filter(manager_id=uid).all()
    for campaign in campaigns:
        result.append(campaign.dict())
    return result


def get_campaign(uid, cid):
    campaign = models.Campaign.objects.filter(id=cid, manager_id=uid).get()
    return campaign.dict()


def get_assignments(uid, cid):
    result = []
    assignments = models.Assignment.objects.filter(campaign_id=cid).all()
    for assignment in assignments:
        result.append(assignment.dict())
    return result


def get_assignment(uid, cid, aid):
    assignment = models.Assignment.objects.filter(id=cid, campaign_id=cid).get()
    return assignment.dict()


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

