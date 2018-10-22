from django.shortcuts import render


# Create your views here.


def login(request):
    data = {}
    return render(request, 'login.html', data)


def account(request):
    data = {}
    return render(request, 'account.html', data)


def manager(request):
    data = {}
    return render(request, 'manager.html', data)


def campaign(request):
    data = {}
    return render(request, 'campaign.html', data)


def canvasser(request):
    data = {}
    return render(request, 'canvasser.html', data)


def assignment(request):
    data = {}
    return render(request, 'assignment.html', data)


def current(request):
    data = {}
    return render(request, 'assignment.html', data)

