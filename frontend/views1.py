from django.shortcuts import render, redirect
from . import utils
import json


def login(request):
    data = {}
    return render(request, 'login.html', data)


def account(request):
    return render(request, 'account1.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def campaigns(request):
    return render(request, 'campaigns1.html', {})


def campaign(request, cid):
    return render(request, 'campaign1.html', {})


def campaign_create(request):
    return render(request, 'campaign_create1.html', {})


def campaign_edit(request, cid):
    return render(request, 'campaign_edit1.html', {})


def campaign_assignments(request, cid):
    return render(request, 'assignments1.html', {})


def campaign_result(request, cid):
    return render(request, 'assignments1.html', {})


def campaign_assignment(request, cid, aid):
    return render(request, 'assignment1.html', {})


def campaign_result(request, cid):
    pass


def canvasser_assignments(request):
    return render(request, 'assignments1.html', {})


def canvasser_assignment(request, id):
    return render(request, 'assignment1.html', {})


def current_assignment(request):
    return render(request, 'assignment1.html', {})


def admin(request):
    return render(request, 'admin1.html', {'settings': [{'name': 'name1', 'value': 1}, {'name': 'name2', 'value': 2}],
                                          'tittle': 'admin'})
