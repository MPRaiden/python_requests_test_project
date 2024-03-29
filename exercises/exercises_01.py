import requests


# Exercise 1.1
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response status code equals 200
def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert response.status_code == 200

# Exercise 1.2
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the value of the response header 'Content-Type' equals 'application/json'
def test_get_response_header_value():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert response.headers['Content-Type'] == 'application/json'


# Exercise 1.3
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'country' has a value equal to 'United States'
def test_check_response_body_element_has_value_united_state():
    response = requests.get('http://api.zippopotam.us/us/90210')
    assert response.json()['country'] == 'United States'


# Exercise 1.4
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the first 'place name' element in the list of places
# has a value equal to 'Beverly Hills'
def test_first_place_has_value_beverly_hills():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert response_body['places'][0]['place name'] == 'Beverly Hills'

# Exercise 1.5
# Perform a GET request to http://api.zippopotam.us/us/90210
# Check that the response body element 'places' has an array
# value with a length of 1 (i.e., there's one place that corresponds
# to the US zip code 90210)

def test_response_body_element_places_has_array():
    response = requests.get('http://api.zippopotam.us/us/90210')
    response_body = response.json()
    assert len(response_body['places']) == 1