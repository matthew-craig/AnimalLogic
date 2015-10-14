import os
import imp
from abc import ABCMeta, abstractmethod

class ILoader():
    __metaclass__=ABCMeta

    @abstractmethod
    def loadData(self, file):
        pass

    @abstractmethod
    def renderData(self, data, data_format, display_format):
        pass

class LoaderManager():
    def __init__(self, module_dir):
        self.module_dir = module_dir
        self.registered_formats = []
        self.modules = {}

    def load_modules(self):
        for root, dirs, files in os.walk(self.module_dir):
            for file in files:
                if (file.endswith('.py')):
                    fname, file_ext = os.path.splitext(file)
                    fp, pathname, description = imp.find_module(fname, [root])
                    try:
                        if not fname.startswith("__"):
                            mod = imp.load_module(fname, fp, pathname, description)
                            format = mod.register(self.registered_formats)
                            index = self.registered_formats.index(format)
                            self.modules[index] = mod
                    finally:
                        if fp:
                            fp.close()
        return

    def loadData(self, file, data_format):
        if data_format == 'auto':
            data_format = self.detectFormat(file)
        for format in self.registered_formats:
            if format == data_format:
                index = self.registered_formats.index(format)
                ldr = self.modules[index].Loader()
                return ldr.loadData(file)

    def renderData(self, data, data_format, display_format):
        for format in self.registered_formats:
            if format == data_format:
                index = self.registered_formats.index(format)
                ldr = self.modules[index].Loader()
                return ldr.renderData(data, data_format, display_format)

    def detectFormat(self, file):
        file, file_ext = os.path.splitext(file)
        file_ext_stripped = file_ext[1:]
        for format in self.registered_formats:
            if format == file_ext_stripped:
                return format
        return False
