# An endpoint for restaurants search

## Installation

1. Go to the project directory, create a virtual environment name 'venv':

   `python3 -m venv venv`

2. Activate the virtual environment:

   `source venv/bin/activate`

3. Install dependencies:

   `pip install -r requirements.txt`

4. Go to folder 'app' in the project directory

   `cd app`

5. Run app in local environment:

   `uvicorn main:app --reload`

6. App is now running at http://127.0.0.1:8000

Request URL example for restaurants search:

http://127.0.0.1:8000/api/restaurants/search/?q=sushi&lat=60.17045&lon=24.93147

## Testing

1. Make sure the virtual environment is running

2. Go to folder 'app' in the project directory

3. Run tests:

   `pytest`

## Frameworks & Libraries

- [FastAPI](https://fastapi.tiangolo.com/)
- [googlemaps](https://github.com/googlemaps/google-maps-services-python)
- [pytest](https://docs.pytest.org/en/latest/)
- [Uvicorn](https://www.uvicorn.org/)

## API Documentation

- Documentation can be found at http://127.0.0.1:8000/docs
