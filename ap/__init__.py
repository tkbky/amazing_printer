from colorama import init
from .inspector import Inspector


def ap(object, options = {}):
    init(autoreset = True)
    inspector = Inspector(options)
    awesome_output = inspector.awesomize(object)
    print(awesome_output)
