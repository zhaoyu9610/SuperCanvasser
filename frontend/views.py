from django.shortcuts import render, redirect
from . import utils


def login(request):
    data = {}
    return render(request, 'login.html', data)


def account(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        data = {'role': utils.getRoles(uid)}
        return render(request, 'account.html', data)
    else:
        return redirect('login')


def admin(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.getRoles(uid)
        if roles[0]:
            data = {'role': roles}
            return render(request, 'admin.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaigns(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.getRoles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'campaigns.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.getRoles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'campaign.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_edit(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.getRoles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'campaign_edit.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_assignments(request, cid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.getRoles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'assignments.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_assignment(request, cid, aid):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.getRoles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'assignment.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def campaign_create(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.getRoles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'campaign_create.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def canvasser_assignments(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.getRoles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'assignments.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def canvasser_assignment(request, id):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.getRoles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'assignment.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')


def current_assignment(request):
    if 'cookie' in request.COOKIES:
        uid = request.COOKIES['cookie']
        roles = utils.getRoles(uid)
        if roles[1]:
            data = {'role': roles}
            return render(request, 'assignment.html', data)
        return render(request, 'error.html', utils.generate_error_data(request, ''))
    else:
        return redirect('login')
