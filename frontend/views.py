from django.shortcuts import render, redirect
from backend.utils import generate_error
from . import utils
import json


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


def signup(request):
    return render(request, 'signup.html', {})


def campaigns(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {
                'role': roles,
                'campaigns': json.dumps(utils.get_campaigns(uid))
            }
            return render(request, 'campaigns.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
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
                'campaign': json.dumps(campaign),
                'geo': utils.get_geo(campaign['locations'])
            }
            print(data['geo'])
            return render(request, 'campaign.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_create(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {
                'role': roles,
                'canvassers': json.dumps(utils.get_canvassers()),
                'managers': json.dumps(utils.get_managers())
            }
            return render(request, 'campaign_create.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_edit(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {
                'role': roles,
                'campaign': json.dumps(utils.get_campaign(uid, cid)),
                'canvassers': json.dumps(utils.get_canvassers()),
                'managers': json.dumps(utils.get_managers())
            }
            return render(request, 'campaign_edit.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_assignments(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {
                'role': roles,
                'assignments': utils.get_assignments(uid, cid)
            }
            return render(request, 'assignments1.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_result(request, cid):
    print(request.COOKIES)
    print(utils.get_roles(cid))
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {
                'role': roles,
                'result': json.dumps(utils.get_result(uid, cid)),
                'campaign': utils.get_campaign(uid, cid)
            }
            return render(request, 'result1.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
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
                'geo': utils.get_geo(assignment['locations'])
            }
            return render(request, 'assignment1.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_result(request, cid):
    pass


def canvasser_assignments(request):
    if 'cookie' in request.COOKIES:
        print("asdfasdfasdf")
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        print("asdfasdfasdfasdf")
        print(roles)
        if roles[2]:
            data = {'role': roles, 'assignments': utils.get_canvasser_assignments(uid)}
            print(data)
            return render(request, 'assignments1.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
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
                'geo': utils.get_geo(assignment['locations'])
            }
            print(data)
            return render(request, 'assignment1.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def current_assignment(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[2]:
            assignment = utils.canvasser_get_next(uid)
            if assignment:
                return render(request, 'assignment1.html', {'role': roles, 'assignment': assignment, 'geo': utils.get_geo(assignment['locations'])})
            else:
                return generate_error(request, "No current assignment")
        return render(request, 'error.html', utils.generate_error_data(request, ''))
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
                'role': utils.get_roles(uid)
            }
            data['users'] = json.dumps(data['users'])
            data['settings'] = json.dumps(data['settings'])
            return render(request, 'admin.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')
