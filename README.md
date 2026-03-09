# USGS Earthquake Data Pipeline

This project implements a Python-based data pipeline that retrieves earthquake event data from the **USGS Earthquake API**, processes the data into daily magnitude buckets, and stores both raw and aggregated results in a **SQLite database**.

The pipeline supports pagination, logging for observability, and offline unit testing using **pytest**.

---

# Quick Start

Clone the repository and run the pipeline in a few steps.

```bash
git clone <repository-url>
cd usgs-earthquake-pipeline

# create virtual environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the pipeline
python3 -m earthquake_app.pipeline
```

---

# Features

* Fetch earthquake event data from the **USGS API**
* Handle pagination to retrieve all available records
* Transform earthquake magnitudes into buckets (`0–2`, `2–4`, `4–6`, `6+`)
* Aggregate earthquake counts by day and magnitude bucket
* Store raw and aggregated results in a **SQLite database**
* Logging for debugging and monitoring pipeline execution
* Unit testing using **pytest** with mocked API responses

---

# Project Structure

```
usgs-earthquake-pipeline
│
├── earthquake_app
│   ├── __init__.py
│   ├── api.py
│   ├── database.py
│   ├── transform.py
│   └── pipeline.py
│
├── tests
│   └── test_pipeline.py
│
├── earthquakes.db
├── requirements.txt
└── README.md
```

---

# Installation

Install project dependencies.

```bash
pip install -r requirements.txt
```

If using Python 3 explicitly:

```bash
pip3 install -r requirements.txt
```

---

# Running the Pipeline

From the **project root directory**, run:

```bash
python3 -m earthquake_app.pipeline
```

The pipeline will:

1. Fetch earthquake data from the USGS API
2. Transform magnitudes into buckets
3. Aggregate earthquake counts by day
4. Store raw and aggregated results in the SQLite database

---

# Running Tests

Run unit tests using:

```bash
pytest
```

Tests mock API responses so they can run reliably without depending on the live USGS API.

---

# Verify Pipeline Output

After running the pipeline, you can inspect the SQLite database to verify results.

Open the database:

```bash
sqlite3 earthquakes.db
```

List tables:

```sql
.tables
```

Check the number of raw earthquake records:

```sql
SELECT COUNT(*) FROM earthquakes;
```

View aggregated results:

```sql
SELECT * FROM daily_aggregates LIMIT 10;
```

Exit SQLite:

```sql
.quit
```

---

# Database Tables

The pipeline creates two tables:

### earthquakes

Stores raw earthquake event data retrieved from the API.

### daily_aggregates

Stores aggregated earthquake counts grouped by:

* date
* magnitude bucket

Example output:

| date       | magnitude_bucket | count |
| ---------- | ---------------- | ----- |
| 2026-03-07 | 0-2              | 152   |
| 2026-03-07 | 2-4              | 98    |
| 2026-03-07 | 4-6              | 19    |

---

# Design Decisions

## Modular Architecture

The project is organized into small modules to improve maintainability and testability:

* **api.py**
  Handles retrieving earthquake data from the USGS API.

* **transform.py**
  Processes earthquake magnitudes into buckets and generates daily aggregates.

* **database.py**
  Manages SQLite table creation and data insertion.

* **pipeline.py**
  Orchestrates the end-to-end workflow.

This modular structure makes the pipeline easier to maintain, extend, and test.

---

## SQLite Database

SQLite was chosen because it is lightweight, requires no external setup, and satisfies the requirement to store both raw and aggregated earthquake data locally.

---

## Pagination

The USGS API returns results in pages. The pipeline uses `limit` and `offset` parameters to ensure all earthquake records are retrieved rather than only the first page.

---

## Logging

Logging is implemented to provide visibility into pipeline execution and help diagnose issues if the pipeline fails.

---

## Testing

The project uses **pytest** for unit testing. API responses are mocked to ensure tests run consistently without depending on the external USGS API.

---

# Example Pipeline Output

```
INFO Starting earthquake pipeline
INFO Database initialized
INFO Fetched page 1 with 10000 events
INFO Inserted 10000 raw events into database
INFO Inserted aggregates for page 1
INFO Fetched page 2 with 248 events
INFO Inserted 248 raw events into database
INFO Inserted aggregates for page 2
INFO Pipeline finished successfully
INFO Processed 2 pages and 10248 total events
```

---

# Tech Stack

* Python 3
* SQLite
* Requests
* Pytest
* Logging

---

# Summary

This project demonstrates:

* API data ingestion
* Data transformation and aggregation
* Database storage
* Logging and observability
* Unit testing with mocked external dependencies
* Modular Python pipeline architecture

---

