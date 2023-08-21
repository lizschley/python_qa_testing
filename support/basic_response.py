import json
import constants.report_paths as rp
import utilities.json_methods as jm


class BasicResponse:
    def __init__(self, response):
        self.status_code = response.status_code
        try:
            self.data = response.json()
        except json.decoder.JSONDecodeError:
            self.data = {}
            self.data['detail'] = response.content.decode()

    @property
    def error_detail(self):
        return self.data['detail']

    def write_to_file(self, filename, folder='example'):
        if len(self.data) == 0:
            print(f'------------------------> No data for {event} <-----------')
            return
        filepath = rp.REPORT_PATHS[folder]['filepath']
        input = {
            'dict_data': self.data,
            'filepath': filepath,
            'filename': filename
        }
        jm.write_json_file(**input)
