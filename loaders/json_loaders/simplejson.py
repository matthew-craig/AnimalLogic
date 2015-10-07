import json
"""
This Module handles loading of XML Files using the standard simplejson module
"""

class jsonLoader:
    @staticmethod
    def load_json(file):
        fhandle = open(file, 'r')
        data = None
        try:
            fdata = fhandle.read()
            data = json.loads(fdata)
        except ValueError:
            print('Failed to parse json data from specified file please ensure file contains valid json')
        return data


