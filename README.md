# AircraftSearcher

## The library get aircraft list in the coordinate area.

### How to Install
Python 3 should be already installed. 
```
bash
$ sudo apt-get install virtualenv
$ cd path/to/current/dir
$ virtualenv .env
$ pip install -e /path/to/repository/aircraft_searcher
```

### Dependencies of packages

* You have to install opensky-api in virtualenv:  `https://opensky-network.org/apidoc`, before use aircraft list.


# Quickstart

### Example

* without parameters, the coordinates of Brussels are used with range 200km.
```
from aircraft_list import AircraftSearcher

get_airplane = AircraftSearcher()
for plane in get_airplane.get_aircraft_in_zone():
    print('Борт:{} из {}'.format(*plane))
```
* with parameters : 

 `get_airplane = AircraftSearcher(distance, (lower_coordinate), (upper_coordinate), (left_coordinate),(right_coordinate))`

```
from aircraft_list import AircraftSearcher

get_airplane = AircraftSearcher(200, (50.763807, 4.383034), (50.913571, 4.404359), (50.819441, 4.244614),(50.792942, 4.482057))
for plane in get_airplane.get_aircraft_in_zone():
    print('Борт:{} из {}'.format(*plane))

```
