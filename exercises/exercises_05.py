from tkinter import N
import xml.etree.ElementTree as et
import requests


# Exercise 5.1
# Write a test that does the following:
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/accounts/12345
# Parse the response into an XML ElementTree
# Check that the root element name is 'account'
# Check that the root element has no attributes
# Check that the root element has no text
def test_xml_response():
    response = requests.get('http://parabank.parasoft.com/parabank/services/bank/accounts/12345')
    response_body_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_xml)
    root = xml_tree.getroot()
    assert root.tag == 'account'
    assert len(root.attrib) == 0
    assert root.text is None

# Exercise 5.2
# Write a test that does the following
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/accounts/12345
# Parse the response into an XML ElementTree
# Find the customerId element in the tree
# Check that the text of the customerId element is '12212'
def test_xml_response_and_element():
    response = requests.get('http://parabank.parasoft.com/parabank/services/bank/accounts/12345')
    response_body_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_xml)
    customer_id = xml_tree.find('customerId')
    assert customer_id.text == '12212'

# Exercise 5.3
# Write a test that does the following
# Perform a GET to http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts
# Parse the response into an XML ElementTree
# Find all 'account' elements in the entire XML document
# Check that there are more than 5 of these 'account' elements
def test_xml_response_and_elements_length():
    response = requests.get('http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts')
    response_body_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_xml)
    account_elements = xml_tree.findall(".//account/*")
    assert len(account_elements) > 5

# Exercise 5.4
# Repeat Exercise 5.3, but now check that:
# - at least one of the accounts is of type 'SAVINGS' (Google!)
# - there is no account that has a customerId that is not equal to 12212
#   (Use your creativity with the last one here... There is a solution, but I couldn't
#    find it on Google.)
def test_using_xpath_to_check_for_elements():
    response = requests.get(
        "http://parabank.parasoft.com/parabank/services/bank/customers/12212/accounts"
    )
    response_body_as_xml = et.fromstring(response.content)
    xml_tree = et.ElementTree(response_body_as_xml)
    savings_accounts = xml_tree.findall(".//account/type[.='SAVINGS']")
    assert len(savings_accounts) > 1
    accounts_with_customerId12 = xml_tree.findall(
        ".//account/customerId[.='12212']"
    )
    all_customerIds = xml_tree.findall(".//account/customerId")
    assert len(accounts_with_customerId12) == len(all_customerIds)