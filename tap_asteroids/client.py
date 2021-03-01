import json
import requests
import os

class AsteroidClient:
    BASE_URL = 'https://api.nasa.gov/neo/rest/v1'

    def __init__(self, config):
        self.api_key = config['api_key']

    def get_browse_neos(self, page_num = 0):
        url = f'{self.BASE_URL}/neo/browse?api_key={self.api_key}&page={page_num}'
        return requests.get(url).json()