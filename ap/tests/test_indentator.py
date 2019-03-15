import unittest

from ..indentator import Indentator


class TestIndentator(unittest.TestCase):
    """
    Unit test for indentator.
    """
    def test_increase_indentator(self):
        indentator = Indentator()
        current_indentation = indentator.indentation
        func = lambda: self.assertEqual(indentator.indentation, current_indentation + indentator.indent_width)
        # before increase indentation
        self.assertEqual(indentator.indentation, current_indentation)
        indentator.increase_indentation(func)
        # after increase indentation
        self.assertEqual(indentator.indentation, current_indentation)
