from api.services import GetSeia


def run():
    instance = GetSeia()
    driver = instance.get_chrome()
    data = instance.obtain_data(driver)
    instance.create_project(data)
    input("Presiona una tecla para salir")

