from .base_formatter import BaseFormatter


class ObjectFormatter(BaseFormatter):
    def __init__(self, object, inspector):
        self.object = object
        self.inspector = inspector

    def format(self):
        attributes = self.object.__dict__
        single_line_attributes = self.single_line_attributes(
            self.printable_attributes,
            attributes
        )
        return '{0} {1}'.format(self.colorize(self.object, None), ', '.join(single_line_attributes))

    def printable_attributes(self, key, value):
        return self.colorize('self.', None) + \
            self.colorize(key, 'str') + \
            self.colorize('=', None) + \
            self.inspector.awesomize(value)

    def single_line_attributes(self, func, attributes):
        multiple_lines = self.inspector.options['multiple_lines']
        self.inspector.options['multiple_lines'] = False
        result = [
             func(key, value) for key, value in attributes.items()
        ]
        self.inspector.options['multiple_lines'] = multiple_lines
        return result
