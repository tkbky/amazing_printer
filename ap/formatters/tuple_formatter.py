from .list_formatter import ListFormatter


class TupleFormatter(ListFormatter):
    def format(self):
        return self.colorize('tuple(', None) + \
            super().format() + \
            self.colorize(')', None)
