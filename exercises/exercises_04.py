import requests
import xml.etree.ElementTree as et


# Exercise 4.1
# Create a function create_xml_body_from_string()
# that returns a docstring (with triple double quotes)
# containing the following XML document:
# <payee>
#     <name>John Smith</name>
#     <address>
#         <street>My street</street>
#         <city>My city</city>
#         <state>My state</state>
#         <zipCode>90210</zipCode>
#     </address>
#     <phoneNumber>0123456789</phoneNumber>
#     <accountNumber>12345</accountNumber>
# </payee>

def create_xml_body_from_string():
    return """
    <payee>
     <name>John Smith</name>
     <address>
         <street>My street</street>
         <city>My city</city>
         <state>My state</state>
         <zipCode>90210</zipCode>
     </address>
     <phoneNumber>0123456789</phoneNumber>
     <accountNumber>12345</accountNumber>
    </payee>
    """

# Exercise 4.2
# Write a test that POSTs the object created in 4.1
# to https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500
# Set the request header 'Content-Type' to 'application/xml'
# Then check that the response status code is 200
# and that the value of the response header 'Content-Type' is also equal to 'application/xml'
def test_post_xml_object():
    xml = create_xml_body_from_string()
    response = requests.post('https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500',
    data=xml, headers={"Content-Type":"application/xml"})
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"

# Exercise 4.3
# Write a method create_xml_body_using_elementtree() that returns
# the same request body as in Exercise 4.1, but now uses the
# ElementTree library (I've imported that for you already, it's available as 'et')
# Make your life a little easier by specifying all element values as strings
def create_xml_body_using_elementtree():
    payee = et.Element('payee')
    name = et.SubElement(payee, 'name')
    address = et.SubElement(payee, 'address')
    street = et.SubElement(address, 'street')
    city = et.SubElement(address, 'city')
    state = et.SubElement(address, 'state')
    zipCode = et.SubElement(address, 'zipCode')
    phoneNumber = et.SubElement(payee, 'phoneNumber')
    accountNumber = et.SubElement(payee, 'accountNumber')
    return payee

def test_post_xml_object_with_et():
    xml = create_xml_body_using_elementtree()
    xml_as_string = et.tostring(xml)
    response = requests.post('https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500',
    data=xml_as_string, headers={"Content-Type":"application/xml"})
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"

# Exercise 4.4
# Repeat Exercise 4.2, but now use the XML document created in Exercise 4.3
# Don't forget to convert the XML document to a string before sending it!
def test_post_xml_object_using_et():
    xml = create_xml_body_using_elementtree()
    xml_as_string = et.tostring(xml)
    response = requests.post('https://parabank.parasoft.com/parabank/services/bank/billpay?accountId=12345&amount=500',
    data=xml_as_string, headers={"Content-Type":"application/xml"})
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/xml"