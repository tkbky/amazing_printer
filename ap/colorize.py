from colorama import Fore

class Colorize:
    """
    Make string colorful.
    Use Coloroma.

    Supported constants/colors:
    - Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    - Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    - Style: DIM, NORMAL, BRIGHT, RESET_ALL
    """

    TYPE_TO_COLOR = {
        'str': 'yellow',
        'list': 'blue',
        'tuple': 'green',
        'none': 'red',
    }

    COLOR_TO_COLORAMA = {
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'green': Fore.GREEN,
        'red': Fore.RED,
        'black': Fore.BLACK,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
    }

    def colorize(self, str, type):
        """
        Return a string with color info

        :param str str: The string to be colorized
        :param str type: The type of what the str originally is, use type(obj).__name__
        """
        colors = self.inspector.options.get('color', Colorize.TYPE_TO_COLOR)
        if type == 'NoneType':
            type = 'none'
        color = Colorize.COLOR_TO_COLORAMA.get(colors.get(type), Fore.RESET)
        return '{0}{1}'.format(color, str)
