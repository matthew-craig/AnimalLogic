import xml.etree.ElementTree as ET
"""
This Module handles loading of XML Files using the ElementTree module
"""


class eTreeLoader:
    @staticmethod
    def loadXML(file):
        root = None
        try:
            tree = ET.parse(file)
            root = tree.getroot()
        except ET.ParseError:
            print('Failed to parse xml data from specified file please ensure file contains valid xml')
        return root
