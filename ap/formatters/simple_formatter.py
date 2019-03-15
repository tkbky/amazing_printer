from .base_formatter import BaseFormatter


class SimpleFormatter(BaseFormatter):
    def __init__(self, object, type):
        self.object = object
        self.type = type

    def format(self):
        out = self.object
        if isinstance(self.object, str):
            out = '\"{}\"'.format(out)
        return self.colorize(out, self.type)

# objs = [
#     'this is a string',
#     {'foo': 'bar'},
#     (1, 2),
#     ['hello', 'world']
# ]
# for o in objs:
#     sf = SimpleFormatter(o, type(o).__name__)
#     print(sf.format())
