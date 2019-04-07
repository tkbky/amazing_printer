from .base_formatter import BaseFormatter


class ListFormatter(BaseFormatter):
    def __init__(self, object, inspector):
        self.object = object
        self.inspector = inspector

    def format(self):
        if len(self.object) == 0:
            return '[]'
        elif self.single_line():
            return self.single_line_list()
        else:
            return self.multiple_lines_list()

    def single_line_list(self):
        list = self.printable_list(self.inspector.options['index'])
        return self.colorize('[', None) + \
            ', '.join(list) + \
            self.colorize(']', None)

    def multiple_lines_list(self):
        list = self.printable_list(self.inspector.options['index'])
        return self.colorize('[\n', None) + \
            ',\n'.join(list) + '\n' + \
            self.inspector.outdent() + \
            self.colorize(']', None)

    def printable_list(self, with_prefix = True):
        data = self.object
        list = []
        for index, datum in enumerate(data):
            width = self.left_width(data)
            prefix = self.list_prefix(index, width) if with_prefix else self.inspector.indent()
            list.append(self.inspector.increase_indentation(
                lambda: self.build_colorized_list(datum, prefix)
            ))
        return list

    def build_colorized_list(self, datum, prefix):
        return '{0}{1}'.format(prefix, self.inspector.awesomize(datum))

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
        if self.single_line():
            return 0
        return len(str(len(data) - 1))

    def list_prefix(self, index, width):
        return self.inspector.indent() + \
            self.colorize('[{0}] '.format(str(index).rjust(width)), 'list')
