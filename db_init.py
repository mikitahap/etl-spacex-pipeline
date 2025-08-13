import mysql.connector
import logging
from dotenv import load_dotenv
import os

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def init_db():
    load_dotenv()

    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    mycursor = db.cursor()
    try:
        mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
        mycursor.execute(f"USE {os.getenv('DB_NAME')}")
        mycursor.execute("CREATE TABLE IF NOT EXISTS launches(flight_number INT, launch_year INT, launch_date_utc DATETIME, rocket_name VARCHAR(255), rocket_type VARCHAR(255), launch_site VARCHAR(255), UNIQUE(launch_date_utc, flight_number))")
        logging.info("Database initialized")
        db.commit()
        mycursor.close()
        db.close()
    except mysql.connector.Error as err:
        logging.error(err)
    except Exception as err:
        logging.error(err)

init_db()