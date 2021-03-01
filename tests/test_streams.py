from tap_asteroids import __version__
import pytest, os 
from tap_asteroids.streams import BrowseNeos, FeedNeos
from tap_asteroids.client import AsteroidClient
from dotenv import load_dotenv

load_dotenv()
config = {
    "apikey": os.getenv('NASA_KEY'),
}

def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.vcr()
def test_get_all_asteroids():
    client = AsteroidClient(config = config)
    state = None
    stream = BrowseNeos(client = client, state = state)
    response = stream.get_all_asteroids(page_limit = 5)
    
    assert 100 == len(response['near_earth_objects'])

    asteroid = response['near_earth_objects'][0]
    assert 'links' in asteroid
    assert 'id' in asteroid
    assert 'neo_reference_id' in asteroid
    assert 'name' in asteroid
    assert 'name_limited' in asteroid
    assert 'designation' in asteroid
    assert 'nasa_jpl_url' in asteroid
    assert 'absolute_magnitude_h' in asteroid
    assert 'estimated_diameter' in asteroid
    assert 'is_potentially_hazardous_asteroid' in asteroid
    assert 'close_approach_data' in asteroid
    assert 'orbital_data' in asteroid
    assert 'is_sentry_object' in asteroid

@pytest.mark.vcr()
def test_get_1month_asteroids():
    client = AsteroidClient(config = config)
    state = None 
    stream = FeedNeos(client = client, state = state)
    response = stream.get_1month_asteroids('2020-01')

    assert 'month' in response
    assert 'element_count' in response 
    assert 'near_earth_objects' in response