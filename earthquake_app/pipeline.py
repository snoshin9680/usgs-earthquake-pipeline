import sqlite3
import logging

from earthquake_app.api import fetch_earthquakes
from earthquake_app.database import init_db, insert_events, insert_aggregates
from earthquake_app.transform import aggregate

logging.basicConfig(level=logging.INFO)


def run_pipeline():
    logging.info("Starting earthquake pipeline")

    conn = sqlite3.connect("earthquakes.db")
    init_db(conn)

    for page in fetch_earthquakes():
        logging.info("Fetched %s events", len(page))

        insert_events(conn, page)

        agg = aggregate(page)
        insert_aggregates(conn, agg)

    logging.info("Pipeline finished")


if __name__ == "__main__":
    run_pipeline()