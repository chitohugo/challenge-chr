from django.test import TestCase

from api.models import Station, Network

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


class TestGetPost(TestCase):
    def test_create_station_and_network(self):
        station = Station()
        station.empty_slots = DATA['network']['stations'][0]['empty_slots']
        station.extra = DATA['network']['stations'][0]['extra']
        station.free_bikes = DATA['network']['stations'][0]['free_bikes']
        station.id = DATA['network']['stations'][0]['id']
        station.latitude = DATA['network']['stations'][0]['latitude']
        station.longitude = DATA['network']['stations'][0]['longitude']
        station.name = DATA['network']['stations'][0]['name']
        station.timestamp = DATA['network']['stations'][0]['timestamp']

        self.assertEqual(station.id, '558b5143b0d6480940e551f6bcc9fdf8')

        network = Network()
        network.company = DATA['network']['company']
        network.gbfs_href = DATA['network']['gbfs_href']
        network.id = DATA['network']['id']
        network.location = DATA['network']['location']
        network.name = DATA['network']['name']
        network.station = station
        self.assertEqual(network.station.id, DATA['network']['stations'][0]['id'])



