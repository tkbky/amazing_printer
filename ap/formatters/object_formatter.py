from .base_formatter import BaseFormatter


class ObjectFormatter(BaseFormatter):
    def __init__(self, object, inspector):
        self.object = object
        self.inspector = inspector

    def format(self):
        attributes = self.object.__dict__
        printable_attributes = [self.colorize('self.', None) + self.colorize(key, 'str') + self.colorize('=', None) + self.colorize(value, 'str') for key, value in attributes.items()]
        return '{0} {1}'.format(self.colorize(self.object, None), ', '.join(printable_attributes))
