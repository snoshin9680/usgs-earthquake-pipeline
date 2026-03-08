from collections import defaultdict
from datetime import datetime


def magnitude_bucket(mag):
    if mag is None:
        return None
    if mag < 2:
        return "0-2"
    if mag < 4:
        return "2-4"
    if mag < 6:
        return "4-6"
    return "6+"


def aggregate(events):
    daily_counts = defaultdict(lambda: defaultdict(int))

    for e in events:
        props = e["properties"]

        mag = props["mag"]
        timestamp = props["time"]

        date = datetime.utcfromtimestamp(timestamp / 1000).date()

        bucket = magnitude_bucket(mag)

        if bucket:
            daily_counts[str(date)][bucket] += 1

    return daily_counts