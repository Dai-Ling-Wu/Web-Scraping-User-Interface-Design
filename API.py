#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from urllib.parse import urlencode, urlparse, parse_qsl

API_KEY='AIzaSyBtqKfIvv7ONsUVqEbKuJIClXycHGNVkcE'

class GoogleMap(object):
    lat = None
    lng = None
    data_type = 'json'
    key = API_KEY
    location = None
    foodquery = None
    id_ = None
    attr = None
    rest = None
    restaurantInfo = []
    restaurantList = []
    attractionInfo = []
    attractionList = []
    def __init__(self, address_or_zip = None, foodkind = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.location = address_or_zip
        self.foodquery = foodkind
        if self.location != None:
            self.get_coordinate()
        if self.foodquery != None:
            self.search_r()
            for i in self.rest:
                self.restaurantInfo.append(self.detail_r(place_id = i))
            self.search_a()
            for i in self.attr:
                self.attractionInfo.append(self.detail_a(place_id = i))
        for i in self.restaurantInfo:
            list1 = [i['name'], i['rating'], i['formatted_address'],i['geometry']['location']['lat'],i['geometry']['location']['lng']]
            self.restaurantList.append(list1)
        for i in self.attractionInfo:
            try:
                list2 = [i['name'], i['rating'], i['formatted_address'],i['geometry']['location']['lat'],i['geometry']['location']['lng']]
                self.attractionList.append(list2)
            except:
                pass
    
    def get_coordinate(self, address_or_zip = None):
        searched_location = self.location
        if address_or_zip != None:
            searched_location = address_or_zip
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        params = {'address': searched_location, "key": self.key}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200,299):
            return {}
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        lat,lng = latlng.get("lat"), latlng.get('lng')
        self.lat = lat
        self.lng = lng
        return lat, lng   
    
    def search_r(self, foodkind = None, radius = 5000, searchplace = None):
        keyword = self.foodquery
        if foodkind != None:
            keyword = foodkind
        lat = self.lat
        lng = self.lng
        if searchplace != None:
            self.get_coordinate(address_or_zip = searchplace)
            lat = self.lat
            lng = self.lng
        endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/{self.data_type}"
        params = {'key':API_KEY, 'location':f"{lat},{lng}", 'radius':radius, 'keyword':keyword}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200,299):
            return {}
        self.rest = [i['place_id'] for i in r.json()['results']]
    
    def search_a(self, radius = 5000, searchplace = None):
        keyword = 'attractions'
        lat = self.lat
        lng = self.lng
        if searchplace != None:
            self.get_coordinate(address_or_zip = searchplace)
            lat = self.lat
            lng = self.lng
        endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/{self.data_type}"
        params = {'key':API_KEY, 'location':f"{lat},{lng}", 'radius':radius, 'keyword':keyword}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200,299):
            return {}
        self.attr = [i['place_id'] for i in r.json()['results']]

    def detail_r(self, place_id="ChIJlXOKcDC3j4ARzal-5j-p-FY", fields=["name", "rating", "formatted_phone_number", "formatted_address","geometry"]):
        endpoint = f"https://maps.googleapis.com/maps/api/place/details/{self.data_type}"
        params = {'place_id':f'{place_id}', 'fields':','.join(fields), 'key':self.key}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200,299):
            return {}
        return r.json()['result']
        
    def detail_a(self, place_id="ChIJlXOKcDC3j4ARzal-5j-p-FY", fields=["name", "rating", "formatted_phone_number", "formatted_address","geometry"]):
        endpoint = f"https://maps.googleapis.com/maps/api/place/details/{self.data_type}"
        params = {'place_id':f'{place_id}', 'fields':','.join(fields), 'key':self.key}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200,299):
            return {}
        return r.json()['result']
        

        
        
        



    


    
   
    



    
        


        
        



        
        
        
        
        
        
        
        
        
        
        
