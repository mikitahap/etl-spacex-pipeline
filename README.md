# SpaceX Launches ETL Pipeline

This repository contains a multi-stage ETL pipeline for SpaceX launch data.

## Current status

**Extractor implemented:**  
The extraction stage is complete and functional. It fetches launch data from the SpaceX public API and saves it as timestamped JSON files. Logging is set up for monitoring.

**Transformer class implemented:**  
Basic transformation logic to clean and restructure extracted data is implemented.

## Upcoming work

- Improving and expanding the transformation stage for more comprehensive data cleaning and enrichment.  
- Implementation of the loading stage to transfer data to databases or other destinations.

## How to use the extractor

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the extractor script located in the raw/ folder:

```bash
python raw/extractor.py
```
Project structure (in progress)
```
/raw          # Extraction scripts and raw data
/transform    # (Planned) Data cleaning and transformation scripts
/load         # (Planned) Data loading to destination (DB, etc)
/README.md    # This file
