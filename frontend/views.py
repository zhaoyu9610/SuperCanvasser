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
        data = {'role': roles}
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
            data = {'role': roles, 'campaigns': json.dump(utils.get_campaigns(uid))}
            return render(request, 'campaigns.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {'role': roles, 'campaign': utils.get_campaign(uid, cid)}
            return render(request, 'campaign.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_create(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'campaign_create.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_edit(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {'role': roles, 'campaign': utils.get_campaign(uid, cid)}
            return render(request, 'campaign_edit.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_assignments(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {'role': roles, 'assignments': utils.get_assignments(uid, cid)}
            return render(request, 'assignments.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_result(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {'role': roles, 'result': utils.get_result(uid, cid)}
            return render(request, 'assignments.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_assignment(request, cid, aid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.get_roles(uid)
        if roles[1]:
            data = {'role': roles, 'assignment': utils.get_assignment(uid, cid, aid)}
            return render(request, 'assignment.html', data)
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
            data = {'role': roles}
            return render(request, 'assignments.html', data)
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
            data = {'role': roles, 'users': utils.get_users(), 'settings': utils.get_settings()}
            return render(request, 'admin.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')