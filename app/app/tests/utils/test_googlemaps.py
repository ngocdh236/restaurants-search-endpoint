from app.utils.googlemaps import get_distance


def test_get_distance():
    assert get_distance((60.17045, 24.93147),
                        (60.169938852212965, 24.941325187683105)) is not -1
    assert get_distance((60.17045, 24.93147), (-232, -23234)) is -1
