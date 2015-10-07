import loaders.loader as ldr
import display.display_cmd as dsp

"""
This Module handles the processing of Personal Data Files
"""


class Personal:
    def __init__(self):
        self.loader = ldr.Loader()
        self.data = []

    def loadPersonalData(self, file, data_format):
        self.data = self.loader.loadData(file, data_format)
        return self.data

    def displayPersonalData(self, data_format, display_format):
        dsp.renderData(self.data, data_format, display_format)
