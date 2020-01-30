from app.utils.file import get_data_from_json_file


def test_get_data_from_json_file():
    assert get_data_from_json_file(path="restaurants.json") is not None
