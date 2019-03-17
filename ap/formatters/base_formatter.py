from ..colorize import Colorize

class BaseFormatter(Colorize):
    def __init__(self):
        pass

    def align(self, value, width):
        return value.rjust(width)

    def single_line(self):
        return self.inspector.options['multiple_lines'] == False
