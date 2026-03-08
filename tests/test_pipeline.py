import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import responses
from earthquake_app.api import fetch_earthquakes


@responses.activate
def test_fetch():
    responses.add(
        responses.GET,
        "https://earthquake.usgs.gov/fdsnws/event/1/query",
        json={
            "features": [
                {
                    "id": "1",
                    "properties": {
                        "mag": 3,
                        "place": "test location",
                        "time": 123456789
                    }
                }
            ]
        },
        status=200,
    )

    responses.add(
        responses.GET,
        "https://earthquake.usgs.gov/fdsnws/event/1/query",
        json={"features": []},
        status=200,
    )

    pages = list(fetch_earthquakes(days=1, limit=1))

    assert len(pages) == 1
    assert pages[0][0]["id"] == "1"