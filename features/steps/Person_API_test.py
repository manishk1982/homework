# Test steps file for validating the Person API code
from behave import *
import requests
# import random

BASE_URL = "http://127.0.0.1:5000"
fields = ['_person_id', '_name', '_age']
dummy_person = {'_person_id': 9874, '_name': "Dummy", '_age': 99}


@given('Set API endpoint as "{endpoint}"')
def step_impl(context, endpoint):
    context.url = f'{BASE_URL}{endpoint}'


@given('Body with non-existing person details')
def step_impl(context):
    person_dict = dict()
    # We can use random generator for the ID. For now to ensure BDD test works successfully, below is commented
    # person_dict['id'] = random.randint(600, 800)
    person_dict['id'] = 2
    person_dict['name'] = "Manish"
    person_dict['age'] = 40
    context.payload = person_dict


@given('Body with existing person details')
def step_impl(context):
    person_dict = dict()
    person_dict['id'] = 2
    person_dict['name'] = "Manish"
    person_dict['age'] = 8
    context.payload = person_dict


@when('Send a POST HTTP request')
def step_impl(context):
    response = requests.post(context.url, data=context.payload)
    context.resp = response.json()


@when('Send a GET HTTP request')
def step_impl(context):
    response = requests.get(context.url)
    context.resp = response.json()


@then('Receive status "{status}" and Response message as "{message}"')
def step_impl(context, status, message):
    status = convert_status_to_bool(status)

    assert context.resp["_status"] is status,\
        f'Response Status -- Expected: {status}, Actual: {context.resp["_status"]}'
    assert context.resp["_message"] == message,\
        f'Response Message -- Expected: {message}, Actual: {context.resp["_message"]}'


@then('Receive response as "{result}"')
def step_impl(context, result):
    if result == "null":
        assert context.resp == [], f'Return Value -- Expected: {result}, Actual: {context.resp}'
    elif result == "not null":
        assert context.resp != [], f'Return Value -- Expected: {result}, Actual: {context.resp}'
    else:
        assert False, "Got invalid expected return value"


@then('valid Person object')
def step_impl(context):
    validate_person_object(context.resp)


@then('valid dummy values')
def step_impl(context):
    for field in fields:
        assert context.resp[field] == dummy_person[field],\
            f'"{field}" value -- Expected: {dummy_person[field]}, Actual: {context.resp[field]}'


@then('validate response for all Person object')
def step_impl(context):
    assert len(context.resp) != 0, "No person record found!!!"

    for person in context.resp:
        # Validate each object has all required fields
        validate_person_object(person)

        # Alternatively we should implement how to re-use an existing @then - as an efficient solution
        # Something like below
        # context.execute_steps('valid Person object')


def convert_status_to_bool(status):
    """ Function to convert string status to boolean
    """

    if status.lower() == "true":
        status = True
    elif status.lower() == "false":
        status = False
    else:
        raise Exception
    return status


def validate_person_object(person):
    """ Function to validate if the input is a valid person object i.e. has all 3 fields
    """

    for field in fields:
        assert field in person.keys(), f'"{field}" missing in the Person object'
