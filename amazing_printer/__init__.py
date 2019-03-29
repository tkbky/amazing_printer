from colorama import init
from .inspector import Inspector

init(autoreset = True)

def ap(object, options = {}):    
    inspector = Inspector(options)
    awesome_output = inspector.awesomize(object)
    print(awesome_output)
