from app.utils.string import is_string_included, remove_special_characters


def test_is_string_included():
    assert is_string_included("sushi", "sushia") is True
    assert is_string_included("sushi", "Hanko Sushi") is True
    assert is_string_included("hello", "japanese") is False


def test_remove_special_characters():
    assert remove_special_characters("€lähi%") == "lähi"
