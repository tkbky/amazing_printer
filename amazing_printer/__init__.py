import os
import yaml

from os.path import expanduser

from colorama import init
from .inspector import Inspector

CONFIG_FILE = ".amazing_printer.yml"

init(autoreset = True)

global_options = {}

def ap(object, options = {}):
    inspector = Inspector({ **global_options, **options })
    awesome_output = inspector.awesomize(object)
    print(awesome_output)

def configure(options = {}):
    global global_options
    global_options = options

def __configure_from_file():
    """
    Look for config file from current directory up to home directory.
    Config file must be named .amazing_printer.yml
    """
    global global_options
    home_directory = expanduser("~")
    current_directory = os.getcwd()

    # Find for config file in current & home directory
    config = __get_config_from_file([current_directory, home_directory])

    if config is None:
        return

    global_options = config

def __get_config_from_file(dirs):
    for dir in dirs:
        for file in os.listdir(dir):
            if file == CONFIG_FILE:
                print(f"Config file found in {os.path.join(dir, file)}")
                with open(CONFIG_FILE, "r") as stream:
                    try:
                        return yaml.safe_load(stream)
                    except yaml.YAMLError as e:
                        print(e)
                        return None
__configure_from_file()
