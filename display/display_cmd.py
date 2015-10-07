import util.custom_types as ctypes
import xml.etree.ElementTree as ET
import json

"""
The displayData class handles displaying data to the command line for a variety of file types and may support
additional display modes for each file format e.g. a json file may be able to be displayed in pretty format mode
other files may support modes that are appropriate for them.
"""

def rawPrintXml(data):
    ET.dump(data)

def prettyPrintXml(data):
    for c in data:
        if c.tag == 'personal':
            print(c.attrib['name'])
        else:
            print("{} : {}".format(c.tag, c.text))
        prettyPrintXml(c)

def rawPrintJson(data):
    print(json.dumps(data, indent=4, sort_keys=True))

def prettyPrintJson(data):
    for key, subdict in data.items():
        for subkey, value in subdict.items():
            for v in value:
                print(v['name'])
                print(v['PN'])
                print(v['Address'])

def renderData(data, data_format, display_format):

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
        if data_format == ctypes.data_formats.xml:
            rawPrintXml(data)
        if data_format == ctypes.data_formats.json:
            rawPrintJson(data)

    if display_format == ctypes.display_formats.pretty:
        if data_format == ctypes.data_formats.xml:
            prettyPrintXml(data)
        if data_format == ctypes.data_formats.json:
            prettyPrintJson(data)
