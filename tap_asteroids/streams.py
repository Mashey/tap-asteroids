import singer 
import datetime, calendar, math, json

LOGGER = singer.get_logger()

class Stream:
    tap_stream_id           = None
    key_properties          = []
    replication_method      = ''
    valid_replication_keys  = []
    replication_key         = 'last_updated_at'
    object_type             = ''
    selected                = True

    def __init__(self, client, state):
        self.client = client
        self.state = state 
    
    def sync(self, *args, **kwargs):
        raise NotImplementedError("Sync of child class not implemented")

class CatalogStream(Stream):
    replication_method: 'INCREMENTAL'

class FullTableStream(Stream):
    replication_method: 'FULL_TABLE'

class AllAsteroids(CatalogStream):
    tap_stream_id = 'all_asteroids'
    key_properties = ['ID']
    object_type = 'Asteroids'

    def records_sync(self, page_limit = None):
        nasa_data = self.client.get_browse_neos()
        nasa_pages = nasa_data['page']['total_pages']
        total_pages = page_limit if page_limit and nasa_pages > page_limit else nasa_pages

        for page in range(total_pages):
            nasa_data = self.client.get_browse_neos(page)

            for asteroid in nasa_data['near_earth_objects']:
                yield asteroid        


STREAMS = {
    'all_asteroids': AllAsteroids,
}