import os
import sys
import loaders.xml_loaders.etree as etree
import loaders.json_loaders.simplejson as simplejson
import util.custom_types as ctypes

"""
File Formats that are currently supported by the loader module can be found in the custom_types module.
Additional formats should be added to the implementation there and the implementation of that loader should be added
to a subfolder with the same name as the file formats extension.

File Loader Class this class can be extended to support additional file formats, currently supported formats
can be seen in the custom_types module this class should contain implementations for all options listed in custom_types
"""


class Loader:
    def __init__(self):
        self.etLoader = etree.eTreeLoader()
        self.sjLoader = simplejson.jsonLoader()
        self.formats = ctypes.data_formats

    @staticmethod
    def detectFormat(file):
        file, file_ext = os.path.splitext(file)
        if file_ext == '.xml':
            return ctypes.data_formats.xml
        elif file_ext == '.json':
            return ctypes.data_formats.json
        else:
            print('File format not recognized')

    def loadData(self, file, pdata_format=ctypes.data_formats.auto):

        if pdata_format is None:
            print('Unrecognized data format specified ignoring will attempt to auto detect')

        data_format = None

        if pdata_format == 'xml':
            data_format = ctypes.data_formats.xml
        elif pdata_format == 'json':
            data_format = ctypes.data_formats.json
        elif pdata_format != ctypes.data_formats.auto:
            print('File format specified is not valid please see --help_ff')
            sys.exit(0)

        if os.path.isfile(file):
            if pdata_format == ctypes.data_formats.auto:
                data_format = Loader.detectFormat(file)
            if data_format == ctypes.data_formats.xml:
                return self.etLoader.loadXML(file)
            elif data_format == ctypes.data_formats.json:
                return self.sjLoader.load_json(file)
        else:
            print('Specified file not found please ensure the path is correct')
            sys.exit(0)
