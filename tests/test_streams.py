# from tap_asteroids import __version__
# import pytest, os 
# from tap_asteroids.streams import BrowseNeos, FeedNeos
# from tap_asteroids.client import AsteroidClient
# from dotenv import load_dotenv

# load_dotenv()
# config = {
#     "apikey": os.getenv('NASA_KEY'),
# }

# def test_version():
#     assert __version__ == '0.1.0'


# # @pytest.mark.vcr()
# def test_get_all_asteroids():
#     client = AsteroidClient(config=config)
#     state = None
#     stream = BrowseNewos(client=client, state=state)
#     response = stream.get_all_asteroids(page_num=1)
#     breakpoint()

#     assert 3 == len(response.keys())