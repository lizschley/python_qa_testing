# Support Folder

These are base objects that are both variable, yet have consistent features that always need to be available. The request and response objects are the two base objects in this code base.  Using base objects makes the code easier to maintain (please read about DRY in helpers_readme.md).

## support/base_api.py

The ABC in the class name for the BaseApi class indicates that this the base object can not be used by itself.  It must be inherited.  Each service inherits the base api object and then instantiates its own setHeaders() method and its own setUrl() method.  You make these any pattern that you need.  You can see two different working patterns in services/example_external_service.py and services/quote_service.py.

services/example_authentication_service.py is not working, but you can get a sense of how it works, by reading the code and comments.  The idea is that once you used whatever secrets were required, that it would produce an auth key which can be passed into the setHeaders() method for any service that accepts that authentication token.

## support/basic_response.py

1. This was created to make the returned data easier to access and also more robust.
   * The status_code is basically the same as in the original response
   * Error messages are accessed in a consistent manner without having to repeat code.
   * Built in reports are easily implemented
      * An example uses the ***example tag** to run the test
      * In addition to the assersions, the code (see ```step_definitions/external_api_test.py```, the method: ```run_rapidapi_and_check_results(context)```) will automatically write the returned json to file
      * This is helpful in understanding intermittent failures or if you just need the information in written form for test evidence
      * This method of reporting is also discussed in ```reports/reporting_readme.md```
2. The results can also be stored in the context, at whatever level is needed, in order to compile reports for end of feature, test-run statistics or general information
