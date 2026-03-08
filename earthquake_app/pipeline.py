import sqlite3
import logging

from earthquake_app.api import fetch_earthquakes
from earthquake_app.database import init_db, insert_events, insert_aggregates
from earthquake_app.transform import aggregate

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def run_pipeline():
    logging.info("Starting earthquake pipeline")

    try:
        conn = sqlite3.connect("earthquakes.db")
        init_db(conn)
        logging.info("Database initialized")

        total_pages = 0
        total_events = 0

        for page in fetch_earthquakes():
            total_pages += 1
            total_events += len(page)

            logging.info("Fetched page %s with %s events", total_pages, len(page))

            insert_events(conn, page)
            logging.info("Inserted %s raw events into database", len(page))

            agg = aggregate(page)
            insert_aggregates(conn, agg)
            logging.info("Inserted aggregates for page %s", total_pages)

        logging.info("Pipeline finished successfully")
        logging.info("Processed %s pages and %s total events", total_pages, total_events)

    except Exception as e:
        logging.exception("Pipeline failed with error: %s", e)
        raise


if __name__ == "__main__":
    run_pipeline()