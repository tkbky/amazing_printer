from colorama import init, Fore

class Colorize:
    """
    Make string colorful.
    Use Coloroma.

    Supported constants/colors:
    - Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    - Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    - Style: DIM, NORMAL, BRIGHT, RESET_ALL
    """

    # TODO:
    # - Make this configurable
    # - Exhaustive
    COLOR_BY_TYPE = {
        'str': Fore.GREEN,
        'list': Fore.BLUE,
        'tuple': Fore.YELLOW,
    }

    def __init__(self):
        raise "This is a mixin. Can't be initialized."

    def colorize(self, str, type):
        """
        Return a string with color info

        :param str str: The string to be colorized
        :param str type: The type of what the str originally is, use type(obj).__name__
        """
        color = Colorize.COLOR_BY_TYPE.get(type, Fore.RESET)
        return '{0}{1}'.format(color, str)


class Indentator:
    """
    Keep track of indentation
    """
    def __init__(self, indent_width = 4):
        self.indent_width = indent_width
        self.indentation = indent_width

    def increase_indentation(self, func):
        self.indentation += self.indent_width
        result = func()
        self.indentation -= self.indent_width
        return result

# indentator = Indentator(4)
# print('*' * indentator.indentation)
# def foo():
#     print('hello world')
# indentator.increase_indentation(foo)
# print('*' * indentator.indentation)

class BaseFormatter(Colorize):
    def __init__(self):
        pass

    def align(self, value, width):
        return value.rjust(width)

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

class Formatter:
    """
    Format object according to their type.
    """
    def __init__(self, inspector):
        self.inspector = inspector

    def format(self, object, type = None):
        """
        Entry point to format an object.
        """
        if isinstance(object, dict):
            return self.format_dict(object)
        else:
            return self.format_str(object)

    def format_str(self, object):
        return SimpleFormatter(object, type(object).__name__).format()

    def format_dict(self, object):
        return DictFormatter(object, self.inspector).format()


class Inspector:
    DEFAULT_OPTIONS = {
        'sort_keys': False, # Do not sort hash keys
    }

    def __init__(self, options = {}):
        self.options = { **self.DEFAULT_OPTIONS, **options }
        self.formatter = Formatter(self)
        self.indentator = Indentator()

    def increase_indentation(self, func):
        return self.indentator.increase_indentation(func)

    def indentation(self):
        return self.indentator.indentation

    def outdent(self):
        return ' ' * (self.indentator.indentation - self.indentator.indent_width)

    def awesomize(self, object):
        return self.formatter.format(object)


class DictFormatter(BaseFormatter):
    def __init__(self, object, inspector):
        self.object = object
        self.inspector = inspector

    def format(self):
        if len(self.object) == 0:
            return '{}'
        else:
            return self.awesome_dict()

    def awesome_dict(self):
        """
        return an awesome dict.
        """
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
        max_key_width = max([len(datum[0]) for datum in data])
        return max_key_width + self.inspector.indentation()


def ap(object, options = {}):
    init(autoreset = True)
    inspector = Inspector(options)
    awesome_output = inspector.awesomize(object)
    print(awesome_output)
