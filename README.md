## Installation

(Please skip step 1 and 3 if project directory already contains venv folder)

1. Go to the project directory, create a virtual environment name 'venv':

`python3 -m venv venv`

2. Activate the virtual environment:

`source venv/bin/activate`

3. Install dependencies:

`pip install -r requirements.txt`

4. Go to 'app' folder in the project directory

5. Run app in local environment:

`uvicorn main:app --reload`

6. App is now running at http://127.0.0.1:8000

Request URL example for restaurants search:
http://127.0.0.1:8000/api/restaurants/search/?q=sushi&lat=60.17045&lon=24.93147

## Testing

1. Go to 'app' folder in the project directory

2. Run app in local environment (some tests require app to run):

`uvicorn main:app --reload`

3. Run tests:

`pytest`

## Frameworks && Libraries

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [pytest](https://docs.pytest.org/en/latest/)
- [googlemaps](https://github.com/googlemaps/google-maps-services-python)

## API Documentation

- Documentation can be found at http://127.0.0.1:8000/docs
