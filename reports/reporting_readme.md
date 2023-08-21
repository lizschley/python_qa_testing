# Reporting Folder

The python-qa-testing-app can produce all sorts of reports, but we will describe three types of reports that are relatively simple:

## Built-in JSON reporting

The built-in reporting is designed to use dictionary data from the the json that is returned by a given request.  In addition to trouble-shooting, reports like this can be used to retrieve test data from any available api.  There are three phases:

### Set Up

1. Set-up the path in the report/folder-name file structure
2. In order to interact with the file structure, programmatically, we use constants/report_paths.py
   * The method to write the report, takes the folder name or actually any string as a key
   * The filename is also an input parameter
   * The key that is passed in to the method, is used to look up the file path
3. Then you write the file, right after receiving the response.  If you use the support/basic_response.py to wrap your request, for example:

    ```Python
        quote_response = BasicResponse(quote_service.add_quotes(good_input))
        quote_response.write_to_file(filename, 'example')
    ```

    This method of reporting is also discussed in ```support/support_readme.md```
4. In the past, reporting was often used to find test data from third-party applications or other micro-services.  In this case, the tests would not be used as regression tests, but have a special tag or the methods would be called as part of a test that needed the valid data in order to test

### Writing the report

The testing step that runs the above method, calls another method,  ```write_to_file(filename, key)``` which is associated with a specific response when it is wrapped in the BasicResponse class (see the ```support/basic_response.py``` file).

Using the key ```example```, Python will look up the filepath in the constants/report_paths.py file. The example key will give you ```reports/example``` as the filepath. It will then write the dictionary saved from the response to the specified file.

If you run the tests with an @example tag, you can see an example of this.  It is also an example of how easy it is to to a random third-party app, so there is a chance that the link will stop working.  **NOTE -** if you do this remember to delete the report!

### Deleting the report

This is not often appropriate data to save in github, so we want to delete this type of report. There is a utility for this: ```utilities/delete_pickles.py```

The file has a lot of documentation and also ```utilities/utilities_readme.md``` gives more information.

## Allure reports

If you set this up according to the directions, you should have the packages needed to implement Allure reporting.

### Setup

Assuming you are running the reports in VSCode using the provided ```.vscode/launch.json```, use the following arguments:

```Json

    "args": [
        "-f",
        "allure_behave.formatter:AllureFormatter",
        "-o",
        "reports/allure",
        "--tags",
        //"testing"
        "regression"
        //"example"
        //"-i",
        //"features/datetime_unittest.feature"
    ]
```

This will produce a lot of json files in the ```reports/allure directory```

### See the Reports

```bash

% allure serve reports/allure

```

This will open a web page that will offer all sorts of interesting views of the reports.

The json files can be deployed anywhere you want, if you know how you want it and how to make it happen.

### Done with Allure

* You'll want to delete the Allure JSON files unless you have some sort of plan
* If you have a plan to use these reports historically, you should develop a system to move the Allure JSON out of your development space
* To stop the service from running on your local machine, enter CTRL-C in your terminal window

## After Scenario, Feature, or entire test run

This test suite does not currently have an example of this, but it is easy to setup using the following pieces:

### Set up

Use the before_all, before_feature, after_all, after_feature and any of the other hooks offered by behave.

* Collect the data that you want when you want it, using constants set up to be available at the level that you will write the report at.

  * For example if you want to write a report after the entire test run collecing the times for all the tests
  * Set up data storage in the before_all section of ```features/environment.py```, such as context.all_test_level = {}

* Within each scenario add the data specific to that scenario.  This can be as simple or complex as you need.  The following is a simple example that would come at the end of the test

    ```context.all_test_level['unique_scenario_key'] = {'scenario time': time}```

### Write the report

For the above example, initiate writing the report in the after_all section of ```features/environment.py```

* You will want the actual code to live in a helper file, such as ```helpers/environment_helper.py```
* You can use the ```utilities/json_methods.py``` for methods that will help with writing .json files
* You can write any type of file that you want: html, csv or text files, so you are not limited, if you want to do something different.
* If you want a running record, you may WANT to share the file in Github

Lots of flexibility and possibilities
