## Installation

1. In the project directory, you can run:

`source venv/bin/activate`

2. Go to folder 'app' inside project directory, you can run:

`uvicorn main:app --reload`

3. You can now search for restaurants by making API call to http://127.0.0.1:8000/api

Example:
http://127.0.0.1:8000/api/restaurants/search/?q=hanko%20sushi&lat=60.17045&lon=24.93147

## Testing

- Go to folder 'app' inside project directory, you can run:

`pytest`

## Frameworks && Libraries

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [pytest](https://docs.pytest.org/en/latest/)
- [googlemaps](https://github.com/googlemaps/google-maps-services-python)

## API Documentation

- Documentation can be found at http://127.0.0.1:8000/docs
