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
