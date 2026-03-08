import sqlite3


def init_db(conn):
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS earthquakes(
        id TEXT PRIMARY KEY,
        magnitude REAL,
        place TEXT,
        time INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS daily_aggregates(
        date TEXT,
        bucket TEXT,
        count INTEGER
    )
    """)

    conn.commit()


def insert_events(conn, events):
    cur = conn.cursor()

    for e in events:
        props = e["properties"]

        cur.execute("""
        INSERT OR IGNORE INTO earthquakes VALUES (?,?,?,?)
        """, (
            e["id"],
            props["mag"],
            props["place"],
            props["time"]
        ))

    conn.commit()


def insert_aggregates(conn, aggregates):
    cur = conn.cursor()

    for date, buckets in aggregates.items():
        for bucket, count in buckets.items():
            cur.execute("""
            INSERT INTO daily_aggregates VALUES (?,?,?)
            """, (date, bucket, count))

    conn.commit()