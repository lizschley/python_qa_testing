import random
import constants.used_in_more_than_one_file as uc


def data_that_matches_existing_person_with_unused_id():
    unused_id = random.randint(3000, 30000)
    return {
        'id': unused_id,
        'firstName': 'Jane',
        'lastName': 'Austen',
        'dates': '1775-12-16 to 1817-7-18',
        'personNote': '',
        'quotes': [{
            'quote': 'How would I do one value descending and the other ascending.',
            'quoteNote': ''
        }]
    }


def data_that_will_successfully_add_a_person_and_two_quotes():
    first_quote = 'All plants are not created equal, particularly in their ability '
    first_quote += 'to support wildlife.'
    second_quote = 'We must shrug off our age-old adversarial relationship with nature, the '
    second_quote += '"nature versus us" attitude that may have worked for our ancestors but is '
    second_quote += 'deadly to us now. '
    unused_id = random.randint(30001, 300000)
    return {
        'id': unused_id,
        'firstName': 'Doug',
        'lastName': 'Tallamy',
        'dates': '68 in April 2020',
        'personNote': 'American entomologist, ecologist and conservationist.',
        'quotes': [{
            'quote': first_quote,
            'quoteNote': ''
        }, {
            'quote': second_quote,
            'quoteNote': ''
        }]
    }


def add_quote_to_jane_austen():
    quote = "I do not want people to be very agreeable, as it saves me the trouble of "
    quote += "liking them a great deal."
    return {
        "id": uc.EXISTING_PERSON_ID,
        "quotes": [{
            "quote": quote,
            "quoteNote": "quote from Sense and Sensibility, spoken by the sixteen-year-old Marianne Dashwood"
        }]
    }


def existing_id_but_first_last_and_dates_do_not_match():
    return {
        "id": uc.EXISTING_PERSON_ID,
        "firstName": "Tamora",
        "lastName": "Pierce",
        "dates": "1954-12-13 - ?",
        "personNote": "",
        "quotes": [{
            "quote": "I am not wise, but I can always learn.",
            "quoteNote": "Alonna says this in The Woman Who Rides Like a Man"
        }]
    }


def add_quote_that_will_sort_before_jane_austen():
    unused_id = random.randint(30001, 300000)
    return {
        'id': unused_id,
        'firstName': 'Alicia',
        'lastName': 'Austen',
        'dates': '2223-12-14 - ?"',
        'personNote': 'not born yet',
        'quotes': [{
            'quote': 'My first best friend is octopus.  We communicate with artificial intelligence',
            'quoteNote': ''
        }]
    }


def original_people_in_sorted_order():
    return [
        {'first': 'Jane', 'last': 'Austen'},
        {'first': 'Rosalind', 'last': 'Franklin'},
        {'first': 'Barack', 'last': 'Obama'},
        {'first': 'Rosa', 'last': 'Parks'},
    ]

