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

    # TODO:
    # - Make this configurable
    # - Exhaustive
    COLOR_BY_TYPE = {
        'str': Fore.YELLOW,
        'list': Fore.BLUE,
        'tuple': Fore.GREEN,
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
