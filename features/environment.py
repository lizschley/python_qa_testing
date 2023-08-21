# This sets up the environment
from services.example_authentication_service import ExampleAuthenticationService
import constants.environment_keys as ek
import helpers.environment_helper as eh
import os


# Note: before_all runs before any features run
# Whenever you reference an environment variable in before_all, Behave will automatically pickup all .env variables
def before_all(context):
    # normal process is to set the environment key, passwords and secrets in environment variables
    environment_key = os.getenv('ENVIRONMENT_KEY')
    context.environment = eh.environment_level_information(environment_key)
    # no login, but this will be whatever login you need
    auth_service = ExampleAuthenticationService(context)
    # the access token (or whatever you need) will be used in the init service
    # each service will have a different base url and can have a different login strategy
    context.environment[ek.ACCESS_TOKEN] = auth_service.get_credentials()


# Note: before_feature runs before each feature runs.  If you use environment variables from .env
#        here, behave will handle them seamlessly
def before_feature(context, feature):
    context.after_feature = {}
    context.feature_level = {}
    # this helps a lo
    eh.set_up_feature_specific_variables(context, feature.name)


# Note: before_scenario runs before each scenario runs
def before_scenario(context, scenario):
    context.scenario_level = {}


# Note: ************ The tests run here **************


# Note: if there was an after_scenario(context, feature) method, it would run after each scenario


# Note: after_feature runs after each feature runs
def after_feature(context, feature):
    eh.find_after_feature_method(context, feature.name)


# Note: if there was an after_all(context) method, it would run after all of the feature tests are done
