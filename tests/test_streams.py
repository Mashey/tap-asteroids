import pytest, os 
from tap_asteroids.streams import AllAsteroids
from tap_asteroids.client import AsteroidClient
from dotenv import load_dotenv

load_dotenv()
config = {
    "api_key": os.getenv('api_key'),
}


@pytest.mark.vcr()
def test_get_all_asteroids():
    client = AsteroidClient(config = config)
    state = None
    stream = AllAsteroids(client = client, state = state)
    response = stream.records_sync(page_limit = 5)