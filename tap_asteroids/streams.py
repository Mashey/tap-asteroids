import singer 
from singer import bookmarks
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
    replication_key = 'record_count'

    def records_sync(self, page_limit = None):
        start_time = singer.get_bookmark(self.state, self.tap_stream_id, self.replication_key)

        if start_time == None:
            start_time = '2021/01/01 00:00:00'

        LOGGER.info('Generating Record')

        nasa_data = self.client.get_browse_neos()
        nasa_pages = nasa_data['page']['total_pages']
        total_pages = page_limit if page_limit and nasa_pages > page_limit else nasa_pages
        record_count = 0


        for page in range(total_pages):
            nasa_data = self.client.get_browse_neos(page)

            for asteroid in nasa_data['near_earth_objects']:
                record_count += 1
                singer.write_bookmark(self.state, self.tap_stream_id, self.replication_key, record_count)
                singer.write_state(self.state)
                yield asteroid



STREAMS = {
    'all_asteroids': AllAsteroids,
}
