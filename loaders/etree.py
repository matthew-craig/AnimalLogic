import util.custom_types as ctypes
import xml.etree.ElementTree as ET
import loader

"""
This Module handles loading of XML Files using the ElementTree module
"""
def register(formats):
    formats.append('xml')
    return 'xml'

class Loader(loader.ILoader):
    def loadData(self, file):
        root = None
        try:
            tree = ET.parse(file)
            root = tree.getroot()
        except ET.ParseError:
            print('Failed to parse xml data from specified file please ensure file contains valid xml')
        return root

    def rawPrintXml(self, data):
        ET.dump(data)

    def prettyPrintXml(self, data):
        for c in data:
            if c.tag == 'personal':
                print(c.attrib['name'])
            else:
                print("{} : {}".format(c.tag, c.text))
            self.prettyPrintXml(c)

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
            if data_format == 'xml':
                self.rawPrintXml(data)

        if display_format == ctypes.display_formats.pretty:
            if data_format == 'xml':
                self.prettyPrintXml(data)

