Feature: Date Time Unit Tests

    @date_diff @regression
    Scenario Outline: you can get future or past dates in string format with YYYY-MM_DD
        Given using <original_date> and parameters that indicate <num_days> <unit> will return date in a YYYY-MM-DD format
        Then the date returned will be <expected_date>
        Examples:
        | original_date | num_days | unit | expected_date |
        | 1934-10-16 | 30 | days in future | 1934-11-15 |
        | 2030-10-16 | 4 | days ago | 2030-10-12 |


    @date_diff @regression
    Scenario Outline: examples of the timediff_from_datetime include years, weeks minutes, past and future datetime
        Given <original_date> will be formatted into a datetime record
        Then with date arithmetic figuring <num> <unit> <direction> the expected date will be <expected_date>
        Examples:
        | original_date | num | unit | direction | expected_date |
        | 06-04-2023 14:30:15 | 3 | weeks | ago | 05-14-2023 14:30:15 |
        | 06-04-2023 14:30:15 | 15 | minutes | in the future | 06-04-2023 14:45:15 |
        | 06-04-2023 14:30:15 | 30 | seconds | in the future | 06-04-2023 14:30:45 |


    @date_diff @regression
    Scenario: you can get date diff by subtracting epoch dates (number of seconds from 1/1/1970)
        Given the epoch ints from two dates that are three weeks apart
        Then the difference between them will be 3 times the number of seconds in a week
