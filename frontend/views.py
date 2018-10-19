from django.shortcuts import render

# Create your views here.


def login(request):
    data = {}
    render(request, 'login.html', data)


def account(request):
    data = {}
    render(request, 'account.html', data)


def manager(request):
    data = {}
    render(request, 'manager.html', data)


def campaign(request):
    data = {}
    render(request, 'campaign.html', data)


def canvasser(request):
    data = {}
    render(request, 'canvasser.html', data)


def assignment(request):
    data = {}
    render(request, 'assignment.html', data)


def current(request):
    data = {}
    render(request, 'assignment.html', data)

