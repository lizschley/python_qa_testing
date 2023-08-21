from behave import step
from services.hello_service import HelloService


# Ref: Scenario Outline --> Test the Hello API
@step('the hello url is called using {name}')
def using_hello_service_make_hello_call(context, name):
    params = {} if name == 'default' else {'name': name}
    hello_service = HelloService(context)
    context.scenario_level['response'] = hello_service.hello_world(params)


@step('the return will be hello plus {name} with default becoming Hello World')
def hello_message_is_hello_name(context, name):
    response = context.scenario_level['response']
    assert response.status_code == 200
    expected_content = name_scenarios(name)
    assert response.json()['content'] == expected_content


def name_scenarios(name):
    # URL has no parameters for default
    if name == 'default':
        return 'Hello, World!'
    return 'Hello, ' + name + '!'
