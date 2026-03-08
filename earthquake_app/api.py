import requests
from datetime import datetime, timedelta

BASE_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"


def fetch_earthquakes(days=30, limit=10000):
    end = datetime.utcnow()
    start = end - timedelta(days=days)

    offset = 1

    while True:
        params = {
            "format": "geojson",
            "starttime": start.strftime("%Y-%m-%d"),
            "endtime": end.strftime("%Y-%m-%d"),
            "limit": limit,
            "offset": offset
        }

        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()
        events = data["features"]

        if not events:
            break

        yield events
        offset += limit