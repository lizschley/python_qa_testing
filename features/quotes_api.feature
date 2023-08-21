Feature: Test Person and Quotes API

    @regression
    Scenario: client makes call to GET existing quotes
        Given the client makes a call to get all existing quotes
        And get all existing quotes is successful
        Then the client gets a sorted array containing the correct number of quotes
        And a new person will get sorted correctly
        And the new person must be deleted so Jane Austen can be number one

    @regression
    Scenario: system does a uniqueness check before a new user is saved
        Given json string input having a new id with existing name and dates
        Then the database will throw data integrity violation exception
        And the transaction will roll back and the new record will not be created

    @regression
    Scenario: add new person with quotes then find by name and then delete all added data
        Given the api is called with good data showing a new person and two quotes
        Then it returns the correct number of quotes with a successful return code
        And person and quotes can be retrieved by name and the data will match the input data
        And the new person and their quotes can be deleted by person id

    @regression
    Scenario: the quotes endpoint allows the system to find an existing person and add new quotes
        Given a person found by id has original quotes saved for further use
        And the api is called with good data to add a second quote for the same person
        Then the successful call will show that the total number of quotes has increased by one
        And the person found again by id now has two quotes with one of them matching input data
        And the new quote can be deleted without deleting the person

    @regression
    Scenario: illegal state error --> adding quotes for existing id with non-matching name or date fields
        Given with only a person id a quote can be added but any person data in the input must match db person record
        Then if only one of first or last names or dates field is wrong it will throw an error
        And the existing person will still exist but the numbers of people and quotes will stay the same


    @regression
    Scenario: required field constraint violation --> thrown if required fields are missing, no record created
        Given if name or dates are missing for adding a new person it will throw a missing fields contraint violation
        And find new person by name will return an empty list
        And a missing quote will also send a missing field error
        Then the total number of quotes or people will not decrease or increase


    @regression
    Scenario: required field constraint violation --> this time for quote with missing data for existing person
        Given adding a quote to an existing person will give a missing field error for a blank quote field
        And the total number of quotes or people will not decrease or increase
        And no quote field key will create an index out of bounds error with message that references quote field
        Then the total number of quotes or people will not decrease or increase
