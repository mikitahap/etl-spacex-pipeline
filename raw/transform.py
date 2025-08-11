import json
import csv
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Transformer:
    def __init__(self):
        self.__files = []

    def __get_files(self):
        self.__files.clear()
        for f in os.listdir('.'):
            if f.startswith("launches") and f.endswith(".json"):
                self.__files.append(f)

        if not self.__files:
            return None
        else:
            latest = max(self.__files)
            return latest

    def __save_data(self, modified_data):
        fieldnames = modified_data[0].keys()
        with open("transformed_launches.csv", "w", newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(modified_data)
            logging.info(f"Loaded transformed data to file transformed_launches.csv")

    def transform(self):
        latest = self.__get_files()
        if not latest:
            logging.error("No launches file found")
            return

        modified_data = []

        try:
            with open(latest) as json_file:
                data = json.load(json_file)

                for launch in data:
                    item = {
                        "flight_number": launch.get("flight_number", ""),
                        "launch_year": launch.get("launch_year", ""),
                        "launch_date_utc": launch.get("launch_date_utc", ""),
                        "rocket_name": launch.get("rocket", {}).get("rocket_name", ""),
                        "rocket_type": launch.get("rocket", {}).get("rocket_type", ""),
                        "launch_site": launch.get("launch_site", {}).get("site_name", ""),
                    }
                    modified_data.append(item)
                logging.info(f"Transformed data about {len(modified_data)} launches")
        except Exception as e:
            logging.error(e)
            return
        self.__save_data(modified_data)

transformer = Transformer()
transformer.transform()