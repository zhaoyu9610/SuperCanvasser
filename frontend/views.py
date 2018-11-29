from django.shortcuts import render, redirect
from . import utils
import json
import datetime
from backend import models


def login(request):
    data = {}
    return render(request, 'login.html', data)


def account(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        data = {
            'role': roles,
            'user': utils.get_user(uid)
        }
        if roles[1]:
            data['availability'] = utils.get_availability(uid)
        return render(request, 'account.html', data)
    else:
        return redirect('login')


def campaigns(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {
                'role': roles,
                'campaigns': utils.get_campaigns(uid)
            }
            return render(request, 'campaigns.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are not manager'))
    else:
        return redirect('login')


def campaign(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            campaign = utils.get_campaign(uid, cid)
            data = {
                'role': roles,
                'campaign': campaign,
                'geo': utils.get_geo(campaign['locations']),
                'rules': utils.get_rules(cid)
            }
            print(data['campaign'])
            return render(request, 'campaign.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are note manager'))
    else:
        return redirect('login')


def campaign_create(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {
                'role': roles,
                'canvassers': utils.get_canvassers(),
                'managers': utils.get_managers()
            }
            return render(request, 'campaign_create.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are not manager'))
    else:
        return redirect('login')


def campaign_edit(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {
                'role': roles,
                'campaign': utils.get_campaign(uid, cid),
                'canvassers': utils.get_canvassers(),
                'managers': utils.get_managers()
            }
            return render(request, 'campaign_edit.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are not manager'))
    else:
        return redirect('login')


def campaign_assignments(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            assignments = utils.get_assignments(uid, cid)
            data = {
                'role': roles,
                'assignments': assignments
            }
            if len(assignments) == 0:
                return render(request, 'error.html', utils.generate_error_data(request, 'No assignments for current campaign, please generate assignment first'))
            return render(request, 'assignments.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are note manager'))
    else:
        return redirect('login')


def campaign_result(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {
                'role': roles,
                'campaign': utils.get_campaign(uid, cid),
                'result': json.loads(utils.get_result(cid)),
                'questions': json.loads(models.Campaign.objects.filter(id=cid).get().questions)
            }
            return render(request, 'result.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are not manager'))
    else:
        return redirect('login')


def campaign_assignment(request, cid, aid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            assignment = utils.get_assignment(uid, cid, aid)
            data = {
                'role': roles,
                'assignment': assignment,
                'geo': utils.get_geo(assignment['locations']),
                'questions': utils.get_questions(aid),
                'talking_points': utils.get_talking_points(aid),
                'canvass': False
            }
            return render(request, 'assignment.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are not manager'))
    else:
        return redirect('login')


def canvasser_assignments(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[2]:
            data = {'role': roles, 'assignments': utils.get_canvasser_assignments(uid)}
            return render(request, 'assignments.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are note canvasser'))
    else:
        return redirect('login')


def canvasser_assignment(request, aid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[2]:
            assignment = utils.canvasser_get_assignment(uid, aid)
            data = {
                'role': roles,
                'assignment': assignment,
                'geo': utils.get_geo(assignment['locations']),
                'questions': utils.get_questions(aid),
                'talking_points': utils.get_talking_points(aid),
                'canvass': False
            }
            return render(request, 'assignment.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are note canvasser'))
    else:
        return redirect('login')


def current_assignment(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[2]:
            assignment, questions = utils.canvasser_get_next(uid)
            if assignment:
                return render(request, 'assignment.html', {'role': roles,
                                                           'assignment': assignment.dict(),
                                                           'geo': utils.get_geo(assignment.dict()['locations']),
                                                           'questions': questions,
                                                           'talking_points': utils.get_talking_points(assignment.id),
                                                           'canvass': True})
            else:
                return render(request, 'error.html', utils.generate_error_data(request, 'No current assignment'))
        return render(request, 'error.html', utils.generate_error_data(request, 'You are note canvasser'))
    else:
        return redirect('login')


def canvass(request, aid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[2]:
            assignment = utils.canvasser_get_assignment(uid, aid)
            a = models.Assignment.objects.filter(id=aid).get()
            data = {
                'role': roles,
                'assignment': assignment,
                'geo': utils.get_geo(assignment['locations']),
                'questions': utils.get_questions(aid),
                'talking_points': utils.get_talking_points(aid),
                'canvass': False,
                'order': [a.name() for a in a.locations.all()]
            }
            return render(request, 'canvass.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are note canvasser'))
    else:
        return redirect('login')


def admin(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[0]:
            data = {
               'settings': utils.get_settings(),
                'users':utils.get_users(),
                'role': utils.get_roles(uid),
                'units': ['', '']
            }
            data['users'] = json.dumps(data['users'])
            data['settings'] = json.dumps(data['settings'])
            return render(request, 'admin.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, 'You are not admin'))
    else:
        return redirect('login')
