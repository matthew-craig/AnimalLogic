import loader as ldr

"""
This Module handles the processing of Personal Data Files
"""


class Personal:
    def __init__(self):
        self.loader = ldr.LoaderManager('loaders')
        self.loader.load_modules()
        self.data = []

    def loadPersonalData(self, file, data_format):
        self.data = self.loader.loadData(file, data_format)
        return self.data

    def displayPersonalData(self, data_format, display_format):
        self.loader.renderData(self.data, data_format, display_format)
