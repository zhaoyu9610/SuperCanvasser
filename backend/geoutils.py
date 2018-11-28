from geopy.geocoders import Nominatim
from . import models
import random
import numpy as np
import datetime
import requests

geolocator = Nominatim(user_agent="SuperCanvasser404")

key = "AIzaSyCWyA_zlCq4-liVwQBMIuWUWcid5H4vmfs"
search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"

def generate_log_lat(location):
    # address = location['street'] + ' '+ location['state'] + ' ' + location['zipcode']
    # print(address)
    # geolocation = geolocator.geocode(address)
    # return geolocation.longitude, geolocation.latitude
    search_payload = {"key": key, "query": location['street'] + ' '+ location['state'] + ' ' + location['zipcode']}
    search_req = requests.get(search_url, params=search_payload)
    search_json = search_req.json()  # json representation of the data
    loc = search_json["results"][0]["geometry"]["location"]
    return loc['lng'], loc['lat']


def date_format(date):
    return datetime.date(date[0], date[1], date[2])


def generate_assignment(campaign_id):
    campaign = models.Campaign.objects.filter(id=campaign_id).get().dict()

    models.Assignment.objects.filter(campaign_id=campaign_id).delete()

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
    while locations:
        start_location = secure_random.choice(locations)
        total_time = duration
        current_assignment = []
        current_location = start_location

        next_location, distance = select_next_location(locations, current_location)
        print('len of current assign')
        print(len(current_assignment))
        total_time = total_time + distance / average_speed + duration
        current_location = next_location
        current_assignment.append(next_location)
        locations.remove(next_location)

        while total_time < max_hour and len(locations)>1:
            next_location, distance = select_next_location(locations, current_location)
            total_time = total_time + distance / average_speed + duration
            current_assignment.append(next_location)
            print('len of current assign')
            print(len(current_assignment))
            locations.remove(next_location)
            print('len of remaining locations')
            print(len(locations))
        assignment_list.append(current_assignment)
    assign_to_canvasser(assignment_list, canvassers, start_date_new, end_date_new, duration, campaign_id)


def assign_to_canvasser(assignment_list, canvassers, start_date, end_date, duration, campaign_id):
    print('number of assignment list')
    print(assignment_list)
    print(start_date, end_date)
    for assignment in assignment_list:
        avail, canvasser, date = find_earliest(canvassers, start_date, end_date)
        location_id = []
        for location in assignment:
            location_id.append(location['id'])
        assignment = models.Assignment.objects.create(duration=duration, campaign_id=campaign_id, canvasser=canvasser,
                                                      date=models.CampaignDate.objects.filter(date=date).get())
        assignment.locations.set(location_id)
        assignment.save()
        avail.assignment = assignment
        avail.save()


def find_earliest(canvassers, start_date, end_date):
    canvasser_id_list = []
    for canvasser in canvassers:
        canvasser_id_list.append(canvasser['id'])
    available_canvassers = models.Availability.objects.filter(canvasser_id__in=canvasser_id_list, assignment=None).order_by('date').all()
    print('len of available canvasser', len(available_canvassers))
    for date in list(available_canvassers):
        print(start_date, end_date, date.date.date)
        if date.date.date >= start_date and date.date.date <= end_date:
            return date, date.canvasser, date.date.date
    print("No time find for the case")
    raise Exception('No Canvasser Available')


def select_next_location(locations, start_location):
    distance_list = []
    for location in locations:
        distance_list.append(calculate_distance(start_location, location))
    print('distance list')
    print(distance_list)
    index = find_minimum(distance_list)
    return [locations[index], distance_list[index]]


def calculate_distance(start_location, location):
    inter_location = find_inter_location(start_location,location)
    return calculate_distance_helper(start_location, inter_location) + calculate_distance_helper(location, inter_location)


def find_inter_location(start_location, location):
    return geolocator.reverse(str(start_location['longitude']) + "," +str(location['latitude']))


def calculate_distance_helper(start_location, location):
    long1 = np.radians(start_location['longitude'])
    lati1 = np.radians(start_location['latitude'])
    long2 = np.radians(location.longitude)
    lati2 = np.radians(location.latitude)
    dlon = long2 - long1
    dlat = lati2 - lati1
    a = np.sin(dlat / 2) ** 2 + np.cos(lati1) * np.cos(lati2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 3956
    return c * r /1000


def find_minimum(distance_list):
    if len(distance_list)>1:
        index = len(distance_list)
        min = distance_list.pop()
        for distance in distance_list:
            if distance < min:
                min = distance
                index = distance_list.index(distance)
        return index
    else:
        return 0
