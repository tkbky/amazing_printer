import unittest
from unittest.mock import MagicMock

from ..inspector import Inspector


class TestInspector(unittest.TestCase):
    """
    Unit test for inspector.
    """
    def test_increase_indentation(self):
        indentator = MagicMock()
        inspector = Inspector(indentator=indentator)
        def func():
            pass
        inspector.increase_indentation(func)
        self.assertEqual(indentator.increase_indentation.call_count, 1)
        self.assertEqual(indentator.increase_indentation.call_args[0], (func,))

    def test_indentation(self):
        indentator = MagicMock()
        inspector = Inspector(indentator=indentator)
        indentator.indentation = 1
        self.assertEqual(inspector.indentation(), 1)

    def test_indent(self):
        indentator = MagicMock(indentation=1)
        inspector = Inspector(indentator=indentator)
        self.assertEqual(inspector.indent(), ' ')
        indentator = MagicMock(indentation=10)
        inspector = Inspector(indentator=indentator)
        self.assertEqual(inspector.indent(), ' ' * 10)

    def test_outdent(self):
        indentator = MagicMock(indentation=1, indent_width=1)
        inspector = Inspector(indentator=indentator)
        self.assertEqual(inspector.outdent(), '')
        indentator = MagicMock(indentation=10, indent_width=1)
        inspector = Inspector(indentator=indentator)
        self.assertEqual(inspector.outdent(), ' ' * 9)

    def test_awesomize(self):
        inspector = Inspector()
        self.assertEqual(inspector.awesomize('hello'), '\x1b[33m"hello"')
