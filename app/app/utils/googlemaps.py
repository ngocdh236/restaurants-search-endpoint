import googlemaps

from app.core.config import GOOGLE_MAPS_KEY


def get_distance(origin, destination):
    """
    Get distance between 2 locations on Google maps using coordinates

    Args:
        origin (tuple): lat/lon of query location
        destination (tuple): lat/lon of restaurant location

    Returns:
        distance in kilometers
    """

    gmaps = googlemaps.Client(key=GOOGLE_MAPS_KEY)
    distance_matrix = gmaps.distance_matrix(
        origins=origin, destinations=destination)

    if distance_matrix["status"] == "OK":
        first_element = distance_matrix["rows"][0]["elements"][0]
        if first_element["status"] == "OK":
            return first_element["distance"]["value"] / 1000

    return -1
