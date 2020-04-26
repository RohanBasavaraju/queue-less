from db import db, Store, Traffic
import geocoder
import datetime
import googlemaps
from googlemaps import convert
import json

def getCurrentLocation():
    currentLoc = geocoder.ip('me').latlng
    js = {
             "lat" : currentLoc[0],
             "lng" : currentLoc[1]
         }
    json_dump = json.dumps(js)
    return convert.latlng(json_dump)

api_key = ''

def getNumPeopleInStore(location):
    hour = datetime.datetime.now().hour
    traffic = Traffic.query.filter_by(coordinate = location, hour = hour).traffic
    return traffic

def updateTraffic(storeId, hour, traffic):
    prevTraffic = Traffic.query.filter_by(storeId=storeId, hour=hour)
    prevTraffic.traffic = prevTraffic.traffic * (prevTraffic.traffic/traffic)
    db.session.flush()
    db.session.commit()

def getNearbyStores(store, currentLocation):
    gmaps = googlemaps.Client(key=api_key)
    possibleStore = gmaps.places_nearby(location=(currentLocation[0],currentLocation[1]), radius = 100000, name = store)
    storeCoord = []
    for ps in possibleStore:
        storeCoord.append(ps['result']['geometry'][location])
    return storeCoord

def calculateBestStoreToGo(currentLocation, nearbyStores):
    gmaps = googlemaps.Client(key=api_key)
    list = calculateDistance(currentLocation, nearbyStores)
    intere = []
    i = 0
    for i, ele in enumerate(list):
        intere.append((ele['elements'][distance][value]),i)
    minDis = min(intere)
    minIdx = intere.index(mindis)
    store = list[destination_addresses][minIdx]
    return store

def calculateDistance(currentLocation, destination):
    gmaps = googlemaps.Client(key=api_key)
    dist_matrix = gmaps.distance_matrix(origins = currentLocation, destinations = destination)
    return dist_matrix

# Failed quick test
# lo = getCurrentLocation()
# print(lo)
# js = {
#         "lat" : lo[0],
#         "lng" : lo[1]
#     }
# jso = json.dumps(js)
# ll = calculateDistance(convert.latlng(jso), 'BestBuy')
# print(ll[1][1])