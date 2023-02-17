from datetime import datetime

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from api.models import Station, Network, Project
from challenge.settings import env

options = Options()

options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")


class GetCitiBik:
    @staticmethod
    def get_data():
        print("Get data Api...")
        try:
            url = env('URL_API')
            response = requests.get(url)
            response = response.json()
            return response
        except requests.exceptions.Timeout as e:
            print(e)

    @staticmethod
    def create_station_network(response):
        print("Saved in db...")
        network = Network()
        network.company = response['network']['company']
        network.gbfs_href = response['network']['gbfs_href']
        network.href = response['network']['href']
        network.location = response['network']['location']
        network.name = response['network']['name']
        for station in response['network']['stations']:
            station['uid'] = station['id']
            del station['id']
            station = Station(**station)
            network.stations = station
            station.save()
            network.save()


class GetSeia:
    @staticmethod
    def get_chrome():
        print('Initializing Chrome...')
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install()
            ),
            options=options
        )

    @staticmethod
    def obtain_data(driver):
        url = env('URL_API2')
        driver.get(url)
        data_lists = []
        option_selects = driver.find_elements(By.XPATH, '//*[@id="main"]/div[3]/div[4]/div/select/option')
        for option in range(1, len(option_selects) + 1):
            print(f"Scraping Page: {option}")
            select = driver.find_element(By.XPATH, f"//*[@id='main']/div[3]/div[4]/div/select/option[{option}]")
            select.click()

            rows = driver.find_elements(By.XPATH, '//*[@id="main"]/div[3]/div[4]/div/table/tbody/tr')
            cols = driver.find_elements(By.XPATH, '//*[@id="main"]/div[3]/div[4]/div/table/tbody/tr[1]/td')

            for row in range(1, len(rows) + 1):
                _data = []
                for col in range(1, len(cols) + 1):
                    result = driver.find_element(
                        By.XPATH,
                        f"//*[@id='main']/div[3]/div[4]/div/table/tbody/tr[{row}]/td[{col}]"
                    ).text
                    _data.append(result)
                data_lists.append(_data)

        driver.quit()
        return data_lists

    def create_project(self, data_lists):
        objs = []
        for data in data_lists:
            objs.append(Project(
                name=data[1],
                type=data[2],
                region=data[3],
                typology=data[4],
                holder=data[5],
                investment=data[6],
                date_admission=self.format_date(data[7]),
                status=data[8]
            )
            )
        print("Saved in DB...")
        Project.objects.bulk_create(objs)

    @staticmethod
    def format_date(data):
        return datetime.strptime(data, '%d/%m/%Y')
