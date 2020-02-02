import requests

from app.utils.googlemaps import get_distance

RESTAURANTS_STR = f"http://127.0.0.1:8000/api/restaurants"


def test_search():
    q_lat = 60.17045
    q_lon = 24.93147

    r = requests.get(
        f"{RESTAURANTS_STR}/search/?q=sushi&lat={q_lat}&lon={q_lon}"
    )

    data = r.json()

    assert r.status_code == 200
    assert len(data) > 0
    for item in data:
        lon, lat = item["location"]
        assert 0 < get_distance((q_lat, q_lon), (lat, lon)) < 3


def test_search_fail():
    r = requests.get(
        f"{RESTAURANTS_STR}/search/?lat=test"
    )

    assert r.status_code == 422
