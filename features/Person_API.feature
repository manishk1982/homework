Feature: Validate CRUD methods for Person model object

  Scenario: Validate the POST API for adding a non-existing person
    Given Set API endpoint as "/add"
    And Body with non-existing person details
    When Send a POST HTTP request
    Then Receive status "True" and Response message as "Person created successfully"

  Scenario: Validate the POST API for adding an existing person
    Given Set API endpoint as "/add"
    And Body with existing person details
    When Send a POST HTTP request
    Then Receive status "False" and Response message as "Person Already Exists"


  Scenario: Validate the GET API for deleting an existing person
    Given Set API endpoint as "/4/delete"
    When Send a GET HTTP request
    Then Receive status "True" and Response message as "Person deleted successfully"

  Scenario: Validate the GET API for deleting a non-existing person
    Given Set API endpoint as "/9876/delete"
    When Send a GET HTTP request
    Then Receive status "False" and Response message as "Person Doesn't Exists"


  Scenario: Validate the GET API to fetch details of an existing person
    Given Set API endpoint as "/2/get"
    When Send a GET HTTP request
    Then Receive response as "not null"
    And  valid Person object

  Scenario: Validate the GET API to fetch details of a non-existing person
    Given Set API endpoint as "/9899/get"
    When Send a GET HTTP request
    Then Receive response as "null"


  Scenario: Validate the GET API to fetch dummy person details
    Given Set API endpoint as "/9874/getDummy"
    When Send a GET HTTP request
    Then Receive response as "not null"
    And valid Person object
    And valid dummy values


  Scenario: Validate the GET API to fetch all person details
    Given Set API endpoint as "/getAll"
    When Send a GET HTTP request
    Then validate response for all Person object
