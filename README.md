# python-qa-testing-app

This test suite is for learning purposes.  It tests a spring boot application which can be found [here](https://github.com/lizschley/spring-qa-testing-app).  Follow the instructions in the README for setup.

Once you have the repository on your local machine, you need to make sure Python is installed (version 3.10.11) and is the version you get when you type the following:

```% Python --version```  in the base directory (~/your_path/python_qa_testing).

## Step 1 - Pull down data from Github

The recommended method for cloning a repository is via ssh. Here is a [link with prerequisites](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)

   1. On the [repository home page](https://github.com/lizschley/spring-qa-testing-app) there is green code button to get the url
   2. Click the green Code button
   3. Make sure you get the ssh option (click pages image to copy url)
   4. Open your terminal in VScode and cd to the directory where your code will live
      ```% cd ".../path/to/directory"```

   5. Once in the directory, enter the following into your terminal
      ```% git clone git@github.com:lizschley/spring-qa-testing-app.git```

## Step 2 - Set up the virtual environment

The following command puts the virtual environment in a directory called virtual_environments in your home folder.  It names the virtual environnent python-testing. Change this however you want.

```% python -m venv ~/virtual_environments/python-testing```

Start the virtual environment:

```% source ~/virtual_environments/python-testing/bin/activate```

Install the necessary packages:

```% pip install -r requirements.txt```

Once that is completed, select the python interpretor

   1. Select the gear in the bottom left corner of VSCode
   2. Command Palette
   3. Type Python: Select Interpretor
       * For venv it needs to be the path to python.exe
       * For Conda, it can be the path to the virtual environment, because Conda manages your python and pip versions

## Step 3 - Setting up the environment variables

1. Making sure to stay in the base directory, copy the example.env to .env
2. If you have a windows, change the ENVIRONMENT_KEY from local_mac to local_windows
3. If you are interested in exploring the existing report or external apis, do the following:
   * Sign up here: [Rapid API](https://rapidapi.com/auth?referral=/arupsarkar/api/login-signup/discussions).
   * It is free, so it gives you a glimpse of wonderful things
   * But it also gives you a host and a key to use in the one test with its example report

## Step 4 - Running the tests

This assumes that you have followed Step 2 in the readme of the [spring-qa-testing-app](https://github.com/lizschley/spring-qa-testing-app)

**Note 1** - If you do not have spring-qa-testing-app running you can run the date_diff tag, instead of regression.  These are unit tests and do not require an external api.

**Note 2** - It is also possible to uncomment "example" instead of "regression", but this requires a host and a key [Rapid API](https://rapidapi.com/auth?referral=/arupsarkar/api/login-signup/discussions) for authentication.

   1. Run the spring-qa-testing-app application
   2. Open ```.vscode/launch.json``` in this repository
   3. In "args", make sure that "--tags" and "regression" are not commented

      ```list
      "args": [
         // "-f",
         // "allure_behave.formatter:AllureFormatter",
         // "-o",
         // "reports/allure",
         "--tags",
         //"testing",
         "regression",
         // "example",
         // "-i",
         // "features/datetime_unittest.feature"
      ]
      ```

   4. Click the Run and Debug button on the lefthand side of VSCode.
      * You will be given the option to run Python: Behave current file. This uses the .vscode/launch.json to control the tests.
      * It gives great debug options
      * To debug a particular test
        * Give the scenario (in the feature file) the *testing tag
        * Open the corresponding step definition
        * Click to the left of the line number; this is a breakpoint.
          * You can put as many as you want
          * Try to put it at the exact line or a little before the error happens
        * Comment the regression tag and uncomment the testing tag
        * Run the tests as specified above
        * If you have put the breakpoint in a good location, processing will stop and you can find out information
          * Go to the debug console
          * At the bottom you can enter python code to see any variable you want or run some python at the command line
          * There are also buttons (see down arrows, etc at the top of the screen) to step through the code
          * Explore how this works; it will save you a ton of time in finding the root cause of errors

## Step 5 - Explore Additional Functionality

### Helpers 

This folder is for common methods. Please see ```helpers/helpers_readme.md``` for more information.

### Services

The services make accessing new endpoints, application or microservices standard and efficient. Please see ```services/services_readme.md``` for more information.

### Reports

**Note** - more information in the Reports ReadMe: ```reports/reporting_readme.md```

There is built-in support for two types of reporting:

   1. Allure reports
   2. Json response data that is returned from http requests
      * Can be used for collecting test data needed in tests
      * Can be used for test evidence

The framework also supports reports that are run at the end of the test run, feature or scenario

### Support

These are resuable classes for requests and responses. Understanding and using these add flexibility and speed to automated tests.  Please see ```support/support_readme.md``` for additional information.

### Utilities

These are previously useful methods that save a lot of time.  Please see ```utilities/utilities_readme.md``` for more information.
