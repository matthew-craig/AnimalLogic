import loaders.loader as ldr
import unittest
import xml.etree.ElementTree as ET

"""
Define Various TestCases
"""


class TestCases(unittest.TestCase):

    def setUp(self):
        self.loader = ldr.Loader()

    def test_detectJSON(self):
        data_format = self.loader.detectFormat('test.json')
        self.assertEqual(data_format, ldr.ctypes.data_formats.json, "json format not detected correctly")

    def test_detectXML(self):
        data_format = self.loader.detectFormat('test.xml')
        self.assertEqual(data_format, ldr.ctypes.data_formats.xml, "xml format not detected correctly")

    def test_loadXML(self):
        data = self.loader.etLoader.loadXML('data/personal_data.xml')
        self.assertTrue(type(data) is ET.Element, "expected xml data in string format")

    def test_loadJSON(self):
        data = self.loader.sjLoader.load_json('data/personal_data.json')
        self.assertTrue(type(data) is dict, "expected xml data in string format")

"""
Test Suite Initialization
"""


def test_suite():
    loader_test_suite = unittest.TestSuite()
    loader_test_suite.addTest(TestCases('test_detectJSON'))
    loader_test_suite.addTest(TestCases('test_detectXML'))
    loader_test_suite.addTest(TestCases('test_loadXML'))
    loader_test_suite.addTest(TestCases('test_loadJSON'))
    return loader_test_suite

"""
Test Suite Execution
"""
suite = test_suite()
unittest.TextTestRunner(verbosity=2).run(suite)
