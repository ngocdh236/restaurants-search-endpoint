import random

from starlette.testclient import TestClient

from main import app
from app.utils.googlemaps import get_distance

client = TestClient(app)
RESTAURANTS_STR = "/api/restaurants"
RESTAURANTS_SEARCH_STR = f"{RESTAURANTS_STR}/search"

def test_search():
    q = "Hanko sushi"
    q_lat = 60.17045
    q_lon = 24.93147

    response = client.get(
        f"{RESTAURANTS_SEARCH_STR}/?q={q}&lat={q_lat}&lon={q_lon}"
    )

    data = response.json()
    random_restaurant = random.choice(data)
    lon, lat = random_restaurant["location"]

    assert response.status_code == 200
    assert len(data) > 0
    assert 0 < get_distance((q_lat, q_lon), (lat, lon)) < 3
    
    response = client.get(
        f"{RESTAURANTS_SEARCH_STR}/?lat=fail&lon={q_lon}"
    )

    error = response.json()
    error_detail = error["detail"]
    
    assert response.status_code == 422
    assert len(error_detail) == 2
    for item in error_detail:
        if "q" in item["loc"]:
            assert item["type"] == "value_error.missing"
        if "lat" in item["loc"]:
            assert item["type"] == "type_error.float"
       