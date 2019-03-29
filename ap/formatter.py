from collections import OrderedDict

from .formatters.dict_formatter import DictFormatter
from .formatters.ordered_dict_formatter import OrderedDictFormatter
from .formatters.tuple_formatter import TupleFormatter
from .formatters.list_formatter import ListFormatter
from .formatters.set_formatter import SetFormatter
from .formatters.object_formatter import ObjectFormatter
from .formatters.simple_formatter import SimpleFormatter


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
        if isinstance(object, OrderedDict):
            return self.format_ordered_dict(dict(object))
        elif hasattr(object, '__dict__'):
            return self.format_object(object)
        elif isinstance(object, dict):
            return self.format_dict(object)
        elif isinstance(object, set):
            return self.format_set(object)
        elif isinstance(object, tuple):
            return self.format_tuple(object)
        elif isinstance(object, list):
            return self.format_list(object)
        else:
            return self.format_str(object)

    def format_str(self, object):
        return SimpleFormatter(object, self.inspector).format()

    def format_dict(self, object):
        return DictFormatter(object, self.inspector).format()

    def format_ordered_dict(self, object):
        return OrderedDictFormatter(object, self.inspector).format()

    def format_tuple(self, object):
        return TupleFormatter(object, self.inspector).format()

    def format_list(self, object):
        return ListFormatter(object, self.inspector).format()

    def format_set(self, object):
        return SetFormatter(object, self.inspector).format()

    def format_object(self, object):
        return ObjectFormatter(object, self.inspector).format()
