import unittest
import xml.etree.ElementTree as ET
import loader as ldr

"""
Define Various TestCases
"""


class TestCases(unittest.TestCase):

    def setUp(self):
        self.loader = ldr.LoaderManager('loaders')
        self.loader.load_modules()

    def test_detectJSON(self):
        data_format = self.loader.detectFormat('test.json')
        self.assertEqual(data_format, 'json', "json format not detected correctly")

    def test_detectXML(self):
        data_format = self.loader.detectFormat('test.xml')
        self.assertEqual(data_format, 'xml', "xml format not detected correctly")

    def test_loadXML(self):
        data = self.loader.loadData('data/personal_data.xml','xml')
        self.assertTrue(type(data) is ET.Element, "expected xml data in string format")

    def test_loadJSON(self):
        data = self.loader.loadData('data/personal_data.json','json')
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
