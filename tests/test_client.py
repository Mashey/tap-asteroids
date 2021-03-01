from tap_asteroids import __version__
import pytest, os 
from tap_asteroids.client import AsteroidClient
from dotenv import load_dotenv

load_dotenv()
config = {
    "apikey": os.getenv('NASA_KEY'),
}

def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.vcr()
def test_get_browse_neos():
    client = AsteroidClient(config=config)
    response = client.get_browse_neos()

    assert 3 == len(response.keys())
    assert 'links' in response
    assert 'page' in response
    assert 'near_earth_objects' in response

    links = response['links']
    assert 2 == len(links.keys())
    assert 'next' in links
    assert 'self' in links

    page = response['page']
    assert 4 == len(page.keys())
    assert 'size' in page
    assert 'total_elements' in page
    assert 'total_pages' in page
    assert 'number' in page

    for near_earth_object in response['near_earth_objects']:
        assert 13 == len(near_earth_object.keys())
        assert 'links' in near_earth_object
        assert 'id' in near_earth_object
        assert 'neo_reference_id' in near_earth_object
        assert 'name' in near_earth_object
        assert 'name_limited' in near_earth_object
        assert 'designation' in near_earth_object
        assert 'nasa_jpl_url' in near_earth_object
        assert 'absolute_magnitude_h' in near_earth_object
        assert 'estimated_diameter' in near_earth_object
        assert 'is_potentially_hazardous_asteroid' in near_earth_object
        assert 'close_approach_data' in near_earth_object
        assert 'orbital_data' in near_earth_object
        assert 'is_sentry_object' in near_earth_object

        links = near_earth_object['links']
        assert 1 == len(links.keys())
        assert 'self' in links
        
        estimated_diameter = near_earth_object['estimated_diameter']
        assert 4 == len(estimated_diameter.keys())
        assert 'kilometers' in estimated_diameter
        assert 'meters' in estimated_diameter
        assert 'miles' in estimated_diameter
        assert 'feet' in estimated_diameter

        kilometers = estimated_diameter['meters']
        assert 2 == len(kilometers.keys())
        assert "estimated_diameter_min" in kilometers
        assert "estimated_diameter_max" in kilometers

        meters = estimated_diameter['meters']
        assert 2 == len(meters.keys())
        assert "estimated_diameter_min" in meters
        assert "estimated_diameter_max" in meters

        miles = estimated_diameter['miles']
        assert 2 == len(miles.keys())
        assert "estimated_diameter_min" in miles
        assert "estimated_diameter_max" in miles

        feet = estimated_diameter['feet']
        assert 2 == len(feet.keys())
        assert "estimated_diameter_min" in feet
        assert "estimated_diameter_max" in feet


        orbital_data = near_earth_object['orbital_data']
        assert 23 == len(orbital_data.keys())
        assert 'orbit_id' in orbital_data
        assert 'orbit_determination_date' in orbital_data
        assert 'first_observation_date' in orbital_data
        assert 'last_observation_date' in orbital_data
        assert 'data_arc_in_days' in orbital_data
        assert 'observations_used' in orbital_data
        assert 'orbit_uncertainty' in orbital_data
        assert 'minimum_orbit_intersection' in orbital_data
        assert 'jupiter_tisserand_invariant' in orbital_data
        assert 'epoch_osculation' in orbital_data
        assert 'eccentricity' in orbital_data
        assert 'semi_major_axis' in orbital_data
        assert 'inclination' in orbital_data
        assert 'ascending_node_longitude' in orbital_data
        assert 'orbital_period' in orbital_data
        assert 'perihelion_distance' in orbital_data
        assert 'perihelion_argument' in orbital_data
        assert 'aphelion_distance' in orbital_data
        assert 'perihelion_time' in orbital_data
        assert 'mean_anomaly' in orbital_data
        assert 'mean_motion' in orbital_data
        assert 'equinox' in orbital_data
        assert 'orbit_class' in orbital_data
        
        orbit_class = orbital_data['orbit_class']
        assert 3 == len(orbit_class.keys())
        assert 'orbit_class_type' in orbit_class
        assert 'orbit_class_range' in orbit_class
        assert 'orbit_class_description' in orbit_class

        for close_approach_data in near_earth_object['close_approach_data']:
            assert 6 == len(close_approach_data.keys())
            assert 'close_approach_date' in close_approach_data
            assert 'close_approach_date_full' in close_approach_data
            assert 'epoch_date_close_approach' in close_approach_data
            assert 'relative_velocity' in close_approach_data
            assert 'miss_distance' in close_approach_data
            assert 'orbiting_body' in close_approach_data

            relative_velocity = close_approach_data['relative_velocity']
            assert 3 == len(relative_velocity.keys())
            assert 'kilometers_per_hour' in relative_velocity
            assert 'kilometers_per_second' in relative_velocity
            assert 'miles_per_hour' in relative_velocity

            miss_distance = close_approach_data['miss_distance']
            assert 4 == len(miss_distance.keys())
            assert 'astronomical' in miss_distance
            assert 'kilometers' in miss_distance
            assert 'lunar' in miss_distance
            assert 'miles' in miss_distance


@pytest.mark.vcr()
def test_get_feed_neos():
    client = AsteroidClient(config=config)
    start_date = '2020-01-01'
    end_date = '2020-01-08'
    response = client.get_feed_neos(start_date, end_date)

    assert 3 == len(response.keys())
    assert 'links' in response
    assert 'element_count' in response
    assert 'near_earth_objects' in response

    links = response['links']
    assert 3 == len(links.keys())
    assert 'next' in links
    assert 'prev' in links
    assert 'self' in links

    near_earth_objects = response['near_earth_objects']
    for date_key, value in near_earth_objects.items():
        for near_earth_object in value:
            assert 10 == len(near_earth_object.keys())
            assert 'absolute_magnitude_h' in near_earth_object
            assert 'close_approach_data' in near_earth_object
            assert 'estimated_diameter' in near_earth_object
            assert 'id' in near_earth_object
            assert 'is_potentially_hazardous_asteroid' in near_earth_object
            assert 'is_sentry_object' in near_earth_object
            assert 'links' in near_earth_object
            assert 'name' in near_earth_object
            assert 'nasa_jpl_url' in near_earth_object
            assert 'neo_reference_id' in near_earth_object

            close_approach_data = near_earth_object['close_approach_data']
            for data in close_approach_data:
                assert 'close_approach_date' in data
                assert 'close_approach_date_full' in data
                assert 'epoch_date_close_approach' in data
                assert 'miss_distance' in data
                assert 'orbiting_body' in data
                assert 'relative_velocity' in data

                miss_distance = data['miss_distance']
                assert 4 == len(miss_distance.keys())
                assert 'astronomical' in miss_distance
                assert 'kilometers' in miss_distance
                assert 'lunar' in miss_distance
                assert 'miles' in miss_distance

            estimated_diameter = near_earth_object['estimated_diameter']
            assert 4 == len(estimated_diameter.keys())
            assert 'kilometers' in estimated_diameter
            assert 'meters' in estimated_diameter
            assert 'miles' in estimated_diameter
            assert 'feet' in estimated_diameter

            links = near_earth_object['links']
            assert 1 == len(links.keys())
            assert 'self' in links