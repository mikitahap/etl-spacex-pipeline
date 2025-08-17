# SpaceX Launches ETL Pipeline

This repository contains a multi-stage ETL pipeline for SpaceX launch data.

## Current status

**Extractor implemented:**  
The extraction stage fetches launch data from the SpaceX public API and saves it as timestamped JSON files. Logging is set up for monitoring.

**Transformer implemented:**  
Basic transformation logic to clean and restructure extracted data is in place.

**Load stage implemented:**  
Data can now be loaded into the configured database.

**Database initialization script added:**  
A script to initialize and set up the database schema is included.

**Docker containerization:**  
The project has been containerized with Docker for easier deployment and consistency across different systems. You can now run the pipeline and the database in isolated containers.

**Apache Airflow scheduling and orchestration added**


## Upcoming work

- Enhancing the transformation stage for more comprehensive data cleaning and enrichment.  
- Additional database integrations or output destinations.  

## How to use the pipeline

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file and fill it with your configuration:

```bash
nano .env
```
Example .env file:

```bash
AIRFLOW_UID=501
AIRFLOW_GID=0
BASE_URL="https://api.spacexdata.com/v3/launches"
ETL_DB_HOST=mysql
ETL_DB_PORT=3306
ETL_DB_USER=etl_user
ETL_DB_PASSWORD=etl_password
ETL_DB_NAME=etl
```

Run using Docker Compose:

```bash
docker-compose up --build
```

Apache Airflow Web UI will be available at http://localhost:8081/

Project structure (in progress)

```bash
Dockerfile
docker-compose.yml
/scripts
    /extract.py   # Extraction scripts and raw data
    /transform.py # Data cleaning and transformation scripts
    /load.py      # Loading scripts to destination (DB, etc)
    /db_init.py   # Database initialization scripts
/dags
    /pipeline_dag.py #dag file for scheduling
/requirements.txt # Project dependencies
/README.md        # This file
```
