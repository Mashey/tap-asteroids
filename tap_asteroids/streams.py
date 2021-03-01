import singer 
import datetime, calendar, math, json

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

    def get_all_asteroids(self, page_limit = None):
        nasa_data = self.client.get_browse_neos()
        nasa_pages = nasa_data['page']['total_pages']
        total_pages = page_limit if page_limit and nasa_pages > page_limit else nasa_pages
        results = {'near_earth_objects': []}

        for page in range(total_pages):
            nasa_data = self.client.get_browse_neos(page)

            for asteroid in nasa_data['near_earth_objects']:
                results['near_earth_objects'].append(asteroid)
        
        return results





class FeedNeos(CatalogStream):
    tap_stream_id = 'feed_neos'
    key_properties = ['ID']
    object_type = 'FeedNeos'

    def get_1month_asteroids(self, start_date):
        date_list = start_date.split('-')
        year = int(date_list[0])
        month = int(date_list[1])
        month_days = calendar.monthrange(year, month)[1]
        num_intervals = math.ceil(month_days/7)

        intervals = []

        for i in range(num_intervals):
            start = i * 7 + 1 
            end = start + 6 
            if end > month_days: end = month_days
            start_interval = f'{start_date}-{str(start).zfill(2)}'
            end_interval = f'{start_date}-{str(end).zfill(2)}'
            intervals.append([start_interval, end_interval])
        
        results = {'month': start_date, 'element_count':0, 'near_earth_objects':{}}

        for interval in intervals:
            nasa_data = self.client.get_feed_neos(interval[0], interval[1])
            results['element_count'] += nasa_data['element_count']

            for k, v in nasa_data['near_earth_objects'].items():
                results['near_earth_objects'][k] = v

        return results