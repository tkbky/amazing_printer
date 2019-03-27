from .dict_formatter import DictFormatter


class OrderedDictFormatter(DictFormatter):
    def format(self):
        return self.colorize('OrderedDict(', None) + \
            super().format() + \
            self.colorize(')', None)
