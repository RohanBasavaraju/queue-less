import db, Store, Traffic
import geocoder
import datetime
import googlemaps

def getCurrentLocation(self):
    currentLoc = geocoder.ip('me')
    return currentLoc

api_key = 'AIzaSyCCSSTJ_rZxxfuAEG8dl4SG_FXXnpkCTXs'

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
    possibleStore = gmaps.places_nearby(location=currentLocation, radius = 100000, name = store)
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
    dist_matrix = gmaps.distance_matrix(origin = currentLocation, destinations = destination)
    return dis_matrix