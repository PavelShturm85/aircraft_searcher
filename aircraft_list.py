#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from opensky_api import OpenSkyApi
from math import cos, fabs


class AircraftSearcher():

    def __init__(self, km=200,
                 coordinates_min_latitude=(50.763807, 4.383034),
                 coordinates_max_latitude=(50.913571, 4.404359),
                 coordinates_min_longitude=(50.819441, 4.244614),
                 coordinates_max_longitude=(50.792942, 4.482057)):

        coordinat_tuple = (coordinates_min_latitude, coordinates_max_latitude,
                           coordinates_min_longitude, coordinates_max_longitude)
        for latitude, longitude in coordinat_tuple:
            if latitude > 90 or latitude < -90 or longitude > 180 or longitude < -180:
                raise ValueError

        if km > 12742:
            raise ValueError

        self._min_latitude, self._ = coordinates_min_latitude
        self._max_latitude, self._ = coordinates_max_latitude
        self._latitude_on_min_longitude, self._min_longitude = coordinates_min_longitude
        self._latitude_on_max_longitude, self._max_longitude = coordinates_max_longitude
        self._km = fabs(km)

    @property
    def __latitude_in_km(self):
        return self._km / 111.134861111

    def __longitude_in_km(self, km, latitude):
        return km / (cos(latitude) * 111.321377778)

    @property
    def _get_corrected_coordinates(self):
        corrected_min_latitude = self._min_latitude - self.__latitude_in_km
        if corrected_min_latitude < -90.0:
            corrected_min_latitude = -90.0

        corrected_max_latitude = self._max_latitude + self.__latitude_in_km
        if corrected_max_latitude > 90.0:
            corrected_max_latitude = 90.0

        corrected_min_longitude = self._min_longitude - \
            self.__longitude_in_km(self._km, self._latitude_on_min_longitude)

        corrected_max_longitude = self._max_longitude + \
            self.__longitude_in_km(self._km, self._latitude_on_max_longitude)

        if corrected_min_longitude > 180.0:
            corrected_min_longitude = corrected_min_longitude - 360.0

        elif corrected_min_longitude < -180.0:
            corrected_min_longitude = -180.0 - corrected_min_longitude

        elif corrected_max_longitude > 180.0:
            corrected_max_longitude = corrected_max_longitude - 360.0

        elif corrected_max_longitude < -180.0:
            corrected_max_longitude = -180.0 - corrected_max_longitude

        elif fabs(corrected_min_longitude) + fabs(corrected_max_longitude) >= 360.0:

            corrected_max_longitude = 180.0
            corrected_min_longitude = -180.0

        elif corrected_min_longitude > corrected_max_longitude:
            corrected_max_longitude = self._max_longitude - \
                self.__longitude_in_km(
                    self._km, self._latitude_on_max_longitude)

            corrected_min_longitude = self._min_longitude + \
                self.__longitude_in_km(
                    self._km, self._latitude_on_min_longitude)

        return (corrected_min_latitude, corrected_max_latitude, corrected_min_longitude, corrected_max_longitude)

    def get_aircraft_in_zone(self):
        api = OpenSkyApi()
        states = api.get_states(bbox=self._get_corrected_coordinates)
        return [(s.callsign, s.origin_country) for s in states.states]


if __name__ == '__main__':

    get_airplane = AircraftSearcher()
    for plane in get_airplane.get_aircraft_in_zone():
        print('Борт:{} из {}'.format(*plane))
