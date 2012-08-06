#import pylatex.tools.is_str as is_str
from pylatex.tools import is_str

class text(object):
    __slots__ = ['string']

    def __init__(self, content):
        if is_str(content):
            self.string = content
        else:
            self.string = repr(content)

    def get_str(self):
        return self.string
