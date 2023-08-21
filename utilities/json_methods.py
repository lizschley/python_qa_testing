''' This is a json utility method.  It only has json extracted from business logic '''
import json
import os
import constants.environment_keys as ek
import helpers.environment_helper as eh
import utilities.date_time as dt
import utilities.utils as utils


def json_to_dict(json_path):
    '''
        json_to_dict takes a json file path, reads the content and uses it to create a dictionary.

        :param json_path: Path to a file on the project directory structure
        :type json_path: String
        :return: dictionary based on the contents of the JSON file
        :rtype: dictionary
    '''
    # Opening JSON file
    file = open(json_path, 'r')
    # load and return JSON object as a dictionary
    data = json.load(file)
    file.close()
    return data


def update_json_file(updated_json_object, file_path):
    '''
    update_json_file takes the file path and updated json object and writes the json
    with the new updates

    :param updated_json_object: this will be updated as part of another process
    :type updated_json_object: dictionary
    :param file_path: This is the path to the json file
    :type file_path: str
    '''
    file_to_update = open(file_path, 'w')
    json.dump(updated_json_object, file_to_update)
    file_to_update.close()


def write_json_file(**kwargs):
    '''
        kwargs keys are as follows:
        1. json_data
        2. dict_data
        3. filepath
        4. filename
        5. mode (defaults to 'w')
    '''
    if utils.key_in_dictionary(kwargs, 'json_data'):
        method = json.dumps
        data = kwargs['json_data']
    elif utils.key_in_dictionary(kwargs, 'dict_data'):
        method = json.dump
        data = kwargs['dict_data']
    else:
        return
    mode = kwargs.get('mode', 'w')
    filepath = create_json_file_path(**kwargs)

    with open(filepath, mode=mode) as file:
        method(data, file, indent=4)
    file.close()


def create_json_file_path(**kwargs):
    '''
    create_json_file_name_with_path creates json output file

    :param directory_path: directory to write to.  defaults to OUT_JSON_PATH, which is always wrong
    :type directory_path: str, optional
    :param filename: if filename is None will create filename with datetime stamp, defaults to None
    :type filename: str, optional
    :return: file_path
    :rtype: str
    '''
    environment_key = os.getenv('ENVIRONMENT_KEY')
    if not environment_key:
        directory_path = kwargs.get('filepath', 'reports')
    else:
        env_data = eh.environment_level_information(environment_key)
        directory_path = env_data[ek.ROOT_DIR] + '/' + kwargs.get('filepath', 'reports')

    filename = kwargs.get('filename', 'default')

    if '.json' not in filename:
        filename = f'{filename}_{dt.string_from_datetime_default_now(None)}.json'
    return directory_path + '/' + filename
