from .list_formatter import ListFormatter


class SetFormatter(ListFormatter):
    def format(self):
        return self.colorize('set(', None) + \
            super().format() + \
            self.colorize(')', None)
