Feature: Show External Application with location id within Charlottesville

    @example
    Scenario: Using the Charlottesville location key you can get Charlottesville or Richmond in the results
        Given you use the maximum of both radius and limit and a Charlottesville location id
        Then you can get Richmond in the result if you use a minimum population of 100000
