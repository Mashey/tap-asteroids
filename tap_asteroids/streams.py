import singer 

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

class BrowseNeos(CatalogStream):
    tap_stream_id = 'browse_neos'
    key_properties = ['ID']
    object_type = 'BrowseNeos'

    def get_all_asteroids(page_num = 0):
        pass

class FeedNeos(CatalogStream):
    tap_stream_id = 'feed_neos'
    key_properties = ['ID']
    object_type = 'FeedNeos'

    def get_1month_asteroids(start_date, end_date):
        pass