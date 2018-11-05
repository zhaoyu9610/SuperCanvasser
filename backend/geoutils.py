from geopy.geocoders import Nominatim
from . import models
import random
import numpy as np
import pandas as pd

geolocator = Nominatim(user_agent="SuperCanvasser404")


def generate_log_lat(location):
    address = location['street'] +' '+ location['city'] +' '+ location['state'] +' '+ location['zipcode']
    geolocation = geolocator.geocode(address)
    return geolocation.longitude, geolocation.latitude


def date_format(date):
    a = str(date[0]) + str(date[1]) + str(date[2])
    return pd.to_datetime(a, format='%Y%m%d', errors='ignore')


def generate_assignment(campaign_id, locations, max_hour, average_speed, duration, canvassers, start_date, end_date):
    assignment_list = []
    secure_random = random.SystemRandom()
    start_date_new = date_format(start_date)
    end_date_new = date_format(end_date)
    dates = pd.date_range(start=start_date_new, end=end_date_new).tolist()
    print(len(locations))
    while locations:
        start_location = secure_random.choice(locations)
        total_time = duration
        current_assignment = []
        current_location = start_location

        next_location, distance = select_next_location(locations, current_location)
        total_time = total_time + distance / average_speed + duration
        current_assignment.append(next_location)
        locations.remove(next_location)

        while total_time < max_hour:
            next_location, distance = select_next_location(locations, current_location)
            total_time = total_time + distance / average_speed + duration
            current_assignment.append(next_location)
            print(len(current_assignment))
            locations.remove(next_location)
            print(len(locations))
        assignment_list.append(current_assignment)
    assign_to_canvasser(assignment_list, canvassers, dates)


def assign_to_canvasser(assignment_list, canvassers, dates):
    for assignment in assignment_list:
        canvasser, date = find_earliest(canvassers, dates)
        assignment.update(canvasser=canvasser, date=date)


def find_earliest(canvassers, dates):
    canvasser_id_list = []
    for canvasser in canvassers:
        canvasser_id_list.append(canvasser.id)
    available_canvassers = models.Availability.objects.filter(canvasser_id__in=canvasser_id_list).order_by('date')
    for date in available_canvassers:
        if(date.date.date in dates):
            return date.canvasser, date.date.date


# def create_assignment(current_assignment, duration, campaign_id):
#     print(len(current_assignment))
#     assignment, _ = models.Assignment.objects.create(duration=duration, campaign_id=campaign_id)
#     location_id = []
#     for location in current_assignment:
#         location_id.append(location.id)
#     assignment.locations.add(location_id)


def select_next_location(locations, start_location):
    distance_list = []
    for location in locations:
        print(location)
        distance_list.append(calculate_distance(start_location, location))
        print(len(distance_list))
    index = find_minimum(distance_list)
    print(index)
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
    return c * r

def find_minimum(distance_list):
    index = len(distance_list)
    min = distance_list.pop()
    for distance in distance_list:
        if distance < min:
            min = distance
            index = distance_list.index(distance)
    return index