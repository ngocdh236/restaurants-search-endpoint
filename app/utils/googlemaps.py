import googlemaps

from app.core.config import GOOGLE_MAPS_KEY


def get_distance(query_location, restaurant_location):
    """
    Return distance between 2 locations on Google maps in kilometers 

    :param tuple query_location: lat/lon of query location
    :param tuple restaurant_location: lat/lon of restaurant location
    :return float:
    """

    gmaps = googlemaps.Client(key=GOOGLE_MAPS_KEY)
    distance_matrix = gmaps.distance_matrix(
        origins=query_location, destinations=restaurant_location)

    if distance_matrix["status"] == "OK":
        first_element = distance_matrix["rows"][0]["elements"][0]
        if first_element["status"] == "OK":
            return first_element["distance"]["value"] / 1000

    return -1
