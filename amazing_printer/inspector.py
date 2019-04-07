from .indentator import Indentator
from .formatter import Formatter


class Inspector:
    DEFAULT_OPTIONS = {
        'sort_keys': False, # Do not sort hash keys
        'indent': 4, # 4 spaces
        'index': True, # Show list indices
        'multiple_lines': True, # Span fields inside a dict or an array into multiple lines,
        'color': {
            'str': 'yellow',
            'list': 'blue',
            'tuple': 'green',
            'none': 'red',
        } # Set color for different literals
    }

    def __init__(self, options = {}, indentator = None):
        self.options = { **self.DEFAULT_OPTIONS, **options }
        self.formatter = Formatter(self)
        self.indentator = indentator or Indentator(self.options['indent'])

    def increase_indentation(self, func):
        return self.indentator.increase_indentation(func)

    def indentation(self):
        return self.indentator.indentation

    def indent(self):
        return ' ' * self.indentator.indentation

    def outdent(self):
        return ' ' * (self.indentator.indentation - self.indentator.indent_width)

    def awesomize(self, object):
        return self.formatter.format(object)
