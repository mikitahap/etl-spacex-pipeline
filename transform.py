import json
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
                    launch_time = launch.get("launch_date_utc", "")
                    if launch_time:
                        launch_time = launch_time.replace("T", " ").replace(".000Z", "")

                    item = {
                        "flight_number": launch.get("flight_number", ""),
                        "launch_year": launch.get("launch_year", ""),
                        "launch_date_utc": launch_time,
                        "rocket_name": launch.get("rocket", {}).get("rocket_name", ""),
                        "rocket_type": launch.get("rocket", {}).get("rocket_type", ""),
                        "launch_site": launch.get("launch_site", {}).get("site_name", ""),
                    }
                    modified_data.append(item)
                logging.info(f"Transformed data about {len(modified_data)} launches")
        except Exception as e:
            logging.error(e)
            return
        return modified_data