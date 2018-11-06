from django.shortcuts import render, redirect
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
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {
                'role': roles,
                'result': json.dumps(utils.get_result(uid, cid))
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
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {'role': roles, 'assignments': utils.get_canvasser_assignments(uid)}
            return render(request, 'assignments1.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def canvasser_assignment(request, id):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'assignment.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def current_assignment(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'assignment.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def admin(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[0]:
            # data = {'role': roles, 'users': json.dumps(utils.get_users()), 'settings': json.dumps(utils.get_settings())}
            data = {
        'settings': [{'id': 1, 'value': 8.0, 'name': 'hours'}, {'id': 2, 'value': 60.0, 'name': 'speed'}],
        'users':[{'id': 1, 'email': 'admin@admin.com', 'password': 'admin', 'admin': True, 'canvasser': False, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}, {'id': 2, 'email': 'manager@manager.com', 'password': 'manager', 'admin': False, 'canvasser': False, 'manager': True, 'phone': '0000000000', 'gender': True, 'address': ''}, {'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}],
        'role': [True, True, True]
    }
            data['users'] = json.dumps(data['users'])
            data['settings'] = json.dumps(data['settings'])
            return render(request, 'admin.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')
