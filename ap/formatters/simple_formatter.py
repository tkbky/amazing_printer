from .base_formatter import BaseFormatter


class SimpleFormatter(BaseFormatter):
    def __init__(self, object, inspector):
        self.object = object
        self.inspector = inspector

    def format(self):
        out = self.object
        object_type = type(self.object).__name__
        if isinstance(self.object, str):
            out = '\"{}\"'.format(out)
        return self.colorize(out, object_type)
