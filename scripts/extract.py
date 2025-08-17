import requests
from datetime import datetime
import json
import logging
import os

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename=None,
        filemode='a',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

class Extractor:
    def __init__(self, url):
        self.__base_url = url

    def __get_data(self):
        try:
            response = requests.get(self.__base_url)
            response.raise_for_status()
            logging.info("Found launches: %d", len(response.json()))
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error("Failed to get data: %s", e)
            return None

    def __save_launches(self, launches):
        current_day = datetime.strftime(datetime.now(), "%Y_%m_%d_%H_%M_%S")
        file_name = f"launches_{current_day}.json"

        with open(file_name, "w") as file:
            file.write(json.dumps(launches, ensure_ascii=True, indent=4, separators=(",", ":")))

        logging.info(f"Saved launches data to file: {file_name}")

    def extract(self):
        launches_data = self.__get_data()
        if launches_data is not None:
            self.__save_launches(launches_data)