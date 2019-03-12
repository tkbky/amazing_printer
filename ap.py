from colorama import init
from colorize import Colorize
from indentator import Indentator

from formatters.dict_formatter import DictFormatter
from formatters.list_formatter import ListFormatter
from formatters.object_formatter import ObjectFormatter
from formatters.simple_formatter import SimpleFormatter


class Formatter:
    """
    Format object according to their type.
    """
    def __init__(self, inspector):
        self.inspector = inspector

    def format(self, object, type = None):
        """
        Entry point to format an object.
        """
        if hasattr(object, '__dict__'):
            return self.format_object(object)
        elif isinstance(object, dict):
            return self.format_dict(object)
        elif isinstance(object, list):
            return self.format_list(object)
        else:
            return self.format_str(object)

    def format_str(self, object):
        return SimpleFormatter(object, type(object).__name__).format()

    def format_dict(self, object):
        return DictFormatter(object, self.inspector).format()

    def format_list(self, object):
        return ListFormatter(object, self.inspector).format()

    def format_object(self, object):
        return ObjectFormatter(object, self.inspector).format()


class Inspector:
    DEFAULT_OPTIONS = {
        'sort_keys': False, # Do not sort hash keys
    }

    def __init__(self, options = {}):
        self.options = { **self.DEFAULT_OPTIONS, **options }
        self.formatter = Formatter(self)
        self.indentator = Indentator()

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


def ap(object, options = {}):
    init(autoreset = True)
    inspector = Inspector(options)
    awesome_output = inspector.awesomize(object)
    print(awesome_output)
