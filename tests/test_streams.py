import pytest, os, json, os.path
from os import path
from tap_asteroids.streams import AllAsteroids
from tap_asteroids.client import AsteroidClient
from unittest.mock import MagicMock

from dotenv import load_dotenv

load_dotenv()
config = {
    "api_key": os.getenv('api_key'),
}

if not path.isfile('test.json'): 
    os.system("python3 -m tap_asteroids.__init__ -c config.json -s state.json --catalog catalog.json > test.json")

def test_records_and_state_from_test_json():
    records = []
    states = []

    with open('test.json') as test_json:
        for json_obj in test_json:
            json_item = json.loads(json_obj)
            if json_item['type'] == 'STATE': states.append(json_item)
            if json_item['type'] == 'RECORD': records.append(json_item)
            if json_item['type'] == 'SCHEMA': schema = json_item

    for state in states:
        assert state['type'] == 'STATE'
        assert 'value' in state 
        assert 'currently_syncing' in state['value']
        if len(state['value'].keys()) > 1:
            assert 'bookmarks' in state['value']
            bookmarks = state['value']['bookmarks']
            assert 'all_asteroids' in bookmarks
            assert 'record_count' in bookmarks['all_asteroids']

    for record in records: 
        assert 'type' in record 
        assert 'stream' in record 
        assert 'record' in record

        assert record['stream'] == 'all_asteroids'

        assert 'links' in record['record']
        assert 'id' in record['record']
        assert 'neo_reference_id' in record['record']
        assert 'name' in record['record']
        assert 'name_limited' in record['record']
        assert 'designation' in record['record']
        assert 'nasa_jpl_url' in record['record']
        assert 'absolute_magnitude_h' in record['record']
        assert 'estimated_diameter' in record['record']
        assert 'is_potentially_hazardous_asteroid' in record['record']
        assert 'close_approach_data' in record['record']
        assert 'orbital_data' in record['record']
        assert 'is_sentry_object' in record['record']
