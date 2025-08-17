import mysql.connector
import logging
from dotenv import load_dotenv
from db_init import init_db
from contextlib import contextmanager
import os

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

@contextmanager
def mysql_connection():
    load_dotenv("/opt/airflow/.env")
    db = mysql.connector.connect(
        host=os.getenv("ETL_DB_HOST"),
        port=os.getenv("ETL_DB_PORT"),
        user=os.getenv("ETL_DB_USER"),
        password=os.getenv("ETL_DB_PASSWORD"),
        database=os.getenv("ETL_DB_NAME")
    )
    try:
        yield db
    finally:
        db.commit()
        db.close()
class Loader():
    def __init__(self):
        load_dotenv("/opt/airflow/.env")
        init_db()

    def load(self, modified_data):
        try:
            if not modified_data:
                logging.error('No data found')
                return

            init_db()

            with mysql_connection() as db:
                mycursor = db.cursor()

                sql_query = "INSERT IGNORE INTO launches (flight_number, launch_year, launch_date_utc, rocket_name, rocket_type, launch_site) VALUES (%s, %s, %s, %s, %s, %s)"

                for item in modified_data:
                    values = (
                        item['flight_number'],
                        item['launch_year'],
                        item['launch_date_utc'],
                        item['rocket_name'],
                        item['rocket_type'],
                        item['launch_site']
                    )
                    mycursor.execute(sql_query, values)

                logging.info("Successfully inserted data into launches table")
                mycursor.close()
        except mysql.connector.Error as e:
            logging.error(f"MySQL error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")