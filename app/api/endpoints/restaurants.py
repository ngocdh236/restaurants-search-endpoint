import json
import operator

from fastapi import APIRouter, Query
from starlette.responses import JSONResponse

from app.utils.googlemaps import get_distance
from app.utils.json import get_data_from_json_file

router = APIRouter()


@router.get("/search")
def search(lat: float, lon: float, q: str = Query(..., min_length=1)):
    """
    /restaurants/search/

    Search for restaurants that match given query string and 
    are closer than 3 kilometers from given coordinates

    Args:
        lat (float): The latitude
        lon (float): The longitude
        q (str): The query string

    Returns: 
        A Starlette JSONResponse
    """

    restaurants = get_data_from_json_file(
        path='restaurants.json')["restaurants"]

    results = []

    for restaurant in restaurants:
        query_strings = q.lower().split()
        matched_strings = 0

        for q_string in query_strings:
            if q_string in restaurant["name"].lower():
                matched_strings += 1

            if q_string in restaurant["description"].lower():
                matched_strings += 1

            if q_string in [tag.lower() for tag in restaurant["tags"]]:
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

    return JSONResponse(status_code=200, content=[result["restaurant"]
                                                  for result in results])
