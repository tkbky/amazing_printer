from .base_formatter import BaseFormatter


class SimpleFormatter(BaseFormatter):
    def __init__(self, object, type):
        self.object = object
        self.type = type

    def format(self):
        out = self.object
        if isinstance(self.object, str):
            out = '\"{}\"'.format(out)
        return self.colorize(out, self.type)
