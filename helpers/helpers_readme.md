# Helpers Folder

Here is where often used code is stored. This is one way remain DRY ("Don't repeat yourself"), a basic principle of software development. In this way, you can write the code once, work out any bugs, and reuse it many times.  For the following reasons, the code base is more maintainable:

1. If the methods are named well, the code becomes self-documenting, thus easier to understand and maintain.
2. If something changes, it only needs to be updated in one place
3. It saves time and lowers frustration

## environment_helper.py

This is used in conjunction with the features/environment.py to do different things at different stages of the test cycle.

For example, we have made it so reports will work equally as well for Windows and Macs, even though there some differences.

You can also add urls for third party applications, if you need them to get test data, either for input to apis or to ensure that the update you did actually made the change you expected. (Note - I have an example report and third party application, called rapidAPI that I use to illustrate this)

You can also have separate urls for different stages, such as development, integration, UAT or even, at times, production.  If you are working with third party applications, the third party may also have different urls for the various environments.

It is possible to also create after-feature reports or even reports with data you collected throughout the test run.

It is impossible to know future needs, but this system is extremely flexible and valuable to maintain.
