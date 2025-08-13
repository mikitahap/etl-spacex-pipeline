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

## Upcoming work

- Enhancing the transformation stage for more comprehensive data cleaning and enrichment.  
- Additional database integrations or output destinations.

## How to use the pipeline

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file and fill it with your MySQL Server information

```bash
nano .env
```

Run the script

```
python3 load.py
```

Project structure (in progress)
```
/extract.py   # Extraction scripts and raw data
/transform.py # Data cleaning and transformation scripts
/load.py      # Loading scripts to destination (DB, etc)
/db_init.py   # Database initialization scripts
/requirements.txt  # Project dependencies
/README.md    # This file
