import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()

class AsteroidClient:
    BASE_URL = 'https://api.nasa.gov/neo/rest/v1'
    apikey = os.getenv('NASA_KEY')

    def get_browse_neos(self, page_num = 0):
        url = f'{self.BASE_URL}/neo/browse?api_key={self.apikey}&page={page_num}'
        return requests.get(url).json()

    def get_feed_neos(self, start_date, end_date):
        url = f'{self.BASE_URL}/feed?api_key={self.apikey}&start_date={start_date}&end_date={end_date}'
        return requests.get(url).json()
