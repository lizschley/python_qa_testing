import os

# params to store keys to make environments flexible

# used to set up the environment you need before any tests run (features/environment.py)
ENVIRONMENT_KEY = 'environment_key'
LOCAL_MAC = 'local_mac'
LOCAL_WINDOWS = 'local_windows'

BASE_URL = 'base_url'
LOCAL_PORT = '8083'
ROOT_DIR = 'root_dir'

# There is no usecase currently for access_token or send_verify_false, but likely useful in real situations
ACCESS_TOKEN = 'access_token'
SEND_VERIFY_FALSE = 'send_verify_false'

# The below variables are only to show example, not necessary for simpler applications
RAPID_API_BASE_URL = 'rapid_api_base_url'
RAPID_API_KEY_VAR = 'X-RapidAPI-Key'
RAPID_API_HOST_VAR = 'X-RapidAPI-Host'
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
RAPID_API_HOST = os.getenv('RAPID_API_HOST')
