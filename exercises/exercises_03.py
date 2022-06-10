import requests
import uuid

# Exercise 3.1
# Create a function create_post() that returns an
# object that follows this structure:
# {
#     "title": "The title of my new post",
#     "body": "A very long string containing the body of my new post",
#     "userId": 1
# }
unique_number = str(uuid.uuid4())

def create_json_object():
    return {
        "title": "The title of my new post",
        "body": "A very long string containing the body of my new post",
        "userId": unique_number 
    }

# Exercise 3.2
# Write a test that POSTs the object created in 3.1
# as JSON to https://jsonplaceholder.typicode.com/posts
# and checks that the response status code is 201
# and that the new post id returned by the API is an integer
# Use the isinstance(variable, type) function for this (Google is your friend!)
def test_post_json_object():
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=create_json_object())
    assert response.status_code == 201
    response_dict = response.json()
    response_id = response_dict['id']
    assert isinstance(response_id, int) is True
    

# Exercise 3.3
# Create a function create_billpay_for(name) that takes
# an argument of type string containing a name and returns
# an object that follows this structure:
# {
#   "name": <value of the name>,
#   "address": {
#     "street": "My street",
#     "city": "My city",
#     "state": "My state",
#     "zipCode": "90210"
#   },
#   "phoneNumber": "0123456789",
#   "accountNumber": 12345
# }
def create_billpay(name):
    return {
   "name": name,
   "address": {
     "street": "My street",
     "city": "My city",
     "state": "My state",
     "zipCode": "90210"
   },
   "phoneNumber": "0123456789",
   "accountNumber": 12345
 }


# Exercise 3.4
# Write a test that POSTs the object created in 3.3 to
# https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500
# Supply a name of your own choice to the create_billpay_for() method
# Make sure that the request header 'Accept' has value 'application/json' (Google ;)
# Check that the response status code is 200 and
# that the response body element 'payeeName' equals the name supplied to the method
def test_post_object_request():
    response = requests.post('https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500', json=create_billpay('faroje'), headers={"Accept":"application/json"})
    assert response.status_code == 200
    