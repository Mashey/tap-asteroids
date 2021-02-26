from tap_asteroids import __version__
import pytest, os 
from tap_asteroids.client import AsteroidClient
from dotenv import load_dotenv

load_dotenv()
config = {
    "apikey": os.getenv('NASA_KEY'),
}

def test_version():
    assert __version__ == '0.1.0'

def test_get_browse_neos():
    client = AsteroidClient(config=config)
    data = client.get_browse_neos()
    breakpoint()    