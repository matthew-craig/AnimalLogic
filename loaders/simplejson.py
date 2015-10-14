import util.custom_types as ctypes
import json
import loader

"""
This Module handles loading of JSON Files using the standard simplejson module
"""
def register(formats):
    formats.append('json')
    return 'json'

class Loader(loader.ILoader):
    def loadData(self, file):
        fhandle = open(file, 'r')
        data = None
        try:
            fdata = fhandle.read()
            data = json.loads(fdata)
        except ValueError:
            print('Failed to parse json data from specified file please ensure file contains valid json')
        return data

    def rawPrintJson(self, data):
        print(json.dumps(data, indent=4, sort_keys=True))

    def prettyPrintJson(self, data):
        for key, subdict in data.items():
            for subkey, value in subdict.items():
                for v in value:
                    print(v['name'])
                    print(v['PN'])
                    print(v['Address'])

    def renderData(self, data, data_format, display_format):

        if display_format == 'raw':
            display_format = ctypes.display_formats.raw
        elif display_format == 'pretty':
            display_format = ctypes.display_formats.pretty
        else:
            print('Display format not recognized please see --help_df')

        if data is None:
            print('No data loaded please ensure the path specified is correct and points to a valid file')
            return

        if data_format is None:
            print('This data format is not currently supported')
            return

        if display_format == ctypes.display_formats.raw or display_format is None:
            if data_format == 'json':
                self.rawPrintJson(data)

        if display_format == ctypes.display_formats.pretty:
            if data_format == 'json':
                self.prettyPrintJson(data)

