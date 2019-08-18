from abc import ABCMeta as ABC, abstractmethod
from fynd_request_builder import request_builder

## Define Image Abstract Classses
class ImageReader:
    __metaclass__ = ABC

    def __init__(self):
        super(ImageReader, self).__init__()

    @abstractmethod
    def read(self):
        pass


class GIFReader(ImageReader):

    def __init__(self):
        super(ImageReader, self).__init__();

    def read(self):
        print("We will read gif from this path")


class PNGReader(ImageReader):

    def __init__(self):
        super(ImageReader, self).__init__();

    def read(self):
        print("We will read png from this path")


def extension_of(path):
    position_of_last_dot = path.rfind('.')
    return path[position_of_last_dot + 1:]


def get_image_reader(path):
    image_type = extension_of(path)
    loader_type = LoadReader(image_type)
    image_reader = loader_type.get_reader()
    image_reader.read()

class LoadReader(object):

    def __init__(self,image_type):
        self.reader_type = image_type

    def get_reader(self):
        reader_dict={
            "gif":GIFReader(),
            "png":PNGReader()
        }
        return reader_dict[self.reader_type]


a = extension_of("abc.gif")
get_image_reader(a)