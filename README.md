# USGS Earthquake Pipeline

This project builds a Python data pipeline that fetches earthquake data from the USGS API, processes the data, and stores results in a SQLite database.

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
