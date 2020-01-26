import json


def get_data_from_json_file(path: str):
    data = None
    with open(path) as data_json:
        data = json.load(data_json)

    return data
