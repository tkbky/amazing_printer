from .base_formatter import BaseFormatter


class ListFormatter(BaseFormatter):
    def __init__(self, object, inspector):
        self.object = object
        self.inspector = inspector

    def format(self):
        if len(self.object) == 0:
            return '[]'
        else:
            return self.awesome_list()

    def awesome_list(self):
        """
        return an awesome list.
        """
        list = self.printable_list()
        return self.colorize('[\n', None) + \
            ',\n'.join(list) + '\n' + \
            self.inspector.outdent() + \
            self.colorize(']', None)

    def printable_list(self):
        data = self.object
        width = self.left_width(data)
        return [
            self.inspector.increase_indentation(
                lambda: self.build_colorized_list(index, datum, width)
            ) for index, datum in enumerate(data)
        ]

    def build_colorized_list(self, index, datum, width):
        return '{0}{1}'.format(self.list_prefix(index, width), self.inspector.awesomize(datum))

    def left_width(self, data):
        """
        return spaces required on the left of the printable list

        e.g.
        the printable list will be:
        [
            [0] 1,
            [1] 2,
            [2] 3
        ]
        so, the spaces on the left is
        indentation + length of the index (in string)
        """
        return len(str(len(data) - 1))

    def list_prefix(self, index, width):
        return self.inspector.indent() + \
            self.colorize('[{0}] '.format(str(index).rjust(width)), 'list')
