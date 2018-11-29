from geopy.geocoders import Nominatim
from . import models
import random
import numpy as np
import datetime
from geopy.distance import geodesic


geolocator = Nominatim(user_agent="SuperCanvasser404")

import requests

key = "AIzaSyCWyA_zlCq4-liVwQBMIuWUWcid5H4vmfs"
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"


def generate_log_lat(location):
    search_payload = {"key": key, "query": location['street'] + ' '+ location['state'] + ' ' + location['zipcode']}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()  # json representation of the data
    loc = search_json["results"][0]["geometry"]["location"]
    return loc['lng'], loc['lat']


def alternative_assignment(current, locations):
    print(current, locations)
    current = models.Location.objects.filter(id=current).get().dict()
    locations = [models.Location.objects.filter(id=a).get().dict() for a in locations]
    ordered_location = []
    while locations:
        next_location, _ = select_next_location(locations, current)
        ordered_location.append(next_location['name'])
        locations.remove(next_location)
    return ordered_location


def date_format(date):
    return datetime.date(date[0], date[1], date[2])


def generate_assignment(campaign_id):
    campaign = models.Campaign.objects.filter(id=campaign_id).get().dict()
    models.Assignment.objects.filter(campaign_id=campaign['id']).delete()
    campaign_id = campaign['id']
    locations = campaign['locations']
    max_hour = models.Parameter.objects.filter(name='hours').get().value
    average_speed = models.Parameter.objects.filter(name='speed').get().value
    duration = campaign['duration']
    canvassers = campaign['canvassers']
    start_date = campaign['start_date']
    end_date = campaign['end_date']
    assignment_list = []
    secure_random = random.SystemRandom()
    start_date_new = date_format(start_date)
    end_date_new = date_format(end_date)
    duration_list = []
    while locations:
        start_location = secure_random.choice(locations)
        total_time = duration
        current_assignment = [start_location]
        current_location = start_location
        locations.remove(current_location)
        while total_time < max_hour and locations:
            next_location, distance = select_next_location(locations, current_location)
            temp = total_time + distance / average_speed + duration
            if temp <= max_hour:
                total_time = total_time + distance / average_speed + duration
                current_assignment.append(next_location)
                current_location = next_location
                locations.remove(next_location)
            else:
                break
        assignment_list.append(current_assignment)
        duration_list.append(total_time)
    assign_to_canvasser(assignment_list, canvassers, start_date_new, end_date_new, duration_list, campaign_id)


def assign_to_canvasser(assignment_list, canvassers, start_date, end_date, duration_list, campaign_id):
    av = find_earliest(canvassers, start_date, end_date)
    for index, assignment in enumerate(assignment_list):
        a = av[index]
        canvasser, date = a.canvasser, a.date.date
        location_id = []
        for location in assignment:
            location_id.append(location['id'])
        duration = duration_list[index]
        assignment = models.Assignment.objects.create(duration=duration, campaign_id=campaign_id, canvasser=canvasser,
                                                      date=models.CampaignDate.objects.filter(date=date).get())
        assignment.locations.set(location_id)
        assignment.save()
        a.assignment = assignment
        a.save()


def find_earliest(canvassers, start_date, end_date):
    canvasser_id_list = []
    for canvasser in canvassers:
        canvasser_id_list.append(canvasser['id'])
    available_canvassers = models.Availability.objects.filter(canvasser_id__in=canvasser_id_list, assignment=None).order_by('date').all()
    available_canvassers = [a for a in available_canvassers if end_date >= a.date.date >= start_date]
    available_canvassers = [a for a in available_canvassers if a.assignment is None]
    return available_canvassers

    # for date in list(available_canvassers):
    #     if date.date.date > start_date and date.date.date < end_date:
    #         return date.canvasser, date.date.date
    # raise Exception('No Canvasser Available')


def select_next_location(locations, start_location):
    distance_list = []
    for location in locations:
        distance_list.append(calculate_distance(start_location, location))
    index = find_minimum(distance_list)
    return [locations[index], distance_list[index]]


def calculate_distance(start_location, location):
    inter_location = find_inter_location(start_location,location)
    d1 = calculate_distance_helper(start_location, inter_location)
    d2 = calculate_distance_helper(location, inter_location)
    return d1+d2


def find_inter_location(start_location, location):
    return {'longitude': start_location['longitude'], 'latitude': location['latitude']}
    # return geolocator.reverse(str(start_location['longitude']) + "," +str(location['latitude']))


def calculate_distance_helper(start_location, location):
    l1 = (start_location['latitude'], start_location['longitude'])
    l2 = (location['latitude'], location['longitude'])
    return geodesic(l1, l2).km
    # long1 = np.radians(start_location['longitude'])
    # lati1 = np.radians(start_location['latitude'])
    # long2 = np.radians(location.longitude)
    # lati2 = np.radians(location.latitude)
    # dlon = ((long2 - long1) * math.pi / 180.0)
    # dlat = lati2 - lati1
    # radius = 6378.137
    # sa = np.sin(dlat / 2)
    # sb = np.sin(dlon / 2)
    # a = sa**2 + np.cos(lati1) * np.cos(lati2) * sb**2
    # c = 2 * np.arcsin(np.sqrt(a))
    # return 2 * c * radius


def find_minimum(distance_list):
    # if len(distance_list)>1:
    #     index = len(distance_list)
    #     min = distance_list.pop()
    #     for distance in distance_list:
    #         if distance < min:
    #             min = distance
    #             index = distance_list.index(distance)
    #     return index
    # else:
    #     return 0
    min_distence = min(distance_list)
    return distance_list.index(min_distence)
