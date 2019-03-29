from .base_formatter import BaseFormatter


class DictFormatter(BaseFormatter):
    def __init__(self, object, inspector):
        self.object = object
        self.inspector = inspector

    def format(self):
        if len(self.object) == 0:
            return '{}'
        elif self.single_line():
            return self.single_line_dict()
        else:
            return self.multiple_lines_dict()

    def single_line_dict(self):
        dict = self.printable_dict()
        return self.colorize('{', None) + \
            ', '.join(dict) + self.colorize('}', None)

    def multiple_lines_dict(self):
        dict = self.printable_dict()
        return self.colorize('{\n', None) + \
            ',\n'.join(dict) + '\n' + \
            self.inspector.outdent() + \
            self.colorize('}', None)

    def printable_dict(self):
        data = self.printable_keys()
        width = self.left_width(data)
        return [
            self.inspector.increase_indentation(
                lambda: self.build_colorized_dict(datum[0], datum[1], width)
            ) for datum in data
        ]

    def build_colorized_dict(self, key, value, width):
        left_pad_colorized_key = self.align(key, width)
        colorized_colon = self.colorize(': ', None)
        awesomized_value = self.inspector.awesomize(value)
        return '{0}{1}{2}'.format(left_pad_colorized_key, colorized_colon, awesomized_value)

    def printable_keys(self):
        """
        return an array of colorized key and raw value pairs

        e.g.
        given:

        object = {
            'a': 'va',
            'c': 'vc',
            'b': {
                'd': 'vd'
            }
        }

        returns:

        [[colorize('a'), 'va'], [colorize('c'), 'vc'], [colorize('b'), { 'd': 'vd' }]]
        """
        keys = self.object.keys()
        if self.inspector.options['sort_keys']:
            keys = sorted(keys)
        return [[self.colorize(key, None), self.object[key]] for key in keys]

    def left_width(self, data):
        """
        Find the spaces we need to pad on the left side of the dictionary.
        e.g.
        {
            'foo': { ... },
            'barbarbar': { ... },
        }
        we want to align this into
        {
                  'foo': { ... },
            'barbarbar': { ... },
        }
        so, the number of spaces we need on the left of the keys is calculated as:
        (number of indentation * indentation width) + max of keys width
        {
        xxxx      'foo': { ... },
            'barbarbar': { ... },
        }
        in this case, left width = (1 * 4) + 9 = 13
        """
        if self.single_line():
            return 0
        max_key_width = max([len(datum[0]) for datum in data])
        return max_key_width + self.inspector.indentation()
