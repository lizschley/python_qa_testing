# put unnecssary error message on comment instead of code
DEFAULT = 'default'
ALLURE = 'allure'
QUOTE = 'quote'


# Todo: Reports are not implemented here, will be in a different application
# Note: they can be implemented by write_to_file method in support/basic_response
REPORT_PATHS = {
    'example': {
        'filepath': 'reports/example'
    },
    'allure': {
        'filepath': 'reports/allure'
    },
    'quote': {
        'filepath': 'reports/quote'
    }
}
