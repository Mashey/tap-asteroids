from tap_asteroids import __version__
import pytest, os 
from tap_asteroids.client import AsteroidClient

def test_version():
    assert __version__ == '0.1.0'


def test_get_browse_neos():
    client = AsteroidClient()
    data = client.get_browse_neos()
    breakpoint()    