from api.services import GetCitiBik


def run():
    instance = GetCitiBik()
    response = instance.get_data()
    instance.create_station_network(response)
