import unittest

from collections import OrderedDict

from ..formatter import Formatter
from ..inspector import Inspector


class ObjectOne:
    def __init__(self):
        self.attr_1 = 'attr 1'
        self.attr_2 = 'attr 2'


class TestFormatter(unittest.TestCase):
    maxDiff = None

    """
    Test all the formatters.
    """
    def test_simple_formatter(self):
        inspector = Inspector()
        formatter = Formatter(inspector)
        object = 'a string'
        self.assertEqual(formatter.format(object), '\x1b[33m"a string"')

    def test_dict_formatter(self):
        inspector = Inspector()
        formatter = Formatter(inspector)
        object = {
            'key_1': 'value_1',
            'key_2': 'value_2',
            'key_3': 'value_3',
        }
        expect ="""\x1b[39m{
    \x1b[39mkey_1\x1b[39m: \x1b[33m"value_1",
    \x1b[39mkey_2\x1b[39m: \x1b[33m"value_2",
    \x1b[39mkey_3\x1b[39m: \x1b[33m"value_3"
\x1b[39m}"""
        self.assertEqual(formatter.format(object), expect)

    def test_ordered_dict_formatter(self):
        inspector = Inspector()
        formatter = Formatter(inspector)
        object = OrderedDict({
            'key_1': 'value_1',
            'key_2': 'value_2',
            'key_3': 'value_3',
        })
        expect ="""\x1b[39mOrderedDict(\x1b[39m{
    \x1b[39mkey_1\x1b[39m: \x1b[33m"value_1",
    \x1b[39mkey_2\x1b[39m: \x1b[33m"value_2",
    \x1b[39mkey_3\x1b[39m: \x1b[33m"value_3"
\x1b[39m}\x1b[39m)"""
        self.assertEqual(formatter.format(object), expect)

    def test_list_formatter(self):
        inspector = Inspector()
        formatter = Formatter(inspector)
        object = ['item_1a', 'item_1b', 'item_1c']
        expect = """\x1b[39m[
    \x1b[34m[0] \x1b[33m"item_1a",
    \x1b[34m[1] \x1b[33m"item_1b",
    \x1b[34m[2] \x1b[33m"item_1c"
\x1b[39m]"""
        self.assertEqual(formatter.format(object), expect)

    def test_list_formatter_no_index(self):
        inspector = Inspector({ 'index': False })
        formatter = Formatter(inspector)
        object = ['item_1a', 'item_1b', 'item_1c']
        expect = """\x1b[39m[
    \x1b[33m"item_1a",
    \x1b[33m"item_1b",
    \x1b[33m"item_1c"
\x1b[39m]"""
        self.assertEqual(formatter.format(object), expect)

    def test_object_formatter(self):
        inspector = Inspector()
        formatter = Formatter(inspector)
        obj = ObjectOne()
        expect = '\x1b[39m{0} \x1b[39mself.\x1b[33mattr_1\x1b[39m=\x1b[33m"attr 1", \x1b[39mself.\x1b[33mattr_2\x1b[39m=\x1b[33m"attr 2"'.format(str(obj))
        self.assertEqual(formatter.format(obj), expect)
