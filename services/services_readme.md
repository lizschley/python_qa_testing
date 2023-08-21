# Services Folder

Services as they are used here, can be any thing that you need. By inheriting the support/base_api.py it becomes extremely easy to set up a new endpoint.

## Hello Service is easiest example

1. See how the service is called in the test: step_definitions/hello_api_test.py
2. The service itself is set up in services/hello_service.py
3. To create a new endpoint, simply create a method that defines the necessary data

## external api test tests an external api

1. services/example_external_service.py is an example of an external api that works currently
2. It has a url and authentication which is set up before any tests are run (see features/environment.py and helpers/environment_helper.py)
3. It requires a host and a key, which you can get by signing up or by asking someone who has signed up.
4. You need to specify the details in the environment_helper.py
5. The usage example is in the test: step_definitions/quote_api_test.py.

## We also have example token authentication documented in comments

1. This is not working, but is documented here: services/example_authentication_service.py
2. See also features/environment.py and helpers/environment_helper.py
3. Generally you set it up when initiating the service
   * Save and pass in the auth key to the setHeaders() method that is a required method for each service (services/hello_service.py)  See documentation in the setHeaders() method
   * setHeaders() is run when the service is initiated, but it can be over-written if necessary in any endpoint
4. setUrl() must be run for each endpoint (all working services have an example of this)
5. Note - this could be totally different based on the given project

## When a service is initiated

1. The initial method for any service always assigns the environment that is specified
   * It uses data that is specific to a given application (code base can have many applications or just one).
     * Usually an application has a specific base_url, which also varies by environment (local, integration, qa etc)
     * Operating systems may also differences in environment details
   * This is unnecessary if you have one application and only run the tests in one environment.
     * But setting up the data in one place does not make it harder to set up, even if you do not need the complexity:
       * Put the information in the ```helpers/environment_helper.py``` in a method that is easily called.
       * Assign the environment information in the before_all method in ```features/environment.py``` by calling the correct method.
   * The idea is to set this up in the beginning and just use it afterwards. It makes everything much easier to maintain.
2. Usually you can call the setHeaders() method when the Service is initiated.  It you need something special for a certain endpoint you can set the headers in the actual endpoint code

## Service definition here vs Service Definition in AAP Microservices

1. For the code we developed for AAP a given service was part of a community of services, each with the same base_url
2. Each service had a different base_route
3. Then each endpoint had a different end route and data
4. To see how to set up an endpoint, look in any of the services
