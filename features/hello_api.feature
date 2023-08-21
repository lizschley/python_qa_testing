Feature: Hello API

    @hello @regression
    Scenario Outline: Test the Hello API
        Given the hello url is called using <name>
        Then the return will be hello plus <name> with default becoming Hello World
        Examples:
        | name    |
        | default |
        | Ninja   |
        | Ronin   |
