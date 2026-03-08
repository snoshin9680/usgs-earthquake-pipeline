## USGS Earthquake Data Pipeline

This project implements a Python data pipeline that retrieves earthquake data
from the USGS API, processes it into daily magnitude buckets, and stores both
raw and aggregated results in a SQLite database. The pipeline supports
pagination, logging, and offline testing using pytest.

## Features
- Fetch earthquake events from the USGS API
- Handle pagination
- Transform magnitude buckets
- Aggregate daily earthquake counts
- Store results in SQLite
- Unit tests using pytest

## Project Structure

earthquake_app/
- api.py
- transform.py
- database.py
- pipeline.py

tests/
- test_pipeline.py

## Run the Pipeline

python -m earthquake_app.pipeline

## Run Tests

pytest

## Install Requirements

pip install -r requirements.txt
------------------------------------------------------------------------------------------------------------------
## Design Decisions

- I separated the project into small modules:
  - `api.py` handles fetching earthquake data from the USGS API
  - `transform.py` handles magnitude bucketing and daily aggregation
  - `database.py` handles SQLite table creation and inserts
  - `pipeline.py` orchestrates the end-to-end workflow

- I used SQLite because it is lightweight, easy to run locally, and matches the assignment requirement to store both raw and aggregated data.

- I used pagination with `limit` and `offset` so the pipeline can fetch all earthquake records rather than only the first page.

- I added logging in the pipeline so the job is easier to debug if it fails or returns unexpected results.

- I used `pytest` with mocked API responses so tests do not depend on the live USGS API and can run reliably offline.

## Example Output
INFO:root:Starting earthquake pipeline
INFO:root:Fetched 10000 events
INFO:root:Fetched 170 events
INFO:root:Pipeline finished



