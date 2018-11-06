from django.shortcuts import render, redirect
from . import utils
import json


def login(request):
    data = {}
    return render(request, 'login.html', data)


def account(request):
    return render(request, 'account1.html', {
        'role': [True, True, True],
        'availability': [{'id': 1, 'date': {'id': 1, 'date': [2018, 10, 1]}, 'assignment': {}}, {'id': 2, 'date': {'id': 3, 'date': [2018, 10, 3]}, 'assignment': {}}, {'id': 3, 'date': {'id': 5, 'date': [2018, 10, 5]}, 'assignment': {}}, {'id': 4, 'date': {'id': 7, 'date': [2018, 10, 7]}, 'assignment': {}}, {'id': 5, 'date': {'id': 10, 'date': [2018, 10, 10]}, 'assignment': {}}, {'id': 6, 'date': {'id': 13, 'date': [2018, 10, 13]}, 'assignment': {}}, {'id': 7, 'date': {'id': 15, 'date': [2018, 10, 15]}, 'assignment': {}}, {'id': 8, 'date': {'id': 17, 'date': [2018, 10, 17]}, 'assignment': {}}, {'id': 9, 'date': {'id': 20, 'date': [2018, 10, 20]}, 'assignment': {}}],
        'user':{'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}
    })


def signup(request):
    return render(request, 'signup.html', {})


def campaigns(request):
    return render(request, 'campaigns1.html', {
        'role': [True, True, True],
        'campaigns': [{'id': 1, 'name': 'Campaign Name', 'talking_points': [], 'start': False, 'finish': False, 'median': None, 'duration': 0.5, 'average': None, 'sd': None, 'questions': [], 'manager': [{'id': 2, 'email': 'manager@manager.com', 'password': 'manager', 'admin': False, 'canvasser': False, 'manager': True, 'phone': '0000000000', 'gender': True, 'address': ''}], 'canvassers': [{'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}], 'locations': [{'id': 1, 'street': '5 Saywood Lane', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': None, 'latitude': None}, {'id': 2, 'street': 'Avalon Pines Drive', 'state': 'NY', 'city': 'Coram', 'zipcode': '', 'longitude': None, 'latitude': None}, {'id': 3, 'street': '5 Seabrook Court', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': None, 'latitude': None}], 'start_date': [2018, 11, 4], 'end_date': [2018, 12, 31]}]
    })


def campaign(request, cid):
    return render(request, 'campaign1.html', {
        'role': [True, True, True],
        'campaign':{'id': 1, 'name': 'Campaign Name', 'talking_points': [], 'start': False, 'finish': False, 'median': None, 'duration': 0.5, 'average': None, 'sd': None, 'questions': [], 'manager': [{'id': 2, 'email': 'manager@manager.com', 'password': 'manager', 'admin': False, 'canvasser': False, 'manager': True, 'phone': '0000000000', 'gender': True, 'address': ''}], 'canvassers': [{'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}], 'locations': [{'id': 1, 'street': '5 Saywood Lane', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': None, 'latitude': None}, {'id': 2, 'street': 'Avalon Pines Drive', 'state': 'NY', 'city': 'Coram', 'zipcode': '', 'longitude': None, 'latitude': None}, {'id': 3, 'street': '5 Seabrook Court', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': None, 'latitude': None}], 'start_date': [2018, 11, 4], 'end_date': [2018, 12, 31]}
    })


def campaign_create(request):
    return render(request, 'campaign_create1.html', {
        'role': [True, True, True],
    })


def campaign_edit(request, cid):
    return render(request, 'campaign_edit1.html', {
        'role': [True, True, True],
        'campaign':{'id': 1, 'name': 'Campaign Name', 'talking_points': [], 'start': False, 'finish': False, 'median': None, 'duration': 0.5, 'average': None, 'sd': None, 'questions': [], 'manager': [{'id': 2, 'email': 'manager@manager.com', 'password': 'manager', 'admin': False, 'canvasser': False, 'manager': True, 'phone': '0000000000', 'gender': True, 'address': ''}], 'canvassers': [{'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}], 'locations': [{'id': 1, 'street': '5 Saywood Lane', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': None, 'latitude': None}, {'id': 2, 'street': 'Avalon Pines Drive', 'state': 'NY', 'city': 'Coram', 'zipcode': '', 'longitude': None, 'latitude': None}, {'id': 3, 'street': '5 Seabrook Court', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': None, 'latitude': None}], 'start_date': [2018, 11, 4], 'end_date': [2018, 12, 31]}
    })


def campaign_assignments(request, cid):
    return render(request, 'assignments1.html', {
        'role': [True, True, True],
        'assignments' : [{'id': 2, 'duration': 0.5, 'campaign': {'id': 1, 'name': 'Campaign Name', 'talking_points': [], 'start': False, 'finish': False, 'median': None, 'duration': 0.5, 'average': None, 'sd': None, 'questions': [], 'manager': [{'id': 2, 'email': 'manager@manager.com', 'password': 'manager', 'admin': False, 'canvasser': False, 'manager': True, 'phone': '0000000000', 'gender': True, 'address': ''}], 'canvassers': [{'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}], 'locations': [{'id': 1, 'street': '5 Saywood Lane', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': -73.102585748451, 'latitude': 40.89601815}, {'id': 2, 'street': 'Avalon Pines Drive', 'state': 'NY', 'city': 'Coram', 'zipcode': '', 'longitude': -73.0056325, 'latitude': 40.8840484}, {'id': 3, 'street': '5 Seabrook Court', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': -73.1061719368158, 'latitude': 40.90147985}], 'start_date': [2018, 1, 1], 'end_date': [2018, 12, 31]}, 'canvassers': {'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}, 'date': {'id': 1, 'date': [2018, 10, 1]}, 'locations': [{'id': 2, 'street': 'Avalon Pines Drive', 'state': 'NY', 'city': 'Coram', 'zipcode': '', 'longitude': -73.0056325, 'latitude': 40.8840484}]}
,{'id': 2, 'duration': 0.5, 'campaign': {'id': 1, 'name': 'Campaign Name', 'talking_points': [], 'start': False, 'finish': False, 'median': None, 'duration': 0.5, 'average': None, 'sd': None, 'questions': [], 'manager': [{'id': 2, 'email': 'manager@manager.com', 'password': 'manager', 'admin': False, 'canvasser': False, 'manager': True, 'phone': '0000000000', 'gender': True, 'address': ''}], 'canvassers': [{'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}], 'locations': [{'id': 1, 'street': '5 Saywood Lane', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': -73.102585748451, 'latitude': 40.89601815}, {'id': 2, 'street': 'Avalon Pines Drive', 'state': 'NY', 'city': 'Coram', 'zipcode': '', 'longitude': -73.0056325, 'latitude': 40.8840484}, {'id': 3, 'street': '5 Seabrook Court', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': -73.1061719368158, 'latitude': 40.90147985}], 'start_date': [2018, 1, 1], 'end_date': [2018, 12, 31]}, 'canvassers': {'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}, 'date': {'id': 1, 'date': [2018, 10, 1]}, 'locations': [{'id': 2, 'street': 'Avalon Pines Drive', 'state': 'NY', 'city': 'Coram', 'zipcode': '', 'longitude': -73.0056325, 'latitude': 40.8840484}]}
]
    })


def campaign_result(request, cid):
    return render(request, 'assignments1.html', {
        'role': [True, True, True],
    })


def campaign_assignment(request, cid, aid):
    return render(request, 'assignment1.html', {
        'role': [True, True, True],
        'assignment': {'id': 2, 'duration': 0.5, 'campaign': {'id': 1, 'name': 'Campaign Name', 'talking_points': [], 'start': False, 'finish': False, 'median': None, 'duration': 0.5, 'average': None, 'sd': None, 'questions': [], 'manager': [{'id': 2, 'email': 'manager@manager.com', 'password': 'manager', 'admin': False, 'canvasser': False, 'manager': True, 'phone': '0000000000', 'gender': True, 'address': ''}], 'canvassers': [{'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}], 'locations': [{'id': 1, 'street': '5 Saywood Lane', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': -73.102585748451, 'latitude': 40.89601815}, {'id': 2, 'street': 'Avalon Pines Drive', 'state': 'NY', 'city': 'Coram', 'zipcode': '', 'longitude': -73.0056325, 'latitude': 40.8840484}, {'id': 3, 'street': '5 Seabrook Court', 'state': 'NY', 'city': 'Stony Brook', 'zipcode': '', 'longitude': -73.1061719368158, 'latitude': 40.90147985}], 'start_date': [2018, 1, 1], 'end_date': [2018, 12, 31]}, 'canvassers': {'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}, 'date': {'id': 1, 'date': [2018, 10, 1]}, 'locations': [{'id': 2, 'street': 'Avalon Pines Drive', 'state': 'NY', 'city': 'Coram', 'zipcode': '', 'longitude': -73.0056325, 'latitude': 40.8840484}]}

    })


def campaign_result(request, cid):
    pass


def canvasser_assignments(request):
    return render(request, 'assignments1.html', {
        'role': [True, True, True]
    })


def canvasser_assignment(request, id):
    return render(request, 'assignment1.html', {
        'role': [True, True, True],
    })


def current_assignment(request):
    return render(request, 'assignment1.html', {
        'role': [True, True, True],
    })


def admin(request):
    return render(request, 'admin1.html', {
        'settings': [{'id': 1, 'value': 8.0, 'name': 'hours'}, {'id': 2, 'value': 60.0, 'name': 'speed'}],
        'users':[{'id': 1, 'email': 'admin@admin.com', 'password': 'admin', 'admin': True, 'canvasser': False, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}, {'id': 2, 'email': 'manager@manager.com', 'password': 'manager', 'admin': False, 'canvasser': False, 'manager': True, 'phone': '0000000000', 'gender': True, 'address': ''}, {'id': 3, 'email': 'canvasser@canvasser.com', 'password': 'canvasser', 'admin': False, 'canvasser': True, 'manager': False, 'phone': '0000000000', 'gender': True, 'address': ''}],
        'role': [True, True, True]
    })
