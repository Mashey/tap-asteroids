import pytest, os, json
from tap_asteroids.streams import AllAsteroids
from tap_asteroids.client import AsteroidClient
from unittest.mock import MagicMock

from dotenv import load_dotenv

load_dotenv()
config = {
    "api_key": os.getenv('api_key'),
}

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
        assert 'bookmarks' in state['value']
        currently_syncing = state['value']['currently_syncing'] 
        assert 'all_asteroids' == currently_syncing or None == currently_syncing

    # for record in records: 
    #     x = 'test' 'xyz'
    #     assert 'type' in record 
    #     assert 'stream' in record 
    #     assert 'record' in record
    #     breakpoint()
    # for obj in test_list: 
    #     # if obj['type'] == 
    #     breakpoint()