# USGS Earthquake Pipeline

This project implements a Python data pipeline that ingests earthquake data from the USGS API, processes the events, and stores aggregated statistics in a SQLite database.

## Features
- Fetches earthquake events from the USGS API
- Handles API pagination
- Transforms and buckets magnitudes
- Aggregates earthquake counts by day and magnitude range
- Stores results in SQLite
- Includes pytest unit tests

## Project Structure

earthquake_app/
- api.py → Fetches earthquake data from USGS API
- transform.py → Aggregates and buckets magnitude ranges
- database.py → Stores results in SQLite
- pipeline.py → Runs the full pipeline

tests/
- test_pipeline.py → Unit tests

## Run the Pipeline
