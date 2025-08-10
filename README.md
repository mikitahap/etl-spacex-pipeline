SpaceX Launches ETL Pipeline
This repository contains a multi-stage ETL pipeline for SpaceX launch data.

Current status
Extractor implemented:
The extraction stage is complete and functional. It fetches launch data from the SpaceX public API and saves it as timestamped JSON files. Logging is set up for monitoring.

Upcoming work:
Transformation and loading stages are planned next to complete the pipeline.

How to use the extractor
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the extractor script located in raw/ folder:

bash
Copy code
python raw/extractor.py
Project structure (work in progress)
bash
Copy code
/raw          # Extraction scripts and raw data
/transform    # (Planned) Data cleaning and transformation scripts
/load         # (Planned) Data loading to destination (DB, etc)
/README.md    # This file
