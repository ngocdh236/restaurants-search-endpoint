import json
import operator

from fastapi import APIRouter, Query

from app.utils.file import get_data_from_json_file
from app.utils.googlemaps import get_distance
from app.utils.string import is_string_included

router = APIRouter()


@router.get("/search/")
def search(lat: float, lon: float, q: str = Query(..., min_length=1)):
    """
    /restaurants/search/

    Search for restaurants that match given query string and
    are closer than 3 kilometers from given coordinates

    Args:
        lat (float): The latitude
        lon (float): The longitude
        q (str): The query string

    """

    restaurants = get_data_from_json_file(
        path='restaurants.json')["restaurants"]

    results = []
    query_strings = q.split()

    for restaurant in restaurants:
        compare_strings = [restaurant["name"], restaurant["description"]] \
            + restaurant["tags"]

        matched_strings = 0

        for q_string in query_strings:
            for c_string in compare_strings:
                if is_string_included(q_string, c_string):
                    matched_strings += 1

        if matched_strings > 0:
            restaurant_lon, restaurant_lat = restaurant["location"]
            distance = get_distance(
                (lat, lon), (restaurant_lat, restaurant_lon))

            if 0 < distance < 3:
                results.append({
                    "restaurant": restaurant,
                    "distance": round(distance, 1),
                    "matched_strings": -matched_strings
                })

    results = sorted(results, key=operator.itemgetter(
        "matched_strings", "distance"))

    return [result["restaurant"]for result in results]
