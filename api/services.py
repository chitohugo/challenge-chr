import requests

from api.models import Station, Network
from challenge.settings import env


class GetCitiBik:
    @classmethod
    def get_data(cls):
        try:
            url = env('URL_API')
            response = requests.get(url)
            response = response.json()
            return response
        except requests.exceptions.Timeout as e:
            print(e)

    @classmethod
    def create_station_network(cls, response):
        network = Network()
        network.company = response['network']['company']
        network.gbfs_href = response['network']['gbfs_href']
        network.href = response['network']['href']
        network.id = response['network']['id']
        network.location = response['network']['location']
        network.name = response['network']['name']
        for station in response['network']['stations']:
            station = Station(**station)
            network.stations = station
            station.save()
            network.save()



