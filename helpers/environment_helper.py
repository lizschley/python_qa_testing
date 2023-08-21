# Set up environment at the feature level
import os
import constants.environment_keys as ek


# Note: the advantage of this format is that it is extremely easy to use, but also quite flexible:
#       For example, each environment could be used a different base_url (a completely different application)
#       Microservices can have a common base_url for all the services and a base route for that particular service
#          with the rest of the url varying per end point
#       It can also be used for different environments, such as local, qa, uat, etc
def environment_level_information(environment_key):
    if environment_key == ek.LOCAL_MAC:
        return environment_local_mac(environment_key)
    if environment_key == ek.LOCAL_WINDOWS:
        return environment_local_windows(environment_key)


def environment_local_mac(environment_key):
    env_data = environment_template()
    env_data[ek.ENVIRONMENT_KEY] = environment_key
    env_data[ek.BASE_URL] = f'http://localhost:{ek.LOCAL_PORT}'
    env_data[ek.SEND_VERIFY_FALSE] = False
    env_data[ek.ROOT_DIR] = '/Users/lizschley/development/python-qa-testing-app'
    # below is example only
    env_data[ek.RAPID_API_BASE_URL] = 'https://wft-geo-db.p.rapidapi.com/v1/geo/locations'
    env_data[ek.RAPID_API_KEY_VAR] = os.getenv(ek.RAPID_API_KEY)
    env_data[ek.RAPID_API_HOST_VAR] = os.getenv(ek.RAPID_API_HOST)
    return env_data


def environment_local_windows(environment_key):
    env_data = environment_template()
    env_data[ek.ENVIRONMENT_KEY] = environment_key
    env_data[ek.BASE_URL] = "http://localhost:{ek.LOCAL_PORT}"
    env_data[ek.SEND_VERIFY_FALSE] = False
    env_data[ek.ROOT_DIR] = 'C:/Users/liz.schley/development/python-qa-testing-app'
    # below is example only
    env_data[ek.RAPID_API_URL] = 'https://wft-geo-db.p.rapidapi.com/v1/geo/locations'
    env_data[ek.RAPID_API_KEY_VAR] = os.getenv(ek.RAPID_API_KEY)
    env_data[ek.RAPID_API_HOST_VAR] = os.getenv(ek.RAPID_API_HOST)
    return env_data


def environment_template():
    return {
        ek.ENVIRONMENT_KEY: '',
        ek.ACCESS_TOKEN: '',
        ek.BASE_URL: '',
        ek.ROOT_DIR: '',
        ek.SEND_VERIFY_FALSE: False,
    }


# this is a way to store a variable to use throughout a given feature
def set_up_feature_specific_variables(context, feature):
    print(f'feature is currently {feature}')


# this is a way to put out feature level reports (or whatever)
# you could also do some data cleanup
# One example is to compare the times the various calls makes within a feature
def find_after_feature_method(context, feature):
    print(f'done with {feature}')
