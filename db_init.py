import mysql.connector
import logging
from dotenv import load_dotenv
import os
from contextlib import contextmanager

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

@contextmanager
def mysql_connection():
    try:
        load_dotenv()

        db = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
        )
        yield db
    except Exception as error:
        logging.error(error)
    finally:
        db.commit()
        db.close()

def init_db():
    with mysql_connection() as db:
        mycursor = db.cursor()
        try:
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')}")
            mycursor.execute(f"USE {os.getenv('DB_NAME')}")
            mycursor.execute("CREATE TABLE IF NOT EXISTS launches(flight_number INT, launch_year INT, launch_date_utc DATETIME, rocket_name VARCHAR(255), rocket_type VARCHAR(255), launch_site VARCHAR(255), UNIQUE(launch_date_utc, flight_number))")
            logging.info("Database initialized")
            mycursor.close()
        except mysql.connector.Error as err:
            logging.error(err)
        except Exception as err:
            logging.error(err)

init_db()