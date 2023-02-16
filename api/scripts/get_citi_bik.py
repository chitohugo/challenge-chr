from api.services import GetCitiBik


def run():
    service = GetCitiBik()
    response = service.get_data()
    service.create_station_network(response)
