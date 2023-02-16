from django.test import TestCase

from api.models import Station, Network
from api.services import GetCitiBik

DATA = {
    "network": {
        "company": [
            "Tembici",
            "PBSC Urban Solutions"
        ],
        "gbfs_href": "https://santiago.publicbikesystem.net/ube/gbfs/v1/",
        "href": "/v2/networks/bikesantiago",
        "id": "bikesantiago",
        "location": {
            "city": "Santiago",
            "country": "CL",
            "latitude": -33.45,
            "longitude": -70.67
        },
        "name": "BikeSantiago",
        "stations": [
            {
                "empty_slots": 14,
                "extra": {
                    "address": "Plaza Egaña 68",
                    "altitude": 0.0,
                    "ebikes": 0,
                    "has_ebikes": True,
                    "last_updated": 1676488404,
                    "normal_bikes": 2,
                    "payment": [
                        "key",
                        "transitcard",
                        "creditcard",
                        "phone"
                    ],
                    "payment-terminal": True,
                    "post_code": "1111",
                    "renting": 1,
                    "returning": 1,
                    "slots": 17,
                    "uid": "190"
                },
                "free_bikes": 2,
                "id": "558b5143b0d6480940e551f6bcc9fdf8",
                "latitude": -33.45261426,
                "longitude": -70.57100594,
                "name": "N10 - Metro Plaza Egaña",
                "timestamp": "2023-02-15T19:14:41.146000Z"
            }
        ]
    }
}


class Tests(TestCase):
    def test_create_station_and_network(self):
        GetCitiBik.create_station_network(DATA)
        network = Network.objects.get()
        station = Station.objects.get()
        assert network.stations.name == station.name

